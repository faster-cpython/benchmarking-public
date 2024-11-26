# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.031x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 294 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 552 ms: 1.18x faster                                                    |
| async_tree_none            | 497 ms                                                   | 424 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 412 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 721 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 728 ms: 1.05x faster                                                    |
| async_generators           | 489 ms                                                   | 476 ms: 1.03x faster                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.7 ms: 1.04x faster                                                   |
| regex_effbot   | 4.89 ms                                                  | 4.99 ms: 1.02x slower                                                   |
| regex_dna      | 253 ms                                                   | 259 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 186 ms: 1.06x faster                                                    |
| json_loads           | 31.7 us                                                  | 31.2 us: 1.02x faster                                                   |
| unpickle_pure_python | 251 us                                                   | 254 us: 1.01x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 362 us: 1.01x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (4): json_dumps, xml_etree_generate, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                                   |
| python_startup_no_site | 8.73 ms                                                  | 8.61 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.10x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 42.2 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.28 ms: 1.47x faster                                                   |
| deepcopy                   | 447 us                                                   | 335 us: 1.34x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 38.1 us: 1.32x faster                                                   |
| python_startup             | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 552 ms: 1.18x faster                                                    |
| async_tree_none            | 497 ms                                                   | 424 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 555 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.52 us: 1.15x faster                                                   |
| go                         | 160 ms                                                   | 138 ms: 1.15x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.02 ms: 1.15x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 412 ms: 1.14x faster                                                    |
| generators                 | 37.6 ms                                                  | 34.7 ms: 1.08x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.2 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 721 ms: 1.07x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 186 ms: 1.06x faster                                                    |
| thrift                     | 968 us                                                   | 920 us: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 728 ms: 1.05x faster                                                    |
| scimark_fft                | 447 ms                                                   | 427 ms: 1.05x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 133 ms: 1.05x faster                                                    |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.7 ms: 1.04x faster                                                   |
| json                       | 5.73 ms                                                  | 5.53 ms: 1.04x faster                                                   |
| pycparser                  | 1.27 sec                                                 | 1.23 sec: 1.03x faster                                                  |
| 2to3                       | 304 ms                                                   | 294 ms: 1.03x faster                                                    |
| telco                      | 9.74 ms                                                  | 9.45 ms: 1.03x faster                                                   |
| sympy_sum                  | 144 ms                                                   | 140 ms: 1.03x faster                                                    |
| async_generators           | 489 ms                                                   | 476 ms: 1.03x faster                                                    |
| logging_silent             | 133 ns                                                   | 130 ns: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.37 ms: 1.02x faster                                                   |
| nqueens                    | 100 ms                                                   | 98.0 ms: 1.02x faster                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 82.0 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 907 ms: 1.02x faster                                                    |
| json_loads                 | 31.7 us                                                  | 31.2 us: 1.02x faster                                                   |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.01x faster                                                    |
| python_startup_no_site     | 8.73 ms                                                  | 8.61 ms: 1.01x faster                                                   |
| richards_super             | 60.1 ms                                                  | 59.3 ms: 1.01x faster                                                   |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.89 sec: 1.01x faster                                                  |
| bpe_tokeniser              | 5.87 sec                                                 | 5.85 sec: 1.00x faster                                                  |
| comprehensions             | 20.4 us                                                  | 20.6 us: 1.01x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 254 us: 1.01x slower                                                    |
| django_template            | 41.6 ms                                                  | 42.2 ms: 1.01x slower                                                   |
| pickle_pure_python         | 357 us                                                   | 362 us: 1.01x slower                                                    |
| fannkuch                   | 461 ms                                                   | 468 ms: 1.01x slower                                                    |
| raytrace                   | 300 ms                                                   | 305 ms: 1.02x slower                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.30 ms: 1.02x slower                                                   |
| chaos                      | 68.0 ms                                                  | 69.4 ms: 1.02x slower                                                   |
| regex_effbot               | 4.89 ms                                                  | 4.99 ms: 1.02x slower                                                   |
| regex_dna                  | 253 ms                                                   | 259 ms: 1.02x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.92 ms: 1.03x slower                                                   |
| tomli_loads                | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                  | 1.43 ms: 1.04x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| pyflate                    | 556 ms                                                   | 579 ms: 1.04x slower                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 4.42 sec: 575.76x slower                                                |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                            |

Benchmark hidden because not significant (30): json_dumps, html5lib, logging_format, richards, xml_etree_generate, scimark_monte_carlo, regex_compile, xml_etree_iterparse, genshi_text, xml_etree_process, sympy_str, float, mdp, spectral_norm, typing_runtime_protocols, sympy_expand, sqlglot_transpile, hexiom, coroutines, asyncio_websockets, coverage, genshi_xml, sqlglot_normalize, sympy_integrate, pidigits, logging_simple, tornado_http, sqlglot_optimize, mako, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x