# Results vs. 3.13.0

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: linux-aarch64
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.030x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.02 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| async_tree_none            | 497 ms                                                   | 425 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 560 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 422 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 725 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 729 ms: 1.06x faster                                                    |
| coroutines                 | 28.5 ms                                                  | 28.4 ms: 1.00x faster                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.05x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| float          | 93.3 ms                                                  | 91.8 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                   |
| regex_dna      | 253 ms                                                   | 247 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 197 ms                                                   | 185 ms: 1.06x faster                                                    |
| xml_etree_iterparse | 149 ms                                                   | 146 ms: 1.02x faster                                                    |
| pickle_pure_python  | 357 us                                                   | 368 us: 1.03x slower                                                    |
| tomli_loads         | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_process, json_dumps, xml_etree_generate, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                                   |
| python_startup_no_site | 8.73 ms                                                  | 8.58 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.10x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 27.3 ms: 1.01x faster                                                   |
| mako            | 13.4 ms                                                  | 13.3 ms: 1.01x faster                                                   |
| django_template | 41.6 ms                                                  | 41.4 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.28 ms: 1.47x faster                                                   |
| deepcopy                   | 447 us                                                   | 331 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 37.6 us: 1.34x faster                                                   |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| async_tree_none            | 497 ms                                                   | 425 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 560 ms: 1.16x faster                                                    |
| go                         | 160 ms                                                   | 138 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.54 us: 1.15x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 5.12 ms: 1.13x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 422 ms: 1.11x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.03 ms: 1.09x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 20.9 ms: 1.08x faster                                                   |
| generators                 | 37.6 ms                                                  | 34.7 ms: 1.08x faster                                                   |
| xml_etree_parse            | 197 ms                                                   | 185 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 725 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 729 ms: 1.06x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.21 sec: 1.05x faster                                                  |
| thrift                     | 968 us                                                   | 924 us: 1.05x faster                                                    |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| json                       | 5.73 ms                                                  | 5.56 ms: 1.03x faster                                                   |
| 2to3                       | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.02x faster                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 81.8 ms: 1.02x faster                                                   |
| regex_dna                  | 253 ms                                                   | 247 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 146 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 82.1 ms: 1.02x faster                                                   |
| python_startup_no_site     | 8.73 ms                                                  | 8.58 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 911 ms: 1.02x faster                                                    |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.02x faster                                                    |
| float                      | 93.3 ms                                                  | 91.8 ms: 1.02x faster                                                   |
| genshi_text                | 27.7 ms                                                  | 27.3 ms: 1.01x faster                                                   |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                                  |
| mako                       | 13.4 ms                                                  | 13.3 ms: 1.01x faster                                                   |
| django_template            | 41.6 ms                                                  | 41.4 ms: 1.01x faster                                                   |
| comprehensions             | 20.4 us                                                  | 20.3 us: 1.01x faster                                                   |
| coroutines                 | 28.5 ms                                                  | 28.4 ms: 1.00x faster                                                   |
| raytrace                   | 300 ms                                                   | 302 ms: 1.01x slower                                                    |
| sympy_expand               | 457 ms                                                   | 462 ms: 1.01x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.89 ms: 1.02x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                   |
| pickle_pure_python         | 357 us                                                   | 368 us: 1.03x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.02 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.05x slower                                                  |
| telco                      | 9.74 ms                                                  | 10.2 ms: 1.05x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                                  |
| scimark_fft                | 447 ms                                                   | 471 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (36): xml_etree_process, logging_format, coverage, richards, sympy_integrate, sympy_sum, regex_compile, richards_super, html5lib, json_dumps, xml_etree_generate, logging_silent, typing_runtime_protocols, tornado_http, scimark_sparse_mat_mult, bpe_tokeniser, fannkuch, sqlglot_transpile, sympy_str, logging_simple, hexiom, sqlglot_normalize, async_generators, json_loads, mdp, nqueens, regex_effbot, spectral_norm, pyflate, pidigits, sqlglot_optimize, asyncio_websockets, genshi_xml, chaos, unpickle_pure_python, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x