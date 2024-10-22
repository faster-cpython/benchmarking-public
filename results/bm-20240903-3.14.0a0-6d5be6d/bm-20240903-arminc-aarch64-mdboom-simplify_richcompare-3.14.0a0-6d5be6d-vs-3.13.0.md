# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.02x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 296 ms: 1.03x faster                                                    |
| docutils       | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| html5lib       | 64.3 ms                                                  | 63.2 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 551 ms: 1.18x faster                                                    |
| async_tree_none            | 493 ms                                                   | 423 ms: 1.17x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 558 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 418 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 727 ms: 1.05x faster                                                    |
| async_generators           | 496 ms                                                   | 479 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 724 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (3): asyncio_tcp, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 108 ms: 1.06x faster                                                    |
| float          | 94.4 ms                                                  | 92.4 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| regex_compile  | 128 ms                                                   | 125 ms: 1.03x faster                                                    |
| regex_dna      | 246 ms                                                   | 253 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 254 us                                                   | 252 us: 1.01x faster                                                    |
| tomli_loads          | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| json_loads           | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, pickle_pure_python, xml_etree_iterparse, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, genshi_text, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 333 us: 1.36x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 37.9 us: 1.35x faster                                                   |
| go                         | 163 ms                                                   | 136 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 551 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.47 us: 1.17x faster                                                   |
| async_tree_none            | 493 ms                                                   | 423 ms: 1.17x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 558 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 418 ms: 1.12x faster                                                    |
| generators                 | 37.8 ms                                                  | 34.7 ms: 1.09x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.2 ms: 1.06x faster                                                   |
| nbody                      | 114 ms                                                   | 108 ms: 1.06x faster                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 6.94 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 727 ms: 1.05x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 133 ms: 1.05x faster                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 80.4 ms: 1.04x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| async_generators           | 496 ms                                                   | 479 ms: 1.04x faster                                                    |
| 2to3                       | 306 ms                                                   | 296 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                 | 1.22 sec: 1.03x faster                                                  |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.39 ms: 1.03x faster                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| logging_silent             | 135 ns                                                   | 131 ns: 1.03x faster                                                    |
| regex_compile              | 128 ms                                                   | 125 ms: 1.03x faster                                                    |
| meteor_contest             | 113 ms                                                   | 110 ms: 1.03x faster                                                    |
| logging_format             | 7.83 us                                                  | 7.64 us: 1.02x faster                                                   |
| sympy_sum                  | 143 ms                                                   | 140 ms: 1.02x faster                                                    |
| float                      | 94.4 ms                                                  | 92.4 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 926 ms                                                   | 907 ms: 1.02x faster                                                    |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| scimark_sor                | 159 ms                                                   | 156 ms: 1.02x faster                                                    |
| html5lib                   | 64.3 ms                                                  | 63.2 ms: 1.02x faster                                                   |
| hexiom                     | 7.13 ms                                                  | 7.02 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 724 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.87 sec: 1.01x faster                                                  |
| mdp                        | 3.36 sec                                                 | 3.32 sec: 1.01x faster                                                  |
| nqueens                    | 98.7 ms                                                  | 97.4 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 254 us                                                   | 252 us: 1.01x faster                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 5.85 sec: 1.01x faster                                                  |
| sympy_expand               | 455 ms                                                   | 458 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.20 sec: 1.01x slower                                                  |
| fannkuch                   | 452 ms                                                   | 460 ms: 1.02x slower                                                    |
| json                       | 5.61 ms                                                  | 5.73 ms: 1.02x slower                                                   |
| regex_dna                  | 246 ms                                                   | 253 ms: 1.03x slower                                                    |
| pyflate                    | 556 ms                                                   | 575 ms: 1.03x slower                                                    |
| docutils                   | 2.91 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| tomli_loads                | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| json_loads                 | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| gc_traversal               | 4.53 ms                                                  | 4.99 ms: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (38): tornado_http, xml_etree_generate, sympy_integrate, sqlglot_normalize, richards_super, genshi_xml, sqlglot_optimize, genshi_text, coverage, chaos, comprehensions, crypto_pyaes, xml_etree_process, richards, pickle_pure_python, scimark_fft, deltablue, logging_simple, sqlglot_transpile, typing_runtime_protocols, asyncio_tcp, thrift, spectral_norm, mako, xml_etree_iterparse, python_startup_no_site, pidigits, django_template, sympy_str, regex_effbot, raytrace, telco, json_dumps, asyncio_websockets, coroutines, sqlglot_parse, xml_etree_parse, pylint
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x