# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.043x faster
- HPT reliability: 96.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 306 ms: 1.02x faster                                                     |
| docutils       | 2.96 sec                                                 | 3.13 sec: 1.06x slower                                                   |
| html5lib       | 65.6 ms                                                  | 62.2 ms: 1.05x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 479 ms: 1.39x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 377 ms: 1.29x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 886 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 919 ms: 1.27x faster                                                     |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                     |
| async_generators           | 500 ms                                                   | 471 ms: 1.06x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 81.4 ms: 1.18x faster                                                    |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.01 ms: 1.27x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                    |
| regex_dna      | 263 ms                                                   | 247 ms: 1.06x faster                                                     |
| regex_compile  | 134 ms                                                   | 126 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                    | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 173 ms: 1.17x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.40 sec: 1.11x faster                                                   |
| xml_etree_generate  | 118 ms                                                   | 108 ms: 1.09x faster                                                     |
| xml_etree_process   | 82.1 ms                                                  | 77.6 ms: 1.06x faster                                                    |
| pickle_pure_python  | 374 us                                                   | 397 us: 1.06x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (3): json_dumps, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.07x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                                    |
| mako           | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 60.9 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.63 sec: 2.11x faster                                                   |
| deepcopy_memo              | 53.0 us                                                  | 36.3 us: 1.46x faster                                                    |
| deepcopy                   | 479 us                                                   | 338 us: 1.42x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 479 ms: 1.39x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 377 ms: 1.29x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 886 ms: 1.29x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.01 ms: 1.27x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 919 ms: 1.27x faster                                                     |
| async_tree_none            | 504 ms                                                   | 398 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                     |
| float                      | 95.8 ms                                                  | 81.4 ms: 1.18x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 173 ms: 1.17x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.69 us: 1.15x faster                                                    |
| spectral_norm              | 143 ms                                                   | 126 ms: 1.14x faster                                                     |
| richards_super             | 60.8 ms                                                  | 53.5 ms: 1.14x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.5 ms: 1.14x faster                                                    |
| richards                   | 54.5 ms                                                  | 48.1 ms: 1.13x faster                                                    |
| scimark_fft                | 463 ms                                                   | 414 ms: 1.12x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.40 sec: 1.11x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.68 us: 1.11x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.09x faster                                                     |
| scimark_sor                | 164 ms                                                   | 151 ms: 1.09x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.53 sec: 1.09x faster                                                   |
| pylint                     | 345 ms                                                   | 320 ms: 1.08x faster                                                     |
| coverage                   | 106 ms                                                   | 98.2 ms: 1.08x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.79 ms: 1.07x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                                    |
| regex_dna                  | 263 ms                                                   | 247 ms: 1.06x faster                                                     |
| async_generators           | 500 ms                                                   | 471 ms: 1.06x faster                                                     |
| regex_compile              | 134 ms                                                   | 126 ms: 1.06x faster                                                     |
| xml_etree_process          | 82.1 ms                                                  | 77.6 ms: 1.06x faster                                                    |
| mako                       | 14.0 ms                                                  | 13.2 ms: 1.06x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 62.2 ms: 1.05x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.70 us: 1.05x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.04x faster                                                   |
| deltablue                  | 3.97 ms                                                  | 3.81 ms: 1.04x faster                                                    |
| logging_simple             | 7.25 us                                                  | 6.96 us: 1.04x faster                                                    |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                                     |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.03x faster                                                   |
| pyflate                    | 582 ms                                                   | 567 ms: 1.03x faster                                                     |
| 2to3                       | 313 ms                                                   | 306 ms: 1.02x faster                                                     |
| genshi_xml                 | 61.6 ms                                                  | 60.9 ms: 1.01x faster                                                    |
| sympy_str                  | 265 ms                                                   | 272 ms: 1.03x slower                                                     |
| pycparser                  | 1.34 sec                                                 | 1.38 sec: 1.03x slower                                                   |
| connected_components       | 547 ms                                                   | 569 ms: 1.04x slower                                                     |
| go                         | 164 ms                                                   | 171 ms: 1.04x slower                                                     |
| fannkuch                   | 478 ms                                                   | 498 ms: 1.04x slower                                                     |
| shortest_path              | 565 ms                                                   | 590 ms: 1.04x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.13 sec: 1.06x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.60 ms: 1.06x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 397 us: 1.06x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 211 us: 1.07x slower                                                     |
| hexiom                     | 7.34 ms                                                  | 7.91 ms: 1.08x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.62 ms: 1.12x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 94.9 ms: 1.12x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                    |
| comprehensions             | 20.8 us                                                  | 24.3 us: 1.17x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.40 sec: 1.21x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.17 sec: 1.21x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 26.3 ms: 1.29x slower                                                    |
| many_optionals             | 626 us                                                   | 878 us: 1.40x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 1.09 sec: 135.24x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (24): pathlib, scimark_monte_carlo, sympy_sum, sqlalchemy_declarative, scimark_sparse_mat_mult, scimark_lu, json_dumps, sympy_integrate, unpickle_pure_python, asyncio_websockets, python_startup, bench_thread_pool, json, coroutines, pidigits, sqlalchemy_imperative, chaos, nqueens, django_template, sympy_expand, nbody, raytrace, meteor_contest, json_loads
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (13) of results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 96.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x