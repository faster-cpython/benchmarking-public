# Results vs. 3.13.0b2

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.03x slower
- HPT reliability: 88.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 302 ms: 1.01x faster                                                     |
| docutils       | 3.10 sec                                                     | 3.13 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 794 ms: 1.04x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                     |
| float          | 91.4 ms                                                      | 90.5 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_dna, regex_effbot, regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|---------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_list         | 5.27 us                                                      | 5.12 us: 1.03x faster                                                    |
| tomli_loads         | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                   |
| pickle              | 13.4 us                                                      | 13.6 us: 1.01x slower                                                    |
| json_loads          | 32.1 us                                                      | 32.6 us: 1.02x slower                                                    |
| xml_etree_iterparse | 147 ms                                                       | 149 ms: 1.02x slower                                                     |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (9): unpickle_list, xml_etree_parse, pickle_dict, xml_etree_generate, unpickle_pure_python, unpickle, xml_etree_process, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.6 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                        | 1.02x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.3 ms: 1.03x faster                                                    |
| mako            | 13.2 ms                                                      | 13.2 ms: 1.00x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup             | 13.0 ms                                                      | 12.6 ms: 1.03x faster                                                    |
| pickle_list                | 5.27 us                                                      | 5.12 us: 1.03x faster                                                    |
| asyncio_tcp                | 584 ms                                                       | 568 ms: 1.03x faster                                                     |
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 138 ms: 1.03x faster                                                     |
| django_template            | 42.3 ms                                                      | 41.3 ms: 1.03x faster                                                    |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                     |
| richards                   | 55.9 ms                                                      | 54.9 ms: 1.02x faster                                                    |
| comprehensions             | 20.5 us                                                      | 20.2 us: 1.02x faster                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                   |
| deepcopy                   | 448 us                                                       | 443 us: 1.01x faster                                                     |
| float                      | 91.4 ms                                                      | 90.5 ms: 1.01x faster                                                    |
| 2to3                       | 305 ms                                                       | 302 ms: 1.01x faster                                                     |
| gc_traversal               | 5.17 ms                                                      | 5.13 ms: 1.01x faster                                                    |
| mako                       | 13.2 ms                                                      | 13.2 ms: 1.00x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.72 ms: 1.01x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.27 ms: 1.01x slower                                                    |
| asyncio_websockets         | 657 ms                                                       | 663 ms: 1.01x slower                                                     |
| docutils                   | 3.10 sec                                                     | 3.13 sec: 1.01x slower                                                   |
| sympy_expand               | 457 ms                                                       | 463 ms: 1.01x slower                                                     |
| generators                 | 37.1 ms                                                      | 37.6 ms: 1.01x slower                                                    |
| pickle                     | 13.4 us                                                      | 13.6 us: 1.01x slower                                                    |
| json                       | 5.64 ms                                                      | 5.73 ms: 1.02x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.6 us: 1.02x slower                                                    |
| sympy_str                  | 265 ms                                                       | 270 ms: 1.02x slower                                                     |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.02x slower                                                     |
| bench_mp_pool              | 7.03 ms                                                      | 7.16 ms: 1.02x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 197 us: 1.02x slower                                                     |
| pprint_safe_repr           | 933 ms                                                       | 953 ms: 1.02x slower                                                     |
| fannkuch                   | 451 ms                                                       | 463 ms: 1.03x slower                                                     |
| create_gc_cycles           | 2.33 ms                                                      | 2.40 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 794 ms: 1.04x slower                                                     |
| telco                      | 10.0 ms                                                      | 164 ms: 16.36x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                             |

Benchmark hidden because not significant (67): python_startup_no_site, sqlglot_normalize, logging_simple, scimark_sor, regex_dna, hexiom, async_tree_none_tg, crypto_pyaes, coverage, unpickle_list, deepcopy_memo, regex_effbot, mypy2, sqlite_synth, spectral_norm, chaos, logging_silent, xml_etree_parse, pickle_dict, xml_etree_generate, async_tree_memoization, async_tree_none, unpickle_pure_python, async_tree_cpu_io_mixed, async_generators, unpickle, deltablue, sqlglot_optimize, async_tree_io, nqueens, scimark_monte_carlo, pyflate, coroutines, scimark_fft, deepcopy_reduce, asyncio_tcp_ssl, pprint_pformat, raytrace, richards_super, pidigits, regex_v8, xml_etree_process, dulwich_log, scimark_sparse_mat_mult, pycparser, regex_compile, mdp, thrift, sympy_integrate, meteor_contest, go, chameleon, logging_format, pickle_pure_python, pathlib, aiohttp, pylint, genshi_xml, sympy_sum, dask, json_dumps, sqlglot_parse, gunicorn, tornado_http, flaskblogging, html5lib, async_tree_memoization_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 88.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x