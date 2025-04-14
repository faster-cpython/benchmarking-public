# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-aarch64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.008x faster
- HPT reliability: 73.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.87x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 9.08 ms                                                  | 8.93 ms: 1.02x faster                                        |
| tornado_http   | 128 ms                                                   | 133 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines                 | 28.5 ms                                                  | 29.2 ms: 1.02x slower                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 728 ms: 1.12x slower                                         |
| async_tree_memoization     | 651 ms                                                   | 737 ms: 1.13x slower                                         |
| async_tree_none            | 497 ms                                                   | 564 ms: 1.13x slower                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 880 ms: 1.15x slower                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 887 ms: 1.15x slower                                         |
| async_tree_none_tg         | 470 ms                                                   | 567 ms: 1.21x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.43 sec: 1.26x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.42 sec: 1.29x slower                                       |
| Geometric mean             | (ref)                                                    | 1.13x slower                                                 |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 106 ms: 1.08x faster                                         |
| Geometric mean | (ref)                                                    | 1.03x faster                                                 |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.2 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 357 us                                                   | 351 us: 1.02x faster                                         |
| tomli_loads          | 2.54 sec                                                 | 2.58 sec: 1.02x slower                                       |
| unpickle_pure_python | 251 us                                                   | 255 us: 1.02x slower                                         |
| json_loads           | 31.7 us                                                  | 32.2 us: 1.02x slower                                        |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (5): json_dumps, xml_etree_process, xml_etree_iterparse, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 12.1 ms: 1.27x faster                                        |
| python_startup_no_site | 8.73 ms                                                  | 10.5 ms: 1.21x slower                                        |
| Geometric mean         | (ref)                                                    | 1.03x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 40.3 ms: 1.03x faster                                        |
| genshi_text     | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                        |
| mako            | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                        |
| Geometric mean  | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 1.96 ms: 1.71x faster                                        |
| typing_runtime_protocols   | 193 us                                                   | 133 us: 1.46x faster                                         |
| gc_traversal               | 5.77 ms                                                  | 4.39 ms: 1.31x faster                                        |
| python_startup             | 15.4 ms                                                  | 12.1 ms: 1.27x faster                                        |
| mypy2                      | 1.15 sec                                                 | 915 ms: 1.26x faster                                         |
| bench_mp_pool              | 7.68 ms                                                  | 6.96 ms: 1.10x faster                                        |
| nbody                      | 114 ms                                                   | 106 ms: 1.08x faster                                         |
| crypto_pyaes               | 83.7 ms                                                  | 78.8 ms: 1.06x faster                                        |
| logging_silent             | 133 ns                                                   | 126 ns: 1.06x faster                                         |
| regex_v8                   | 31.8 ms                                                  | 30.2 ms: 1.05x faster                                        |
| spectral_norm              | 143 ms                                                   | 135 ms: 1.05x faster                                         |
| thrift                     | 968 us                                                   | 926 us: 1.05x faster                                         |
| generators                 | 37.6 ms                                                  | 36.2 ms: 1.04x faster                                        |
| deepcopy_memo              | 50.4 us                                                  | 48.5 us: 1.04x faster                                        |
| nqueens                    | 100 ms                                                   | 96.6 ms: 1.04x faster                                        |
| django_template            | 41.6 ms                                                  | 40.3 ms: 1.03x faster                                        |
| deepcopy_reduce            | 4.07 us                                                  | 3.94 us: 1.03x faster                                        |
| deepcopy                   | 447 us                                                   | 434 us: 1.03x faster                                         |
| sympy_sum                  | 144 ms                                                   | 139 ms: 1.03x faster                                         |
| sympy_str                  | 264 ms                                                   | 257 ms: 1.03x faster                                         |
| pprint_safe_repr           | 926 ms                                                   | 903 ms: 1.03x faster                                         |
| genshi_text                | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                        |
| pprint_pformat             | 1.90 sec                                                 | 1.86 sec: 1.02x faster                                       |
| sympy_expand               | 457 ms                                                   | 448 ms: 1.02x faster                                         |
| sqlglot_optimize           | 62.2 ms                                                  | 61.0 ms: 1.02x faster                                        |
| pickle_pure_python         | 357 us                                                   | 351 us: 1.02x faster                                         |
| telco                      | 9.74 ms                                                  | 9.57 ms: 1.02x faster                                        |
| hexiom                     | 7.11 ms                                                  | 6.98 ms: 1.02x faster                                        |
| chameleon                  | 9.08 ms                                                  | 8.93 ms: 1.02x faster                                        |
| mako                       | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                        |
| sqlglot_normalize          | 127 ms                                                   | 125 ms: 1.01x faster                                         |
| raytrace                   | 300 ms                                                   | 295 ms: 1.01x faster                                         |
| chaos                      | 68.0 ms                                                  | 67.1 ms: 1.01x faster                                        |
| scimark_fft                | 447 ms                                                   | 442 ms: 1.01x faster                                         |
| meteor_contest             | 114 ms                                                   | 114 ms: 1.01x slower                                         |
| tomli_loads                | 2.54 sec                                                 | 2.58 sec: 1.02x slower                                       |
| unpickle_pure_python       | 251 us                                                   | 255 us: 1.02x slower                                         |
| bench_thread_pool          | 1.27 ms                                                  | 1.30 ms: 1.02x slower                                        |
| json_loads                 | 31.7 us                                                  | 32.2 us: 1.02x slower                                        |
| coroutines                 | 28.5 ms                                                  | 29.2 ms: 1.02x slower                                        |
| coverage                   | 99.1 ms                                                  | 102 ms: 1.03x slower                                         |
| logging_simple             | 7.07 us                                                  | 7.26 us: 1.03x slower                                        |
| scimark_sor                | 160 ms                                                   | 166 ms: 1.04x slower                                         |
| tornado_http               | 128 ms                                                   | 133 ms: 1.04x slower                                         |
| pathlib                    | 22.7 ms                                                  | 23.7 ms: 1.04x slower                                        |
| deltablue                  | 3.82 ms                                                  | 4.03 ms: 1.06x slower                                        |
| pyflate                    | 556 ms                                                   | 597 ms: 1.07x slower                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 728 ms: 1.12x slower                                         |
| async_tree_memoization     | 651 ms                                                   | 737 ms: 1.13x slower                                         |
| async_tree_none            | 497 ms                                                   | 564 ms: 1.13x slower                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 880 ms: 1.15x slower                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 887 ms: 1.15x slower                                         |
| async_tree_none_tg         | 470 ms                                                   | 567 ms: 1.21x slower                                         |
| python_startup_no_site     | 8.73 ms                                                  | 10.5 ms: 1.21x slower                                        |
| async_tree_io_tg           | 1.13 sec                                                 | 1.43 sec: 1.26x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.42 sec: 1.29x slower                                       |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (32): json_dumps, pylint, xml_etree_process, regex_compile, scimark_lu, genshi_xml, sqlglot_parse, sympy_integrate, json, comprehensions, sqlglot_transpile, html5lib, async_generators, xml_etree_iterparse, float, xml_etree_generate, mdp, fannkuch, regex_dna, pidigits, asyncio_websockets, regex_effbot, scimark_sparse_mat_mult, go, pycparser, scimark_monte_carlo, docutils, xml_etree_parse, 2to3, richards_super, richards, logging_format
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dulwich_log, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 73.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.87x