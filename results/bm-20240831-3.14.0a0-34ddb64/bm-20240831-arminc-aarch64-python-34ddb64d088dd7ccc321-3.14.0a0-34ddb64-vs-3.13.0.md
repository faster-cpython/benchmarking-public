# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.02x faster
- HPT reliability: 99.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 294 ms: 1.04x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.04 sec: 1.05x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                                    |
| async_tree_none            | 493 ms                                                   | 422 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 559 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 726 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 474 ms: 1.05x faster                                                    |
| asyncio_tcp                | 568 ms                                                   | 551 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 722 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.16 sec: 1.01x faster                                                  |
| coroutines                 | 28.2 ms                                                  | 28.3 ms: 1.00x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.12 sec: 1.01x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.16 sec: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| float          | 94.4 ms                                                  | 92.7 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.2 ms: 1.04x faster                                                   |
| regex_compile  | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| json_loads      | 31.4 us                                                  | 32.5 us: 1.03x slower                                                   |
| tomli_loads     | 2.53 sec                                                 | 2.62 sec: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_process, pickle_pure_python, unpickle_pure_python, xml_etree_generate, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                  | 41.4 ms: 1.02x faster                                                   |
| mako            | 13.3 ms                                                  | 13.3 ms: 1.00x faster                                                   |
| genshi_xml      | 60.2 ms                                                  | 60.0 ms: 1.00x faster                                                   |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 337 us: 1.34x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 38.2 us: 1.33x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                                    |
| go                         | 163 ms                                                   | 138 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 422 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.51 us: 1.16x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 416 ms: 1.12x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 559 ms: 1.12x faster                                                    |
| generators                 | 37.8 ms                                                  | 35.0 ms: 1.08x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.0 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 726 ms: 1.05x faster                                                    |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 474 ms: 1.05x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.2 ms: 1.04x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.00 ms: 1.04x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.21 sec: 1.04x faster                                                  |
| 2to3                       | 306 ms                                                   | 294 ms: 1.04x faster                                                    |
| logging_silent             | 135 ns                                                   | 131 ns: 1.03x faster                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| asyncio_tcp                | 568 ms                                                   | 551 ms: 1.03x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.40 ms: 1.03x faster                                                   |
| logging_format             | 7.83 us                                                  | 7.64 us: 1.02x faster                                                   |
| regex_compile              | 128 ms                                                   | 126 ms: 1.02x faster                                                    |
| django_template            | 42.3 ms                                                  | 41.4 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 722 ms: 1.02x faster                                                    |
| sympy_sum                  | 143 ms                                                   | 141 ms: 1.02x faster                                                    |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| sympy_integrate            | 21.0 ms                                                  | 20.6 ms: 1.02x faster                                                   |
| scimark_fft                | 447 ms                                                   | 439 ms: 1.02x faster                                                    |
| logging_simple             | 7.04 us                                                  | 6.91 us: 1.02x faster                                                   |
| float                      | 94.4 ms                                                  | 92.7 ms: 1.02x faster                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.5 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                   | 112 ms: 1.02x faster                                                    |
| thrift                     | 946 us                                                   | 931 us: 1.02x faster                                                    |
| scimark_sor                | 159 ms                                                   | 157 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 915 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.16 sec: 1.01x faster                                                  |
| xml_etree_parse            | 188 ms                                                   | 186 ms: 1.01x faster                                                    |
| mako                       | 13.3 ms                                                  | 13.3 ms: 1.00x faster                                                   |
| genshi_xml                 | 60.2 ms                                                  | 60.0 ms: 1.00x faster                                                   |
| coroutines                 | 28.2 ms                                                  | 28.3 ms: 1.00x slower                                                   |
| raytrace                   | 298 ms                                                   | 301 ms: 1.01x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 99.9 ms: 1.01x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.12 sec: 1.01x slower                                                  |
| sqlglot_parse              | 1.38 ms                                                  | 1.40 ms: 1.01x slower                                                   |
| richards                   | 53.5 ms                                                  | 54.3 ms: 1.02x slower                                                   |
| sympy_expand               | 455 ms                                                   | 462 ms: 1.02x slower                                                    |
| comprehensions             | 20.4 us                                                  | 20.8 us: 1.02x slower                                                   |
| pyflate                    | 556 ms                                                   | 567 ms: 1.02x slower                                                    |
| fannkuch                   | 452 ms                                                   | 465 ms: 1.03x slower                                                    |
| regex_dna                  | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| json_loads                 | 31.4 us                                                  | 32.5 us: 1.03x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 2.62 sec: 1.04x slower                                                  |
| docutils                   | 2.91 sec                                                 | 3.04 sec: 1.05x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.16 sec: 1.07x slower                                                  |
| create_gc_cycles           | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 4.99 ms: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (31): tornado_http, sqlglot_normalize, xml_etree_process, html5lib, pickle_pure_python, genshi_text, chaos, bpe_tokeniser, mdp, unpickle_pure_python, hexiom, xml_etree_generate, sqlglot_transpile, pprint_pformat, sympy_str, python_startup_no_site, json_dumps, spectral_norm, pidigits, telco, sqlglot_optimize, asyncio_websockets, regex_effbot, typing_runtime_protocols, coverage, richards_super, crypto_pyaes, json, deltablue, xml_etree_iterparse, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: dulwich_log

# HPT report

- Reliability score: 99.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x