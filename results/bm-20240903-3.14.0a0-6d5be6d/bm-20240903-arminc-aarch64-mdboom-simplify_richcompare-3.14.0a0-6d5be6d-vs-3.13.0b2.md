# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 296 ms: 1.03x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                                  |
| html5lib       | 66.1 ms                                                      | 63.2 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 423 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 558 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 418 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 551 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 727 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 724 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 108 ms: 1.06x faster                                                    |
| float          | 91.4 ms                                                      | 92.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                       | 125 ms: 1.02x faster                                                    |
| regex_dna      | 259 ms                                                       | 253 ms: 1.02x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| json_loads         | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| tomli_loads        | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| json_dumps         | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean     | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_process, xml_etree_parse, pickle_pure_python, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.77 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 333 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 37.9 us: 1.34x faster                                                   |
| go                         | 161 ms                                                       | 136 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.47 us: 1.16x faster                                                   |
| async_tree_none            | 492 ms                                                       | 423 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 558 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 418 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 551 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 727 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| pathlib                    | 22.8 ms                                                      | 21.2 ms: 1.07x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 133 ms: 1.06x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| nbody                      | 114 ms                                                       | 108 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 724 ms: 1.05x faster                                                    |
| richards                   | 55.9 ms                                                      | 53.3 ms: 1.05x faster                                                   |
| html5lib                   | 66.1 ms                                                      | 63.2 ms: 1.05x faster                                                   |
| richards_super             | 62.3 ms                                                      | 59.7 ms: 1.04x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 4.99 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.87 sec: 1.03x faster                                                  |
| 2to3                       | 305 ms                                                       | 296 ms: 1.03x faster                                                    |
| docutils                   | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                                  |
| pprint_safe_repr           | 933 ms                                                       | 907 ms: 1.03x faster                                                    |
| meteor_contest             | 113 ms                                                       | 110 ms: 1.03x faster                                                    |
| asyncio_tcp                | 584 ms                                                       | 568 ms: 1.03x faster                                                    |
| logging_simple             | 7.21 us                                                      | 7.02 us: 1.03x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.39 ms: 1.03x faster                                                   |
| sympy_sum                  | 144 ms                                                       | 140 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 80.4 ms: 1.02x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.64 us: 1.02x faster                                                   |
| regex_compile              | 128 ms                                                       | 125 ms: 1.02x faster                                                    |
| scimark_sor                | 159 ms                                                       | 156 ms: 1.02x faster                                                    |
| telco                      | 10.0 ms                                                      | 9.81 ms: 1.02x faster                                                   |
| regex_dna                  | 259 ms                                                       | 253 ms: 1.02x faster                                                    |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| async_generators           | 488 ms                                                       | 479 ms: 1.02x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| thrift                     | 962 us                                                       | 947 us: 1.02x faster                                                    |
| nqueens                    | 98.9 ms                                                      | 97.4 ms: 1.02x faster                                                   |
| logging_silent             | 133 ns                                                       | 131 ns: 1.02x faster                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.01x faster                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 6.94 ms: 1.01x faster                                                   |
| comprehensions             | 20.5 us                                                      | 20.3 us: 1.01x faster                                                   |
| float                      | 91.4 ms                                                      | 92.4 ms: 1.01x slower                                                   |
| raytrace                   | 297 ms                                                       | 300 ms: 1.01x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 460 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.77 ms: 1.02x slower                                                   |
| json_loads                 | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| pyflate                    | 557 ms                                                       | 575 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (34): create_gc_cycles, sqlglot_normalize, sqlglot_parse, xml_etree_process, sqlglot_optimize, genshi_xml, tornado_http, sympy_integrate, deltablue, hexiom, typing_runtime_protocols, xml_etree_parse, coverage, asyncio_tcp_ssl, mdp, pickle_pure_python, sympy_str, chaos, spectral_norm, genshi_text, scimark_fft, unpickle_pure_python, crypto_pyaes, sympy_expand, xml_etree_iterparse, django_template, python_startup, pidigits, pycparser, bpe_tokeniser, asyncio_websockets, sqlglot_transpile, json, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x