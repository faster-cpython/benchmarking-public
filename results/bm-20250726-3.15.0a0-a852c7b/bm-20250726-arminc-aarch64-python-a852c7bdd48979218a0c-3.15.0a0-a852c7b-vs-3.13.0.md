# Results vs. 3.13.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: linux-aarch64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.027x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 301 ms: 1.04x faster                                                    |
| html5lib       | 65.6 ms                                                  | 61.5 ms: 1.07x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 456 ms: 1.45x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 459 ms: 1.44x faster                                                    |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 866 ms: 1.32x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 900 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 655 ms: 1.20x faster                                                    |
| async_generators           | 500 ms                                                   | 453 ms: 1.11x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.6 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.2 ms: 1.20x faster                                                   |
| regex_dna      | 263 ms                                                   | 223 ms: 1.18x faster                                                    |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.12x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                  |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (6): json_dumps, xml_etree_generate, xml_etree_process, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.54 ms: 1.03x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.64 sec: 2.10x faster                                                  |
| deepcopy                   | 479 us                                                   | 325 us: 1.47x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 456 ms: 1.45x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 459 ms: 1.44x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.4 us: 1.42x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                   |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 866 ms: 1.32x faster                                                    |
| go                         | 164 ms                                                   | 126 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 900 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 655 ms: 1.20x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.2 ms: 1.20x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.56 us: 1.19x faster                                                   |
| regex_dna                  | 263 ms                                                   | 223 ms: 1.18x faster                                                    |
| spectral_norm              | 143 ms                                                   | 123 ms: 1.16x faster                                                    |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.14x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.12x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.9 ms: 1.12x faster                                                   |
| float                      | 95.8 ms                                                  | 85.6 ms: 1.12x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 78.8 ms: 1.11x faster                                                   |
| async_generators           | 500 ms                                                   | 453 ms: 1.11x faster                                                    |
| pyflate                    | 582 ms                                                   | 527 ms: 1.10x faster                                                    |
| pylint                     | 345 ms                                                   | 316 ms: 1.09x faster                                                    |
| scimark_fft                | 463 ms                                                   | 424 ms: 1.09x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.51 sec: 1.09x faster                                                  |
| tomli_loads                | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                  |
| pprint_pformat             | 1.99 sec                                                 | 1.82 sec: 1.09x faster                                                  |
| sqlite_synth               | 4.08 us                                                  | 3.76 us: 1.08x faster                                                   |
| sympy_integrate            | 21.4 ms                                                  | 19.9 ms: 1.08x faster                                                   |
| hexiom                     | 7.34 ms                                                  | 6.81 ms: 1.08x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                  |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                    |
| pprint_safe_repr           | 962 ms                                                   | 894 ms: 1.08x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.57 us: 1.07x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 22.7 ms: 1.07x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 61.5 ms: 1.07x faster                                                   |
| nqueens                    | 105 ms                                                   | 98.5 ms: 1.06x faster                                                   |
| thrift                     | 1.01 ms                                                  | 954 us: 1.06x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.82 sec: 1.06x faster                                                  |
| logging_simple             | 7.25 us                                                  | 6.86 us: 1.06x faster                                                   |
| meteor_contest             | 117 ms                                                   | 111 ms: 1.05x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| comprehensions             | 20.8 us                                                  | 19.8 us: 1.05x faster                                                   |
| 2to3                       | 313 ms                                                   | 301 ms: 1.04x faster                                                    |
| richards_super             | 60.8 ms                                                  | 59.0 ms: 1.03x faster                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 8.54 ms: 1.03x faster                                                   |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| connected_components       | 547 ms                                                   | 557 ms: 1.02x slower                                                    |
| shortest_path              | 565 ms                                                   | 581 ms: 1.03x slower                                                    |
| raytrace                   | 310 ms                                                   | 327 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.19 ms: 1.08x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.76 ms: 1.11x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.78 ms: 1.15x slower                                                   |
| many_optionals             | 626 us                                                   | 924 us: 1.47x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 48.6 ms: 2.39x slower                                                   |
| telco                      | 10.5 ms                                                  | 163 ms: 15.61x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 2.17 sec: 268.91x slower                                                |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (29): json_dumps, chaos, xml_etree_generate, fannkuch, coverage, logging_silent, sympy_sum, xml_etree_process, richards, genshi_text, typing_runtime_protocols, mako, json, crypto_pyaes, pidigits, asyncio_websockets, django_template, unpickle_pure_python, docutils, coroutines, deltablue, sympy_expand, json_loads, genshi_xml, bench_thread_pool, sympy_str, pickle_pure_python, nbody, scimark_lu
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x