# Results vs. 3.13.0b2

- fork: python
- ref: d27a53fc02a87e76066f
- machine: linux-aarch64
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 299 ms: 1.02x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.14 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 405 ms: 1.18x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 560 ms: 1.15x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 532 ms: 1.14x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.08 sec: 1.13x faster                                                  |
| async_tree_none            | 492 ms                                                       | 442 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 728 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 711 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 107 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads    | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                                  |
| json_loads     | 32.1 us                                                      | 32.4 us: 1.01x slower                                                   |
| json_dumps     | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_generate, pickle_pure_python, xml_etree_process, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.0 ms: 1.00x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.85 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.4 ms: 1.02x faster                                                   |
| mako            | 13.2 ms                                                      | 13.2 ms: 1.00x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 332 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.0 us: 1.34x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 405 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.45 us: 1.17x faster                                                   |
| async_tree_memoization     | 645 ms                                                       | 560 ms: 1.15x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 532 ms: 1.14x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.08 sec: 1.13x faster                                                  |
| async_tree_none            | 492 ms                                                       | 442 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 728 ms: 1.09x faster                                                    |
| richards                   | 55.9 ms                                                      | 52.0 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 711 ms: 1.07x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.85 ms: 1.07x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.9 ms: 1.07x faster                                                   |
| nbody                      | 114 ms                                                       | 107 ms: 1.06x faster                                                    |
| richards_super             | 62.3 ms                                                      | 58.7 ms: 1.06x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.7 ms: 1.05x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                    |
| logging_simple             | 7.21 us                                                      | 6.97 us: 1.03x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.58 us: 1.03x faster                                                   |
| asyncio_tcp                | 584 ms                                                       | 567 ms: 1.03x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| logging_silent             | 133 ns                                                       | 130 ns: 1.03x faster                                                    |
| django_template            | 42.3 ms                                                      | 41.4 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.41 ms: 1.02x faster                                                   |
| deltablue                  | 3.88 ms                                                      | 3.80 ms: 1.02x faster                                                   |
| 2to3                       | 305 ms                                                       | 299 ms: 1.02x faster                                                    |
| thrift                     | 962 us                                                       | 943 us: 1.02x faster                                                    |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.02x faster                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                                  |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| chaos                      | 68.3 ms                                                      | 67.2 ms: 1.02x faster                                                   |
| scimark_fft                | 445 ms                                                       | 439 ms: 1.01x faster                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.19 sec: 1.01x faster                                                  |
| mako                       | 13.2 ms                                                      | 13.2 ms: 1.00x slower                                                   |
| python_startup             | 13.0 ms                                                      | 13.0 ms: 1.00x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.94 sec: 1.01x slower                                                  |
| bpe_tokeniser              | 5.83 sec                                                     | 5.86 sec: 1.01x slower                                                  |
| json_loads                 | 32.1 us                                                      | 32.4 us: 1.01x slower                                                   |
| sympy_expand               | 457 ms                                                       | 462 ms: 1.01x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.14 sec: 1.01x slower                                                  |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 949 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.85 ms: 1.03x slower                                                   |
| fannkuch                   | 451 ms                                                       | 466 ms: 1.03x slower                                                    |
| pyflate                    | 557 ms                                                       | 582 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (43): xml_etree_parse, sqlglot_normalize, tornado_http, sqlglot_parse, xml_etree_generate, meteor_contest, dask, genshi_xml, create_gc_cycles, regex_effbot, raytrace, go, regex_dna, pycparser, sqlglot_optimize, async_generators, regex_compile, pickle_pure_python, spectral_norm, xml_etree_process, scimark_monte_carlo, sympy_sum, nqueens, sqlglot_transpile, xml_etree_iterparse, unpickle_pure_python, json, sympy_str, mdp, pidigits, comprehensions, typing_runtime_protocols, telco, bench_mp_pool, asyncio_websockets, float, coverage, hexiom, crypto_pyaes, genshi_text, sympy_integrate, html5lib, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x