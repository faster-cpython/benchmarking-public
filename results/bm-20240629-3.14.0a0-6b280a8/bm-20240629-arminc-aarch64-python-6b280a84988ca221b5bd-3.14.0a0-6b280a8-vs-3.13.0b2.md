# Results vs. 3.13.0b2

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: linux-aarch64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.02x faster
- HPT reliability: 85.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 3.07 sec: 1.01x faster                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 409 ms: 1.16x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                  |
| async_tree_memoization     | 645 ms                                                       | 569 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 533 ms: 1.13x faster                                                    |
| async_tree_none            | 492 ms                                                       | 441 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 731 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 713 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| float          | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 248 ms: 1.04x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|---------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                  |
| xml_etree_iterparse | 147 ms                                                       | 149 ms: 1.01x slower                                                    |
| json_dumps          | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| json_loads          | 32.1 us                                                      | 33.0 us: 1.03x slower                                                   |
| Geometric mean      | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_pure_python, unpickle_pure_python, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.82 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                   |
| mako           | 13.2 ms                                                      | 13.6 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 331 us: 1.36x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 37.8 us: 1.34x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 409 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.47 us: 1.16x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                  |
| async_tree_memoization     | 645 ms                                                       | 569 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 533 ms: 1.13x faster                                                    |
| async_tree_none            | 492 ms                                                       | 441 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 731 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 713 ms: 1.07x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.86 ms: 1.07x faster                                                   |
| richards                   | 55.9 ms                                                      | 52.8 ms: 1.06x faster                                                   |
| richards_super             | 62.3 ms                                                      | 59.2 ms: 1.05x faster                                                   |
| regex_dna                  | 259 ms                                                       | 248 ms: 1.04x faster                                                    |
| logging_simple             | 7.21 us                                                      | 6.93 us: 1.04x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.9 ms: 1.04x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 137 ms: 1.03x faster                                                    |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.69 us: 1.02x faster                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                  |
| docutils                   | 3.10 sec                                                     | 3.07 sec: 1.01x faster                                                  |
| scimark_fft                | 445 ms                                                       | 448 ms: 1.01x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.35 sec: 1.01x slower                                                  |
| fannkuch                   | 451 ms                                                       | 456 ms: 1.01x slower                                                    |
| sympy_str                  | 265 ms                                                       | 268 ms: 1.01x slower                                                    |
| sympy_expand               | 457 ms                                                       | 462 ms: 1.01x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 946 ms: 1.01x slower                                                    |
| float                      | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.24 sec: 1.01x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.01x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                   |
| coverage                   | 98.4 ms                                                      | 100 ms: 1.02x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 29.6 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.82 ms: 1.03x slower                                                   |
| generators                 | 37.1 ms                                                      | 38.1 ms: 1.03x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| json_loads                 | 32.1 us                                                      | 33.0 us: 1.03x slower                                                   |
| json                       | 5.64 ms                                                      | 5.81 ms: 1.03x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.6 ms: 1.03x slower                                                   |
| pyflate                    | 557 ms                                                       | 583 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 207 us: 1.07x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (47): dask, xml_etree_parse, bench_thread_pool, bench_mp_pool, tornado_http, sqlglot_parse, deltablue, meteor_contest, asyncio_tcp, sqlglot_normalize, logging_silent, regex_v8, crypto_pyaes, python_startup, scimark_sor, nqueens, scimark_monte_carlo, pidigits, html5lib, bpe_tokeniser, regex_compile, go, async_generators, pickle_pure_python, comprehensions, unpickle_pure_python, pprint_pformat, thrift, sqlglot_optimize, scimark_sparse_mat_mult, xml_etree_process, spectral_norm, 2to3, asyncio_websockets, pycparser, raytrace, chaos, telco, sympy_integrate, hexiom, dulwich_log, sympy_sum, genshi_xml, create_gc_cycles, django_template, pylint, xml_etree_generate
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 85.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x