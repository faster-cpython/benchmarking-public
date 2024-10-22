# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: linux-aarch64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.00x slower
- HPT reliability: 81.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| chameleon      | 9.02 ms                                                  | 9.16 ms: 1.02x slower                                          |
| docutils       | 2.91 sec                                                 | 3.10 sec: 1.07x slower                                         |
| html5lib       | 64.3 ms                                                  | 66.1 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                    | 1.01x slower                                                   |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 599 ms: 1.08x faster                                           |
| asyncio_tcp                | 568 ms                                                   | 582 ms: 1.03x slower                                           |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                         |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 784 ms: 1.03x slower                                           |
| coroutines                 | 28.2 ms                                                  | 29.1 ms: 1.03x slower                                          |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 761 ms: 1.03x slower                                           |
| async_tree_memoization     | 626 ms                                                   | 649 ms: 1.04x slower                                           |
| async_tree_io              | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                         |
| async_tree_io_tg           | 1.09 sec                                                 | 1.28 sec: 1.17x slower                                         |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                   |

Benchmark hidden because not significant (4): async_generators, async_tree_none, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 91.2 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.98 ms: 1.02x slower                                          |
| regex_dna      | 246 ms                                                   | 253 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                    | 1.01x slower                                                   |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_iterparse | 147 ms                                                   | 148 ms: 1.01x slower                                           |
| xml_etree_parse     | 188 ms                                                   | 198 ms: 1.06x slower                                           |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                   |

Benchmark hidden because not significant (7): pickle_pure_python, unpickle_pure_python, json_loads, tomli_loads, xml_etree_generate, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 28.4 ms: 1.02x slower                                          |
| genshi_xml     | 60.2 ms                                                  | 62.0 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                    | 1.02x slower                                                   |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| mypy2                      | 1.18 sec                                                 | 765 ms: 1.55x faster                                           |
| async_tree_memoization_tg  | 649 ms                                                   | 599 ms: 1.08x faster                                           |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.04x faster                                         |
| float                      | 94.4 ms                                                  | 91.2 ms: 1.03x faster                                          |
| json                       | 5.61 ms                                                  | 5.47 ms: 1.03x faster                                          |
| bench_mp_pool              | 7.30 ms                                                  | 7.12 ms: 1.03x faster                                          |
| telco                      | 9.73 ms                                                  | 9.54 ms: 1.02x faster                                          |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                          |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.5 ms: 1.02x faster                                          |
| bpe_tokeniser              | 5.90 sec                                                 | 5.81 sec: 1.02x faster                                         |
| deepcopy_reduce            | 4.07 us                                                  | 4.01 us: 1.01x faster                                          |
| go                         | 163 ms                                                   | 161 ms: 1.01x faster                                           |
| deepcopy_memo              | 51.0 us                                                  | 50.5 us: 1.01x faster                                          |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.51 ms: 1.01x faster                                          |
| richards                   | 53.5 ms                                                  | 53.0 ms: 1.01x faster                                          |
| scimark_fft                | 447 ms                                                   | 444 ms: 1.01x faster                                           |
| deepcopy                   | 451 us                                                   | 450 us: 1.00x faster                                           |
| logging_simple             | 7.04 us                                                  | 7.06 us: 1.00x slower                                          |
| thrift                     | 946 us                                                   | 949 us: 1.00x slower                                           |
| xml_etree_iterparse        | 147 ms                                                   | 148 ms: 1.01x slower                                           |
| sympy_str                  | 264 ms                                                   | 267 ms: 1.01x slower                                           |
| sympy_expand               | 455 ms                                                   | 460 ms: 1.01x slower                                           |
| pprint_pformat             | 1.90 sec                                                 | 1.93 sec: 1.02x slower                                         |
| chameleon                  | 9.02 ms                                                  | 9.16 ms: 1.02x slower                                          |
| sympy_integrate            | 21.0 ms                                                  | 21.4 ms: 1.02x slower                                          |
| regex_effbot               | 4.87 ms                                                  | 4.98 ms: 1.02x slower                                          |
| genshi_text                | 27.7 ms                                                  | 28.4 ms: 1.02x slower                                          |
| pprint_safe_repr           | 926 ms                                                   | 948 ms: 1.02x slower                                           |
| asyncio_tcp                | 568 ms                                                   | 582 ms: 1.03x slower                                           |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                         |
| regex_dna                  | 246 ms                                                   | 253 ms: 1.03x slower                                           |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 784 ms: 1.03x slower                                           |
| html5lib                   | 64.3 ms                                                  | 66.1 ms: 1.03x slower                                          |
| coroutines                 | 28.2 ms                                                  | 29.1 ms: 1.03x slower                                          |
| genshi_xml                 | 60.2 ms                                                  | 62.0 ms: 1.03x slower                                          |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 761 ms: 1.03x slower                                           |
| async_tree_memoization     | 626 ms                                                   | 649 ms: 1.04x slower                                           |
| xml_etree_parse            | 188 ms                                                   | 198 ms: 1.06x slower                                           |
| dask                       | 350 ms                                                   | 374 ms: 1.07x slower                                           |
| docutils                   | 2.91 sec                                                 | 3.10 sec: 1.07x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                         |
| create_gc_cycles           | 2.12 ms                                                  | 2.34 ms: 1.10x slower                                          |
| gc_traversal               | 4.53 ms                                                  | 5.07 ms: 1.12x slower                                          |
| async_tree_io_tg           | 1.09 sec                                                 | 1.28 sec: 1.17x slower                                         |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                   |

Benchmark hidden because not significant (48): tornado_http, sqlglot_transpile, pickle_pure_python, crypto_pyaes, async_generators, regex_v8, richards_super, 2to3, coverage, unpickle_pure_python, chaos, sqlglot_normalize, logging_silent, scimark_lu, generators, hexiom, regex_compile, raytrace, json_loads, spectral_norm, nqueens, tomli_loads, mdp, python_startup_no_site, xml_etree_generate, scimark_sor, django_template, logging_format, async_tree_none, xml_etree_process, pidigits, fannkuch, nbody, meteor_contest, comprehensions, bench_thread_pool, pyflate, sqlglot_parse, sqlglot_optimize, asyncio_websockets, pathlib, deltablue, sympy_sum, typing_runtime_protocols, json_dumps, async_tree_none_tg, mako, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 81.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x