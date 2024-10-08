# Results vs. 3.13.0b2

- fork: python
- ref: c8db0e817e7e0db50153
- machine: linux-aarch64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.05x slower
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| docutils       | 3.10 sec                                                     | 2.99 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 418 ms: 1.18x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 558 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 549 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 726 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 716 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| float          | 91.4 ms                                                      | 94.6 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 5.03 ms: 1.01x slower                                                   |
| regex_dna      | 259 ms                                                       | 262 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 31.3 us: 1.03x faster                                                   |
| unpickle             | 19.8 us                                                      | 19.4 us: 1.02x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| pickle_list          | 5.27 us                                                      | 5.32 us: 1.01x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 254 us: 1.01x slower                                                    |
| pickle               | 13.4 us                                                      | 13.6 us: 1.02x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| pickle_pure_python   | 359 us                                                       | 370 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, pickle_dict, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 28.1 ms: 1.02x slower                                                   |
| mako           | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.6 us: 1.35x faster                                                   |
| deepcopy                   | 448 us                                                       | 333 us: 1.35x faster                                                    |
| async_tree_none            | 492 ms                                                       | 418 ms: 1.18x faster                                                    |
| go                         | 161 ms                                                       | 139 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 558 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.52 us: 1.15x faster                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 549 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 726 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| pathlib                    | 22.8 ms                                                      | 21.3 ms: 1.07x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                                  |
| generators                 | 37.1 ms                                                      | 34.9 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 716 ms: 1.07x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 133 ms: 1.06x faster                                                    |
| richards                   | 55.9 ms                                                      | 52.7 ms: 1.06x faster                                                   |
| telco                      | 10.0 ms                                                      | 9.47 ms: 1.06x faster                                                   |
| asyncio_tcp                | 584 ms                                                       | 558 ms: 1.05x faster                                                    |
| richards_super             | 62.3 ms                                                      | 59.7 ms: 1.04x faster                                                   |
| docutils                   | 3.10 sec                                                     | 2.99 sec: 1.03x faster                                                  |
| 2to3                       | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| thrift                     | 962 us                                                       | 931 us: 1.03x faster                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.26 ms: 1.03x faster                                                   |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| scimark_fft                | 445 ms                                                       | 434 ms: 1.03x faster                                                    |
| json_loads                 | 32.1 us                                                      | 31.3 us: 1.03x faster                                                   |
| async_generators           | 488 ms                                                       | 477 ms: 1.02x faster                                                    |
| logging_silent             | 133 ns                                                       | 130 ns: 1.02x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                   |
| sympy_sum                  | 144 ms                                                       | 141 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.41 ms: 1.02x faster                                                   |
| logging_simple             | 7.21 us                                                      | 7.05 us: 1.02x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.4 us: 1.02x faster                                                   |
| pprint_safe_repr           | 933 ms                                                       | 915 ms: 1.02x faster                                                    |
| sqlite_synth               | 3.90 us                                                      | 3.83 us: 1.02x faster                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.89 sec: 1.02x faster                                                  |
| logging_format             | 7.82 us                                                      | 7.70 us: 1.02x faster                                                   |
| regex_compile              | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                      | 28.6 ms: 1.01x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| mdp                        | 3.33 sec                                                     | 3.31 sec: 1.00x faster                                                  |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| pickle_list                | 5.27 us                                                      | 5.32 us: 1.01x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 254 us: 1.01x slower                                                    |
| regex_effbot               | 4.98 ms                                                      | 5.03 ms: 1.01x slower                                                   |
| regex_dna                  | 259 ms                                                       | 262 ms: 1.01x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.74 ms: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.6 us: 1.02x slower                                                   |
| chaos                      | 68.3 ms                                                      | 69.7 ms: 1.02x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 28.1 ms: 1.02x slower                                                   |
| raytrace                   | 297 ms                                                       | 304 ms: 1.02x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| fannkuch                   | 451 ms                                                       | 463 ms: 1.03x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 370 us: 1.03x slower                                                    |
| float                      | 91.4 ms                                                      | 94.6 ms: 1.03x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.30 ms: 1.04x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 5.71 sec: 812.04x slower                                                |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                            |

Benchmark hidden because not significant (36): tornado_http, xml_etree_parse, sqlglot_normalize, json, html5lib, xml_etree_process, sqlglot_parse, spectral_norm, sympy_str, meteor_contest, scimark_monte_carlo, asyncio_tcp_ssl, bpe_tokeniser, gc_traversal, scimark_sor, sympy_expand, pyflate, pidigits, pickle_dict, typing_runtime_protocols, python_startup_no_site, dulwich_log, coverage, asyncio_websockets, django_template, crypto_pyaes, genshi_xml, pycparser, nqueens, comprehensions, sympy_integrate, hexiom, sqlglot_optimize, unpickle_list, deltablue, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-arminc-aarch64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: unpack_sequence

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x