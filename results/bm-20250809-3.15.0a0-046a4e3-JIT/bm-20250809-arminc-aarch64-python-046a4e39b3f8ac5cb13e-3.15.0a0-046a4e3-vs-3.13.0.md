# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-aarch64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.016x faster
- HPT reliability: 99.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.12 sec: 1.05x slower                                                  |
| html5lib       | 65.6 ms                                                  | 63.4 ms: 1.03x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 913 ms: 1.28x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 380 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 399 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 659 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 672 ms: 1.18x faster                                                    |
| async_generators           | 500 ms                                                   | 487 ms: 1.03x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.3 ms: 1.16x faster                                                   |
| nbody          | 118 ms                                                   | 127 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.3 ms: 1.24x faster                                                   |
| regex_dna      | 263 ms                                                   | 223 ms: 1.18x faster                                                    |
| regex_compile  | 134 ms                                                   | 123 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps          | 14.2 ms                                                  | 12.0 ms: 1.18x faster                                                   |
| tomli_loads         | 2.67 sec                                                 | 2.33 sec: 1.15x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 177 ms: 1.14x faster                                                    |
| xml_etree_generate  | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 146 ms: 1.09x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 77.2 ms: 1.06x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 12.7 ms: 1.10x faster                                                   |
| genshi_xml     | 61.6 ms                                                  | 62.9 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.63 sec: 2.11x faster                                                  |
| deepcopy                   | 479 us                                                   | 324 us: 1.48x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 36.7 us: 1.44x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                   |
| async_tree_io              | 1.14 sec                                                 | 884 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 913 ms: 1.28x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 380 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 399 ms: 1.26x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.3 ms: 1.24x faster                                                   |
| spectral_norm              | 143 ms                                                   | 116 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 659 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.56 us: 1.19x faster                                                   |
| json_dumps                 | 14.2 ms                                                  | 12.0 ms: 1.18x faster                                                   |
| richards                   | 54.5 ms                                                  | 46.3 ms: 1.18x faster                                                   |
| regex_dna                  | 263 ms                                                   | 223 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 672 ms: 1.18x faster                                                    |
| float                      | 95.8 ms                                                  | 82.3 ms: 1.16x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.33 sec: 1.15x faster                                                  |
| xml_etree_parse            | 203 ms                                                   | 177 ms: 1.14x faster                                                    |
| scimark_fft                | 463 ms                                                   | 406 ms: 1.14x faster                                                    |
| richards_super             | 60.8 ms                                                  | 53.4 ms: 1.14x faster                                                   |
| pyflate                    | 582 ms                                                   | 513 ms: 1.13x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.36 sec: 1.12x faster                                                  |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.5 ms: 1.10x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.70 us: 1.10x faster                                                   |
| mako                       | 14.0 ms                                                  | 12.7 ms: 1.10x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| go                         | 164 ms                                                   | 151 ms: 1.09x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 146 ms: 1.09x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.5 ms: 1.08x faster                                                   |
| regex_compile              | 134 ms                                                   | 123 ms: 1.08x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.1 ms: 1.08x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 77.2 ms: 1.06x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.65 us: 1.06x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| chaos                      | 70.7 ms                                                  | 67.1 ms: 1.05x faster                                                   |
| meteor_contest             | 117 ms                                                   | 112 ms: 1.05x faster                                                    |
| deltablue                  | 3.97 ms                                                  | 3.79 ms: 1.05x faster                                                   |
| nqueens                    | 105 ms                                                   | 100 ms: 1.05x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.04x faster                                                  |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 63.4 ms: 1.03x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.03x faster                                                  |
| async_generators           | 500 ms                                                   | 487 ms: 1.03x faster                                                    |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| sympy_str                  | 265 ms                                                   | 271 ms: 1.02x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 62.9 ms: 1.02x slower                                                   |
| connected_components       | 547 ms                                                   | 563 ms: 1.03x slower                                                    |
| shortest_path              | 565 ms                                                   | 591 ms: 1.05x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 89.2 ms: 1.05x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.12 sec: 1.05x slower                                                  |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.03 ms: 1.06x slower                                                   |
| raytrace                   | 310 ms                                                   | 327 ms: 1.06x slower                                                    |
| nbody                      | 118 ms                                                   | 127 ms: 1.08x slower                                                    |
| comprehensions             | 20.8 us                                                  | 22.6 us: 1.08x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.72 ms: 1.10x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.25 sec: 1.13x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.09 sec: 1.14x slower                                                  |
| gc_traversal               | 5.92 ms                                                  | 6.77 ms: 1.14x slower                                                   |
| many_optionals             | 626 us                                                   | 991 us: 1.58x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 48.1 ms: 2.37x slower                                                   |
| telco                      | 10.5 ms                                                  | 163 ms: 15.57x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 1.23 sec: 152.60x slower                                                |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (24): pylint, unpickle_pure_python, genshi_text, thrift, json, fannkuch, logging_simple, sympy_integrate, sympy_sum, python_startup_no_site, coverage, json_loads, pidigits, asyncio_websockets, hexiom, 2to3, pycparser, bench_thread_pool, coroutines, sympy_expand, typing_runtime_protocols, scimark_lu, django_template, pickle_pure_python
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 99.24% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x