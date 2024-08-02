# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-aarch64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.03x slower
- HPT reliability: 53.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 303 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (4): chameleon, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.23 sec: 1.03x faster                                                  |
| async_tree_none            | 492 ms                                                       | 486 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 792 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 90.6 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 131 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|---------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list         | 5.27 us                                                      | 5.19 us: 1.02x faster                                                   |
| xml_etree_generate  | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| json_loads          | 32.1 us                                                      | 32.3 us: 1.01x slower                                                   |
| json_dumps          | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| unpickle_list       | 6.52 us                                                      | 6.63 us: 1.02x slower                                                   |
| pickle              | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| xml_etree_iterparse | 147 ms                                                       | 152 ms: 1.04x slower                                                    |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (7): pickle_dict, xml_etree_process, tomli_loads, unpickle, pickle_pure_python, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.3 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.4 ms                                                      | 61.2 ms: 1.01x slower                                                   |
| genshi_text    | 27.4 ms                                                      | 28.6 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-arminc-aarch64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup             | 13.0 ms                                                      | 12.3 ms: 1.05x faster                                                   |
| richards                   | 55.9 ms                                                      | 53.3 ms: 1.05x faster                                                   |
| regex_dna                  | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.8 ms: 1.05x faster                                                   |
| richards_super             | 62.3 ms                                                      | 60.1 ms: 1.04x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.23 sec: 1.03x faster                                                  |
| logging_simple             | 7.21 us                                                      | 7.00 us: 1.03x faster                                                   |
| thrift                     | 962 us                                                       | 942 us: 1.02x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 139 ms: 1.02x faster                                                    |
| pickle_list                | 5.27 us                                                      | 5.19 us: 1.02x faster                                                   |
| async_tree_none            | 492 ms                                                       | 486 ms: 1.01x faster                                                    |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.91 sec: 1.01x faster                                                  |
| float                      | 91.4 ms                                                      | 90.6 ms: 1.01x faster                                                   |
| 2to3                       | 305 ms                                                       | 303 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.22 sec: 1.01x slower                                                  |
| json_loads                 | 32.1 us                                                      | 32.3 us: 1.01x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.07 us: 1.01x slower                                                   |
| sympy_str                  | 265 ms                                                       | 268 ms: 1.01x slower                                                    |
| coverage                   | 98.4 ms                                                      | 99.5 ms: 1.01x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.37 sec: 1.01x slower                                                  |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 21.1 ms: 1.01x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 61.2 ms: 1.01x slower                                                   |
| unpickle_list              | 6.52 us                                                      | 6.63 us: 1.02x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 197 us: 1.02x slower                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.29 ms: 1.02x slower                                                   |
| regex_compile              | 128 ms                                                       | 131 ms: 1.02x slower                                                    |
| fannkuch                   | 451 ms                                                       | 463 ms: 1.03x slower                                                    |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 2.42 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 792 ms: 1.04x slower                                                    |
| pyflate                    | 557 ms                                                       | 578 ms: 1.04x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 152 ms: 1.04x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 28.6 ms: 1.04x slower                                                   |
| generators                 | 37.1 ms                                                      | 39.0 ms: 1.05x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 7.41 ms: 1.05x slower                                                   |
| telco                      | 10.0 ms                                                      | 166 ms: 16.53x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (58): async_tree_none_tg, asyncio_tcp, sqlglot_parse, django_template, python_startup_no_site, nbody, chaos, async_tree_cpu_io_mixed, sqlglot_normalize, pickle_dict, xml_etree_process, hexiom, crypto_pyaes, scimark_fft, async_tree_memoization, tomli_loads, scimark_sparse_mat_mult, dulwich_log, docutils, unpickle, scimark_sor, async_tree_io, pickle_pure_python, spectral_norm, sqlite_synth, logging_silent, meteor_contest, deltablue, regex_v8, pycparser, nqueens, coroutines, raytrace, pprint_safe_repr, asyncio_websockets, deepcopy, logging_format, pidigits, go, sympy_sum, xml_etree_parse, sqlglot_optimize, json, dask, comprehensions, chameleon, scimark_monte_carlo, unpickle_pure_python, sympy_expand, deepcopy_memo, flaskblogging, pylint, async_generators, mako, bench_thread_pool, tornado_http, html5lib, async_tree_memoization_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 53.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x