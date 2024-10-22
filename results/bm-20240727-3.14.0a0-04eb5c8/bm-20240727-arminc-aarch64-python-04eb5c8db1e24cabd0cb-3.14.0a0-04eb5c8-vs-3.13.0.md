# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.01x faster
- HPT reliability: 91.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.91 sec                                                 | 3.11 sec: 1.07x slower                                                  |
| html5lib       | 64.3 ms                                                  | 66.4 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 543 ms: 1.20x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 563 ms: 1.11x faster                                                    |
| async_tree_none            | 493 ms                                                   | 444 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 730 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 712 ms: 1.03x faster                                                    |
| coroutines                 | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 580 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.13 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| float          | 94.4 ms                                                  | 92.0 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                                   |
| regex_dna      | 246 ms                                                   | 255 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 147 ms                                                   | 145 ms: 1.01x faster                                                    |
| unpickle_pure_python | 254 us                                                   | 251 us: 1.01x faster                                                    |
| tomli_loads          | 2.53 sec                                                 | 2.55 sec: 1.01x slower                                                  |
| json_loads           | 31.4 us                                                  | 32.8 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, pickle_pure_python, xml_etree_process, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                  | 41.6 ms: 1.02x faster                                                   |
| genshi_xml      | 60.2 ms                                                  | 61.2 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 335 us: 1.35x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 38.2 us: 1.34x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 543 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.43 us: 1.19x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 563 ms: 1.11x faster                                                    |
| async_tree_none            | 493 ms                                                   | 444 ms: 1.11x faster                                                    |
| generators                 | 37.8 ms                                                  | 35.3 ms: 1.07x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.3 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 730 ms: 1.05x faster                                                    |
| logging_silent             | 135 ns                                                   | 129 ns: 1.05x faster                                                    |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 30.4 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 712 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.37 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.03x faster                                                  |
| richards_super             | 60.3 ms                                                  | 58.7 ms: 1.03x faster                                                   |
| float                      | 94.4 ms                                                  | 92.0 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.03x faster                                                    |
| richards                   | 53.5 ms                                                  | 52.3 ms: 1.02x faster                                                   |
| scimark_fft                | 447 ms                                                   | 438 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.0 ms: 1.02x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.15 ms: 1.02x faster                                                   |
| chaos                      | 68.8 ms                                                  | 67.5 ms: 1.02x faster                                                   |
| django_template            | 42.3 ms                                                  | 41.6 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 147 ms                                                   | 145 ms: 1.01x faster                                                    |
| unpickle_pure_python       | 254 us                                                   | 251 us: 1.01x faster                                                    |
| coverage                   | 98.5 ms                                                  | 97.4 ms: 1.01x faster                                                   |
| logging_simple             | 7.04 us                                                  | 6.97 us: 1.01x faster                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.84 sec: 1.01x faster                                                  |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                                  |
| tomli_loads                | 2.53 sec                                                 | 2.55 sec: 1.01x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| genshi_xml                 | 60.2 ms                                                  | 61.2 ms: 1.02x slower                                                   |
| sympy_expand               | 455 ms                                                   | 463 ms: 1.02x slower                                                    |
| sympy_str                  | 264 ms                                                   | 268 ms: 1.02x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 580 ms: 1.02x slower                                                    |
| json                       | 5.61 ms                                                  | 5.74 ms: 1.02x slower                                                   |
| telco                      | 9.73 ms                                                  | 9.95 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 197 us: 1.02x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.95 sec: 1.03x slower                                                  |
| sympy_sum                  | 143 ms                                                   | 147 ms: 1.03x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 952 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.24 sec: 1.03x slower                                                  |
| html5lib                   | 64.3 ms                                                  | 66.4 ms: 1.03x slower                                                   |
| thrift                     | 946 us                                                   | 977 us: 1.03x slower                                                    |
| regex_dna                  | 246 ms                                                   | 255 ms: 1.04x slower                                                    |
| dask                       | 350 ms                                                   | 364 ms: 1.04x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.13 sec: 1.04x slower                                                  |
| json_loads                 | 31.4 us                                                  | 32.8 us: 1.04x slower                                                   |
| pyflate                    | 556 ms                                                   | 580 ms: 1.04x slower                                                    |
| fannkuch                   | 452 ms                                                   | 476 ms: 1.05x slower                                                    |
| gc_traversal               | 4.53 ms                                                  | 4.82 ms: 1.06x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.11 sec: 1.07x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.33 ms: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (33): logging_format, tornado_http, xml_etree_generate, scimark_sor, crypto_pyaes, sqlglot_normalize, spectral_norm, async_generators, 2to3, go, raytrace, python_startup, deltablue, sqlglot_optimize, regex_compile, pidigits, pickle_pure_python, mako, meteor_contest, hexiom, xml_etree_process, xml_etree_parse, json_dumps, asyncio_websockets, sympy_integrate, comprehensions, nqueens, genshi_text, regex_effbot, python_startup_no_site, async_tree_io, sqlglot_transpile, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 91.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x