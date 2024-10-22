# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 56.55%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.91 sec                                                 | 3.12 sec: 1.08x slower                                                  |
| html5lib       | 64.3 ms                                                  | 68.2 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                    | 1.04x slower                                                            |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 536 ms: 1.21x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 407 ms: 1.15x faster                                                    |
| async_tree_none            | 493 ms                                                   | 437 ms: 1.13x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 562 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 725 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 707 ms: 1.04x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.03x faster                                                  |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 592 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 93.0 ms: 1.02x faster                                                   |
| nbody          | 114 ms                                                   | 116 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                   | 128 ms: 1.01x faster                                                    |
| regex_dna      | 246 ms                                                   | 251 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads     | 31.4 us                                                  | 33.3 us: 1.06x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (8): xml_etree_process, unpickle_pure_python, tomli_loads, pickle_pure_python, json_dumps, xml_etree_generate, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.75 ms                                                  | 9.03 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 28.0 ms: 1.01x slower                                                   |
| mako           | 13.3 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 451 us                                                   | 333 us: 1.35x faster                                                    |
| deepcopy_memo              | 51.0 us                                                  | 39.3 us: 1.30x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 536 ms: 1.21x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.39 us: 1.20x faster                                                   |
| async_tree_none_tg         | 467 ms                                                   | 407 ms: 1.15x faster                                                    |
| async_tree_none            | 493 ms                                                   | 437 ms: 1.13x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 562 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 725 ms: 1.05x faster                                                    |
| pathlib                    | 22.4 ms                                                  | 21.5 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 707 ms: 1.04x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.03x faster                                                  |
| bench_mp_pool              | 7.30 ms                                                  | 7.08 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                 | 1.23 sec: 1.03x faster                                                  |
| logging_format             | 7.83 us                                                  | 7.64 us: 1.03x faster                                                   |
| logging_silent             | 135 ns                                                   | 132 ns: 1.02x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.79 sec: 1.02x faster                                                  |
| logging_simple             | 7.04 us                                                  | 6.92 us: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                   | 112 ms: 1.02x faster                                                    |
| float                      | 94.4 ms                                                  | 93.0 ms: 1.02x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 138 ms: 1.01x faster                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 82.8 ms: 1.01x faster                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.53 ms: 1.01x faster                                                   |
| regex_compile              | 128 ms                                                   | 128 ms: 1.01x faster                                                    |
| genshi_text                | 27.7 ms                                                  | 28.0 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 194 us: 1.01x slower                                                    |
| nbody                      | 114 ms                                                   | 116 ms: 1.02x slower                                                    |
| coverage                   | 98.5 ms                                                  | 100 ms: 1.02x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 100 ms: 1.02x slower                                                    |
| json                       | 5.61 ms                                                  | 5.71 ms: 1.02x slower                                                   |
| regex_dna                  | 246 ms                                                   | 251 ms: 1.02x slower                                                    |
| fannkuch                   | 452 ms                                                   | 460 ms: 1.02x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                   |
| mako                       | 13.3 ms                                                  | 13.6 ms: 1.02x slower                                                   |
| sympy_expand               | 455 ms                                                   | 465 ms: 1.02x slower                                                    |
| thrift                     | 946 us                                                   | 969 us: 1.03x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.95 sec: 1.03x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 952 ms: 1.03x slower                                                    |
| sympy_str                  | 264 ms                                                   | 271 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| telco                      | 9.73 ms                                                  | 10.0 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 9.03 ms: 1.03x slower                                                   |
| sympy_integrate            | 21.0 ms                                                  | 21.7 ms: 1.03x slower                                                   |
| pyflate                    | 556 ms                                                   | 578 ms: 1.04x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 592 ms: 1.04x slower                                                    |
| sympy_sum                  | 143 ms                                                   | 150 ms: 1.05x slower                                                    |
| dask                       | 350 ms                                                   | 368 ms: 1.05x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 68.2 ms: 1.06x slower                                                   |
| json_loads                 | 31.4 us                                                  | 33.3 us: 1.06x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.28 ms: 1.07x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.12 sec: 1.08x slower                                                  |
| gc_traversal               | 4.53 ms                                                  | 4.98 ms: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (37): go, richards, crypto_pyaes, richards_super, scimark_sor, xml_etree_process, bench_thread_pool, async_generators, pylint, deltablue, scimark_fft, unpickle_pure_python, chaos, mdp, hexiom, 2to3, tomli_loads, sqlglot_transpile, django_template, pidigits, spectral_norm, pickle_pure_python, regex_effbot, raytrace, json_dumps, comprehensions, generators, xml_etree_generate, sqlglot_normalize, sqlglot_optimize, xml_etree_parse, asyncio_websockets, async_tree_io_tg, python_startup, xml_etree_iterparse, genshi_xml, tornado_http
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: dulwich_log

# HPT report

- Reliability score: 56.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x