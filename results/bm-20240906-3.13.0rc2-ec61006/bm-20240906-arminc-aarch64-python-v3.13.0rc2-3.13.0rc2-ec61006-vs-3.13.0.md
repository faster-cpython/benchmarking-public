# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: linux-aarch64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.00x slower
- HPT reliability: 97.51%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.91 sec                                                 | 3.10 sec: 1.07x slower                                         |
| html5lib       | 64.3 ms                                                  | 67.6 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                    | 1.02x slower                                                   |

Benchmark hidden because not significant (3): 2to3, chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 603 ms: 1.08x faster                                           |
| async_generators           | 496 ms                                                   | 483 ms: 1.03x faster                                           |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 644 ms: 1.03x slower                                           |
| coroutines                 | 28.2 ms                                                  | 29.2 ms: 1.03x slower                                          |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 761 ms: 1.03x slower                                           |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 790 ms: 1.03x slower                                           |
| asyncio_tcp                | 568 ms                                                   | 592 ms: 1.04x slower                                           |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.09x slower                                         |
| async_tree_io_tg           | 1.09 sec                                                 | 1.28 sec: 1.17x slower                                         |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                   |

Benchmark hidden because not significant (3): async_tree_none, async_tree_none_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 91.5 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                          |
| regex_dna      | 246 ms                                                   | 252 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                    | 1.00x slower                                                   |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 359 us                                                   | 354 us: 1.01x faster                                           |
| unpickle_pure_python | 254 us                                                   | 251 us: 1.01x faster                                           |
| tomli_loads          | 2.53 sec                                                 | 2.55 sec: 1.01x slower                                         |
| xml_etree_iterparse  | 147 ms                                                   | 148 ms: 1.01x slower                                           |
| pickle               | 13.5 us                                                  | 13.6 us: 1.01x slower                                          |
| xml_etree_parse      | 188 ms                                                   | 195 ms: 1.04x slower                                           |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                   |

Benchmark hidden because not significant (8): unpickle_list, pickle_dict, xml_etree_process, xml_etree_generate, json_dumps, pickle_list, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                          |
| python_startup_no_site | 8.75 ms                                                  | 8.63 ms: 1.01x faster                                          |
| Geometric mean         | (ref)                                                    | 1.01x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml     | 60.2 ms                                                  | 61.1 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                    | 1.01x slower                                                   |

Benchmark hidden because not significant (3): mako, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| mypy2                      | 1.18 sec                                                 | 761 ms: 1.56x faster                                           |
| async_tree_memoization_tg  | 649 ms                                                   | 603 ms: 1.08x faster                                           |
| pycparser                  | 1.26 sec                                                 | 1.21 sec: 1.04x faster                                         |
| float                      | 94.4 ms                                                  | 91.5 ms: 1.03x faster                                          |
| async_generators           | 496 ms                                                   | 483 ms: 1.03x faster                                           |
| hexiom                     | 7.13 ms                                                  | 7.00 ms: 1.02x faster                                          |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.3 ms: 1.02x faster                                          |
| bpe_tokeniser              | 5.90 sec                                                 | 5.80 sec: 1.02x faster                                         |
| python_startup             | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                          |
| pickle_pure_python         | 359 us                                                   | 354 us: 1.01x faster                                           |
| python_startup_no_site     | 8.75 ms                                                  | 8.63 ms: 1.01x faster                                          |
| richards_super             | 60.3 ms                                                  | 59.5 ms: 1.01x faster                                          |
| go                         | 163 ms                                                   | 161 ms: 1.01x faster                                           |
| unpickle_pure_python       | 254 us                                                   | 251 us: 1.01x faster                                           |
| regex_v8                   | 31.5 ms                                                  | 31.1 ms: 1.01x faster                                          |
| richards                   | 53.5 ms                                                  | 52.9 ms: 1.01x faster                                          |
| logging_simple             | 7.04 us                                                  | 6.96 us: 1.01x faster                                          |
| pyflate                    | 556 ms                                                   | 550 ms: 1.01x faster                                           |
| deepcopy                   | 451 us                                                   | 453 us: 1.00x slower                                           |
| sympy_str                  | 264 ms                                                   | 266 ms: 1.01x slower                                           |
| tomli_loads                | 2.53 sec                                                 | 2.55 sec: 1.01x slower                                         |
| sqlite_synth               | 3.84 us                                                  | 3.88 us: 1.01x slower                                          |
| xml_etree_iterparse        | 147 ms                                                   | 148 ms: 1.01x slower                                           |
| thrift                     | 946 us                                                   | 956 us: 1.01x slower                                           |
| deepcopy_reduce            | 4.07 us                                                  | 4.12 us: 1.01x slower                                          |
| pickle                     | 13.5 us                                                  | 13.6 us: 1.01x slower                                          |
| pprint_pformat             | 1.90 sec                                                 | 1.92 sec: 1.01x slower                                         |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.67 ms: 1.01x slower                                          |
| fannkuch                   | 452 ms                                                   | 458 ms: 1.01x slower                                           |
| unpack_sequence            | 57.2 ns                                                  | 58.0 ns: 1.01x slower                                          |
| pathlib                    | 22.4 ms                                                  | 22.7 ms: 1.01x slower                                          |
| logging_silent             | 135 ns                                                   | 137 ns: 1.02x slower                                           |
| genshi_xml                 | 60.2 ms                                                  | 61.1 ms: 1.02x slower                                          |
| pprint_safe_repr           | 926 ms                                                   | 942 ms: 1.02x slower                                           |
| regex_dna                  | 246 ms                                                   | 252 ms: 1.02x slower                                           |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                         |
| spectral_norm              | 141 ms                                                   | 145 ms: 1.03x slower                                           |
| async_tree_memoization     | 626 ms                                                   | 644 ms: 1.03x slower                                           |
| coroutines                 | 28.2 ms                                                  | 29.2 ms: 1.03x slower                                          |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 761 ms: 1.03x slower                                           |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 790 ms: 1.03x slower                                           |
| flaskblogging              | 4.60 ms                                                  | 4.78 ms: 1.04x slower                                          |
| telco                      | 9.73 ms                                                  | 10.1 ms: 1.04x slower                                          |
| xml_etree_parse            | 188 ms                                                   | 195 ms: 1.04x slower                                           |
| asyncio_tcp                | 568 ms                                                   | 592 ms: 1.04x slower                                           |
| html5lib                   | 64.3 ms                                                  | 67.6 ms: 1.05x slower                                          |
| bench_mp_pool              | 7.30 ms                                                  | 7.75 ms: 1.06x slower                                          |
| docutils                   | 2.91 sec                                                 | 3.10 sec: 1.07x slower                                         |
| dask                       | 350 ms                                                   | 373 ms: 1.07x slower                                           |
| gc_traversal               | 4.53 ms                                                  | 4.92 ms: 1.09x slower                                          |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.09x slower                                         |
| create_gc_cycles           | 2.12 ms                                                  | 2.33 ms: 1.10x slower                                          |
| async_tree_io_tg           | 1.09 sec                                                 | 1.28 sec: 1.17x slower                                         |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                   |

Benchmark hidden because not significant (49): async_tree_none, unpickle_list, logging_format, chameleon, tornado_http, 2to3, chaos, pickle_dict, nbody, crypto_pyaes, sympy_sum, xml_etree_process, sqlglot_transpile, xml_etree_generate, json_dumps, scimark_fft, bench_thread_pool, json, pickle_list, sympy_integrate, pidigits, regex_compile, json_loads, comprehensions, mako, deltablue, genshi_text, coverage, regex_effbot, sqlglot_normalize, nqueens, meteor_contest, scimark_sor, mdp, generators, sympy_expand, sqlglot_optimize, typing_runtime_protocols, scimark_lu, async_tree_none_tg, aiohttp, asyncio_websockets, deepcopy_memo, raytrace, unpickle, django_template, gunicorn, sqlglot_parse, pylint

# HPT report

- Reliability score: 97.51% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x