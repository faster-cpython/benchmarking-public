# Results vs. 3.13.0b2

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-aarch64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.02x faster
- HPT reliability: 99.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 398 ms: 1.20x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 547 ms: 1.18x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 531 ms: 1.14x faster                                                    |
| async_tree_none            | 492 ms                                                       | 433 ms: 1.14x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.09 sec: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 699 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 729 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.14x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| float          | 91.4 ms                                                      | 92.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.02x faster                                                   |
| regex_effbot   | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 127 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.56 sec: 1.01x faster                                                  |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| json_loads           | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 255 us: 1.01x slower                                                    |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.78 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.8 ms: 1.01x slower                                                   |
| mako           | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 332 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 37.9 us: 1.34x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 398 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.42 us: 1.18x faster                                                   |
| async_tree_memoization     | 645 ms                                                       | 547 ms: 1.18x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 531 ms: 1.14x faster                                                    |
| async_tree_none            | 492 ms                                                       | 433 ms: 1.14x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.09 sec: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 699 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 729 ms: 1.09x faster                                                    |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.5 ms: 1.06x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 134 ms: 1.05x faster                                                    |
| regex_dna                  | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| richards                   | 55.9 ms                                                      | 53.4 ms: 1.05x faster                                                   |
| logging_simple             | 7.21 us                                                      | 6.98 us: 1.03x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.59 us: 1.03x faster                                                   |
| richards_super             | 62.3 ms                                                      | 60.6 ms: 1.03x faster                                                   |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.37 ms: 1.03x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.05 ms: 1.03x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.02x faster                                                   |
| deltablue                  | 3.88 ms                                                      | 3.79 ms: 1.02x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.88 ms: 1.02x faster                                                   |
| logging_silent             | 133 ns                                                       | 131 ns: 1.02x faster                                                    |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.02x faster                                                   |
| telco                      | 10.0 ms                                                      | 9.88 ms: 1.01x faster                                                   |
| regex_compile              | 128 ms                                                       | 127 ms: 1.01x faster                                                    |
| coverage                   | 98.4 ms                                                      | 97.4 ms: 1.01x faster                                                   |
| mdp                        | 3.33 sec                                                     | 3.31 sec: 1.01x faster                                                  |
| tomli_loads                | 2.57 sec                                                     | 2.56 sec: 1.01x faster                                                  |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.23 sec: 1.01x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| float                      | 91.4 ms                                                      | 92.5 ms: 1.01x slower                                                   |
| sympy_str                  | 265 ms                                                       | 268 ms: 1.01x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 27.8 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 255 us: 1.01x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 1.74 ms: 1.01x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 21.2 ms: 1.02x slower                                                   |
| pyflate                    | 557 ms                                                       | 566 ms: 1.02x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 147 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.78 ms: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 463 ms: 1.03x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 201 us: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (38): create_gc_cycles, xml_etree_parse, sqlglot_optimize, scimark_sor, xml_etree_process, 2to3, tornado_http, sqlglot_normalize, sqlglot_parse, django_template, go, meteor_contest, pickle_pure_python, asyncio_tcp, scimark_monte_carlo, chaos, comprehensions, async_generators, scimark_fft, hexiom, pycparser, pprint_pformat, pidigits, pprint_safe_repr, bpe_tokeniser, bench_mp_pool, docutils, nqueens, raytrace, crypto_pyaes, spectral_norm, genshi_xml, sympy_expand, asyncio_websockets, thrift, json, html5lib, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x