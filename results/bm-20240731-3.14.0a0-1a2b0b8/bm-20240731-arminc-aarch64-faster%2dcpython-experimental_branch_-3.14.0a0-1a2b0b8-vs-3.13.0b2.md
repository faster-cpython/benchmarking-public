# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-aarch64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.02x faster
- HPT reliability: 93.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 3.20 sec: 1.03x slower                                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                      |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 404 ms: 1.18x faster                                                              |
| async_tree_memoization     | 645 ms                                                       | 557 ms: 1.16x faster                                                              |
| async_tree_memoization_tg  | 604 ms                                                       | 533 ms: 1.13x faster                                                              |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.13x faster                                                            |
| async_tree_none            | 492 ms                                                       | 436 ms: 1.13x faster                                                              |
| async_tree_io              | 1.22 sec                                                     | 1.12 sec: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 726 ms: 1.09x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 713 ms: 1.07x faster                                                              |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                              |
| float          | 91.4 ms                                                      | 93.7 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 253 ms: 1.02x faster                                                              |
| regex_v8       | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads    | 2.57 sec                                                     | 2.56 sec: 1.01x faster                                                            |
| json_loads     | 32.1 us                                                      | 32.6 us: 1.02x slower                                                             |
| json_dumps     | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                      |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_process, unpickle_pure_python, xml_etree_generate, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                             |
| python_startup_no_site | 8.60 ms                                                      | 8.91 ms: 1.04x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                             |
| genshi_xml     | 60.4 ms                                                      | 61.6 ms: 1.02x slower                                                             |
| mako           | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 329 us: 1.36x faster                                                              |
| deepcopy_memo              | 50.8 us                                                      | 38.3 us: 1.32x faster                                                             |
| async_tree_none_tg         | 476 ms                                                       | 404 ms: 1.18x faster                                                              |
| deepcopy_reduce            | 4.04 us                                                      | 3.45 us: 1.17x faster                                                             |
| async_tree_memoization     | 645 ms                                                       | 557 ms: 1.16x faster                                                              |
| async_tree_memoization_tg  | 604 ms                                                       | 533 ms: 1.13x faster                                                              |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.13x faster                                                            |
| async_tree_none            | 492 ms                                                       | 436 ms: 1.13x faster                                                              |
| async_tree_io              | 1.22 sec                                                     | 1.12 sec: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 726 ms: 1.09x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 713 ms: 1.07x faster                                                              |
| richards                   | 55.9 ms                                                      | 52.9 ms: 1.06x faster                                                             |
| richards_super             | 62.3 ms                                                      | 59.2 ms: 1.05x faster                                                             |
| pathlib                    | 22.8 ms                                                      | 21.7 ms: 1.05x faster                                                             |
| generators                 | 37.1 ms                                                      | 35.4 ms: 1.05x faster                                                             |
| gc_traversal               | 5.17 ms                                                      | 4.95 ms: 1.04x faster                                                             |
| logging_silent             | 133 ns                                                       | 130 ns: 1.03x faster                                                              |
| logging_simple             | 7.21 us                                                      | 7.01 us: 1.03x faster                                                             |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                                              |
| asyncio_tcp                | 584 ms                                                       | 569 ms: 1.03x faster                                                              |
| telco                      | 10.0 ms                                                      | 9.77 ms: 1.03x faster                                                             |
| regex_dna                  | 259 ms                                                       | 253 ms: 1.02x faster                                                              |
| scimark_lu                 | 141 ms                                                       | 139 ms: 1.02x faster                                                              |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                             |
| regex_v8                   | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                             |
| logging_format             | 7.82 us                                                      | 7.70 us: 1.02x faster                                                             |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.01x faster                                                             |
| chaos                      | 68.3 ms                                                      | 67.6 ms: 1.01x faster                                                             |
| tomli_loads                | 2.57 sec                                                     | 2.56 sec: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.20 sec: 1.00x faster                                                            |
| sqlglot_transpile          | 1.71 ms                                                      | 1.72 ms: 1.01x slower                                                             |
| bpe_tokeniser              | 5.83 sec                                                     | 5.87 sec: 1.01x slower                                                            |
| pprint_safe_repr           | 933 ms                                                       | 942 ms: 1.01x slower                                                              |
| sympy_str                  | 265 ms                                                       | 268 ms: 1.01x slower                                                              |
| sympy_expand               | 457 ms                                                       | 463 ms: 1.01x slower                                                              |
| scimark_monte_carlo        | 82.3 ms                                                      | 83.4 ms: 1.01x slower                                                             |
| json_loads                 | 32.1 us                                                      | 32.6 us: 1.02x slower                                                             |
| scimark_sor                | 159 ms                                                       | 162 ms: 1.02x slower                                                              |
| genshi_text                | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                             |
| python_startup             | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                             |
| sympy_integrate            | 20.9 ms                                                      | 21.2 ms: 1.02x slower                                                             |
| genshi_xml                 | 60.4 ms                                                      | 61.6 ms: 1.02x slower                                                             |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                             |
| float                      | 91.4 ms                                                      | 93.7 ms: 1.02x slower                                                             |
| mako                       | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                             |
| typing_runtime_protocols   | 193 us                                                       | 199 us: 1.03x slower                                                              |
| fannkuch                   | 451 ms                                                       | 465 ms: 1.03x slower                                                              |
| docutils                   | 3.10 sec                                                     | 3.20 sec: 1.03x slower                                                            |
| python_startup_no_site     | 8.60 ms                                                      | 8.91 ms: 1.04x slower                                                             |
| pyflate                    | 557 ms                                                       | 580 ms: 1.04x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                      |

Benchmark hidden because not significant (40): xml_etree_parse, dask, xml_etree_process, sqlglot_normalize, regex_effbot, scimark_sparse_mat_mult, go, unpickle_pure_python, 2to3, async_generators, spectral_norm, pycparser, pprint_pformat, pidigits, raytrace, tornado_http, django_template, sqlglot_optimize, sqlglot_parse, bench_mp_pool, regex_compile, xml_etree_generate, asyncio_websockets, mdp, comprehensions, thrift, deltablue, crypto_pyaes, meteor_contest, scimark_fft, pickle_pure_python, nqueens, coverage, create_gc_cycles, json, sympy_sum, hexiom, xml_etree_iterparse, html5lib, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 93.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x