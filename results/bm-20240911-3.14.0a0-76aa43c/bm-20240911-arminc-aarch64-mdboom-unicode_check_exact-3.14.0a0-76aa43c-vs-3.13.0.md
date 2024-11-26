# Results vs. 3.13.0

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-aarch64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.035x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.89 sec                                                 | 3.00 sec: 1.04x slower                                                 |
| Geometric mean | (ref)                                                    | 1.01x faster                                                           |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.18x faster                                                   |
| async_tree_none            | 497 ms                                                   | 424 ms: 1.17x faster                                                   |
| async_tree_memoization     | 651 ms                                                   | 555 ms: 1.17x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 722 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 727 ms: 1.05x faster                                                   |
| async_generators           | 489 ms                                                   | 476 ms: 1.03x faster                                                   |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                 |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                   |
| float          | 93.3 ms                                                  | 92.1 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                    | 1.02x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 246 ms: 1.03x faster                                                   |
| regex_v8       | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                  |
| regex_compile  | 127 ms                                                   | 124 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|--------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse    | 197 ms                                                   | 187 ms: 1.05x faster                                                   |
| xml_etree_generate | 113 ms                                                   | 111 ms: 1.02x faster                                                   |
| tomli_loads        | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                                 |
| Geometric mean     | (ref)                                                    | 1.01x faster                                                           |

Benchmark hidden because not significant (6): xml_etree_process, xml_etree_iterparse, json_dumps, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                  |
| python_startup_no_site | 8.73 ms                                                  | 8.62 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                    | 1.10x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 27.3 ms: 1.01x faster                                                  |
| django_template | 41.6 ms                                                  | 42.7 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                           |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.27 ms: 1.48x faster                                                  |
| deepcopy                   | 447 us                                                   | 328 us: 1.36x faster                                                   |
| deepcopy_memo              | 50.4 us                                                  | 37.3 us: 1.35x faster                                                  |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                  |
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.18x faster                                                   |
| go                         | 160 ms                                                   | 136 ms: 1.18x faster                                                   |
| async_tree_none            | 497 ms                                                   | 424 ms: 1.17x faster                                                   |
| async_tree_memoization     | 651 ms                                                   | 555 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.49 us: 1.17x faster                                                  |
| gc_traversal               | 5.77 ms                                                  | 5.02 ms: 1.15x faster                                                  |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 7.05 ms: 1.09x faster                                                  |
| generators                 | 37.6 ms                                                  | 34.7 ms: 1.08x faster                                                  |
| pathlib                    | 22.7 ms                                                  | 21.2 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 722 ms: 1.06x faster                                                   |
| pycparser                  | 1.27 sec                                                 | 1.20 sec: 1.06x faster                                                 |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 727 ms: 1.05x faster                                                   |
| xml_etree_parse            | 197 ms                                                   | 187 ms: 1.05x faster                                                   |
| thrift                     | 968 us                                                   | 921 us: 1.05x faster                                                   |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 1.22 ms: 1.04x faster                                                  |
| json                       | 5.73 ms                                                  | 5.54 ms: 1.03x faster                                                  |
| sympy_sum                  | 144 ms                                                   | 139 ms: 1.03x faster                                                   |
| scimark_sor                | 160 ms                                                   | 155 ms: 1.03x faster                                                   |
| nqueens                    | 100 ms                                                   | 97.0 ms: 1.03x faster                                                  |
| regex_dna                  | 253 ms                                                   | 246 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                                   |
| regex_v8                   | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                  |
| logging_format             | 7.82 us                                                  | 7.62 us: 1.03x faster                                                  |
| async_generators           | 489 ms                                                   | 476 ms: 1.03x faster                                                   |
| regex_compile              | 127 ms                                                   | 124 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 904 ms: 1.02x faster                                                   |
| xml_etree_generate         | 113 ms                                                   | 111 ms: 1.02x faster                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 81.9 ms: 1.02x faster                                                  |
| logging_simple             | 7.07 us                                                  | 6.92 us: 1.02x faster                                                  |
| pprint_pformat             | 1.90 sec                                                 | 1.86 sec: 1.02x faster                                                 |
| scimark_fft                | 447 ms                                                   | 439 ms: 1.02x faster                                                   |
| mdp                        | 3.34 sec                                                 | 3.29 sec: 1.02x faster                                                 |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.02x faster                                                   |
| genshi_text                | 27.7 ms                                                  | 27.3 ms: 1.01x faster                                                  |
| coverage                   | 99.1 ms                                                  | 97.7 ms: 1.01x faster                                                  |
| typing_runtime_protocols   | 193 us                                                   | 191 us: 1.01x faster                                                   |
| float                      | 93.3 ms                                                  | 92.1 ms: 1.01x faster                                                  |
| python_startup_no_site     | 8.73 ms                                                  | 8.62 ms: 1.01x faster                                                  |
| richards_super             | 60.1 ms                                                  | 59.4 ms: 1.01x faster                                                  |
| sympy_str                  | 264 ms                                                   | 261 ms: 1.01x faster                                                   |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                  |
| bpe_tokeniser              | 5.87 sec                                                 | 5.83 sec: 1.01x faster                                                 |
| raytrace                   | 300 ms                                                   | 302 ms: 1.01x slower                                                   |
| deltablue                  | 3.82 ms                                                  | 3.89 ms: 1.02x slower                                                  |
| django_template            | 41.6 ms                                                  | 42.7 ms: 1.03x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                                 |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                 |
| docutils                   | 2.89 sec                                                 | 3.00 sec: 1.04x slower                                                 |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                                 |
| telco                      | 9.74 ms                                                  | 10.2 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                           |

Benchmark hidden because not significant (31): html5lib, scimark_sparse_mat_mult, 2to3, genshi_xml, richards, scimark_monte_carlo, xml_etree_process, sympy_integrate, tornado_http, xml_etree_iterparse, logging_silent, spectral_norm, json_dumps, fannkuch, mako, unpickle_pure_python, asyncio_websockets, sqlglot_transpile, sqlglot_normalize, json_loads, hexiom, sympy_expand, pidigits, comprehensions, sqlglot_optimize, pickle_pure_python, pyflate, chaos, regex_effbot, sqlglot_parse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x