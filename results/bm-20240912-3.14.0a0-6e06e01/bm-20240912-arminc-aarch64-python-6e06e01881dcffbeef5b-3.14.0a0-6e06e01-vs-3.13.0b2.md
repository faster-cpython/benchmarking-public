# Results vs. 3.13.0b2

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-aarch64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.02x faster
- HPT reliability: 99.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 297 ms: 1.03x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.05 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 421 ms: 1.17x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 562 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 720 ms: 1.10x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 553 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 718 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 110 ms: 1.03x faster                                                    |
| float          | 91.4 ms                                                      | 92.9 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| regex_dna      | 259 ms                                                       | 255 ms: 1.01x faster                                                    |
| regex_compile  | 128 ms                                                       | 127 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|--------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list      | 6.52 us                                                      | 6.40 us: 1.02x faster                                                   |
| pickle_list        | 5.27 us                                                      | 5.20 us: 1.01x faster                                                   |
| json_loads         | 32.1 us                                                      | 31.7 us: 1.01x faster                                                   |
| unpickle           | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| pickle             | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| json_dumps         | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| tomli_loads        | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| pickle_pure_python | 359 us                                                       | 373 us: 1.04x slower                                                    |
| Geometric mean     | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_parse, unpickle_pure_python, pickle_dict, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.5 us: 1.35x faster                                                   |
| deepcopy                   | 448 us                                                       | 337 us: 1.33x faster                                                    |
| async_tree_none            | 492 ms                                                       | 421 ms: 1.17x faster                                                    |
| go                         | 161 ms                                                       | 139 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 562 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.57 us: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 720 ms: 1.10x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 553 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.08x faster                                                  |
| pathlib                    | 22.8 ms                                                      | 21.1 ms: 1.08x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.9 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 718 ms: 1.06x faster                                                    |
| richards                   | 55.9 ms                                                      | 52.8 ms: 1.06x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 135 ms: 1.05x faster                                                    |
| richards_super             | 62.3 ms                                                      | 60.1 ms: 1.04x faster                                                   |
| nbody                      | 114 ms                                                       | 110 ms: 1.03x faster                                                    |
| thrift                     | 962 us                                                       | 931 us: 1.03x faster                                                    |
| asyncio_tcp                | 584 ms                                                       | 567 ms: 1.03x faster                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.27 ms: 1.03x faster                                                   |
| 2to3                       | 305 ms                                                       | 297 ms: 1.03x faster                                                    |
| sqlite_synth               | 3.90 us                                                      | 3.81 us: 1.02x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| async_generators           | 488 ms                                                       | 479 ms: 1.02x faster                                                    |
| unpickle_list              | 6.52 us                                                      | 6.40 us: 1.02x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.09 ms: 1.02x faster                                                   |
| docutils                   | 3.10 sec                                                     | 3.05 sec: 1.02x faster                                                  |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.02x faster                                                    |
| regex_dna                  | 259 ms                                                       | 255 ms: 1.01x faster                                                    |
| pickle_list                | 5.27 us                                                      | 5.20 us: 1.01x faster                                                   |
| json_loads                 | 32.1 us                                                      | 31.7 us: 1.01x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.91 sec: 1.01x faster                                                  |
| regex_compile              | 128 ms                                                       | 127 ms: 1.01x faster                                                    |
| spectral_norm              | 141 ms                                                       | 140 ms: 1.01x faster                                                    |
| coverage                   | 98.4 ms                                                      | 97.6 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 933 ms                                                       | 926 ms: 1.01x faster                                                    |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 7.11 ms: 1.01x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.37 sec: 1.01x slower                                                  |
| raytrace                   | 297 ms                                                       | 301 ms: 1.02x slower                                                    |
| float                      | 91.4 ms                                                      | 92.9 ms: 1.02x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 1.75 ms: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.2 ms: 1.02x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 462 ms: 1.02x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| pickle_pure_python         | 359 us                                                       | 373 us: 1.04x slower                                                    |
| pyflate                    | 557 ms                                                       | 580 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (43): sqlglot_normalize, scimark_sor, scimark_sparse_mat_mult, xml_etree_generate, sympy_sum, json, typing_runtime_protocols, sympy_str, html5lib, sympy_integrate, regex_effbot, nqueens, logging_silent, coroutines, logging_simple, sqlglot_optimize, scimark_monte_carlo, deltablue, genshi_text, comprehensions, xml_etree_parse, crypto_pyaes, pidigits, asyncio_tcp_ssl, django_template, scimark_fft, bpe_tokeniser, genshi_xml, chaos, sqlglot_parse, unpickle_pure_python, asyncio_websockets, tornado_http, pickle_dict, logging_format, pycparser, xml_etree_process, python_startup_no_site, sympy_expand, dulwich_log, hexiom, xml_etree_iterparse, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: unpack_sequence

# HPT report

- Reliability score: 99.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x