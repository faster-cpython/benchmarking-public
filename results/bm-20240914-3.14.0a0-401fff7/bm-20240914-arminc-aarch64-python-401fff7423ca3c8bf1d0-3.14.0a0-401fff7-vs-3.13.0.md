# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.030x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 497 ms                                                   | 424 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 558 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 422 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 728 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 737 ms: 1.04x faster                                                    |
| async_generators           | 489 ms                                                   | 483 ms: 1.01x faster                                                    |
| coroutines                 | 28.5 ms                                                  | 28.7 ms: 1.01x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.19 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| float          | 93.3 ms                                                  | 92.7 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| regex_dna      | 253 ms                                                   | 249 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse    | 197 ms                                                   | 189 ms: 1.04x faster                                                    |
| pickle_pure_python | 357 us                                                   | 362 us: 1.01x slower                                                    |
| tomli_loads        | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| Geometric mean     | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (6): json_dumps, xml_etree_generate, xml_etree_process, xml_etree_iterparse, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                                   |
| python_startup_no_site | 8.73 ms                                                  | 8.62 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.10x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.33 ms: 1.44x faster                                                   |
| deepcopy                   | 447 us                                                   | 334 us: 1.34x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 37.7 us: 1.34x faster                                                   |
| python_startup             | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                                   |
| async_tree_none            | 497 ms                                                   | 424 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 558 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.52 us: 1.16x faster                                                   |
| go                         | 160 ms                                                   | 139 ms: 1.15x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.18 ms: 1.12x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 422 ms: 1.11x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.01 ms: 1.10x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 20.7 ms: 1.09x faster                                                   |
| generators                 | 37.6 ms                                                  | 34.7 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 728 ms: 1.06x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| pycparser                  | 1.27 sec                                                 | 1.22 sec: 1.05x faster                                                  |
| thrift                     | 968 us                                                   | 931 us: 1.04x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 189 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 737 ms: 1.04x faster                                                    |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.23 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                                    |
| json                       | 5.73 ms                                                  | 5.57 ms: 1.03x faster                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 81.3 ms: 1.03x faster                                                   |
| 2to3                       | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| logging_format             | 7.82 us                                                  | 7.63 us: 1.02x faster                                                   |
| spectral_norm              | 143 ms                                                   | 140 ms: 1.02x faster                                                    |
| meteor_contest             | 114 ms                                                   | 111 ms: 1.02x faster                                                    |
| richards                   | 53.6 ms                                                  | 52.7 ms: 1.02x faster                                                   |
| regex_dna                  | 253 ms                                                   | 249 ms: 1.02x faster                                                    |
| coverage                   | 99.1 ms                                                  | 97.5 ms: 1.02x faster                                                   |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.01x faster                                                    |
| async_generators           | 489 ms                                                   | 483 ms: 1.01x faster                                                    |
| python_startup_no_site     | 8.73 ms                                                  | 8.62 ms: 1.01x faster                                                   |
| richards_super             | 60.1 ms                                                  | 59.4 ms: 1.01x faster                                                   |
| scimark_fft                | 447 ms                                                   | 442 ms: 1.01x faster                                                    |
| float                      | 93.3 ms                                                  | 92.7 ms: 1.01x faster                                                   |
| pprint_pformat             | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                                  |
| coroutines                 | 28.5 ms                                                  | 28.7 ms: 1.01x slower                                                   |
| pyflate                    | 556 ms                                                   | 562 ms: 1.01x slower                                                    |
| raytrace                   | 300 ms                                                   | 303 ms: 1.01x slower                                                    |
| telco                      | 9.74 ms                                                  | 9.86 ms: 1.01x slower                                                   |
| mako                       | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| pickle_pure_python         | 357 us                                                   | 362 us: 1.01x slower                                                    |
| chaos                      | 68.0 ms                                                  | 69.0 ms: 1.02x slower                                                   |
| deltablue                  | 3.82 ms                                                  | 3.92 ms: 1.03x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.19 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (36): json_dumps, scimark_sparse_mat_mult, sympy_sum, xml_etree_generate, html5lib, scimark_monte_carlo, xml_etree_process, logging_simple, genshi_text, regex_compile, xml_etree_iterparse, typing_runtime_protocols, logging_silent, tornado_http, mdp, bpe_tokeniser, pprint_safe_repr, fannkuch, hexiom, sympy_integrate, sympy_str, genshi_xml, django_template, sqlglot_optimize, asyncio_websockets, json_loads, pidigits, sqlglot_normalize, sqlglot_transpile, regex_effbot, nqueens, unpickle_pure_python, sympy_expand, comprehensions, sqlglot_parse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x