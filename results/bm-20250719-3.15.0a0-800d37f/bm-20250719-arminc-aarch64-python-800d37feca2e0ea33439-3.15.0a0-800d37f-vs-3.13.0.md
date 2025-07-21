# Results vs. 3.13.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-aarch64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.034x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 303 ms: 1.03x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                    |
| async_tree_none            | 504 ms                                                   | 372 ms: 1.35x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 871 ms: 1.31x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 892 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 654 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                    |
| async_generators           | 500 ms                                                   | 459 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.9 ms: 1.13x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.91 ms: 1.31x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.6 ms: 1.22x faster                                                   |
| regex_dna      | 263 ms                                                   | 219 ms: 1.20x faster                                                    |
| regex_compile  | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.11x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 112 ms: 1.06x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 79.0 ms: 1.04x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (4): unpickle_pure_python, json_dumps, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 14.8 ms: 1.09x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.42 ms: 1.04x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.06x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.70 sec: 2.03x faster                                                  |
| deepcopy                   | 479 us                                                   | 331 us: 1.45x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.2 us: 1.42x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 467 ms: 1.42x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                    |
| async_tree_none            | 504 ms                                                   | 372 ms: 1.35x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 871 ms: 1.31x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 892 ms: 1.31x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.91 ms: 1.31x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 654 ms: 1.22x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.6 ms: 1.22x faster                                                   |
| spectral_norm              | 143 ms                                                   | 118 ms: 1.22x faster                                                    |
| regex_dna                  | 263 ms                                                   | 219 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.61 us: 1.18x faster                                                   |
| generators                 | 40.3 ms                                                  | 35.3 ms: 1.14x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                                    |
| float                      | 95.8 ms                                                  | 84.9 ms: 1.13x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.11x faster                                                    |
| pylint                     | 345 ms                                                   | 315 ms: 1.10x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.2 ms: 1.09x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                  |
| bpe_tokeniser              | 6.02 sec                                                 | 5.51 sec: 1.09x faster                                                  |
| scimark_fft                | 463 ms                                                   | 424 ms: 1.09x faster                                                    |
| regex_compile              | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| meteor_contest             | 117 ms                                                   | 107 ms: 1.09x faster                                                    |
| async_generators           | 500 ms                                                   | 459 ms: 1.09x faster                                                    |
| pyflate                    | 582 ms                                                   | 534 ms: 1.09x faster                                                    |
| python_startup             | 16.0 ms                                                  | 14.8 ms: 1.09x faster                                                   |
| pprint_pformat             | 1.99 sec                                                 | 1.84 sec: 1.08x faster                                                  |
| hexiom                     | 7.34 ms                                                  | 6.80 ms: 1.08x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 22.6 ms: 1.08x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                  |
| k_core                     | 2.99 sec                                                 | 2.78 sec: 1.08x faster                                                  |
| sqlite_synth               | 4.08 us                                                  | 3.81 us: 1.07x faster                                                   |
| pprint_safe_repr           | 962 ms                                                   | 900 ms: 1.07x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 112 ms: 1.06x faster                                                    |
| thrift                     | 1.01 ms                                                  | 957 us: 1.06x faster                                                    |
| nqueens                    | 105 ms                                                   | 99.7 ms: 1.05x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| json                       | 5.94 ms                                                  | 5.65 ms: 1.05x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.75 us: 1.05x faster                                                   |
| chaos                      | 70.7 ms                                                  | 67.6 ms: 1.05x faster                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 8.42 ms: 1.04x faster                                                   |
| logging_simple             | 7.25 us                                                  | 6.97 us: 1.04x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 79.0 ms: 1.04x faster                                                   |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                                    |
| richards_super             | 60.8 ms                                                  | 58.8 ms: 1.03x faster                                                   |
| 2to3                       | 313 ms                                                   | 303 ms: 1.03x faster                                                    |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| sympy_str                  | 265 ms                                                   | 262 ms: 1.01x faster                                                    |
| connected_components       | 547 ms                                                   | 557 ms: 1.02x slower                                                    |
| shortest_path              | 565 ms                                                   | 582 ms: 1.03x slower                                                    |
| raytrace                   | 310 ms                                                   | 328 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.09 ms: 1.06x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.82 ms: 1.13x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.94 ms: 1.17x slower                                                   |
| many_optionals             | 626 us                                                   | 760 us: 1.21x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 28.1 ms: 1.38x slower                                                   |
| telco                      | 10.5 ms                                                  | 163 ms: 15.63x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 3.17 sec: 393.38x slower                                                |
| Geometric mean             | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (25): sympy_integrate, sympy_sum, html5lib, mako, comprehensions, richards, unpickle_pure_python, json_dumps, sympy_expand, coverage, fannkuch, asyncio_websockets, pidigits, coroutines, json_loads, scimark_lu, typing_runtime_protocols, docutils, genshi_xml, nbody, crypto_pyaes, deltablue, bench_thread_pool, django_template, pickle_pure_python
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x