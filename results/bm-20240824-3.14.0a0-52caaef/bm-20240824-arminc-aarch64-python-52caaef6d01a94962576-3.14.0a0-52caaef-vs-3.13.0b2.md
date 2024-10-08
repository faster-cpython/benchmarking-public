# Results vs. 3.13.0b2

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 297 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 423 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 557 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 419 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 727 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 732 ms: 1.04x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 108 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                       | 123 ms: 1.04x faster                                                    |
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process | 80.8 ms                                                      | 78.3 ms: 1.03x faster                                                   |
| json_loads        | 32.1 us                                                      | 32.6 us: 1.01x slower                                                   |
| tomli_loads       | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                  |
| Geometric mean    | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_parse, pickle_pure_python, xml_etree_generate, json_dumps, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.77 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (3): genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.0 us: 1.34x faster                                                   |
| deepcopy                   | 448 us                                                       | 336 us: 1.33x faster                                                    |
| async_tree_none            | 492 ms                                                       | 423 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 557 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.50 us: 1.15x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 419 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 727 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| pathlib                    | 22.8 ms                                                      | 21.2 ms: 1.07x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| generators                 | 37.1 ms                                                      | 35.0 ms: 1.06x faster                                                   |
| nbody                      | 114 ms                                                       | 108 ms: 1.06x faster                                                    |
| richards_super             | 62.3 ms                                                      | 59.0 ms: 1.06x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 4.91 ms: 1.05x faster                                                   |
| richards                   | 55.9 ms                                                      | 53.0 ms: 1.05x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 134 ms: 1.05x faster                                                    |
| logging_simple             | 7.21 us                                                      | 6.90 us: 1.04x faster                                                   |
| thrift                     | 962 us                                                       | 921 us: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 732 ms: 1.04x faster                                                    |
| regex_compile              | 128 ms                                                       | 123 ms: 1.04x faster                                                    |
| asyncio_tcp                | 584 ms                                                       | 564 ms: 1.03x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.87 sec: 1.03x faster                                                  |
| xml_etree_process          | 80.8 ms                                                      | 78.3 ms: 1.03x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.61 us: 1.03x faster                                                   |
| pprint_safe_repr           | 933 ms                                                       | 909 ms: 1.03x faster                                                    |
| regex_dna                  | 259 ms                                                       | 252 ms: 1.03x faster                                                    |
| 2to3                       | 305 ms                                                       | 297 ms: 1.03x faster                                                    |
| telco                      | 10.0 ms                                                      | 9.77 ms: 1.03x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.4 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                       | 111 ms: 1.02x faster                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| sympy_sum                  | 144 ms                                                       | 141 ms: 1.02x faster                                                    |
| logging_silent             | 133 ns                                                       | 132 ns: 1.01x faster                                                    |
| scimark_sor                | 159 ms                                                       | 158 ms: 1.01x faster                                                    |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.37 sec: 1.01x slower                                                  |
| fannkuch                   | 451 ms                                                       | 458 ms: 1.01x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.6 us: 1.01x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                  |
| python_startup_no_site     | 8.60 ms                                                      | 8.77 ms: 1.02x slower                                                   |
| raytrace                   | 297 ms                                                       | 303 ms: 1.02x slower                                                    |
| go                         | 161 ms                                                       | 193 ms: 1.20x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (44): tornado_http, xml_etree_parse, sympy_integrate, typing_runtime_protocols, scimark_monte_carlo, create_gc_cycles, genshi_xml, scimark_sparse_mat_mult, pickle_pure_python, xml_etree_generate, hexiom, sqlglot_optimize, nqueens, scimark_fft, bench_mp_pool, async_generators, spectral_norm, pyflate, sqlglot_normalize, docutils, pycparser, float, json_dumps, sqlglot_parse, pidigits, sqlglot_transpile, coverage, sympy_str, asyncio_tcp_ssl, bpe_tokeniser, chaos, crypto_pyaes, python_startup, json, django_template, deltablue, unpickle_pure_python, sympy_expand, genshi_text, asyncio_websockets, comprehensions, html5lib, xml_etree_iterparse, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x