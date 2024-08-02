# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 84.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 3.12 sec: 1.01x slower                                                  |
| html5lib       | 66.1 ms                                                      | 68.2 ms: 1.03x slower                                                   |
| tornado_http   | 128 ms                                                       | 136 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 407 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.15x faster                                                  |
| async_tree_memoization     | 645 ms                                                       | 562 ms: 1.15x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 536 ms: 1.13x faster                                                    |
| async_tree_none            | 492 ms                                                       | 437 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 725 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 707 ms: 1.08x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 116 ms: 1.02x slower                                                    |
| float          | 91.4 ms                                                      | 93.0 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads       | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                                  |
| xml_etree_process | 80.8 ms                                                      | 79.6 ms: 1.02x faster                                                   |
| json_dumps        | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| json_loads        | 32.1 us                                                      | 33.3 us: 1.04x slower                                                   |
| Geometric mean    | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_generate, pickle_pure_python, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.5 ms: 1.04x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 9.03 ms: 1.05x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                   |
| mako           | 13.2 ms                                                      | 13.6 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 333 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 39.3 us: 1.29x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 3.39 us: 1.19x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 407 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.15x faster                                                  |
| async_tree_memoization     | 645 ms                                                       | 562 ms: 1.15x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 536 ms: 1.13x faster                                                    |
| async_tree_none            | 492 ms                                                       | 437 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 725 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 707 ms: 1.08x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.5 ms: 1.06x faster                                                   |
| richards                   | 55.9 ms                                                      | 53.0 ms: 1.05x faster                                                   |
| logging_simple             | 7.21 us                                                      | 6.92 us: 1.04x faster                                                   |
| richards_super             | 62.3 ms                                                      | 59.9 ms: 1.04x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 4.98 ms: 1.04x faster                                                   |
| regex_dna                  | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 138 ms: 1.03x faster                                                    |
| logging_format             | 7.82 us                                                      | 7.64 us: 1.02x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.02x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                                  |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.02x faster                                                    |
| xml_etree_process          | 80.8 ms                                                      | 79.6 ms: 1.02x faster                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.79 sec: 1.01x faster                                                  |
| docutils                   | 3.10 sec                                                     | 3.12 sec: 1.01x slower                                                  |
| mdp                        | 3.33 sec                                                     | 3.36 sec: 1.01x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 1.95 sec: 1.01x slower                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 100 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                  |
| nbody                      | 114 ms                                                       | 116 ms: 1.02x slower                                                    |
| float                      | 91.4 ms                                                      | 93.0 ms: 1.02x slower                                                   |
| sympy_expand               | 457 ms                                                       | 465 ms: 1.02x slower                                                    |
| coverage                   | 98.4 ms                                                      | 100 ms: 1.02x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 952 ms: 1.02x slower                                                    |
| fannkuch                   | 451 ms                                                       | 460 ms: 1.02x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                   |
| sympy_str                  | 265 ms                                                       | 271 ms: 1.02x slower                                                    |
| generators                 | 37.1 ms                                                      | 38.0 ms: 1.02x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 68.2 ms: 1.03x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.6 ms: 1.04x slower                                                   |
| python_startup             | 13.0 ms                                                      | 13.5 ms: 1.04x slower                                                   |
| json_loads                 | 32.1 us                                                      | 33.3 us: 1.04x slower                                                   |
| pyflate                    | 557 ms                                                       | 578 ms: 1.04x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 21.7 ms: 1.04x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 150 ms: 1.05x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 9.03 ms: 1.05x slower                                                   |
| tornado_http               | 128 ms                                                       | 136 ms: 1.06x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 64.6 ms: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (40): xml_etree_parse, deltablue, sqlglot_parse, logging_silent, regex_v8, scimark_sor, dask, scimark_sparse_mat_mult, regex_compile, comprehensions, sqlglot_normalize, django_template, go, crypto_pyaes, pidigits, coroutines, spectral_norm, telco, scimark_fft, xml_etree_generate, typing_runtime_protocols, 2to3, pickle_pure_python, pycparser, sqlglot_optimize, chaos, scimark_monte_carlo, bench_mp_pool, asyncio_websockets, hexiom, raytrace, thrift, unpickle_pure_python, bench_thread_pool, async_generators, json, pylint, asyncio_tcp, xml_etree_iterparse, genshi_xml
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 84.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x