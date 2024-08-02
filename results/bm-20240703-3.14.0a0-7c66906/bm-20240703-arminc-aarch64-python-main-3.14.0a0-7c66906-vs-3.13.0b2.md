# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: linux-aarch64
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.02x faster
- HPT reliability: 58.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 404 ms: 1.18x faster                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.09 sec: 1.17x faster                                  |
| async_tree_memoization     | 645 ms                                                       | 556 ms: 1.16x faster                                    |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 534 ms: 1.13x faster                                    |
| async_tree_none            | 492 ms                                                       | 437 ms: 1.13x faster                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 725 ms: 1.09x faster                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 709 ms: 1.08x faster                                    |
| Geometric mean             | (ref)                                                        | 1.13x faster                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------:|
| float          | 91.4 ms                                                      | 92.9 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                    |
| regex_effbot   | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                            |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------:|
| tomli_loads          | 2.57 sec                                                     | 2.56 sec: 1.01x faster                                  |
| xml_etree_generate   | 114 ms                                                       | 113 ms: 1.00x faster                                    |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                    |
| unpickle_pure_python | 251 us                                                       | 254 us: 1.01x slower                                    |
| json_loads           | 32.1 us                                                      | 33.2 us: 1.03x slower                                   |
| json_dumps           | 13.1 ms                                                      | 13.6 ms: 1.04x slower                                   |
| Geometric mean       | (ref)                                                        | 1.01x slower                                            |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.81 ms: 1.02x slower                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                   |
| mako           | 13.2 ms                                                      | 13.7 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                        | 1.02x slower                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 335 us: 1.34x faster                                    |
| deepcopy_memo              | 50.8 us                                                      | 39.1 us: 1.30x faster                                   |
| async_tree_none_tg         | 476 ms                                                       | 404 ms: 1.18x faster                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.09 sec: 1.17x faster                                  |
| deepcopy_reduce            | 4.04 us                                                      | 3.47 us: 1.16x faster                                   |
| async_tree_memoization     | 645 ms                                                       | 556 ms: 1.16x faster                                    |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 534 ms: 1.13x faster                                    |
| async_tree_none            | 492 ms                                                       | 437 ms: 1.13x faster                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 725 ms: 1.09x faster                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 709 ms: 1.08x faster                                    |
| gc_traversal               | 5.17 ms                                                      | 4.86 ms: 1.06x faster                                   |
| pathlib                    | 22.8 ms                                                      | 21.7 ms: 1.05x faster                                   |
| richards                   | 55.9 ms                                                      | 53.2 ms: 1.05x faster                                   |
| richards_super             | 62.3 ms                                                      | 59.6 ms: 1.05x faster                                   |
| logging_simple             | 7.21 us                                                      | 6.92 us: 1.04x faster                                   |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                    |
| asyncio_tcp                | 584 ms                                                       | 565 ms: 1.03x faster                                    |
| logging_format             | 7.82 us                                                      | 7.61 us: 1.03x faster                                   |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.02x faster                                   |
| thrift                     | 962 us                                                       | 943 us: 1.02x faster                                    |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.02x faster                                   |
| regex_effbot               | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.77 sec: 1.01x faster                                  |
| tomli_loads                | 2.57 sec                                                     | 2.56 sec: 1.01x faster                                  |
| xml_etree_generate         | 114 ms                                                       | 113 ms: 1.00x faster                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.72 ms: 1.00x slower                                   |
| raytrace                   | 297 ms                                                       | 299 ms: 1.01x slower                                    |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                    |
| telco                      | 10.0 ms                                                      | 10.1 ms: 1.01x slower                                   |
| unpickle_pure_python       | 251 us                                                       | 254 us: 1.01x slower                                    |
| sympy_str                  | 265 ms                                                       | 269 ms: 1.01x slower                                    |
| coroutines                 | 29.0 ms                                                      | 29.4 ms: 1.01x slower                                   |
| float                      | 91.4 ms                                                      | 92.9 ms: 1.02x slower                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 83.8 ms: 1.02x slower                                   |
| sympy_sum                  | 144 ms                                                       | 146 ms: 1.02x slower                                    |
| sympy_expand               | 457 ms                                                       | 466 ms: 1.02x slower                                    |
| python_startup             | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                   |
| json                       | 5.64 ms                                                      | 5.76 ms: 1.02x slower                                   |
| genshi_text                | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                   |
| generators                 | 37.1 ms                                                      | 38.0 ms: 1.02x slower                                   |
| sympy_integrate            | 20.9 ms                                                      | 21.3 ms: 1.02x slower                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.81 ms: 1.02x slower                                   |
| typing_runtime_protocols   | 193 us                                                       | 199 us: 1.03x slower                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.99 sec: 1.03x slower                                  |
| fannkuch                   | 451 ms                                                       | 466 ms: 1.03x slower                                    |
| json_loads                 | 32.1 us                                                      | 33.2 us: 1.03x slower                                   |
| json_dumps                 | 13.1 ms                                                      | 13.6 ms: 1.04x slower                                   |
| pprint_safe_repr           | 933 ms                                                       | 970 ms: 1.04x slower                                    |
| mako                       | 13.2 ms                                                      | 13.7 ms: 1.04x slower                                   |
| coverage                   | 98.4 ms                                                      | 103 ms: 1.05x slower                                    |
| pyflate                    | 557 ms                                                       | 586 ms: 1.05x slower                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                            |

Benchmark hidden because not significant (38): dask, regex_v8, scimark_sor, django_template, xml_etree_process, sqlglot_parse, docutils, xml_etree_parse, meteor_contest, chaos, crypto_pyaes, deltablue, asyncio_tcp_ssl, go, 2to3, mdp, pidigits, asyncio_websockets, scimark_sparse_mat_mult, logging_silent, scimark_fft, async_generators, spectral_norm, pycparser, nbody, bench_mp_pool, hexiom, regex_compile, sqlglot_optimize, pickle_pure_python, sqlglot_normalize, genshi_xml, nqueens, dulwich_log, comprehensions, pylint, tornado_http, html5lib
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 58.34% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x