# Results vs. 3.13.0b2

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: linux-aarch64
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.05x slower
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 293 ms: 1.04x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.03 sec: 1.02x faster                                                  |
| html5lib       | 66.1 ms                                                      | 64.2 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 550 ms: 1.17x faster                                                    |
| async_tree_none            | 492 ms                                                       | 428 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 420 ms: 1.13x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.15 sec: 1.11x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 545 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 722 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 708 ms: 1.08x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.16 sec: 1.05x faster                                                  |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 94.6 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                       | 124 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.2 us: 1.03x faster                                                   |
| json_loads           | 32.1 us                                                      | 31.3 us: 1.03x faster                                                   |
| pickle_list          | 5.27 us                                                      | 5.17 us: 1.02x faster                                                   |
| unpickle_pure_python | 251 us                                                       | 255 us: 1.01x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 364 us: 1.02x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| pickle               | 13.4 us                                                      | 13.9 us: 1.04x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 153 ms: 1.04x slower                                                    |
| json_dumps           | 13.1 ms                                                      | 14.6 ms: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, pickle_dict, unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 13.0 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.1 ms: 1.01x faster                                                   |
| mako           | 13.2 ms                                                      | 13.6 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 332 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 37.8 us: 1.34x faster                                                   |
| go                         | 161 ms                                                       | 137 ms: 1.18x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 550 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.51 us: 1.15x faster                                                   |
| async_tree_none            | 492 ms                                                       | 428 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 420 ms: 1.13x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.15 sec: 1.11x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 545 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 722 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 708 ms: 1.08x faster                                                    |
| telco                      | 10.0 ms                                                      | 9.31 ms: 1.08x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.2 ms: 1.07x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                   |
| richards                   | 55.9 ms                                                      | 52.9 ms: 1.06x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 134 ms: 1.06x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.16 sec: 1.05x faster                                                  |
| 2to3                       | 305 ms                                                       | 293 ms: 1.04x faster                                                    |
| richards_super             | 62.3 ms                                                      | 59.9 ms: 1.04x faster                                                   |
| asyncio_tcp                | 584 ms                                                       | 563 ms: 1.04x faster                                                    |
| logging_format             | 7.82 us                                                      | 7.55 us: 1.04x faster                                                   |
| logging_simple             | 7.21 us                                                      | 6.96 us: 1.03x faster                                                   |
| thrift                     | 962 us                                                       | 931 us: 1.03x faster                                                    |
| regex_compile              | 128 ms                                                       | 124 ms: 1.03x faster                                                    |
| html5lib                   | 66.1 ms                                                      | 64.2 ms: 1.03x faster                                                   |
| logging_silent             | 133 ns                                                       | 130 ns: 1.03x faster                                                    |
| unpickle                   | 19.8 us                                                      | 19.2 us: 1.03x faster                                                   |
| json_loads                 | 32.1 us                                                      | 31.3 us: 1.03x faster                                                   |
| async_generators           | 488 ms                                                       | 475 ms: 1.03x faster                                                    |
| pprint_safe_repr           | 933 ms                                                       | 911 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.89 sec: 1.02x faster                                                  |
| bpe_tokeniser              | 5.83 sec                                                     | 5.70 sec: 1.02x faster                                                  |
| meteor_contest             | 113 ms                                                       | 111 ms: 1.02x faster                                                    |
| docutils                   | 3.10 sec                                                     | 3.03 sec: 1.02x faster                                                  |
| pickle_list                | 5.27 us                                                      | 5.17 us: 1.02x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.09 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| genshi_text                | 27.4 ms                                                      | 27.1 ms: 1.01x faster                                                   |
| scimark_fft                | 445 ms                                                       | 441 ms: 1.01x faster                                                    |
| python_startup             | 13.0 ms                                                      | 13.0 ms: 1.00x slower                                                   |
| scimark_sor                | 159 ms                                                       | 161 ms: 1.01x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 255 us: 1.01x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.28 ms: 1.02x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.24 sec: 1.02x slower                                                  |
| pickle_pure_python         | 359 us                                                       | 364 us: 1.02x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.74 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 84.5 ms: 1.03x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| mako                       | 13.2 ms                                                      | 13.6 ms: 1.03x slower                                                   |
| chaos                      | 68.3 ms                                                      | 70.5 ms: 1.03x slower                                                   |
| float                      | 91.4 ms                                                      | 94.6 ms: 1.03x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.9 us: 1.04x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 153 ms: 1.04x slower                                                    |
| raytrace                   | 297 ms                                                       | 310 ms: 1.04x slower                                                    |
| fannkuch                   | 451 ms                                                       | 471 ms: 1.04x slower                                                    |
| pyflate                    | 557 ms                                                       | 582 ms: 1.05x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 14.6 ms: 1.12x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 5.11 sec: 727.29x slower                                                |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                            |

Benchmark hidden because not significant (38): sqlglot_normalize, tornado_http, sympy_sum, json, xml_etree_generate, xml_etree_process, genshi_xml, spectral_norm, dulwich_log, crypto_pyaes, sympy_str, sqlglot_optimize, coverage, sympy_expand, regex_v8, asyncio_tcp_ssl, mdp, asyncio_websockets, pickle_dict, sqlite_synth, pidigits, sqlglot_parse, unpickle_list, django_template, nbody, hexiom, regex_dna, regex_effbot, scimark_sparse_mat_mult, comprehensions, python_startup_no_site, nqueens, deltablue, sympy_integrate, typing_runtime_protocols, create_gc_cycles, xml_etree_parse, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-arminc-aarch64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: unpack_sequence

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x