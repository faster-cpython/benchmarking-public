# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-aarch64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.02x faster
- HPT reliability: 98.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 301 ms: 1.01x faster                                                              |
| docutils       | 3.10 sec                                                     | 3.05 sec: 1.02x faster                                                            |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 405 ms: 1.18x faster                                                              |
| async_tree_memoization     | 645 ms                                                       | 552 ms: 1.17x faster                                                              |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.14x faster                                                            |
| async_tree_none            | 492 ms                                                       | 439 ms: 1.12x faster                                                              |
| async_tree_io              | 1.22 sec                                                     | 1.09 sec: 1.12x faster                                                            |
| async_tree_memoization_tg  | 604 ms                                                       | 540 ms: 1.12x faster                                                              |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 725 ms: 1.09x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 707 ms: 1.08x faster                                                              |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                              |
| float          | 91.4 ms                                                      | 92.3 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                                              |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|---------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_generate  | 114 ms                                                       | 111 ms: 1.02x faster                                                              |
| tomli_loads         | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                                            |
| xml_etree_iterparse | 147 ms                                                       | 147 ms: 1.00x slower                                                              |
| json_dumps          | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                             |
| Geometric mean      | (ref)                                                        | 1.00x faster                                                                      |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_parse, xml_etree_process, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.89 ms: 1.03x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.5 ms: 1.02x faster                                                             |
| mako            | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                             |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                      |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 328 us: 1.37x faster                                                              |
| deepcopy_memo              | 50.8 us                                                      | 38.9 us: 1.30x faster                                                             |
| deepcopy_reduce            | 4.04 us                                                      | 3.42 us: 1.18x faster                                                             |
| async_tree_none_tg         | 476 ms                                                       | 405 ms: 1.18x faster                                                              |
| async_tree_memoization     | 645 ms                                                       | 552 ms: 1.17x faster                                                              |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.14x faster                                                            |
| async_tree_none            | 492 ms                                                       | 439 ms: 1.12x faster                                                              |
| async_tree_io              | 1.22 sec                                                     | 1.09 sec: 1.12x faster                                                            |
| async_tree_memoization_tg  | 604 ms                                                       | 540 ms: 1.12x faster                                                              |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 725 ms: 1.09x faster                                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 707 ms: 1.08x faster                                                              |
| richards                   | 55.9 ms                                                      | 52.1 ms: 1.07x faster                                                             |
| pathlib                    | 22.8 ms                                                      | 21.4 ms: 1.06x faster                                                             |
| gc_traversal               | 5.17 ms                                                      | 4.88 ms: 1.06x faster                                                             |
| generators                 | 37.1 ms                                                      | 35.0 ms: 1.06x faster                                                             |
| richards_super             | 62.3 ms                                                      | 58.9 ms: 1.06x faster                                                             |
| telco                      | 10.0 ms                                                      | 9.60 ms: 1.04x faster                                                             |
| regex_dna                  | 259 ms                                                       | 249 ms: 1.04x faster                                                              |
| scimark_lu                 | 141 ms                                                       | 137 ms: 1.04x faster                                                              |
| logging_simple             | 7.21 us                                                      | 6.96 us: 1.03x faster                                                             |
| coroutines                 | 29.0 ms                                                      | 28.2 ms: 1.03x faster                                                             |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.38 ms: 1.03x faster                                                             |
| asyncio_tcp                | 584 ms                                                       | 570 ms: 1.02x faster                                                              |
| logging_silent             | 133 ns                                                       | 130 ns: 1.02x faster                                                              |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                              |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.02x faster                                                             |
| regex_effbot               | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                             |
| django_template            | 42.3 ms                                                      | 41.5 ms: 1.02x faster                                                             |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                              |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                             |
| meteor_contest             | 113 ms                                                       | 111 ms: 1.02x faster                                                              |
| tomli_loads                | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                                            |
| docutils                   | 3.10 sec                                                     | 3.05 sec: 1.02x faster                                                            |
| 2to3                       | 305 ms                                                       | 301 ms: 1.01x faster                                                              |
| scimark_fft                | 445 ms                                                       | 440 ms: 1.01x faster                                                              |
| go                         | 161 ms                                                       | 159 ms: 1.01x faster                                                              |
| xml_etree_iterparse        | 147 ms                                                       | 147 ms: 1.00x slower                                                              |
| pprint_pformat             | 1.93 sec                                                     | 1.94 sec: 1.00x slower                                                            |
| bpe_tokeniser              | 5.83 sec                                                     | 5.86 sec: 1.00x slower                                                            |
| sqlglot_transpile          | 1.71 ms                                                      | 1.72 ms: 1.01x slower                                                             |
| coverage                   | 98.4 ms                                                      | 99.3 ms: 1.01x slower                                                             |
| float                      | 91.4 ms                                                      | 92.3 ms: 1.01x slower                                                             |
| sympy_str                  | 265 ms                                                       | 268 ms: 1.01x slower                                                              |
| mdp                        | 3.33 sec                                                     | 3.37 sec: 1.01x slower                                                            |
| bench_mp_pool              | 7.03 ms                                                      | 7.12 ms: 1.01x slower                                                             |
| json                       | 5.64 ms                                                      | 5.73 ms: 1.02x slower                                                             |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                             |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                             |
| comprehensions             | 20.5 us                                                      | 20.9 us: 1.02x slower                                                             |
| pprint_safe_repr           | 933 ms                                                       | 952 ms: 1.02x slower                                                              |
| typing_runtime_protocols   | 193 us                                                       | 198 us: 1.02x slower                                                              |
| fannkuch                   | 451 ms                                                       | 463 ms: 1.03x slower                                                              |
| python_startup_no_site     | 8.60 ms                                                      | 8.89 ms: 1.03x slower                                                             |
| pyflate                    | 557 ms                                                       | 576 ms: 1.03x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                      |

Benchmark hidden because not significant (37): sqlglot_normalize, tornado_http, dask, pickle_pure_python, logging_format, chaos, scimark_sor, thrift, sqlglot_optimize, genshi_xml, scimark_monte_carlo, xml_etree_parse, pycparser, hexiom, spectral_norm, deltablue, pidigits, xml_etree_process, crypto_pyaes, regex_compile, sqlglot_parse, asyncio_tcp_ssl, sympy_expand, regex_v8, python_startup, unpickle_pure_python, sympy_integrate, dulwich_log, asyncio_websockets, genshi_text, nqueens, raytrace, sympy_sum, async_generators, json_loads, html5lib, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x