# Results vs. base

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.00x faster
- HPT reliability: 99.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                       | 302 ms: 1.01x faster                                                     |
| chameleon      | 9.23 ms                                                      | 9.02 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 110 ms                                                       | 112 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_compile, regex_v8, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 199 ms                                                       | 191 ms: 1.04x faster                                                     |
| xml_etree_generate   | 118 ms                                                       | 113 ms: 1.04x faster                                                     |
| tomli_loads          | 2.64 sec                                                     | 2.54 sec: 1.04x faster                                                   |
| pickle_list          | 5.26 us                                                      | 5.12 us: 1.03x faster                                                    |
| unpickle_pure_python | 255 us                                                       | 251 us: 1.02x faster                                                     |
| pickle_dict          | 38.0 us                                                      | 37.5 us: 1.01x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                       | 149 ms: 1.01x faster                                                     |
| json_loads           | 32.3 us                                                      | 32.6 us: 1.01x slower                                                    |
| unpickle             | 19.5 us                                                      | 19.7 us: 1.01x slower                                                    |
| unpickle_list        | 6.31 us                                                      | 6.46 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (4): xml_etree_process, pickle, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 42.6 ms                                                      | 41.3 ms: 1.03x faster                                                    |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pyflate                  | 595 ms                                                       | 557 ms: 1.07x faster                                                     |
| xml_etree_parse          | 199 ms                                                       | 191 ms: 1.04x faster                                                     |
| xml_etree_generate       | 118 ms                                                       | 113 ms: 1.04x faster                                                     |
| tomli_loads              | 2.64 sec                                                     | 2.54 sec: 1.04x faster                                                   |
| django_template          | 42.6 ms                                                      | 41.3 ms: 1.03x faster                                                    |
| typing_runtime_protocols | 203 us                                                       | 197 us: 1.03x faster                                                     |
| pickle_list              | 5.26 us                                                      | 5.12 us: 1.03x faster                                                    |
| richards                 | 56.3 ms                                                      | 54.9 ms: 1.03x faster                                                    |
| deepcopy                 | 453 us                                                       | 443 us: 1.02x faster                                                     |
| chameleon                | 9.23 ms                                                      | 9.02 ms: 1.02x faster                                                    |
| telco                    | 167 ms                                                       | 164 ms: 1.02x faster                                                     |
| coroutines               | 29.7 ms                                                      | 29.0 ms: 1.02x faster                                                    |
| nqueens                  | 101 ms                                                       | 99.0 ms: 1.02x faster                                                    |
| sympy_integrate          | 21.4 ms                                                      | 21.0 ms: 1.02x faster                                                    |
| unpickle_pure_python     | 255 us                                                       | 251 us: 1.02x faster                                                     |
| sympy_expand             | 470 ms                                                       | 463 ms: 1.01x faster                                                     |
| dulwich_log              | 59.5 ms                                                      | 58.7 ms: 1.01x faster                                                    |
| crypto_pyaes             | 82.4 ms                                                      | 81.2 ms: 1.01x faster                                                    |
| pickle_dict              | 38.0 us                                                      | 37.5 us: 1.01x faster                                                    |
| 2to3                     | 306 ms                                                       | 302 ms: 1.01x faster                                                     |
| scimark_sor              | 160 ms                                                       | 158 ms: 1.01x faster                                                     |
| scimark_lu               | 139 ms                                                       | 138 ms: 1.01x faster                                                     |
| coverage                 | 98.6 ms                                                      | 97.5 ms: 1.01x faster                                                    |
| deepcopy_reduce          | 4.09 us                                                      | 4.04 us: 1.01x faster                                                    |
| hexiom                   | 7.07 ms                                                      | 7.01 ms: 1.01x faster                                                    |
| bench_thread_pool        | 1.28 ms                                                      | 1.27 ms: 1.01x faster                                                    |
| xml_etree_iterparse      | 150 ms                                                       | 149 ms: 1.01x faster                                                     |
| sqlglot_transpile        | 1.73 ms                                                      | 1.72 ms: 1.01x faster                                                    |
| gc_traversal             | 5.09 ms                                                      | 5.13 ms: 1.01x slower                                                    |
| scimark_fft              | 442 ms                                                       | 446 ms: 1.01x slower                                                     |
| json_loads               | 32.3 us                                                      | 32.6 us: 1.01x slower                                                    |
| nbody                    | 110 ms                                                       | 112 ms: 1.01x slower                                                     |
| unpickle                 | 19.5 us                                                      | 19.7 us: 1.01x slower                                                    |
| json                     | 5.65 ms                                                      | 5.73 ms: 1.01x slower                                                    |
| bench_mp_pool            | 7.04 ms                                                      | 7.16 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl          | 2.17 sec                                                     | 2.22 sec: 1.02x slower                                                   |
| chaos                    | 66.5 ms                                                      | 67.9 ms: 1.02x slower                                                    |
| thrift                   | 946 us                                                       | 967 us: 1.02x slower                                                     |
| unpickle_list            | 6.31 us                                                      | 6.46 us: 1.02x slower                                                    |
| asyncio_tcp              | 545 ms                                                       | 568 ms: 1.04x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (61): sqlglot_optimize, xml_etree_process, logging_silent, regex_compile, deepcopy_memo, mypy2, create_gc_cycles, pylint, genshi_xml, async_tree_cpu_io_mixed, sqlglot_normalize, regex_v8, pickle, scimark_monte_carlo, pycparser, comprehensions, aiohttp, deltablue, genshi_text, json_dumps, pickle_pure_python, richards_super, pathlib, logging_simple, asyncio_websockets, sympy_sum, sqlite_synth, async_tree_memoization, fannkuch, pidigits, python_startup_no_site, regex_dna, float, pprint_pformat, dask, async_tree_memoization_tg, sympy_str, async_tree_cpu_io_mixed_tg, python_startup, async_tree_none_tg, async_generators, async_tree_none, scimark_sparse_mat_mult, raytrace, mdp, gunicorn, flaskblogging, regex_effbot, mako, tornado_http, docutils, pprint_safe_repr, meteor_contest, spectral_norm, async_tree_io_tg, generators, async_tree_io, logging_format, go, sqlglot_parse, html5lib

# HPT report

- Reliability score: 99.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x