# Results vs. 3.13.0

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: linux-aarch64
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.028x faster
- HPT reliability: 99.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 293 ms: 1.04x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.03 sec: 1.05x slower                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 545 ms: 1.19x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 550 ms: 1.18x faster                                                    |
| async_tree_none            | 497 ms                                                   | 428 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 420 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 708 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 722 ms: 1.06x faster                                                    |
| async_generators           | 489 ms                                                   | 475 ms: 1.03x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.16 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.07x faster                                                            |

Benchmark hidden because not significant (3): asyncio_websockets, coroutines, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 94.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                   |
| regex_compile  | 127 ms                                                   | 124 ms: 1.03x faster                                                    |
| regex_effbot   | 4.89 ms                                                  | 5.01 ms: 1.02x slower                                                   |
| regex_dna      | 253 ms                                                   | 260 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 31.7 us                                                  | 31.3 us: 1.01x faster                                                   |
| unpickle_pure_python | 251 us                                                   | 255 us: 1.02x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 364 us: 1.02x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| json_dumps           | 13.6 ms                                                  | 14.6 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| mako            | 13.4 ms                                                  | 13.6 ms: 1.01x slower                                                   |
| django_template | 41.6 ms                                                  | 42.4 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.37 ms: 1.41x faster                                                   |
| deepcopy                   | 447 us                                                   | 332 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 37.8 us: 1.33x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 545 ms: 1.19x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 550 ms: 1.18x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| go                         | 160 ms                                                   | 137 ms: 1.17x faster                                                    |
| async_tree_none            | 497 ms                                                   | 428 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.51 us: 1.16x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 5.09 ms: 1.13x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 420 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 708 ms: 1.09x faster                                                    |
| generators                 | 37.6 ms                                                  | 34.7 ms: 1.08x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.2 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 722 ms: 1.06x faster                                                    |
| telco                      | 9.74 ms                                                  | 9.31 ms: 1.05x faster                                                   |
| thrift                     | 968 us                                                   | 931 us: 1.04x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                    |
| 2to3                       | 304 ms                                                   | 293 ms: 1.04x faster                                                    |
| logging_format             | 7.82 us                                                  | 7.55 us: 1.04x faster                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 5.70 sec: 1.03x faster                                                  |
| async_generators           | 489 ms                                                   | 475 ms: 1.03x faster                                                    |
| json                       | 5.73 ms                                                  | 5.57 ms: 1.03x faster                                                   |
| pycparser                  | 1.27 sec                                                 | 1.24 sec: 1.03x faster                                                  |
| crypto_pyaes               | 83.7 ms                                                  | 81.5 ms: 1.03x faster                                                   |
| regex_v8                   | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                   |
| regex_compile              | 127 ms                                                   | 124 ms: 1.03x faster                                                    |
| logging_silent             | 133 ns                                                   | 130 ns: 1.03x faster                                                    |
| meteor_contest             | 114 ms                                                   | 111 ms: 1.02x faster                                                    |
| genshi_text                | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| spectral_norm              | 143 ms                                                   | 140 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 911 ms: 1.02x faster                                                    |
| logging_simple             | 7.07 us                                                  | 6.96 us: 1.02x faster                                                   |
| scimark_fft                | 447 ms                                                   | 441 ms: 1.01x faster                                                    |
| json_loads                 | 31.7 us                                                  | 31.3 us: 1.01x faster                                                   |
| coverage                   | 99.1 ms                                                  | 97.9 ms: 1.01x faster                                                   |
| pprint_pformat             | 1.90 sec                                                 | 1.89 sec: 1.01x faster                                                  |
| sympy_integrate            | 20.8 ms                                                  | 21.1 ms: 1.01x slower                                                   |
| mako                       | 13.4 ms                                                  | 13.6 ms: 1.01x slower                                                   |
| float                      | 93.3 ms                                                  | 94.6 ms: 1.01x slower                                                   |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.02x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 255 us: 1.02x slower                                                    |
| django_template            | 41.6 ms                                                  | 42.4 ms: 1.02x slower                                                   |
| pickle_pure_python         | 357 us                                                   | 364 us: 1.02x slower                                                    |
| fannkuch                   | 461 ms                                                   | 471 ms: 1.02x slower                                                    |
| regex_effbot               | 4.89 ms                                                  | 5.01 ms: 1.02x slower                                                   |
| deltablue                  | 3.82 ms                                                  | 3.92 ms: 1.03x slower                                                   |
| regex_dna                  | 253 ms                                                   | 260 ms: 1.03x slower                                                    |
| raytrace                   | 300 ms                                                   | 310 ms: 1.03x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.42 ms: 1.03x slower                                                   |
| chaos                      | 68.0 ms                                                  | 70.5 ms: 1.04x slower                                                   |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| pyflate                    | 556 ms                                                   | 582 ms: 1.05x slower                                                    |
| docutils                   | 2.89 sec                                                 | 3.03 sec: 1.05x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.16 sec: 1.05x slower                                                  |
| json_dumps                 | 13.6 ms                                                  | 14.6 ms: 1.08x slower                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 5.11 sec: 665.37x slower                                                |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                            |

Benchmark hidden because not significant (30): html5lib, tornado_http, richards, sympy_sum, xml_etree_generate, genshi_xml, xml_etree_process, python_startup_no_site, sqlglot_normalize, asyncio_websockets, mdp, richards_super, sympy_expand, sympy_str, nqueens, coroutines, hexiom, sqlglot_optimize, bench_thread_pool, nbody, pidigits, sqlglot_transpile, xml_etree_parse, scimark_sor, scimark_monte_carlo, typing_runtime_protocols, scimark_sparse_mat_mult, async_tree_io_tg, xml_etree_iterparse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 99.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x