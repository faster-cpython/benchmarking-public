# Results vs. 3.13.0b2

- fork: python
- ref: fe85a8291d9aa11c9ce9
- machine: linux-aarch64
- commit hash: fe85a82
- commit date: 2024-08-26
- overall geometric mean: 1.02x faster
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 296 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 420 ms: 1.17x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 551 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 546 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 723 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 728 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 109 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 245 ms: 1.05x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 251 us                                                       | 254 us: 1.01x slower                                                    |
| json_loads           | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| xml_etree_iterparse  | 147 ms                                                       | 151 ms: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_process, xml_etree_parse, pickle_pure_python, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.6 ms: 1.01x slower                                                   |
| mako           | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.0 us: 1.34x faster                                                   |
| deepcopy                   | 448 us                                                       | 338 us: 1.33x faster                                                    |
| async_tree_none            | 492 ms                                                       | 420 ms: 1.17x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 551 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.52 us: 1.15x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 546 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 723 ms: 1.09x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 20.8 ms: 1.09x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| gc_traversal               | 5.17 ms                                                      | 4.83 ms: 1.07x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| generators                 | 37.1 ms                                                      | 35.0 ms: 1.06x faster                                                   |
| regex_dna                  | 259 ms                                                       | 245 ms: 1.05x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 135 ms: 1.05x faster                                                    |
| nbody                      | 114 ms                                                       | 109 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 728 ms: 1.05x faster                                                    |
| richards_super             | 62.3 ms                                                      | 59.6 ms: 1.05x faster                                                   |
| richards                   | 55.9 ms                                                      | 53.4 ms: 1.05x faster                                                   |
| asyncio_tcp                | 584 ms                                                       | 560 ms: 1.04x faster                                                    |
| thrift                     | 962 us                                                       | 927 us: 1.04x faster                                                    |
| logging_simple             | 7.21 us                                                      | 6.95 us: 1.04x faster                                                   |
| telco                      | 10.0 ms                                                      | 9.68 ms: 1.04x faster                                                   |
| 2to3                       | 305 ms                                                       | 296 ms: 1.03x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.89 sec: 1.02x faster                                                  |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.02x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.67 us: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.43 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 933 ms                                                       | 918 ms: 1.02x faster                                                    |
| logging_silent             | 133 ns                                                       | 132 ns: 1.01x faster                                                    |
| scimark_fft                | 445 ms                                                       | 440 ms: 1.01x faster                                                    |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.01x faster                                                    |
| sympy_sum                  | 144 ms                                                       | 142 ms: 1.01x faster                                                    |
| sympy_str                  | 265 ms                                                       | 263 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.20 sec: 1.00x faster                                                  |
| bpe_tokeniser              | 5.83 sec                                                     | 5.87 sec: 1.01x slower                                                  |
| genshi_text                | 27.4 ms                                                      | 27.6 ms: 1.01x slower                                                   |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 254 us: 1.01x slower                                                    |
| pyflate                    | 557 ms                                                       | 563 ms: 1.01x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 1.74 ms: 1.02x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                                   |
| raytrace                   | 297 ms                                                       | 302 ms: 1.02x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| fannkuch                   | 451 ms                                                       | 464 ms: 1.03x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 151 ms: 1.03x slower                                                    |
| go                         | 161 ms                                                       | 193 ms: 1.20x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (37): sqlglot_normalize, regex_compile, scimark_sor, xml_etree_process, xml_etree_parse, coverage, genshi_xml, pickle_pure_python, sympy_integrate, sqlglot_optimize, docutils, xml_etree_generate, pycparser, regex_v8, async_generators, json_dumps, asyncio_websockets, html5lib, spectral_norm, float, nqueens, tornado_http, mdp, sqlglot_parse, pidigits, comprehensions, sympy_expand, typing_runtime_protocols, scimark_monte_carlo, bench_mp_pool, django_template, chaos, deltablue, hexiom, json, crypto_pyaes, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x