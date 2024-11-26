# Results vs. 3.13.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: linux-aarch64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.030x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 2.99 sec: 1.04x slower                                                  |
| tornado_http   | 128 ms                                                   | 124 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 497 ms                                                   | 418 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 558 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 413 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 716 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 726 ms: 1.06x faster                                                    |
| async_generators           | 489 ms                                                   | 477 ms: 1.03x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.4 ms: 1.05x faster                                                   |
| regex_effbot   | 4.89 ms                                                  | 5.03 ms: 1.03x slower                                                   |
| regex_dna      | 253 ms                                                   | 262 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 188 ms: 1.05x faster                                                    |
| json_loads           | 31.7 us                                                  | 31.3 us: 1.01x faster                                                   |
| unpickle_pure_python | 251 us                                                   | 254 us: 1.01x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 370 us: 1.04x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (4): json_dumps, xml_etree_generate, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                                   |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 28.1 ms: 1.01x slower                                                   |
| django_template | 41.6 ms                                                  | 42.6 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.26 ms: 1.48x faster                                                   |
| deepcopy                   | 447 us                                                   | 333 us: 1.34x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 37.6 us: 1.34x faster                                                   |
| async_tree_none            | 497 ms                                                   | 418 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                                   |
| async_tree_memoization     | 651 ms                                                   | 558 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.52 us: 1.16x faster                                                   |
| go                         | 160 ms                                                   | 139 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 413 ms: 1.14x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.16 ms: 1.12x faster                                                   |
| generators                 | 37.6 ms                                                  | 34.9 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 716 ms: 1.07x faster                                                    |
| pathlib                    | 22.7 ms                                                  | 21.3 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 726 ms: 1.06x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 133 ms: 1.05x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 188 ms: 1.05x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.4 ms: 1.05x faster                                                   |
| thrift                     | 968 us                                                   | 931 us: 1.04x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.23 sec: 1.04x faster                                                  |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| scimark_fft                | 447 ms                                                   | 434 ms: 1.03x faster                                                    |
| json                       | 5.73 ms                                                  | 5.56 ms: 1.03x faster                                                   |
| 2to3                       | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| telco                      | 9.74 ms                                                  | 9.47 ms: 1.03x faster                                                   |
| tornado_http               | 128 ms                                                   | 124 ms: 1.03x faster                                                    |
| async_generators           | 489 ms                                                   | 477 ms: 1.03x faster                                                    |
| sympy_sum                  | 144 ms                                                   | 141 ms: 1.02x faster                                                    |
| logging_silent             | 133 ns                                                   | 130 ns: 1.02x faster                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 82.0 ms: 1.02x faster                                                   |
| spectral_norm              | 143 ms                                                   | 140 ms: 1.02x faster                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 82.5 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 915 ms: 1.01x faster                                                    |
| json_loads                 | 31.7 us                                                  | 31.3 us: 1.01x faster                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 5.81 sec: 1.01x faster                                                  |
| mdp                        | 3.34 sec                                                 | 3.31 sec: 1.01x faster                                                  |
| unpickle_pure_python       | 251 us                                                   | 254 us: 1.01x slower                                                    |
| genshi_text                | 27.7 ms                                                  | 28.1 ms: 1.01x slower                                                   |
| raytrace                   | 300 ms                                                   | 304 ms: 1.01x slower                                                    |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.02x slower                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 1.30 ms: 1.02x slower                                                   |
| django_template            | 41.6 ms                                                  | 42.6 ms: 1.02x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.03x slower                                                   |
| chaos                      | 68.0 ms                                                  | 69.7 ms: 1.03x slower                                                   |
| deltablue                  | 3.82 ms                                                  | 3.93 ms: 1.03x slower                                                   |
| regex_effbot               | 4.89 ms                                                  | 5.03 ms: 1.03x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| docutils                   | 2.89 sec                                                 | 2.99 sec: 1.04x slower                                                  |
| regex_dna                  | 253 ms                                                   | 262 ms: 1.04x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 370 us: 1.04x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| bench_mp_pool              | 7.68 ms                                                  | 5.71 sec: 742.90x slower                                                |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                            |

Benchmark hidden because not significant (34): html5lib, richards, scimark_sparse_mat_mult, logging_format, json_dumps, python_startup_no_site, xml_etree_generate, regex_compile, richards_super, meteor_contest, scimark_sor, xml_etree_process, nqueens, logging_simple, coverage, pprint_pformat, sympy_str, sympy_expand, pyflate, asyncio_websockets, coroutines, pidigits, sqlglot_transpile, sqlglot_normalize, hexiom, fannkuch, xml_etree_iterparse, typing_runtime_protocols, genshi_xml, mako, sympy_integrate, float, sqlglot_optimize, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x