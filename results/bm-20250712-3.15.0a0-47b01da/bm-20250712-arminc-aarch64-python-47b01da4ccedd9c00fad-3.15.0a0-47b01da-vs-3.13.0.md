# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-aarch64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.033x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 300 ms: 1.04x faster                                                    |
| docutils       | 2.96 sec                                                 | 2.93 sec: 1.01x faster                                                  |
| html5lib       | 65.6 ms                                                  | 61.5 ms: 1.07x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.12 sec: 1.07x faster                                                  |
| Geometric mean | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 473 ms: 1.40x faster                                                    |
| async_tree_none            | 504 ms                                                   | 374 ms: 1.35x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 883 ms: 1.32x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 872 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 652 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                    |
| async_generators           | 500 ms                                                   | 460 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.3 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.85 ms: 1.32x faster                                                   |
| regex_dna      | 263 ms                                                   | 221 ms: 1.19x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 28.6 ms: 1.14x faster                                                   |
| regex_compile  | 134 ms                                                   | 122 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.18x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                    |
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 111 ms: 1.06x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 78.8 ms: 1.04x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (4): unpickle_pure_python, json_dumps, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.59 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 59.7 ms: 1.03x faster                                                   |
| django_template | 39.4 ms                                                  | 41.7 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                  |
| deepcopy                   | 479 us                                                   | 321 us: 1.49x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.2 us: 1.42x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 473 ms: 1.40x faster                                                    |
| async_tree_none            | 504 ms                                                   | 374 ms: 1.35x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.85 ms: 1.32x faster                                                   |
| async_tree_io_tg           | 1.16 sec                                                 | 883 ms: 1.32x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 872 ms: 1.31x faster                                                    |
| go                         | 164 ms                                                   | 127 ms: 1.30x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 652 ms: 1.23x faster                                                    |
| spectral_norm              | 143 ms                                                   | 118 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.55 us: 1.19x faster                                                   |
| regex_dna                  | 263 ms                                                   | 221 ms: 1.19x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.4 ms: 1.14x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 28.6 ms: 1.14x faster                                                   |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                                    |
| float                      | 95.8 ms                                                  | 85.3 ms: 1.12x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                    |
| pyflate                    | 582 ms                                                   | 522 ms: 1.11x faster                                                    |
| regex_compile              | 134 ms                                                   | 122 ms: 1.10x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.82 sec: 1.09x faster                                                  |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.3 ms: 1.09x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.52 sec: 1.09x faster                                                  |
| pprint_safe_repr           | 962 ms                                                   | 884 ms: 1.09x faster                                                    |
| async_generators           | 500 ms                                                   | 460 ms: 1.09x faster                                                    |
| meteor_contest             | 117 ms                                                   | 108 ms: 1.09x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                  |
| scimark_fft                | 463 ms                                                   | 427 ms: 1.08x faster                                                    |
| pylint                     | 345 ms                                                   | 319 ms: 1.08x faster                                                    |
| hexiom                     | 7.34 ms                                                  | 6.79 ms: 1.08x faster                                                   |
| nqueens                    | 105 ms                                                   | 97.1 ms: 1.08x faster                                                   |
| sympy_sum                  | 151 ms                                                   | 141 ms: 1.08x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.80 us: 1.07x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.12 sec: 1.07x faster                                                  |
| pycparser                  | 1.34 sec                                                 | 1.26 sec: 1.07x faster                                                  |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| thrift                     | 1.01 ms                                                  | 946 us: 1.07x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 61.5 ms: 1.07x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.06x faster                                                    |
| chaos                      | 70.7 ms                                                  | 66.7 ms: 1.06x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.65 us: 1.06x faster                                                   |
| sympy_integrate            | 21.4 ms                                                  | 20.3 ms: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                  |
| richards                   | 54.5 ms                                                  | 52.2 ms: 1.04x faster                                                   |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                                    |
| 2to3                       | 313 ms                                                   | 300 ms: 1.04x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 78.8 ms: 1.04x faster                                                   |
| comprehensions             | 20.8 us                                                  | 20.0 us: 1.04x faster                                                   |
| genshi_xml                 | 61.6 ms                                                  | 59.7 ms: 1.03x faster                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 8.59 ms: 1.02x faster                                                   |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 2.93 sec: 1.01x faster                                                  |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.90 ms: 1.04x slower                                                   |
| connected_components       | 547 ms                                                   | 574 ms: 1.05x slower                                                    |
| raytrace                   | 310 ms                                                   | 326 ms: 1.05x slower                                                    |
| shortest_path              | 565 ms                                                   | 594 ms: 1.05x slower                                                    |
| django_template            | 39.4 ms                                                  | 41.7 ms: 1.06x slower                                                   |
| many_optionals             | 626 us                                                   | 745 us: 1.19x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 7.17 ms: 1.21x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 4.13 ms: 1.22x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 27.8 ms: 1.37x slower                                                   |
| telco                      | 10.5 ms                                                  | 166 ms: 15.87x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 2.81 sec: 347.99x slower                                                |
| Geometric mean             | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (23): genshi_text, json, pathlib, mako, sympy_expand, fannkuch, typing_runtime_protocols, logging_simple, unpickle_pure_python, pidigits, coverage, crypto_pyaes, asyncio_websockets, json_dumps, json_loads, scimark_lu, coroutines, deltablue, richards_super, bench_thread_pool, sympy_str, nbody, pickle_pure_python
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x