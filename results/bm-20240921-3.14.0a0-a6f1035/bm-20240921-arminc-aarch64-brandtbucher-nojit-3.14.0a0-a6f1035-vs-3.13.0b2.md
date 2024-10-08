# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.02x faster
- HPT reliability: 97.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 297 ms: 1.03x faster                                           |
| docutils       | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                         |
| html5lib       | 66.1 ms                                                      | 64.5 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                        | 1.02x faster                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 417 ms: 1.18x faster                                           |
| async_tree_memoization     | 645 ms                                                       | 553 ms: 1.17x faster                                           |
| async_tree_none_tg         | 476 ms                                                       | 419 ms: 1.14x faster                                           |
| async_tree_memoization_tg  | 604 ms                                                       | 552 ms: 1.10x faster                                           |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                         |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 736 ms: 1.08x faster                                           |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                         |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 721 ms: 1.06x faster                                           |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                           |
| float          | 91.4 ms                                                      | 94.9 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                        | 1.00x slower                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 251 ms: 1.03x faster                                           |
| regex_v8       | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                          |
| regex_effbot   | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                        | 1.02x faster                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.4 us: 1.02x faster                                          |
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.02x faster                                           |
| unpickle_list        | 6.52 us                                                      | 6.42 us: 1.02x faster                                          |
| pickle_list          | 5.27 us                                                      | 5.21 us: 1.01x faster                                          |
| unpickle_pure_python | 251 us                                                       | 254 us: 1.01x slower                                           |
| xml_etree_iterparse  | 147 ms                                                       | 149 ms: 1.02x slower                                           |
| pickle               | 13.4 us                                                      | 13.6 us: 1.02x slower                                          |
| tomli_loads          | 2.57 sec                                                     | 2.66 sec: 1.04x slower                                         |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                   |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_process, json_loads, pickle_dict, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.3 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                        | 1.01x slower                                                   |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 335 us: 1.34x faster                                           |
| deepcopy_memo              | 50.8 us                                                      | 39.2 us: 1.29x faster                                          |
| async_tree_none            | 492 ms                                                       | 417 ms: 1.18x faster                                           |
| go                         | 161 ms                                                       | 138 ms: 1.17x faster                                           |
| async_tree_memoization     | 645 ms                                                       | 553 ms: 1.17x faster                                           |
| async_tree_none_tg         | 476 ms                                                       | 419 ms: 1.14x faster                                           |
| deepcopy_reduce            | 4.04 us                                                      | 3.58 us: 1.13x faster                                          |
| async_tree_memoization_tg  | 604 ms                                                       | 552 ms: 1.10x faster                                           |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                         |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 736 ms: 1.08x faster                                           |
| pathlib                    | 22.8 ms                                                      | 21.4 ms: 1.07x faster                                          |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                         |
| richards                   | 55.9 ms                                                      | 52.8 ms: 1.06x faster                                          |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 721 ms: 1.06x faster                                           |
| richards_super             | 62.3 ms                                                      | 59.4 ms: 1.05x faster                                          |
| generators                 | 37.1 ms                                                      | 35.4 ms: 1.05x faster                                          |
| scimark_lu                 | 141 ms                                                       | 135 ms: 1.05x faster                                           |
| asyncio_tcp                | 584 ms                                                       | 560 ms: 1.04x faster                                           |
| thrift                     | 962 us                                                       | 926 us: 1.04x faster                                           |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                           |
| regex_dna                  | 259 ms                                                       | 251 ms: 1.03x faster                                           |
| docutils                   | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                         |
| 2to3                       | 305 ms                                                       | 297 ms: 1.03x faster                                           |
| pprint_pformat             | 1.93 sec                                                     | 1.88 sec: 1.03x faster                                         |
| gc_traversal               | 5.17 ms                                                      | 5.04 ms: 1.03x faster                                          |
| html5lib                   | 66.1 ms                                                      | 64.5 ms: 1.03x faster                                          |
| pprint_safe_repr           | 933 ms                                                       | 911 ms: 1.02x faster                                           |
| scimark_sor                | 159 ms                                                       | 156 ms: 1.02x faster                                           |
| regex_v8                   | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                          |
| unpickle                   | 19.8 us                                                      | 19.4 us: 1.02x faster                                          |
| async_generators           | 488 ms                                                       | 480 ms: 1.02x faster                                           |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.02x faster                                           |
| unpickle_list              | 6.52 us                                                      | 6.42 us: 1.02x faster                                          |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.45 ms: 1.02x faster                                          |
| logging_format             | 7.82 us                                                      | 7.71 us: 1.01x faster                                          |
| pickle_list                | 5.27 us                                                      | 5.21 us: 1.01x faster                                          |
| regex_effbot               | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                          |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                          |
| bpe_tokeniser              | 5.83 sec                                                     | 5.87 sec: 1.01x slower                                         |
| mdp                        | 3.33 sec                                                     | 3.35 sec: 1.01x slower                                         |
| pyflate                    | 557 ms                                                       | 563 ms: 1.01x slower                                           |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                          |
| unpickle_pure_python       | 251 us                                                       | 254 us: 1.01x slower                                           |
| bench_mp_pool              | 7.03 ms                                                      | 7.12 ms: 1.01x slower                                          |
| pycparser                  | 1.22 sec                                                     | 1.24 sec: 1.01x slower                                         |
| chaos                      | 68.3 ms                                                      | 69.2 ms: 1.01x slower                                          |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.02x slower                                          |
| hexiom                     | 7.08 ms                                                      | 7.18 ms: 1.02x slower                                          |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.02x slower                                           |
| pickle                     | 13.4 us                                                      | 13.6 us: 1.02x slower                                          |
| raytrace                   | 297 ms                                                       | 302 ms: 1.02x slower                                           |
| fannkuch                   | 451 ms                                                       | 465 ms: 1.03x slower                                           |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                          |
| tomli_loads                | 2.57 sec                                                     | 2.66 sec: 1.04x slower                                         |
| float                      | 91.4 ms                                                      | 94.9 ms: 1.04x slower                                          |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                   |

Benchmark hidden because not significant (41): sqlglot_normalize, xml_etree_parse, create_gc_cycles, logging_simple, xml_etree_process, tornado_http, django_template, regex_compile, json_loads, coroutines, typing_runtime_protocols, sqlglot_parse, sqlite_synth, sqlglot_optimize, logging_silent, coverage, scimark_fft, sympy_sum, scimark_monte_carlo, asyncio_tcp_ssl, pidigits, pickle_dict, meteor_contest, genshi_text, nqueens, pickle_pure_python, bench_thread_pool, comprehensions, crypto_pyaes, sympy_expand, asyncio_websockets, sympy_integrate, json, sympy_str, spectral_norm, dulwich_log, python_startup_no_site, deltablue, json_dumps, genshi_xml, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035.json: unpack_sequence

# HPT report

- Reliability score: 97.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x