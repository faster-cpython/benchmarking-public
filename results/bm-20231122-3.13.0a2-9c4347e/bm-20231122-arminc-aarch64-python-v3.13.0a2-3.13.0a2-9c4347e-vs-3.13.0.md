# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-aarch64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.008x faster
- HPT reliability: 74.68%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 303 ms: 1.00x faster                                         |
| chameleon      | 9.08 ms                                                  | 8.96 ms: 1.01x faster                                        |
| tornado_http   | 128 ms                                                   | 135 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_generators           | 489 ms                                                   | 480 ms: 1.02x faster                                         |
| coroutines                 | 28.5 ms                                                  | 29.2 ms: 1.03x slower                                        |
| async_tree_memoization     | 651 ms                                                   | 736 ms: 1.13x slower                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 882 ms: 1.15x slower                                         |
| async_tree_none            | 497 ms                                                   | 572 ms: 1.15x slower                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 763 ms: 1.18x slower                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 907 ms: 1.18x slower                                         |
| async_tree_none_tg         | 470 ms                                                   | 590 ms: 1.26x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.47 sec: 1.30x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.44 sec: 1.30x slower                                       |
| Geometric mean             | (ref)                                                    | 1.14x slower                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 105 ms: 1.09x faster                                         |
| float          | 93.3 ms                                                  | 90.6 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                    | 1.04x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.0 ms: 1.06x faster                                        |
| regex_effbot   | 4.89 ms                                                  | 4.61 ms: 1.06x faster                                        |
| regex_dna      | 253 ms                                                   | 246 ms: 1.03x faster                                         |
| regex_compile  | 127 ms                                                   | 129 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                    | 1.03x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.6 ms                                                  | 12.4 ms: 1.09x faster                                        |
| pickle_pure_python   | 357 us                                                   | 346 us: 1.03x faster                                         |
| json_loads           | 31.7 us                                                  | 30.8 us: 1.03x faster                                        |
| unpickle_pure_python | 251 us                                                   | 253 us: 1.01x slower                                         |
| tomli_loads          | 2.54 sec                                                 | 2.57 sec: 1.01x slower                                       |
| Geometric mean       | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_generate, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 12.6 ms: 1.22x faster                                        |
| python_startup_no_site | 8.73 ms                                                  | 10.9 ms: 1.25x slower                                        |
| Geometric mean         | (ref)                                                    | 1.01x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 12.8 ms: 1.04x faster                                        |
| django_template | 41.6 ms                                                  | 40.9 ms: 1.02x faster                                        |
| genshi_text     | 27.7 ms                                                  | 27.9 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 1.89 ms: 1.77x faster                                        |
| typing_runtime_protocols   | 193 us                                                   | 138 us: 1.40x faster                                         |
| gc_traversal               | 5.77 ms                                                  | 4.44 ms: 1.30x faster                                        |
| mypy2                      | 1.15 sec                                                 | 892 ms: 1.29x faster                                         |
| python_startup             | 15.4 ms                                                  | 12.6 ms: 1.22x faster                                        |
| bench_mp_pool              | 7.68 ms                                                  | 6.91 ms: 1.11x faster                                        |
| spectral_norm              | 143 ms                                                   | 129 ms: 1.11x faster                                         |
| json_dumps                 | 13.6 ms                                                  | 12.4 ms: 1.09x faster                                        |
| nbody                      | 114 ms                                                   | 105 ms: 1.09x faster                                         |
| crypto_pyaes               | 83.7 ms                                                  | 77.5 ms: 1.08x faster                                        |
| regex_v8                   | 31.8 ms                                                  | 30.0 ms: 1.06x faster                                        |
| regex_effbot               | 4.89 ms                                                  | 4.61 ms: 1.06x faster                                        |
| thrift                     | 968 us                                                   | 923 us: 1.05x faster                                         |
| deepcopy_memo              | 50.4 us                                                  | 48.2 us: 1.04x faster                                        |
| json                       | 5.73 ms                                                  | 5.49 ms: 1.04x faster                                        |
| scimark_fft                | 447 ms                                                   | 428 ms: 1.04x faster                                         |
| mako                       | 13.4 ms                                                  | 12.8 ms: 1.04x faster                                        |
| deepcopy_reduce            | 4.07 us                                                  | 3.93 us: 1.04x faster                                        |
| comprehensions             | 20.4 us                                                  | 19.7 us: 1.03x faster                                        |
| deepcopy                   | 447 us                                                   | 433 us: 1.03x faster                                         |
| pickle_pure_python         | 357 us                                                   | 346 us: 1.03x faster                                         |
| scimark_monte_carlo        | 83.6 ms                                                  | 81.1 ms: 1.03x faster                                        |
| float                      | 93.3 ms                                                  | 90.6 ms: 1.03x faster                                        |
| richards                   | 53.6 ms                                                  | 52.2 ms: 1.03x faster                                        |
| json_loads                 | 31.7 us                                                  | 30.8 us: 1.03x faster                                        |
| sqlglot_normalize          | 127 ms                                                   | 123 ms: 1.03x faster                                         |
| regex_dna                  | 253 ms                                                   | 246 ms: 1.03x faster                                         |
| sqlglot_optimize           | 62.2 ms                                                  | 60.6 ms: 1.03x faster                                        |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.34 ms: 1.03x faster                                        |
| sympy_sum                  | 144 ms                                                   | 140 ms: 1.03x faster                                         |
| nqueens                    | 100 ms                                                   | 97.6 ms: 1.03x faster                                        |
| logging_silent             | 133 ns                                                   | 130 ns: 1.02x faster                                         |
| sympy_integrate            | 20.8 ms                                                  | 20.4 ms: 1.02x faster                                        |
| sympy_expand               | 457 ms                                                   | 448 ms: 1.02x faster                                         |
| django_template            | 41.6 ms                                                  | 40.9 ms: 1.02x faster                                        |
| async_generators           | 489 ms                                                   | 480 ms: 1.02x faster                                         |
| chaos                      | 68.0 ms                                                  | 66.9 ms: 1.02x faster                                        |
| sympy_str                  | 264 ms                                                   | 260 ms: 1.02x faster                                         |
| chameleon                  | 9.08 ms                                                  | 8.96 ms: 1.01x faster                                        |
| pprint_safe_repr           | 926 ms                                                   | 916 ms: 1.01x faster                                         |
| pycparser                  | 1.27 sec                                                 | 1.26 sec: 1.01x faster                                       |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                       |
| fannkuch                   | 461 ms                                                   | 458 ms: 1.01x faster                                         |
| telco                      | 9.74 ms                                                  | 9.69 ms: 1.01x faster                                        |
| mdp                        | 3.34 sec                                                 | 3.33 sec: 1.00x faster                                       |
| raytrace                   | 300 ms                                                   | 299 ms: 1.00x faster                                         |
| 2to3                       | 304 ms                                                   | 303 ms: 1.00x faster                                         |
| meteor_contest             | 114 ms                                                   | 114 ms: 1.01x slower                                         |
| genshi_text                | 27.7 ms                                                  | 27.9 ms: 1.01x slower                                        |
| unpickle_pure_python       | 251 us                                                   | 253 us: 1.01x slower                                         |
| richards_super             | 60.1 ms                                                  | 60.7 ms: 1.01x slower                                        |
| tomli_loads                | 2.54 sec                                                 | 2.57 sec: 1.01x slower                                       |
| pyflate                    | 556 ms                                                   | 565 ms: 1.01x slower                                         |
| scimark_sor                | 160 ms                                                   | 162 ms: 1.02x slower                                         |
| regex_compile              | 127 ms                                                   | 129 ms: 1.02x slower                                         |
| bench_thread_pool          | 1.27 ms                                                  | 1.31 ms: 1.02x slower                                        |
| coroutines                 | 28.5 ms                                                  | 29.2 ms: 1.03x slower                                        |
| deltablue                  | 3.82 ms                                                  | 4.00 ms: 1.05x slower                                        |
| generators                 | 37.6 ms                                                  | 39.5 ms: 1.05x slower                                        |
| pathlib                    | 22.7 ms                                                  | 23.9 ms: 1.05x slower                                        |
| tornado_http               | 128 ms                                                   | 135 ms: 1.06x slower                                         |
| async_tree_memoization     | 651 ms                                                   | 736 ms: 1.13x slower                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 882 ms: 1.15x slower                                         |
| async_tree_none            | 497 ms                                                   | 572 ms: 1.15x slower                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 763 ms: 1.18x slower                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 907 ms: 1.18x slower                                         |
| python_startup_no_site     | 8.73 ms                                                  | 10.9 ms: 1.25x slower                                        |
| async_tree_none_tg         | 470 ms                                                   | 590 ms: 1.26x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.47 sec: 1.30x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.44 sec: 1.30x slower                                       |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (18): pylint, xml_etree_process, logging_format, hexiom, html5lib, sqlglot_transpile, sqlglot_parse, docutils, xml_etree_generate, asyncio_websockets, xml_etree_parse, pidigits, xml_etree_iterparse, go, genshi_xml, logging_simple, coverage, scimark_lu
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dulwich_log, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 74.68% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.86x