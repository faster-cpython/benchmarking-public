# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-aarch64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.094x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 382 ms: 1.26x slower                                         |
| docutils       | 2.89 sec                                                 | 3.61 sec: 1.25x slower                                       |
| html5lib       | 66.4 ms                                                  | 71.8 ms: 1.08x slower                                        |
| sphinx         | 1.17 sec                                                 | 1.46 sec: 1.25x slower                                       |
| tornado_http   | 128 ms                                                   | 147 ms: 1.15x slower                                         |
| Geometric mean | (ref)                                                    | 1.20x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 542 ms: 1.20x faster                                         |
| async_tree_memoization     | 651 ms                                                   | 605 ms: 1.08x faster                                         |
| async_tree_none            | 497 ms                                                   | 463 ms: 1.07x faster                                         |
| async_tree_none_tg         | 470 ms                                                   | 451 ms: 1.04x faster                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                         |
| coroutines                 | 28.5 ms                                                  | 28.9 ms: 1.01x slower                                        |
| async_generators           | 489 ms                                                   | 507 ms: 1.04x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.19 sec: 1.07x slower                                       |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.10x slower                                       |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 97.2 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 244 ms: 1.04x faster                                         |
| regex_compile  | 127 ms                                                   | 179 ms: 1.41x slower                                         |
| Geometric mean | (ref)                                                    | 1.08x slower                                                 |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 186 ms: 1.06x faster                                         |
| xml_etree_generate   | 113 ms                                                   | 111 ms: 1.02x faster                                         |
| tomli_loads          | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                       |
| json_dumps           | 13.6 ms                                                  | 14.4 ms: 1.06x slower                                        |
| unpickle_pure_python | 251 us                                                   | 268 us: 1.07x slower                                         |
| pickle_pure_python   | 357 us                                                   | 389 us: 1.09x slower                                         |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (3): xml_etree_process, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.7 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                        |
| genshi_text     | 27.7 ms                                                  | 34.2 ms: 1.23x slower                                        |
| django_template | 41.6 ms                                                  | 52.4 ms: 1.26x slower                                        |
| genshi_xml      | 60.3 ms                                                  | 84.1 ms: 1.39x slower                                        |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 39.2 us: 1.28x faster                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 542 ms: 1.20x faster                                         |
| deepcopy                   | 447 us                                                   | 377 us: 1.19x faster                                         |
| async_tree_memoization     | 651 ms                                                   | 605 ms: 1.08x faster                                         |
| async_tree_none            | 497 ms                                                   | 463 ms: 1.07x faster                                         |
| xml_etree_parse            | 197 ms                                                   | 186 ms: 1.06x faster                                         |
| pathlib                    | 22.7 ms                                                  | 21.6 ms: 1.05x faster                                        |
| python_startup             | 15.4 ms                                                  | 14.7 ms: 1.05x faster                                        |
| async_tree_none_tg         | 470 ms                                                   | 451 ms: 1.04x faster                                         |
| scimark_sor                | 160 ms                                                   | 154 ms: 1.04x faster                                         |
| regex_dna                  | 253 ms                                                   | 244 ms: 1.04x faster                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                         |
| deepcopy_reduce            | 4.07 us                                                  | 3.98 us: 1.02x faster                                        |
| xml_etree_generate         | 113 ms                                                   | 111 ms: 1.02x faster                                         |
| thrift                     | 968 us                                                   | 956 us: 1.01x faster                                         |
| mako                       | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                        |
| coroutines                 | 28.5 ms                                                  | 28.9 ms: 1.01x slower                                        |
| bpe_tokeniser              | 5.87 sec                                                 | 5.97 sec: 1.02x slower                                       |
| scimark_fft                | 447 ms                                                   | 454 ms: 1.02x slower                                         |
| coverage                   | 99.1 ms                                                  | 101 ms: 1.02x slower                                         |
| logging_format             | 7.82 us                                                  | 8.08 us: 1.03x slower                                        |
| async_generators           | 489 ms                                                   | 507 ms: 1.04x slower                                         |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                       |
| float                      | 93.3 ms                                                  | 97.2 ms: 1.04x slower                                        |
| mdp                        | 3.34 sec                                                 | 3.51 sec: 1.05x slower                                       |
| logging_simple             | 7.07 us                                                  | 7.45 us: 1.05x slower                                        |
| json_dumps                 | 13.6 ms                                                  | 14.4 ms: 1.06x slower                                        |
| unpickle_pure_python       | 251 us                                                   | 268 us: 1.07x slower                                         |
| scimark_monte_carlo        | 83.6 ms                                                  | 89.5 ms: 1.07x slower                                        |
| async_tree_io              | 1.11 sec                                                 | 1.19 sec: 1.07x slower                                       |
| bench_thread_pool          | 1.27 ms                                                  | 1.37 ms: 1.08x slower                                        |
| gc_traversal               | 5.77 ms                                                  | 6.22 ms: 1.08x slower                                        |
| html5lib                   | 66.4 ms                                                  | 71.8 ms: 1.08x slower                                        |
| scimark_lu                 | 139 ms                                                   | 151 ms: 1.08x slower                                         |
| meteor_contest             | 114 ms                                                   | 123 ms: 1.08x slower                                         |
| spectral_norm              | 143 ms                                                   | 155 ms: 1.08x slower                                         |
| crypto_pyaes               | 83.7 ms                                                  | 90.8 ms: 1.08x slower                                        |
| pickle_pure_python         | 357 us                                                   | 389 us: 1.09x slower                                         |
| fannkuch                   | 461 ms                                                   | 503 ms: 1.09x slower                                         |
| create_gc_cycles           | 3.35 ms                                                  | 3.67 ms: 1.10x slower                                        |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 7.16 ms: 1.10x slower                                        |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.10x slower                                       |
| pyflate                    | 556 ms                                                   | 615 ms: 1.11x slower                                         |
| typing_runtime_protocols   | 193 us                                                   | 218 us: 1.13x slower                                         |
| go                         | 160 ms                                                   | 184 ms: 1.15x slower                                         |
| tornado_http               | 128 ms                                                   | 147 ms: 1.15x slower                                         |
| raytrace                   | 300 ms                                                   | 349 ms: 1.17x slower                                         |
| richards_super             | 60.1 ms                                                  | 71.4 ms: 1.19x slower                                        |
| deltablue                  | 3.82 ms                                                  | 4.55 ms: 1.19x slower                                        |
| pycparser                  | 1.27 sec                                                 | 1.52 sec: 1.19x slower                                       |
| richards                   | 53.6 ms                                                  | 64.2 ms: 1.20x slower                                        |
| comprehensions             | 20.4 us                                                  | 24.7 us: 1.21x slower                                        |
| genshi_text                | 27.7 ms                                                  | 34.2 ms: 1.23x slower                                        |
| sqlglot_parse              | 1.38 ms                                                  | 1.70 ms: 1.23x slower                                        |
| sqlglot_normalize          | 127 ms                                                   | 157 ms: 1.24x slower                                         |
| nqueens                    | 100 ms                                                   | 125 ms: 1.25x slower                                         |
| sphinx                     | 1.17 sec                                                 | 1.46 sec: 1.25x slower                                       |
| docutils                   | 2.89 sec                                                 | 3.61 sec: 1.25x slower                                       |
| chaos                      | 68.0 ms                                                  | 85.0 ms: 1.25x slower                                        |
| 2to3                       | 304 ms                                                   | 382 ms: 1.26x slower                                         |
| django_template            | 41.6 ms                                                  | 52.4 ms: 1.26x slower                                        |
| sqlglot_transpile          | 1.73 ms                                                  | 2.20 ms: 1.27x slower                                        |
| sympy_expand               | 457 ms                                                   | 594 ms: 1.30x slower                                         |
| pprint_safe_repr           | 926 ms                                                   | 1.21 sec: 1.31x slower                                       |
| sqlglot_optimize           | 62.2 ms                                                  | 82.2 ms: 1.32x slower                                        |
| pprint_pformat             | 1.90 sec                                                 | 2.55 sec: 1.34x slower                                       |
| sympy_str                  | 264 ms                                                   | 357 ms: 1.35x slower                                         |
| genshi_xml                 | 60.3 ms                                                  | 84.1 ms: 1.39x slower                                        |
| regex_compile              | 127 ms                                                   | 179 ms: 1.41x slower                                         |
| sympy_integrate            | 20.8 ms                                                  | 29.4 ms: 1.41x slower                                        |
| pylint                     | 342 ms                                                   | 494 ms: 1.45x slower                                         |
| hexiom                     | 7.11 ms                                                  | 10.3 ms: 1.45x slower                                        |
| sympy_sum                  | 144 ms                                                   | 215 ms: 1.50x slower                                         |
| generators                 | 37.6 ms                                                  | 59.0 ms: 1.57x slower                                        |
| bench_mp_pool              | 7.68 ms                                                  | 1.45 sec: 188.77x slower                                     |
| Geometric mean             | (ref)                                                    | 1.17x slower                                                 |

Benchmark hidden because not significant (13): json, async_tree_cpu_io_mixed, regex_v8, xml_etree_process, telco, json_loads, logging_silent, regex_effbot, pidigits, asyncio_websockets, python_startup_no_site, nbody, xml_etree_iterparse
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.094x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.08x