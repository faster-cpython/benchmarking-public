# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 292 ms: 1.04x faster                                                    |
| docutils       | 3.10 sec                                                     | 2.98 sec: 1.04x faster                                                  |
| html5lib       | 66.1 ms                                                      | 63.5 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                        | 1.04x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 423 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 556 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 412 ms: 1.16x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 545 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 724 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.16 sec: 1.09x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 721 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| float          | 91.4 ms                                                      | 92.9 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 246 ms: 1.05x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 127 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process    | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                   |
| unpickle_pure_python | 251 us                                                       | 254 us: 1.01x slower                                                    |
| json_loads           | 32.1 us                                                      | 32.9 us: 1.03x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| json_dumps           | 13.1 ms                                                      | 13.6 ms: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_generate, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.73 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.0 us: 1.34x faster                                                   |
| deepcopy                   | 448 us                                                       | 337 us: 1.33x faster                                                    |
| async_tree_none            | 492 ms                                                       | 423 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 556 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.49 us: 1.16x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 412 ms: 1.16x faster                                                    |
| go                         | 161 ms                                                       | 140 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 545 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 724 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.16 sec: 1.09x faster                                                  |
| asyncio_tcp                | 584 ms                                                       | 538 ms: 1.09x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.1 ms: 1.08x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.6 ms: 1.07x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| richards                   | 55.9 ms                                                      | 52.7 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 721 ms: 1.06x faster                                                    |
| regex_dna                  | 259 ms                                                       | 246 ms: 1.05x faster                                                    |
| richards_super             | 62.3 ms                                                      | 59.2 ms: 1.05x faster                                                   |
| 2to3                       | 305 ms                                                       | 292 ms: 1.04x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.97 ms: 1.04x faster                                                   |
| docutils                   | 3.10 sec                                                     | 2.98 sec: 1.04x faster                                                  |
| html5lib                   | 66.1 ms                                                      | 63.5 ms: 1.04x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                    |
| thrift                     | 962 us                                                       | 926 us: 1.04x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.87 sec: 1.03x faster                                                  |
| logging_simple             | 7.21 us                                                      | 7.01 us: 1.03x faster                                                   |
| pprint_safe_repr           | 933 ms                                                       | 910 ms: 1.03x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.16 sec: 1.02x faster                                                  |
| regex_v8                   | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                   |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.42 ms: 1.02x faster                                                   |
| async_generators           | 488 ms                                                       | 479 ms: 1.02x faster                                                    |
| sympy_sum                  | 144 ms                                                       | 142 ms: 1.01x faster                                                    |
| regex_compile              | 128 ms                                                       | 127 ms: 1.01x faster                                                    |
| sympy_str                  | 265 ms                                                       | 263 ms: 1.01x faster                                                    |
| unpickle_pure_python       | 251 us                                                       | 254 us: 1.01x slower                                                    |
| pyflate                    | 557 ms                                                       | 562 ms: 1.01x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 196 us: 1.01x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 5.90 sec: 1.01x slower                                                  |
| mdp                        | 3.33 sec                                                     | 3.37 sec: 1.01x slower                                                  |
| python_startup_no_site     | 8.60 ms                                                      | 8.73 ms: 1.02x slower                                                   |
| float                      | 91.4 ms                                                      | 92.9 ms: 1.02x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 7.15 ms: 1.02x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 7.21 ms: 1.02x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| raytrace                   | 297 ms                                                       | 303 ms: 1.02x slower                                                    |
| json                       | 5.64 ms                                                      | 5.77 ms: 1.02x slower                                                   |
| json_loads                 | 32.1 us                                                      | 32.9 us: 1.03x slower                                                   |
| fannkuch                   | 451 ms                                                       | 464 ms: 1.03x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| json_dumps                 | 13.1 ms                                                      | 13.6 ms: 1.04x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (35): tornado_http, create_gc_cycles, sqlglot_parse, xml_etree_parse, meteor_contest, logging_format, scimark_monte_carlo, telco, scimark_sor, sqlglot_optimize, genshi_xml, pycparser, spectral_norm, xml_etree_generate, sqlglot_normalize, sympy_integrate, coroutines, sympy_expand, logging_silent, pickle_pure_python, scimark_fft, deltablue, python_startup, xml_etree_iterparse, pidigits, sqlglot_transpile, coverage, genshi_text, django_template, comprehensions, chaos, crypto_pyaes, asyncio_websockets, nqueens, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x