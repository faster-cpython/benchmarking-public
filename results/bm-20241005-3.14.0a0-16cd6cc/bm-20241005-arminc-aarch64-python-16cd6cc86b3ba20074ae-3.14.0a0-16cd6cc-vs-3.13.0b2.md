# Results vs. 3.13.0b2

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.04x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 294 ms: 1.04x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                                  |
| html5lib       | 66.1 ms                                                      | 64.8 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 555 ms: 1.16x faster                                                    |
| async_tree_none            | 492 ms                                                       | 424 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 412 ms: 1.16x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 552 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 728 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.08x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 721 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 110 ms: 1.04x faster                                                    |
| float          | 91.4 ms                                                      | 93.0 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|--------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads         | 32.1 us                                                      | 31.2 us: 1.03x faster                                                   |
| xml_etree_parse    | 191 ms                                                       | 186 ms: 1.03x faster                                                    |
| unpickle           | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| xml_etree_generate | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| pickle_dict        | 37.6 us                                                      | 37.4 us: 1.01x faster                                                   |
| json_dumps         | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| tomli_loads        | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| pickle             | 13.4 us                                                      | 13.7 us: 1.03x slower                                                   |
| Geometric mean     | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_process, pickle_list, unpickle_pure_python, pickle_pure_python, xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.9 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.8 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 335 us: 1.34x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.1 us: 1.33x faster                                                   |
| async_tree_memoization     | 645 ms                                                       | 555 ms: 1.16x faster                                                    |
| go                         | 161 ms                                                       | 138 ms: 1.16x faster                                                    |
| async_tree_none            | 492 ms                                                       | 424 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 412 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.52 us: 1.15x faster                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 552 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 728 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.08x faster                                                  |
| pathlib                    | 22.8 ms                                                      | 21.2 ms: 1.08x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 133 ms: 1.06x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| telco                      | 10.0 ms                                                      | 9.45 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 721 ms: 1.06x faster                                                    |
| richards                   | 55.9 ms                                                      | 53.0 ms: 1.05x faster                                                   |
| richards_super             | 62.3 ms                                                      | 59.3 ms: 1.05x faster                                                   |
| thrift                     | 962 us                                                       | 920 us: 1.05x faster                                                    |
| asyncio_tcp                | 584 ms                                                       | 559 ms: 1.04x faster                                                    |
| scimark_fft                | 445 ms                                                       | 427 ms: 1.04x faster                                                    |
| 2to3                       | 305 ms                                                       | 294 ms: 1.04x faster                                                    |
| nbody                      | 114 ms                                                       | 110 ms: 1.04x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.02 ms: 1.03x faster                                                   |
| json_loads                 | 32.1 us                                                      | 31.2 us: 1.03x faster                                                   |
| docutils                   | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                                  |
| xml_etree_parse            | 191 ms                                                       | 186 ms: 1.03x faster                                                    |
| pprint_safe_repr           | 933 ms                                                       | 907 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.37 ms: 1.03x faster                                                   |
| sympy_sum                  | 144 ms                                                       | 140 ms: 1.03x faster                                                    |
| logging_silent             | 133 ns                                                       | 130 ns: 1.03x faster                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.03x faster                                                   |
| async_generators           | 488 ms                                                       | 476 ms: 1.02x faster                                                    |
| sqlite_synth               | 3.90 us                                                      | 3.81 us: 1.02x faster                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.89 sec: 1.02x faster                                                  |
| html5lib                   | 66.1 ms                                                      | 64.8 ms: 1.02x faster                                                   |
| json                       | 5.64 ms                                                      | 5.53 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| regex_compile              | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.72 us: 1.01x faster                                                   |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.01x faster                                                    |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.20 sec: 1.01x faster                                                  |
| pickle_dict                | 37.6 us                                                      | 37.4 us: 1.01x faster                                                   |
| python_startup             | 13.0 ms                                                      | 12.9 ms: 1.01x faster                                                   |
| coverage                   | 98.4 ms                                                      | 99.3 ms: 1.01x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| chaos                      | 68.3 ms                                                      | 69.4 ms: 1.02x slower                                                   |
| float                      | 91.4 ms                                                      | 93.0 ms: 1.02x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.03x slower                                                   |
| raytrace                   | 297 ms                                                       | 305 ms: 1.03x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.30 ms: 1.03x slower                                                   |
| fannkuch                   | 451 ms                                                       | 468 ms: 1.04x slower                                                    |
| pyflate                    | 557 ms                                                       | 579 ms: 1.04x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.8 ms: 1.05x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 4.42 sec: 629.34x slower                                                |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                            |

Benchmark hidden because not significant (37): sqlglot_normalize, logging_simple, regex_v8, meteor_contest, nqueens, xml_etree_process, sympy_str, django_template, sympy_expand, typing_runtime_protocols, pickle_list, crypto_pyaes, mdp, regex_dna, dulwich_log, python_startup_no_site, regex_effbot, pidigits, bpe_tokeniser, sympy_integrate, genshi_text, asyncio_websockets, genshi_xml, sqlglot_optimize, hexiom, comprehensions, tornado_http, scimark_monte_carlo, sqlglot_parse, spectral_norm, unpickle_pure_python, pycparser, pickle_pure_python, deltablue, xml_etree_iterparse, unpickle_list, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: unpack_sequence

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x