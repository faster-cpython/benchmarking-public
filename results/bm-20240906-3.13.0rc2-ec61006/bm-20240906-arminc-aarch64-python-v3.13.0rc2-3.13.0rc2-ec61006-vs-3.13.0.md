# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: linux-aarch64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.011x faster
- HPT reliability: 90.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| chameleon      | 9.08 ms                                                  | 8.94 ms: 1.02x faster                                          |
| docutils       | 2.89 sec                                                 | 3.10 sec: 1.07x slower                                         |
| Geometric mean | (ref)                                                    | 1.02x slower                                                   |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 603 ms: 1.08x faster                                           |
| async_tree_none           | 497 ms                                                   | 488 ms: 1.02x faster                                           |
| async_generators          | 489 ms                                                   | 483 ms: 1.01x faster                                           |
| coroutines                | 28.5 ms                                                  | 29.2 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 790 ms: 1.03x slower                                           |
| async_tree_io             | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                         |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                         |
| Geometric mean            | (ref)                                                    | 1.01x slower                                                   |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 91.5 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.1 ms: 1.02x faster                                          |
| regex_compile  | 127 ms                                                   | 128 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                    | 1.00x faster                                                   |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_iterparse | 149 ms                                                   | 148 ms: 1.01x faster                                           |
| json_loads          | 31.7 us                                                  | 31.4 us: 1.01x faster                                          |
| Geometric mean      | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (7): json_dumps, xml_etree_process, pickle_pure_python, xml_etree_parse, xml_etree_generate, unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                          |
| python_startup_no_site | 8.73 ms                                                  | 8.63 ms: 1.01x faster                                          |
| Geometric mean         | (ref)                                                    | 1.09x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 42.6 ms: 1.02x slower                                          |
| Geometric mean  | (ref)                                                    | 1.01x slower                                                   |

Benchmark hidden because not significant (3): mako, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| mypy2                     | 1.15 sec                                                 | 761 ms: 1.52x faster                                           |
| create_gc_cycles          | 3.35 ms                                                  | 2.33 ms: 1.44x faster                                          |
| python_startup            | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                          |
| gc_traversal              | 5.77 ms                                                  | 4.92 ms: 1.17x faster                                          |
| async_tree_memoization_tg | 649 ms                                                   | 603 ms: 1.08x faster                                           |
| pycparser                 | 1.27 sec                                                 | 1.21 sec: 1.05x faster                                         |
| json                      | 5.73 ms                                                  | 5.60 ms: 1.02x faster                                          |
| regex_v8                  | 31.8 ms                                                  | 31.1 ms: 1.02x faster                                          |
| float                     | 93.3 ms                                                  | 91.5 ms: 1.02x faster                                          |
| async_tree_none           | 497 ms                                                   | 488 ms: 1.02x faster                                           |
| crypto_pyaes              | 83.7 ms                                                  | 82.2 ms: 1.02x faster                                          |
| chameleon                 | 9.08 ms                                                  | 8.94 ms: 1.02x faster                                          |
| hexiom                    | 7.11 ms                                                  | 7.00 ms: 1.02x faster                                          |
| logging_simple            | 7.07 us                                                  | 6.96 us: 1.02x faster                                          |
| thrift                    | 968 us                                                   | 956 us: 1.01x faster                                           |
| async_generators          | 489 ms                                                   | 483 ms: 1.01x faster                                           |
| pyflate                   | 556 ms                                                   | 550 ms: 1.01x faster                                           |
| bpe_tokeniser             | 5.87 sec                                                 | 5.80 sec: 1.01x faster                                         |
| python_startup_no_site    | 8.73 ms                                                  | 8.63 ms: 1.01x faster                                          |
| richards_super            | 60.1 ms                                                  | 59.5 ms: 1.01x faster                                          |
| xml_etree_iterparse       | 149 ms                                                   | 148 ms: 1.01x faster                                           |
| json_loads                | 31.7 us                                                  | 31.4 us: 1.01x faster                                          |
| regex_compile             | 127 ms                                                   | 128 ms: 1.01x slower                                           |
| mdp                       | 3.34 sec                                                 | 3.38 sec: 1.01x slower                                         |
| deepcopy                  | 447 us                                                   | 453 us: 1.01x slower                                           |
| pprint_pformat            | 1.90 sec                                                 | 1.92 sec: 1.01x slower                                         |
| sqlglot_normalize         | 127 ms                                                   | 129 ms: 1.02x slower                                           |
| pprint_safe_repr          | 926 ms                                                   | 942 ms: 1.02x slower                                           |
| django_template           | 41.6 ms                                                  | 42.6 ms: 1.02x slower                                          |
| scimark_sparse_mat_mult   | 6.51 ms                                                  | 6.67 ms: 1.02x slower                                          |
| coroutines                | 28.5 ms                                                  | 29.2 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 790 ms: 1.03x slower                                           |
| logging_silent            | 133 ns                                                   | 137 ns: 1.03x slower                                           |
| telco                     | 9.74 ms                                                  | 10.1 ms: 1.04x slower                                          |
| docutils                  | 2.89 sec                                                 | 3.10 sec: 1.07x slower                                         |
| async_tree_io             | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                         |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                         |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (52): json_dumps, scimark_monte_carlo, richards, nqueens, xml_etree_process, async_tree_cpu_io_mixed_tg, async_tree_memoization, nbody, logging_format, pickle_pure_python, xml_etree_parse, fannkuch, xml_etree_generate, regex_dna, sympy_sum, sqlglot_transpile, coverage, typing_runtime_protocols, mako, regex_effbot, scimark_fft, scimark_sor, sympy_expand, bench_thread_pool, 2to3, async_tree_none_tg, pidigits, genshi_text, comprehensions, raytrace, pathlib, asyncio_websockets, meteor_contest, unpickle_pure_python, tomli_loads, go, sympy_integrate, chaos, scimark_lu, sympy_str, sqlglot_optimize, bench_mp_pool, generators, deltablue, deepcopy_reduce, genshi_xml, spectral_norm, tornado_http, html5lib, deepcopy_memo, sqlglot_parse, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.011x faster
# HPT report

- Reliability score: 90.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x