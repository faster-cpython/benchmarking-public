# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-aarch64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.02x faster
- HPT reliability: 96.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 3.17 sec: 1.02x slower                                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                      |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 402 ms: 1.18x faster                                                              |
| async_tree_memoization     | 645 ms                                                       | 558 ms: 1.16x faster                                                              |
| async_tree_memoization_tg  | 604 ms                                                       | 536 ms: 1.13x faster                                                              |
| async_tree_io_tg           | 1.27 sec                                                     | 1.14 sec: 1.12x faster                                                            |
| async_tree_io              | 1.22 sec                                                     | 1.09 sec: 1.12x faster                                                            |
| async_tree_none            | 492 ms                                                       | 443 ms: 1.11x faster                                                              |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 736 ms: 1.08x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 710 ms: 1.07x faster                                                              |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                              |
| float          | 91.4 ms                                                      | 92.2 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                      |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 2.57 sec                                                     | 2.48 sec: 1.04x faster                                                            |
| unpickle_pure_python | 251 us                                                       | 249 us: 1.01x faster                                                              |
| json_dumps           | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                             |
| json_loads           | 32.1 us                                                      | 32.7 us: 1.02x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                      |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_process, pickle_pure_python, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                             |
| mako           | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                             |
| genshi_xml     | 60.4 ms                                                      | 62.2 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-arminc-aarch64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 329 us: 1.36x faster                                                              |
| deepcopy_memo              | 50.8 us                                                      | 38.6 us: 1.31x faster                                                             |
| async_tree_none_tg         | 476 ms                                                       | 402 ms: 1.18x faster                                                              |
| deepcopy_reduce            | 4.04 us                                                      | 3.44 us: 1.17x faster                                                             |
| async_tree_memoization     | 645 ms                                                       | 558 ms: 1.16x faster                                                              |
| async_tree_memoization_tg  | 604 ms                                                       | 536 ms: 1.13x faster                                                              |
| async_tree_io_tg           | 1.27 sec                                                     | 1.14 sec: 1.12x faster                                                            |
| async_tree_io              | 1.22 sec                                                     | 1.09 sec: 1.12x faster                                                            |
| async_tree_none            | 492 ms                                                       | 443 ms: 1.11x faster                                                              |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 736 ms: 1.08x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 710 ms: 1.07x faster                                                              |
| richards                   | 55.9 ms                                                      | 52.2 ms: 1.07x faster                                                             |
| generators                 | 37.1 ms                                                      | 34.9 ms: 1.06x faster                                                             |
| richards_super             | 62.3 ms                                                      | 58.9 ms: 1.06x faster                                                             |
| pathlib                    | 22.8 ms                                                      | 21.6 ms: 1.05x faster                                                             |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                              |
| tomli_loads                | 2.57 sec                                                     | 2.48 sec: 1.04x faster                                                            |
| logging_simple             | 7.21 us                                                      | 6.95 us: 1.04x faster                                                             |
| logging_silent             | 133 ns                                                       | 129 ns: 1.03x faster                                                              |
| gc_traversal               | 5.17 ms                                                      | 5.04 ms: 1.03x faster                                                             |
| telco                      | 10.0 ms                                                      | 9.76 ms: 1.03x faster                                                             |
| logging_format             | 7.82 us                                                      | 7.63 us: 1.02x faster                                                             |
| coroutines                 | 29.0 ms                                                      | 28.4 ms: 1.02x faster                                                             |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                                              |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.02x faster                                                             |
| async_generators           | 488 ms                                                       | 480 ms: 1.02x faster                                                              |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                              |
| go                         | 161 ms                                                       | 158 ms: 1.02x faster                                                              |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.01x faster                                                              |
| unpickle_pure_python       | 251 us                                                       | 249 us: 1.01x faster                                                              |
| sqlglot_transpile          | 1.71 ms                                                      | 1.71 ms: 1.00x slower                                                             |
| float                      | 91.4 ms                                                      | 92.2 ms: 1.01x slower                                                             |
| sympy_str                  | 265 ms                                                       | 268 ms: 1.01x slower                                                              |
| pyflate                    | 557 ms                                                       | 563 ms: 1.01x slower                                                              |
| crypto_pyaes               | 82.0 ms                                                      | 83.0 ms: 1.01x slower                                                             |
| pprint_safe_repr           | 933 ms                                                       | 946 ms: 1.01x slower                                                              |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                             |
| python_startup_no_site     | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                                             |
| json_loads                 | 32.1 us                                                      | 32.7 us: 1.02x slower                                                             |
| typing_runtime_protocols   | 193 us                                                       | 197 us: 1.02x slower                                                              |
| nqueens                    | 98.9 ms                                                      | 101 ms: 1.02x slower                                                              |
| hexiom                     | 7.08 ms                                                      | 7.22 ms: 1.02x slower                                                             |
| docutils                   | 3.10 sec                                                     | 3.17 sec: 1.02x slower                                                            |
| sympy_integrate            | 20.9 ms                                                      | 21.3 ms: 1.02x slower                                                             |
| genshi_text                | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                             |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                             |
| genshi_xml                 | 60.4 ms                                                      | 62.2 ms: 1.03x slower                                                             |
| fannkuch                   | 451 ms                                                       | 466 ms: 1.03x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                      |

Benchmark hidden because not significant (42): xml_etree_parse, dask, sqlglot_normalize, sqlglot_parse, xml_etree_process, scimark_sparse_mat_mult, deltablue, meteor_contest, scimark_fft, regex_v8, sqlglot_optimize, create_gc_cycles, regex_effbot, coverage, django_template, pidigits, 2to3, asyncio_websockets, pprint_pformat, html5lib, raytrace, regex_compile, mdp, thrift, python_startup, chaos, json, asyncio_tcp, bpe_tokeniser, spectral_norm, asyncio_tcp_ssl, pickle_pure_python, sympy_expand, bench_mp_pool, pycparser, comprehensions, scimark_monte_carlo, xml_etree_generate, xml_etree_iterparse, sympy_sum, tornado_http, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 96.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x