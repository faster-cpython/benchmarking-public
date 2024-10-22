# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b4
- machine: linux-aarch64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.00x slower
- HPT reliability: 92.08%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| docutils       | 2.91 sec                                                 | 3.05 sec: 1.05x slower                                       |
| html5lib       | 64.3 ms                                                  | 66.6 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (3): 2to3, chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 619 ms: 1.05x faster                                         |
| asyncio_websockets         | 656 ms                                                   | 661 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                       |
| coroutines                 | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                        |
| asyncio_tcp                | 568 ms                                                   | 580 ms: 1.02x slower                                         |
| async_tree_none_tg         | 467 ms                                                   | 484 ms: 1.03x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 785 ms: 1.07x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 817 ms: 1.07x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.21 sec: 1.10x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.22 sec: 1.11x slower                                       |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                 |

Benchmark hidden because not significant (3): async_generators, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.03x faster                                         |
| float          | 94.4 ms                                                  | 91.6 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                        |
| regex_compile  | 128 ms                                                   | 127 ms: 1.01x faster                                         |
| regex_dna      | 246 ms                                                   | 253 ms: 1.03x slower                                         |
| Geometric mean | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| json_loads     | 31.4 us                                                  | 32.4 us: 1.03x slower                                        |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (8): pickle_pure_python, tomli_loads, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 60.2 ms                                                  | 59.5 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (3): django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                      | 1.18 sec                                                 | 766 ms: 1.54x faster                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 619 ms: 1.05x faster                                         |
| nbody                      | 114 ms                                                   | 110 ms: 1.03x faster                                         |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.03x faster                                       |
| float                      | 94.4 ms                                                  | 91.6 ms: 1.03x faster                                        |
| regex_v8                   | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                        |
| python_startup             | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                        |
| scimark_monte_carlo        | 83.8 ms                                                  | 81.8 ms: 1.02x faster                                        |
| bench_mp_pool              | 7.30 ms                                                  | 7.14 ms: 1.02x faster                                        |
| bpe_tokeniser              | 5.90 sec                                                 | 5.80 sec: 1.02x faster                                       |
| scimark_lu                 | 139 ms                                                   | 137 ms: 1.02x faster                                         |
| generators                 | 37.8 ms                                                  | 37.3 ms: 1.01x faster                                        |
| deepcopy_memo              | 51.0 us                                                  | 50.4 us: 1.01x faster                                        |
| genshi_xml                 | 60.2 ms                                                  | 59.5 ms: 1.01x faster                                        |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.52 ms: 1.01x faster                                        |
| regex_compile              | 128 ms                                                   | 127 ms: 1.01x faster                                         |
| sqlglot_optimize           | 62.4 ms                                                  | 62.2 ms: 1.00x faster                                        |
| pyflate                    | 556 ms                                                   | 560 ms: 1.01x slower                                         |
| fannkuch                   | 452 ms                                                   | 455 ms: 1.01x slower                                         |
| asyncio_websockets         | 656 ms                                                   | 661 ms: 1.01x slower                                         |
| thrift                     | 946 us                                                   | 956 us: 1.01x slower                                         |
| pprint_pformat             | 1.90 sec                                                 | 1.92 sec: 1.01x slower                                       |
| sympy_expand               | 455 ms                                                   | 460 ms: 1.01x slower                                         |
| sympy_str                  | 264 ms                                                   | 267 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                       |
| logging_simple             | 7.04 us                                                  | 7.13 us: 1.01x slower                                        |
| coverage                   | 98.5 ms                                                  | 99.9 ms: 1.01x slower                                        |
| json                       | 5.61 ms                                                  | 5.70 ms: 1.01x slower                                        |
| pprint_safe_repr           | 926 ms                                                   | 941 ms: 1.02x slower                                         |
| coroutines                 | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                        |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.02x slower                                        |
| pathlib                    | 22.4 ms                                                  | 22.8 ms: 1.02x slower                                        |
| asyncio_tcp                | 568 ms                                                   | 580 ms: 1.02x slower                                         |
| regex_dna                  | 246 ms                                                   | 253 ms: 1.03x slower                                         |
| json_loads                 | 31.4 us                                                  | 32.4 us: 1.03x slower                                        |
| html5lib                   | 64.3 ms                                                  | 66.6 ms: 1.03x slower                                        |
| async_tree_none_tg         | 467 ms                                                   | 484 ms: 1.03x slower                                         |
| docutils                   | 2.91 sec                                                 | 3.05 sec: 1.05x slower                                       |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 785 ms: 1.07x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 817 ms: 1.07x slower                                         |
| dask                       | 350 ms                                                   | 376 ms: 1.07x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.21 sec: 1.10x slower                                       |
| create_gc_cycles           | 2.12 ms                                                  | 2.33 ms: 1.10x slower                                        |
| gc_traversal               | 4.53 ms                                                  | 4.98 ms: 1.10x slower                                        |
| async_tree_io_tg           | 1.09 sec                                                 | 1.22 sec: 1.11x slower                                       |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                 |

Benchmark hidden because not significant (47): tornado_http, async_generators, sympy_sum, chameleon, telco, sqlglot_transpile, go, pylint, richards, hexiom, richards_super, logging_silent, scimark_fft, mdp, sqlglot_normalize, pickle_pure_python, python_startup_no_site, spectral_norm, crypto_pyaes, logging_format, django_template, tomli_loads, deepcopy, chaos, pidigits, sympy_integrate, deltablue, genshi_text, scimark_sor, unpickle_pure_python, raytrace, mako, xml_etree_generate, regex_effbot, 2to3, xml_etree_iterparse, deepcopy_reduce, xml_etree_parse, sqlglot_parse, typing_runtime_protocols, nqueens, json_dumps, meteor_contest, async_tree_none, bench_thread_pool, async_tree_memoization, xml_etree_process
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b.json: dulwich_log

# HPT report

- Reliability score: 92.08% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x