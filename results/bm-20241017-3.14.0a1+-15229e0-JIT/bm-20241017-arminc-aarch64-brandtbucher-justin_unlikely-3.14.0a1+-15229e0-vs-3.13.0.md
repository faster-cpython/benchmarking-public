# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-aarch64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.095x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 385 ms: 1.27x slower                                                      |
| docutils       | 2.89 sec                                                 | 3.62 sec: 1.25x slower                                                    |
| html5lib       | 66.4 ms                                                  | 71.1 ms: 1.07x slower                                                     |
| sphinx         | 1.17 sec                                                 | 1.45 sec: 1.24x slower                                                    |
| tornado_http   | 128 ms                                                   | 146 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                    | 1.19x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 539 ms: 1.20x faster                                                      |
| async_tree_none            | 497 ms                                                   | 458 ms: 1.08x faster                                                      |
| async_tree_memoization     | 651 ms                                                   | 603 ms: 1.08x faster                                                      |
| async_tree_none_tg         | 470 ms                                                   | 448 ms: 1.05x faster                                                      |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                                      |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 755 ms: 1.02x faster                                                      |
| coroutines                 | 28.5 ms                                                  | 28.6 ms: 1.00x slower                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.16 sec: 1.04x slower                                                    |
| async_generators           | 489 ms                                                   | 513 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.10x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 119 ms: 1.04x slower                                                      |
| float          | 93.3 ms                                                  | 97.2 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                    | 1.03x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 245 ms: 1.03x faster                                                      |
| regex_v8       | 31.8 ms                                                  | 31.4 ms: 1.01x faster                                                     |
| regex_compile  | 127 ms                                                   | 183 ms: 1.44x slower                                                      |
| Geometric mean | (ref)                                                    | 1.08x slower                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 185 ms: 1.06x faster                                                      |
| tomli_loads          | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                    |
| json_dumps           | 13.6 ms                                                  | 14.3 ms: 1.05x slower                                                     |
| unpickle_pure_python | 251 us                                                   | 266 us: 1.06x slower                                                      |
| pickle_pure_python   | 357 us                                                   | 387 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                              |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.6 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                    | 1.03x faster                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 50.9 ms: 1.22x slower                                                     |
| genshi_text     | 27.7 ms                                                  | 34.2 ms: 1.23x slower                                                     |
| genshi_xml      | 60.3 ms                                                  | 84.6 ms: 1.40x slower                                                     |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                              |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 39.3 us: 1.28x faster                                                     |
| async_tree_memoization_tg  | 649 ms                                                   | 539 ms: 1.20x faster                                                      |
| deepcopy                   | 447 us                                                   | 379 us: 1.18x faster                                                      |
| async_tree_none            | 497 ms                                                   | 458 ms: 1.08x faster                                                      |
| async_tree_memoization     | 651 ms                                                   | 603 ms: 1.08x faster                                                      |
| xml_etree_parse            | 197 ms                                                   | 185 ms: 1.06x faster                                                      |
| pathlib                    | 22.7 ms                                                  | 21.5 ms: 1.05x faster                                                     |
| python_startup             | 15.4 ms                                                  | 14.6 ms: 1.05x faster                                                     |
| async_tree_none_tg         | 470 ms                                                   | 448 ms: 1.05x faster                                                      |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                                      |
| regex_dna                  | 253 ms                                                   | 245 ms: 1.03x faster                                                      |
| deepcopy_reduce            | 4.07 us                                                  | 3.99 us: 1.02x faster                                                     |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 755 ms: 1.02x faster                                                      |
| regex_v8                   | 31.8 ms                                                  | 31.4 ms: 1.01x faster                                                     |
| coroutines                 | 28.5 ms                                                  | 28.6 ms: 1.00x slower                                                     |
| thrift                     | 968 us                                                   | 979 us: 1.01x slower                                                      |
| logging_silent             | 133 ns                                                   | 135 ns: 1.01x slower                                                      |
| bpe_tokeniser              | 5.87 sec                                                 | 6.04 sec: 1.03x slower                                                    |
| logging_format             | 7.82 us                                                  | 8.06 us: 1.03x slower                                                     |
| scimark_fft                | 447 ms                                                   | 463 ms: 1.04x slower                                                      |
| nbody                      | 114 ms                                                   | 119 ms: 1.04x slower                                                      |
| float                      | 93.3 ms                                                  | 97.2 ms: 1.04x slower                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.16 sec: 1.04x slower                                                    |
| mdp                        | 3.34 sec                                                 | 3.49 sec: 1.04x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                    |
| logging_simple             | 7.07 us                                                  | 7.41 us: 1.05x slower                                                     |
| async_generators           | 489 ms                                                   | 513 ms: 1.05x slower                                                      |
| json_dumps                 | 13.6 ms                                                  | 14.3 ms: 1.05x slower                                                     |
| unpickle_pure_python       | 251 us                                                   | 266 us: 1.06x slower                                                      |
| scimark_lu                 | 139 ms                                                   | 148 ms: 1.06x slower                                                      |
| html5lib                   | 66.4 ms                                                  | 71.1 ms: 1.07x slower                                                     |
| bench_thread_pool          | 1.27 ms                                                  | 1.37 ms: 1.08x slower                                                     |
| gc_traversal               | 5.77 ms                                                  | 6.23 ms: 1.08x slower                                                     |
| crypto_pyaes               | 83.7 ms                                                  | 90.7 ms: 1.08x slower                                                     |
| spectral_norm              | 143 ms                                                   | 155 ms: 1.08x slower                                                      |
| pickle_pure_python         | 357 us                                                   | 387 us: 1.08x slower                                                      |
| scimark_monte_carlo        | 83.6 ms                                                  | 90.7 ms: 1.09x slower                                                     |
| meteor_contest             | 114 ms                                                   | 124 ms: 1.09x slower                                                      |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 7.16 ms: 1.10x slower                                                     |
| create_gc_cycles           | 3.35 ms                                                  | 3.68 ms: 1.10x slower                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.10x slower                                                    |
| fannkuch                   | 461 ms                                                   | 508 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 193 us                                                   | 218 us: 1.13x slower                                                      |
| tornado_http               | 128 ms                                                   | 146 ms: 1.14x slower                                                      |
| pyflate                    | 556 ms                                                   | 643 ms: 1.15x slower                                                      |
| go                         | 160 ms                                                   | 185 ms: 1.16x slower                                                      |
| raytrace                   | 300 ms                                                   | 352 ms: 1.18x slower                                                      |
| richards                   | 53.6 ms                                                  | 63.8 ms: 1.19x slower                                                     |
| pycparser                  | 1.27 sec                                                 | 1.52 sec: 1.19x slower                                                    |
| richards_super             | 60.1 ms                                                  | 71.7 ms: 1.19x slower                                                     |
| deltablue                  | 3.82 ms                                                  | 4.63 ms: 1.21x slower                                                     |
| django_template            | 41.6 ms                                                  | 50.9 ms: 1.22x slower                                                     |
| comprehensions             | 20.4 us                                                  | 24.9 us: 1.22x slower                                                     |
| nqueens                    | 100 ms                                                   | 123 ms: 1.23x slower                                                      |
| genshi_text                | 27.7 ms                                                  | 34.2 ms: 1.23x slower                                                     |
| sqlglot_normalize          | 127 ms                                                   | 156 ms: 1.23x slower                                                      |
| sphinx                     | 1.17 sec                                                 | 1.45 sec: 1.24x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.71 ms: 1.24x slower                                                     |
| docutils                   | 2.89 sec                                                 | 3.62 sec: 1.25x slower                                                    |
| 2to3                       | 304 ms                                                   | 385 ms: 1.27x slower                                                      |
| chaos                      | 68.0 ms                                                  | 87.2 ms: 1.28x slower                                                     |
| sqlglot_transpile          | 1.73 ms                                                  | 2.24 ms: 1.29x slower                                                     |
| sympy_expand               | 457 ms                                                   | 592 ms: 1.30x slower                                                      |
| sqlglot_optimize           | 62.2 ms                                                  | 82.9 ms: 1.33x slower                                                     |
| pprint_safe_repr           | 926 ms                                                   | 1.24 sec: 1.34x slower                                                    |
| sympy_str                  | 264 ms                                                   | 363 ms: 1.37x slower                                                      |
| pprint_pformat             | 1.90 sec                                                 | 2.61 sec: 1.38x slower                                                    |
| genshi_xml                 | 60.3 ms                                                  | 84.6 ms: 1.40x slower                                                     |
| sympy_integrate            | 20.8 ms                                                  | 29.3 ms: 1.41x slower                                                     |
| regex_compile              | 127 ms                                                   | 183 ms: 1.44x slower                                                      |
| hexiom                     | 7.11 ms                                                  | 10.2 ms: 1.44x slower                                                     |
| pylint                     | 342 ms                                                   | 493 ms: 1.44x slower                                                      |
| sympy_sum                  | 144 ms                                                   | 216 ms: 1.51x slower                                                      |
| generators                 | 37.6 ms                                                  | 58.9 ms: 1.57x slower                                                     |
| bench_mp_pool              | 7.68 ms                                                  | 1.92 sec: 250.31x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.17x slower                                                              |

Benchmark hidden because not significant (12): xml_etree_generate, coverage, regex_effbot, python_startup_no_site, mako, xml_etree_process, json, json_loads, asyncio_websockets, pidigits, xml_etree_iterparse, telco
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.095x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.08x