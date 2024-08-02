# Results vs. base

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-aarch64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| html5lib       | 68.0 ms                                                                 | 66.6 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                             |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 718 ms                                                                  | 705 ms: 1.02x faster                                                     |
| Geometric mean             | (ref)                                                                   | 1.00x faster                                                             |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_memoization_tg, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 114 ms                                                                  | 112 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                             |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 30.8 ms                                                                 | 31.1 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                             |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|--------------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps         | 13.9 ms                                                                 | 13.3 ms: 1.05x faster                                                    |
| json_loads         | 33.1 us                                                                 | 32.3 us: 1.03x faster                                                    |
| xml_etree_process  | 81.4 ms                                                                 | 79.9 ms: 1.02x faster                                                    |
| xml_etree_generate | 113 ms                                                                  | 111 ms: 1.01x faster                                                     |
| xml_etree_parse    | 188 ms                                                                  | 196 ms: 1.04x slower                                                     |
| Geometric mean     | (ref)                                                                   | 1.00x faster                                                             |

Benchmark hidden because not significant (4): unpickle_pure_python, tomli_loads, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.8 ms                                                                 | 27.8 ms: 1.03x faster                                                    |
| genshi_xml     | 62.3 ms                                                                 | 60.4 ms: 1.03x faster                                                    |
| mako           | 13.6 ms                                                                 | 13.4 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps                 | 13.9 ms                                                                 | 13.3 ms: 1.05x faster                                                    |
| scimark_sparse_mat_mult    | 6.67 ms                                                                 | 6.41 ms: 1.04x faster                                                    |
| pyflate                    | 580 ms                                                                  | 558 ms: 1.04x faster                                                     |
| telco                      | 10.3 ms                                                                 | 9.94 ms: 1.04x faster                                                    |
| genshi_text                | 28.8 ms                                                                 | 27.8 ms: 1.03x faster                                                    |
| asyncio_tcp                | 579 ms                                                                  | 560 ms: 1.03x faster                                                     |
| genshi_xml                 | 62.3 ms                                                                 | 60.4 ms: 1.03x faster                                                    |
| gc_traversal               | 5.07 ms                                                                 | 4.93 ms: 1.03x faster                                                    |
| logging_simple             | 7.28 us                                                                 | 7.07 us: 1.03x faster                                                    |
| json                       | 5.85 ms                                                                 | 5.69 ms: 1.03x faster                                                    |
| json_loads                 | 33.1 us                                                                 | 32.3 us: 1.03x faster                                                    |
| asyncio_tcp_ssl            | 2.22 sec                                                                | 2.17 sec: 1.02x faster                                                   |
| richards_super             | 60.3 ms                                                                 | 59.0 ms: 1.02x faster                                                    |
| deepcopy_memo              | 39.3 us                                                                 | 38.5 us: 1.02x faster                                                    |
| html5lib                   | 68.0 ms                                                                 | 66.6 ms: 1.02x faster                                                    |
| pathlib                    | 21.6 ms                                                                 | 21.2 ms: 1.02x faster                                                    |
| fannkuch                   | 470 ms                                                                  | 461 ms: 1.02x faster                                                     |
| nbody                      | 114 ms                                                                  | 112 ms: 1.02x faster                                                     |
| scimark_lu                 | 139 ms                                                                  | 136 ms: 1.02x faster                                                     |
| xml_etree_process          | 81.4 ms                                                                 | 79.9 ms: 1.02x faster                                                    |
| mako                       | 13.6 ms                                                                 | 13.4 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 718 ms                                                                  | 705 ms: 1.02x faster                                                     |
| scimark_fft                | 448 ms                                                                  | 441 ms: 1.02x faster                                                     |
| sympy_expand               | 463 ms                                                                  | 457 ms: 1.01x faster                                                     |
| hexiom                     | 7.13 ms                                                                 | 7.04 ms: 1.01x faster                                                    |
| xml_etree_generate         | 113 ms                                                                  | 111 ms: 1.01x faster                                                     |
| raytrace                   | 300 ms                                                                  | 297 ms: 1.01x faster                                                     |
| pprint_pformat             | 1.92 sec                                                                | 1.90 sec: 1.01x faster                                                   |
| pprint_safe_repr           | 939 ms                                                                  | 931 ms: 1.01x faster                                                     |
| mdp                        | 3.33 sec                                                                | 3.31 sec: 1.01x faster                                                   |
| python_startup             | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                                    |
| regex_v8                   | 30.8 ms                                                                 | 31.1 ms: 1.01x slower                                                    |
| deepcopy_reduce            | 3.42 us                                                                 | 3.51 us: 1.03x slower                                                    |
| dulwich_log                | 59.5 ms                                                                 | 61.2 ms: 1.03x slower                                                    |
| nqueens                    | 99.2 ms                                                                 | 103 ms: 1.04x slower                                                     |
| xml_etree_parse            | 188 ms                                                                  | 196 ms: 1.04x slower                                                     |
| Geometric mean             | (ref)                                                                   | 1.01x faster                                                             |

Benchmark hidden because not significant (54): tornado_http, richards, python_startup_no_site, logging_format, pylint, sympy_integrate, bench_mp_pool, regex_effbot, sqlglot_transpile, logging_silent, sympy_str, scimark_sor, deltablue, regex_dna, chaos, async_tree_cpu_io_mixed, coroutines, unpickle_pure_python, thrift, go, bench_thread_pool, tomli_loads, spectral_norm, sqlglot_normalize, crypto_pyaes, pycparser, async_tree_none_tg, regex_compile, bpe_tokeniser, async_tree_memoization, async_tree_none, scimark_monte_carlo, float, generators, pidigits, 2to3, typing_runtime_protocols, asyncio_websockets, create_gc_cycles, async_generators, async_tree_memoization_tg, deepcopy, sqlglot_parse, meteor_contest, comprehensions, docutils, async_tree_io_tg, pickle_pure_python, coverage, django_template, sympy_sum, async_tree_io, sqlglot_optimize, xml_etree_iterparse

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x