# Results vs. 3.13.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: linux-aarch64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.013x faster
- HPT reliability: 95.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (5): 2to3, chameleon, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 651 ms                                                   | 617 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 730 ms: 1.05x faster                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.08 sec: 1.04x faster                                                   |
| async_tree_none            | 497 ms                                                   | 486 ms: 1.02x faster                                                     |
| async_tree_none_tg         | 470 ms                                                   | 460 ms: 1.02x faster                                                     |
| async_tree_memoization_tg  | 649 ms                                                   | 645 ms: 1.01x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (5): async_tree_io, async_tree_cpu_io_mixed, async_generators, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.1 ms: 1.06x faster                                                    |
| regex_dna      | 253 ms                                                   | 252 ms: 1.01x faster                                                     |
| regex_compile  | 127 ms                                                   | 130 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|--------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads        | 2.54 sec                                                 | 2.56 sec: 1.01x slower                                                   |
| pickle_pure_python | 357 us                                                   | 363 us: 1.02x slower                                                     |
| Geometric mean     | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (7): json_dumps, xml_etree_process, xml_etree_generate, json_loads, xml_etree_iterparse, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.4 ms: 1.15x faster                                                    |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 13.4 ms                                                  | 13.3 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.13 ms: 1.57x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 4.52 ms: 1.28x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.4 ms: 1.15x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.1 ms: 1.06x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 617 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 730 ms: 1.05x faster                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.08 sec: 1.04x faster                                                   |
| async_tree_none            | 497 ms                                                   | 486 ms: 1.02x faster                                                     |
| nqueens                    | 100 ms                                                   | 97.8 ms: 1.02x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 460 ms: 1.02x faster                                                     |
| fannkuch                   | 461 ms                                                   | 451 ms: 1.02x faster                                                     |
| crypto_pyaes               | 83.7 ms                                                  | 82.1 ms: 1.02x faster                                                    |
| thrift                     | 968 us                                                   | 960 us: 1.01x faster                                                     |
| mako                       | 13.4 ms                                                  | 13.3 ms: 1.01x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 645 ms: 1.01x faster                                                     |
| scimark_fft                | 447 ms                                                   | 444 ms: 1.01x faster                                                     |
| regex_dna                  | 253 ms                                                   | 252 ms: 1.01x faster                                                     |
| bpe_tokeniser              | 5.87 sec                                                 | 5.92 sec: 1.01x slower                                                   |
| pyflate                    | 556 ms                                                   | 561 ms: 1.01x slower                                                     |
| tomli_loads                | 2.54 sec                                                 | 2.56 sec: 1.01x slower                                                   |
| go                         | 160 ms                                                   | 162 ms: 1.02x slower                                                     |
| pickle_pure_python         | 357 us                                                   | 363 us: 1.02x slower                                                     |
| regex_compile              | 127 ms                                                   | 130 ms: 1.02x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (66): json_dumps, tornado_http, xml_etree_process, async_tree_io, nbody, hexiom, spectral_norm, sympy_sum, logging_simple, sqlglot_transpile, deepcopy_memo, pycparser, raytrace, json, async_tree_cpu_io_mixed, coverage, bench_mp_pool, logging_format, sympy_integrate, sqlglot_parse, scimark_sor, comprehensions, django_template, xml_etree_generate, async_generators, meteor_contest, scimark_monte_carlo, docutils, html5lib, genshi_text, sympy_expand, bench_thread_pool, scimark_sparse_mat_mult, json_loads, pathlib, typing_runtime_protocols, xml_etree_iterparse, pidigits, coroutines, sqlglot_normalize, float, richards_super, mdp, richards, pprint_pformat, scimark_lu, telco, sympy_str, pprint_safe_repr, asyncio_websockets, 2to3, chameleon, genshi_xml, regex_effbot, chaos, generators, python_startup_no_site, deepcopy, unpickle_pure_python, deltablue, sqlglot_optimize, logging_silent, pylint, deepcopy_reduce, xml_etree_parse, mypy2
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240930-3.13.0rc2+-1ba3555/bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x faster
# HPT report

- Reliability score: 95.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x