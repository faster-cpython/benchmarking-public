# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-aarch64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.009x faster
- HPT reliability: 55.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 9.08 ms                                                  | 8.95 ms: 1.01x faster                                        |
| docutils       | 2.89 sec                                                 | 3.10 sec: 1.07x slower                                       |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 604 ms: 1.07x faster                                         |
| coroutines                | 28.5 ms                                                  | 29.0 ms: 1.02x slower                                        |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 791 ms: 1.03x slower                                         |
| async_tree_io             | 1.11 sec                                                 | 1.22 sec: 1.10x slower                                       |
| async_tree_io_tg          | 1.13 sec                                                 | 1.27 sec: 1.13x slower                                       |
| Geometric mean            | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (6): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_generators, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 91.4 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.1 ms: 1.02x faster                                        |
| regex_effbot   | 4.89 ms                                                  | 4.98 ms: 1.02x slower                                        |
| regex_dna      | 253 ms                                                   | 259 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_iterparse | 149 ms                                                   | 147 ms: 1.02x faster                                         |
| tomli_loads         | 2.54 sec                                                 | 2.57 sec: 1.01x slower                                       |
| json_loads          | 31.7 us                                                  | 32.1 us: 1.01x slower                                        |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (6): json_dumps, xml_etree_parse, xml_etree_generate, unpickle_pure_python, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                        |
| Geometric mean | (ref)                                                    | 1.10x faster                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                        |
| genshi_text     | 27.7 ms                                                  | 27.4 ms: 1.01x faster                                        |
| django_template | 41.6 ms                                                  | 42.3 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                     | 1.15 sec                                                 | 767 ms: 1.50x faster                                         |
| create_gc_cycles          | 3.35 ms                                                  | 2.33 ms: 1.44x faster                                        |
| python_startup            | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                        |
| gc_traversal              | 5.77 ms                                                  | 5.17 ms: 1.12x faster                                        |
| bench_mp_pool             | 7.68 ms                                                  | 7.03 ms: 1.09x faster                                        |
| async_tree_memoization_tg | 649 ms                                                   | 604 ms: 1.07x faster                                         |
| pycparser                 | 1.27 sec                                                 | 1.22 sec: 1.04x faster                                       |
| regex_v8                  | 31.8 ms                                                  | 31.1 ms: 1.02x faster                                        |
| fannkuch                  | 461 ms                                                   | 451 ms: 1.02x faster                                         |
| crypto_pyaes              | 83.7 ms                                                  | 82.0 ms: 1.02x faster                                        |
| float                     | 93.3 ms                                                  | 91.4 ms: 1.02x faster                                        |
| xml_etree_iterparse       | 149 ms                                                   | 147 ms: 1.02x faster                                         |
| mako                      | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                        |
| chameleon                 | 9.08 ms                                                  | 8.95 ms: 1.01x faster                                        |
| bench_thread_pool         | 1.27 ms                                                  | 1.26 ms: 1.01x faster                                        |
| generators                | 37.6 ms                                                  | 37.1 ms: 1.01x faster                                        |
| genshi_text               | 27.7 ms                                                  | 27.4 ms: 1.01x faster                                        |
| raytrace                  | 300 ms                                                   | 297 ms: 1.01x faster                                         |
| bpe_tokeniser             | 5.87 sec                                                 | 5.83 sec: 1.01x faster                                       |
| pprint_safe_repr          | 926 ms                                                   | 933 ms: 1.01x slower                                         |
| tomli_loads               | 2.54 sec                                                 | 2.57 sec: 1.01x slower                                       |
| json_loads                | 31.7 us                                                  | 32.1 us: 1.01x slower                                        |
| scimark_lu                | 139 ms                                                   | 141 ms: 1.01x slower                                         |
| deltablue                 | 3.82 ms                                                  | 3.88 ms: 1.02x slower                                        |
| django_template           | 41.6 ms                                                  | 42.3 ms: 1.02x slower                                        |
| coroutines                | 28.5 ms                                                  | 29.0 ms: 1.02x slower                                        |
| pprint_pformat            | 1.90 sec                                                 | 1.93 sec: 1.02x slower                                       |
| regex_effbot              | 4.89 ms                                                  | 4.98 ms: 1.02x slower                                        |
| logging_simple            | 7.07 us                                                  | 7.21 us: 1.02x slower                                        |
| regex_dna                 | 253 ms                                                   | 259 ms: 1.02x slower                                         |
| telco                     | 9.74 ms                                                  | 10.0 ms: 1.03x slower                                        |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 791 ms: 1.03x slower                                         |
| richards_super            | 60.1 ms                                                  | 62.3 ms: 1.04x slower                                        |
| richards                  | 53.6 ms                                                  | 55.9 ms: 1.04x slower                                        |
| docutils                  | 2.89 sec                                                 | 3.10 sec: 1.07x slower                                       |
| async_tree_io             | 1.11 sec                                                 | 1.22 sec: 1.10x slower                                       |
| async_tree_io_tg          | 1.13 sec                                                 | 1.27 sec: 1.13x slower                                       |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (52): json_dumps, xml_etree_parse, json, scimark_monte_carlo, python_startup_no_site, pylint, sqlglot_transpile, nqueens, spectral_norm, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, deepcopy_reduce, coverage, thrift, hexiom, html5lib, scimark_fft, nbody, asyncio_websockets, mdp, async_generators, scimark_sor, meteor_contest, genshi_xml, sympy_sum, pyflate, logging_format, tornado_http, typing_runtime_protocols, sympy_integrate, xml_etree_generate, sympy_expand, deepcopy, pidigits, pathlib, unpickle_pure_python, logging_silent, xml_etree_process, sympy_str, 2to3, pickle_pure_python, chaos, scimark_sparse_mat_mult, go, sqlglot_optimize, regex_compile, comprehensions, deepcopy_memo, async_tree_none_tg, sqlglot_normalize, sqlglot_parse
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.009x faster
# HPT report

- Reliability score: 55.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x