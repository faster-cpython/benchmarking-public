# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.029x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 296 ms: 1.02x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.02 sec: 1.04x slower                                                  |
| tornado_http   | 128 ms                                                   | 125 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 497 ms                                                   | 424 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 563 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 421 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 725 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 728 ms: 1.05x faster                                                    |
| async_generators           | 489 ms                                                   | 481 ms: 1.02x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 112 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.6 ms: 1.04x faster                                                   |
| regex_dna      | 253 ms                                                   | 248 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 188 ms: 1.05x faster                                                    |
| unpickle_pure_python | 251 us                                                   | 256 us: 1.02x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 366 us: 1.03x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (5): json_dumps, xml_etree_generate, json_loads, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| django_template | 41.6 ms                                                  | 42.5 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.28 ms: 1.47x faster                                                   |
| deepcopy                   | 447 us                                                   | 329 us: 1.36x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 37.8 us: 1.33x faster                                                   |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| async_tree_none            | 497 ms                                                   | 424 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.48 us: 1.17x faster                                                   |
| async_tree_memoization     | 651 ms                                                   | 563 ms: 1.15x faster                                                    |
| go                         | 160 ms                                                   | 138 ms: 1.15x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.12 ms: 1.13x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 421 ms: 1.12x faster                                                    |
| pathlib                    | 22.7 ms                                                  | 20.9 ms: 1.09x faster                                                   |
| generators                 | 37.6 ms                                                  | 34.7 ms: 1.08x faster                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 7.14 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 725 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 728 ms: 1.05x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 188 ms: 1.05x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| regex_v8                   | 31.8 ms                                                  | 30.6 ms: 1.04x faster                                                   |
| thrift                     | 968 us                                                   | 933 us: 1.04x faster                                                    |
| json                       | 5.73 ms                                                  | 5.53 ms: 1.04x faster                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| nbody                      | 114 ms                                                   | 112 ms: 1.03x faster                                                    |
| logging_format             | 7.82 us                                                  | 7.63 us: 1.02x faster                                                   |
| 2to3                       | 304 ms                                                   | 296 ms: 1.02x faster                                                    |
| tornado_http               | 128 ms                                                   | 125 ms: 1.02x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.02x faster                                                    |
| genshi_text                | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 81.9 ms: 1.02x faster                                                   |
| regex_dna                  | 253 ms                                                   | 248 ms: 1.02x faster                                                    |
| async_generators           | 489 ms                                                   | 481 ms: 1.02x faster                                                    |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.02x faster                                                    |
| spectral_norm              | 143 ms                                                   | 140 ms: 1.02x faster                                                    |
| sympy_sum                  | 144 ms                                                   | 141 ms: 1.02x faster                                                    |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.01x faster                                                    |
| scimark_fft                | 447 ms                                                   | 441 ms: 1.01x faster                                                    |
| logging_simple             | 7.07 us                                                  | 6.98 us: 1.01x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 920 ms: 1.01x faster                                                    |
| pyflate                    | 556 ms                                                   | 564 ms: 1.01x slower                                                    |
| raytrace                   | 300 ms                                                   | 305 ms: 1.02x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                  |
| django_template            | 41.6 ms                                                  | 42.5 ms: 1.02x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 256 us: 1.02x slower                                                    |
| chaos                      | 68.0 ms                                                  | 69.6 ms: 1.02x slower                                                   |
| pickle_pure_python         | 357 us                                                   | 366 us: 1.03x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.94 ms: 1.03x slower                                                   |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.02 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.05x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                  | 1.44 ms: 1.05x slower                                                   |
| telco                      | 9.74 ms                                                  | 10.5 ms: 1.08x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (36): html5lib, json_dumps, nqueens, scimark_sparse_mat_mult, genshi_xml, xml_etree_generate, richards, python_startup_no_site, regex_compile, sqlglot_optimize, sympy_integrate, logging_silent, richards_super, sympy_str, fannkuch, float, pprint_pformat, asyncio_websockets, json_loads, coverage, coroutines, sqlglot_normalize, mdp, pidigits, xml_etree_iterparse, xml_etree_process, bpe_tokeniser, mako, scimark_monte_carlo, sympy_expand, typing_runtime_protocols, regex_effbot, comprehensions, hexiom, sqlglot_transpile, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.029x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x