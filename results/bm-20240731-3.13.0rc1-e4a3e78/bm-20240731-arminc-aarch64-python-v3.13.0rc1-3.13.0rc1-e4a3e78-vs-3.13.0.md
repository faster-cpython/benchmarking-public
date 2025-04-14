# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: linux-aarch64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.011x faster
- HPT reliability: 64.28%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.89 sec                                                 | 3.10 sec: 1.07x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x slower                                                   |

Benchmark hidden because not significant (4): 2to3, chameleon, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 599 ms: 1.08x faster                                           |
| coroutines                | 28.5 ms                                                  | 29.1 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 784 ms: 1.02x slower                                           |
| async_tree_io             | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                         |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                         |
| Geometric mean            | (ref)                                                    | 1.02x slower                                                   |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, asyncio_websockets, async_generators, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 91.2 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.3 ms: 1.02x faster                                          |
| regex_effbot   | 4.89 ms                                                  | 4.98 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                    | 1.00x slower                                                   |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_iterparse | 149 ms                                                   | 148 ms: 1.01x faster                                           |
| json_loads          | 31.7 us                                                  | 31.4 us: 1.01x faster                                          |
| tomli_loads         | 2.54 sec                                                 | 2.53 sec: 1.01x faster                                         |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                   |

Benchmark hidden because not significant (6): pickle_pure_python, xml_etree_process, xml_etree_generate, json_dumps, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                          |
| Geometric mean | (ref)                                                    | 1.09x faster                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 42.3 ms: 1.02x slower                                          |
| genshi_text     | 27.7 ms                                                  | 28.4 ms: 1.02x slower                                          |
| genshi_xml      | 60.3 ms                                                  | 62.0 ms: 1.03x slower                                          |
| Geometric mean  | (ref)                                                    | 1.02x slower                                                   |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| mypy2                     | 1.15 sec                                                 | 765 ms: 1.51x faster                                           |
| create_gc_cycles          | 3.35 ms                                                  | 2.34 ms: 1.43x faster                                          |
| python_startup            | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                          |
| gc_traversal              | 5.77 ms                                                  | 5.07 ms: 1.14x faster                                          |
| async_tree_memoization_tg | 649 ms                                                   | 599 ms: 1.08x faster                                           |
| bench_mp_pool             | 7.68 ms                                                  | 7.12 ms: 1.08x faster                                          |
| json                      | 5.73 ms                                                  | 5.47 ms: 1.05x faster                                          |
| pycparser                 | 1.27 sec                                                 | 1.22 sec: 1.05x faster                                         |
| float                     | 93.3 ms                                                  | 91.2 ms: 1.02x faster                                          |
| telco                     | 9.74 ms                                                  | 9.54 ms: 1.02x faster                                          |
| crypto_pyaes              | 83.7 ms                                                  | 82.0 ms: 1.02x faster                                          |
| thrift                    | 968 us                                                   | 949 us: 1.02x faster                                           |
| fannkuch                  | 461 ms                                                   | 453 ms: 1.02x faster                                           |
| regex_v8                  | 31.8 ms                                                  | 31.3 ms: 1.02x faster                                          |
| deepcopy_reduce           | 4.07 us                                                  | 4.01 us: 1.02x faster                                          |
| coverage                  | 99.1 ms                                                  | 97.9 ms: 1.01x faster                                          |
| bpe_tokeniser             | 5.87 sec                                                 | 5.81 sec: 1.01x faster                                         |
| xml_etree_iterparse       | 149 ms                                                   | 148 ms: 1.01x faster                                           |
| json_loads                | 31.7 us                                                  | 31.4 us: 1.01x faster                                          |
| raytrace                  | 300 ms                                                   | 297 ms: 1.01x faster                                           |
| tomli_loads               | 2.54 sec                                                 | 2.53 sec: 1.01x faster                                         |
| mdp                       | 3.34 sec                                                 | 3.36 sec: 1.01x slower                                         |
| sympy_str                 | 264 ms                                                   | 267 ms: 1.01x slower                                           |
| logging_silent            | 133 ns                                                   | 135 ns: 1.01x slower                                           |
| django_template           | 41.6 ms                                                  | 42.3 ms: 1.02x slower                                          |
| pprint_pformat            | 1.90 sec                                                 | 1.93 sec: 1.02x slower                                         |
| deltablue                 | 3.82 ms                                                  | 3.89 ms: 1.02x slower                                          |
| regex_effbot              | 4.89 ms                                                  | 4.98 ms: 1.02x slower                                          |
| coroutines                | 28.5 ms                                                  | 29.1 ms: 1.02x slower                                          |
| genshi_text               | 27.7 ms                                                  | 28.4 ms: 1.02x slower                                          |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 784 ms: 1.02x slower                                           |
| pprint_safe_repr          | 926 ms                                                   | 948 ms: 1.02x slower                                           |
| sympy_integrate           | 20.8 ms                                                  | 21.4 ms: 1.03x slower                                          |
| genshi_xml                | 60.3 ms                                                  | 62.0 ms: 1.03x slower                                          |
| docutils                  | 2.89 sec                                                 | 3.10 sec: 1.07x slower                                         |
| async_tree_io             | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                         |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                         |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (52): nqueens, scimark_monte_carlo, sqlglot_transpile, richards, spectral_norm, async_tree_cpu_io_mixed_tg, scimark_fft, pickle_pure_python, async_tree_none, xml_etree_process, scimark_sor, pathlib, html5lib, richards_super, scimark_lu, xml_etree_generate, tornado_http, async_tree_memoization, logging_simple, json_dumps, regex_dna, scimark_sparse_mat_mult, nbody, 2to3, hexiom, deepcopy_memo, logging_format, python_startup_no_site, pidigits, meteor_contest, typing_runtime_protocols, generators, asyncio_websockets, comprehensions, deepcopy, go, pyflate, bench_thread_pool, async_generators, sympy_expand, chaos, xml_etree_parse, regex_compile, sympy_sum, chameleon, sqlglot_normalize, sqlglot_parse, sqlglot_optimize, unpickle_pure_python, async_tree_none_tg, mako, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: asyncio_tcp, asyncio_tcp_ssl, dask

- Geometric mean (including insignificant results): 1.011x faster
# HPT report

- Reliability score: 64.28% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.91x