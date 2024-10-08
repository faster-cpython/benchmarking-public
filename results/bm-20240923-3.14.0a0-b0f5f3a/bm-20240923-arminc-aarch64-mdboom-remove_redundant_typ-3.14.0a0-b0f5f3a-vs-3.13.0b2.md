# Results vs. 3.13.0b2

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-aarch64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.02x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.03 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 419 ms: 1.17x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 553 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 549 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 723 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 718 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| float          | 91.4 ms                                                      | 93.3 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 186 ms: 1.03x faster                                                    |
| xml_etree_process    | 80.8 ms                                                      | 79.3 ms: 1.02x faster                                                   |
| json_loads           | 32.1 us                                                      | 31.7 us: 1.01x faster                                                   |
| unpickle             | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 149 ms: 1.01x slower                                                    |
| pickle_dict          | 37.6 us                                                      | 38.3 us: 1.02x slower                                                   |
| pickle               | 13.4 us                                                      | 13.6 us: 1.02x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 256 us: 1.02x slower                                                    |
| json_dumps           | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, pickle_list, unpickle_list, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 333 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.0 us: 1.34x faster                                                   |
| async_tree_none            | 492 ms                                                       | 419 ms: 1.17x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 553 ms: 1.17x faster                                                    |
| go                         | 161 ms                                                       | 138 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.50 us: 1.15x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 549 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 723 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| pathlib                    | 22.8 ms                                                      | 21.2 ms: 1.07x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 718 ms: 1.06x faster                                                    |
| richards                   | 55.9 ms                                                      | 52.7 ms: 1.06x faster                                                   |
| richards_super             | 62.3 ms                                                      | 59.1 ms: 1.05x faster                                                   |
| asyncio_tcp                | 584 ms                                                       | 561 ms: 1.04x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                    |
| 2to3                       | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| thrift                     | 962 us                                                       | 932 us: 1.03x faster                                                    |
| xml_etree_parse            | 191 ms                                                       | 186 ms: 1.03x faster                                                    |
| sympy_sum                  | 144 ms                                                       | 139 ms: 1.03x faster                                                    |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| regex_dna                  | 259 ms                                                       | 252 ms: 1.03x faster                                                    |
| logging_simple             | 7.21 us                                                      | 7.02 us: 1.03x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.02x faster                                                   |
| docutils                   | 3.10 sec                                                     | 3.03 sec: 1.02x faster                                                  |
| pprint_pformat             | 1.93 sec                                                     | 1.88 sec: 1.02x faster                                                  |
| logging_format             | 7.82 us                                                      | 7.65 us: 1.02x faster                                                   |
| pprint_safe_repr           | 933 ms                                                       | 914 ms: 1.02x faster                                                    |
| xml_etree_process          | 80.8 ms                                                      | 79.3 ms: 1.02x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                   |
| json                       | 5.64 ms                                                      | 5.54 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.6 ms: 1.02x faster                                                   |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.01x faster                                                    |
| json_loads                 | 32.1 us                                                      | 31.7 us: 1.01x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.19 sec: 1.01x faster                                                  |
| logging_silent             | 133 ns                                                       | 132 ns: 1.01x faster                                                    |
| sympy_integrate            | 20.9 ms                                                      | 20.6 ms: 1.01x faster                                                   |
| spectral_norm              | 141 ms                                                       | 140 ms: 1.01x faster                                                    |
| sympy_str                  | 265 ms                                                       | 263 ms: 1.01x faster                                                    |
| mdp                        | 3.33 sec                                                     | 3.31 sec: 1.01x faster                                                  |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 7.12 ms: 1.01x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 59.4 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.01x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 83.6 ms: 1.02x slower                                                   |
| pickle_dict                | 37.6 us                                                      | 38.3 us: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.6 us: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 459 ms: 1.02x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.74 ms: 1.02x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 256 us: 1.02x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                   |
| raytrace                   | 297 ms                                                       | 302 ms: 1.02x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 101 ms: 1.02x slower                                                    |
| float                      | 91.4 ms                                                      | 93.3 ms: 1.02x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.02x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| pyflate                    | 557 ms                                                       | 580 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (34): tornado_http, sqlglot_parse, gc_traversal, regex_compile, django_template, async_generators, genshi_text, xml_etree_generate, meteor_contest, html5lib, crypto_pyaes, regex_effbot, sqlite_synth, pycparser, scimark_fft, sqlglot_optimize, scimark_sparse_mat_mult, pickle_list, sqlglot_normalize, pidigits, sympy_expand, bpe_tokeniser, comprehensions, unpickle_list, hexiom, typing_runtime_protocols, pickle_pure_python, asyncio_websockets, coverage, chaos, python_startup_no_site, deltablue, genshi_xml, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x