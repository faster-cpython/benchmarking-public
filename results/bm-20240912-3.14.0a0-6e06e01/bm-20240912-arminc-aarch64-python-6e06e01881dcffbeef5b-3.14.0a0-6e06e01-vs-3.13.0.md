# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-aarch64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.027x faster
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 297 ms: 1.02x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.05 sec: 1.06x slower                                                  |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 497 ms                                                   | 421 ms: 1.18x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 562 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 718 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 720 ms: 1.06x faster                                                    |
| async_generators           | 489 ms                                                   | 479 ms: 1.02x faster                                                    |
| coroutines                 | 28.5 ms                                                  | 28.9 ms: 1.01x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.5 ms: 1.04x faster                                                   |
| regex_dna      | 253 ms                                                   | 255 ms: 1.01x slower                                                    |
| regex_effbot   | 4.89 ms                                                  | 4.95 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|--------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python | 357 us                                                   | 373 us: 1.04x slower                                                    |
| tomli_loads        | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| Geometric mean     | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (7): xml_etree_parse, json_dumps, xml_etree_generate, xml_etree_iterparse, json_loads, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                   |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| django_template | 41.6 ms                                                  | 42.3 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.27 ms: 1.48x faster                                                   |
| deepcopy_memo              | 50.4 us                                                  | 37.5 us: 1.34x faster                                                   |
| deepcopy                   | 447 us                                                   | 337 us: 1.33x faster                                                    |
| async_tree_none            | 497 ms                                                   | 421 ms: 1.18x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 562 ms: 1.16x faster                                                    |
| go                         | 160 ms                                                   | 139 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.57 us: 1.14x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 5.09 ms: 1.13x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.11 ms: 1.08x faster                                                   |
| generators                 | 37.6 ms                                                  | 34.9 ms: 1.08x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.1 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 718 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 720 ms: 1.06x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.5 ms: 1.04x faster                                                   |
| thrift                     | 968 us                                                   | 931 us: 1.04x faster                                                    |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.04x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.23 sec: 1.03x faster                                                  |
| json                       | 5.73 ms                                                  | 5.59 ms: 1.03x faster                                                   |
| 2to3                       | 304 ms                                                   | 297 ms: 1.02x faster                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 81.9 ms: 1.02x faster                                                   |
| async_generators           | 489 ms                                                   | 479 ms: 1.02x faster                                                    |
| spectral_norm              | 143 ms                                                   | 140 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 82.1 ms: 1.02x faster                                                   |
| nqueens                    | 100 ms                                                   | 98.4 ms: 1.02x faster                                                   |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| coverage                   | 99.1 ms                                                  | 97.6 ms: 1.02x faster                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 5.83 sec: 1.01x faster                                                  |
| comprehensions             | 20.4 us                                                  | 20.5 us: 1.01x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                                  |
| regex_dna                  | 253 ms                                                   | 255 ms: 1.01x slower                                                    |
| mako                       | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| mdp                        | 3.34 sec                                                 | 3.37 sec: 1.01x slower                                                  |
| regex_effbot               | 4.89 ms                                                  | 4.95 ms: 1.01x slower                                                   |
| coroutines                 | 28.5 ms                                                  | 28.9 ms: 1.01x slower                                                   |
| deltablue                  | 3.82 ms                                                  | 3.87 ms: 1.01x slower                                                   |
| django_template            | 41.6 ms                                                  | 42.3 ms: 1.02x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                  | 1.43 ms: 1.04x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| pyflate                    | 556 ms                                                   | 580 ms: 1.04x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 373 us: 1.04x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| telco                      | 9.74 ms                                                  | 10.2 ms: 1.05x slower                                                   |
| docutils                   | 2.89 sec                                                 | 3.05 sec: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (38): xml_etree_parse, richards, scimark_sor, json_dumps, genshi_text, html5lib, xml_etree_generate, sympy_sum, typing_runtime_protocols, scimark_sparse_mat_mult, sympy_integrate, xml_etree_iterparse, python_startup_no_site, regex_compile, float, scimark_fft, sympy_str, logging_silent, sqlglot_normalize, pprint_safe_repr, richards_super, json_loads, pidigits, genshi_xml, fannkuch, asyncio_websockets, sqlglot_optimize, raytrace, chaos, tornado_http, unpickle_pure_python, sqlglot_transpile, hexiom, logging_format, sympy_expand, xml_etree_process, logging_simple, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 99.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x