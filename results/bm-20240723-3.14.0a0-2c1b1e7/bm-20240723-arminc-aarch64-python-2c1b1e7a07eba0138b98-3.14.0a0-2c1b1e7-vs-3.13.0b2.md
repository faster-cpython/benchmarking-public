# Results vs. 3.13.0b2

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: linux-aarch64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 301 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 407 ms: 1.17x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 569 ms: 1.13x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.14 sec: 1.12x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 543 ms: 1.11x faster                                                    |
| async_tree_none            | 492 ms                                                       | 443 ms: 1.11x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.12 sec: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 734 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 710 ms: 1.08x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| float          | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads    | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                  |
| json_loads     | 32.1 us                                                      | 32.6 us: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (7): xml_etree_parse, xml_etree_process, xml_etree_generate, pickle_pure_python, unpickle_pure_python, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.80 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.7 ms: 1.01x faster                                                   |
| mako            | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-arminc-aarch64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 328 us: 1.37x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.8 us: 1.31x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 3.37 us: 1.20x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 407 ms: 1.17x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 569 ms: 1.13x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.14 sec: 1.12x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 543 ms: 1.11x faster                                                    |
| async_tree_none            | 492 ms                                                       | 443 ms: 1.11x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.12 sec: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 734 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 710 ms: 1.08x faster                                                    |
| richards                   | 55.9 ms                                                      | 52.3 ms: 1.07x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.8 ms: 1.07x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.3 ms: 1.07x faster                                                   |
| richards_super             | 62.3 ms                                                      | 59.0 ms: 1.06x faster                                                   |
| telco                      | 10.0 ms                                                      | 9.54 ms: 1.05x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                    |
| dask                       | 370 ms                                                       | 360 ms: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                      | 28.2 ms: 1.03x faster                                                   |
| thrift                     | 962 us                                                       | 939 us: 1.02x faster                                                    |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                   |
| logging_simple             | 7.21 us                                                      | 7.05 us: 1.02x faster                                                   |
| logging_silent             | 133 ns                                                       | 131 ns: 1.02x faster                                                    |
| deltablue                  | 3.88 ms                                                      | 3.80 ms: 1.02x faster                                                   |
| nqueens                    | 98.9 ms                                                      | 97.1 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                       | 111 ms: 1.02x faster                                                    |
| logging_format             | 7.82 us                                                      | 7.68 us: 1.02x faster                                                   |
| django_template            | 42.3 ms                                                      | 41.7 ms: 1.01x faster                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                  |
| 2to3                       | 305 ms                                                       | 301 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.92 sec: 1.01x faster                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 1.71 ms: 1.00x faster                                                   |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| pyflate                    | 557 ms                                                       | 562 ms: 1.01x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.6 us: 1.01x slower                                                   |
| float                      | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 198 us: 1.02x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.80 ms: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 478 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (51): xml_etree_parse, tornado_http, xml_etree_process, sqlglot_parse, gc_traversal, sqlglot_optimize, dulwich_log, create_gc_cycles, bench_thread_pool, chaos, docutils, scimark_fft, xml_etree_generate, scimark_sparse_mat_mult, pickle_pure_python, sympy_sum, async_generators, scimark_sor, raytrace, regex_dna, spectral_norm, regex_effbot, mdp, crypto_pyaes, sqlglot_normalize, pidigits, go, scimark_monte_carlo, hexiom, bpe_tokeniser, regex_compile, pprint_safe_repr, asyncio_tcp_ssl, sympy_expand, sympy_str, asyncio_websockets, asyncio_tcp, unpickle_pure_python, bench_mp_pool, json, sympy_integrate, python_startup, coverage, json_dumps, comprehensions, genshi_xml, pycparser, genshi_text, html5lib, xml_etree_iterparse, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x