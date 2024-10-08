# Results vs. 3.13.0b2

- fork: python
- ref: e38d0afe3548b856ccf0
- machine: linux-aarch64
- commit hash: e38d0af
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.23%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.06 sec: 1.01x faster                                                  |
| html5lib       | 66.1 ms                                                      | 67.0 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 427 ms: 1.15x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 563 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 421 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 729 ms: 1.09x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.13 sec: 1.08x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 731 ms: 1.04x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 109 ms: 1.04x faster                                                    |
| float          | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.83 ms: 1.03x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 30.6 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 255 us: 1.02x slower                                                    |
| json_loads           | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.0 us: 1.34x faster                                                   |
| deepcopy                   | 448 us                                                       | 338 us: 1.33x faster                                                    |
| async_tree_none            | 492 ms                                                       | 427 ms: 1.15x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 563 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.54 us: 1.14x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 421 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 729 ms: 1.09x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.13 sec: 1.08x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| pathlib                    | 22.8 ms                                                      | 21.3 ms: 1.07x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 4.89 ms: 1.06x faster                                                   |
| generators                 | 37.1 ms                                                      | 35.2 ms: 1.06x faster                                                   |
| richards_super             | 62.3 ms                                                      | 59.4 ms: 1.05x faster                                                   |
| regex_dna                  | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| richards                   | 55.9 ms                                                      | 53.3 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 731 ms: 1.04x faster                                                    |
| nbody                      | 114 ms                                                       | 109 ms: 1.04x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                    |
| 2to3                       | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| logging_simple             | 7.21 us                                                      | 6.96 us: 1.03x faster                                                   |
| thrift                     | 962 us                                                       | 931 us: 1.03x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.83 ms: 1.03x faster                                                   |
| asyncio_tcp                | 584 ms                                                       | 572 ms: 1.02x faster                                                    |
| scimark_sor                | 159 ms                                                       | 156 ms: 1.02x faster                                                    |
| logging_silent             | 133 ns                                                       | 131 ns: 1.02x faster                                                    |
| telco                      | 10.0 ms                                                      | 9.84 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.44 ms: 1.02x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.02x faster                                                    |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.6 ms: 1.02x faster                                                   |
| docutils                   | 3.10 sec                                                     | 3.06 sec: 1.01x faster                                                  |
| float                      | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                   |
| sympy_expand               | 457 ms                                                       | 462 ms: 1.01x slower                                                    |
| pyflate                    | 557 ms                                                       | 562 ms: 1.01x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 100 ms: 1.01x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 67.0 ms: 1.01x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 83.1 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 255 us: 1.02x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.24 sec: 1.02x slower                                                  |
| fannkuch                   | 451 ms                                                       | 460 ms: 1.02x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.75 ms: 1.02x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| raytrace                   | 297 ms                                                       | 303 ms: 1.02x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| go                         | 161 ms                                                       | 192 ms: 1.20x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (40): coroutines, create_gc_cycles, logging_format, xml_etree_parse, regex_compile, sympy_sum, xml_etree_process, comprehensions, async_generators, sqlglot_normalize, sqlglot_optimize, django_template, scimark_fft, sympy_str, sympy_integrate, asyncio_tcp_ssl, typing_runtime_protocols, pprint_pformat, spectral_norm, pidigits, scimark_monte_carlo, python_startup, sqlglot_parse, bpe_tokeniser, pprint_safe_repr, genshi_xml, mdp, hexiom, chaos, coverage, tornado_http, asyncio_websockets, deltablue, python_startup_no_site, genshi_text, xml_etree_iterparse, bench_mp_pool, pickle_pure_python, json, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x