# Results vs. 3.13.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: linux-aarch64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.012x slower
- HPT reliability: 96.39%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.89 sec                                                 | 3.12 sec: 1.08x slower                                                   |
| sphinx         | 1.17 sec                                                 | 1.22 sec: 1.04x slower                                                   |
| Geometric mean | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 550 ms: 1.18x faster                                                     |
| async_tree_none           | 497 ms                                                   | 457 ms: 1.09x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 611 ms: 1.07x faster                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                                   |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 120 ms: 1.05x slower                                                     |
| float          | 93.3 ms                                                  | 99.9 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 33.3 ms: 1.05x slower                                                    |
| regex_effbot   | 4.89 ms                                                  | 5.11 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 31.7 us                                                  | 32.7 us: 1.03x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 381 us: 1.07x slower                                                     |
| unpickle_pure_python | 251 us                                                   | 269 us: 1.07x slower                                                     |
| tomli_loads          | 2.54 sec                                                 | 2.74 sec: 1.08x slower                                                   |
| json_dumps           | 13.6 ms                                                  | 14.8 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_generate, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.73 ms                                                  | 8.95 ms: 1.03x slower                                                    |
| python_startup         | 15.4 ms                                                  | 16.2 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.04x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 43.6 ms: 1.05x slower                                                    |
| mako            | 13.4 ms                                                  | 14.0 ms: 1.05x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 29.4 ms: 1.06x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo             | 50.4 us                                                  | 39.6 us: 1.27x faster                                                    |
| deepcopy                  | 447 us                                                   | 355 us: 1.26x faster                                                     |
| async_tree_memoization_tg | 649 ms                                                   | 550 ms: 1.18x faster                                                     |
| go                        | 160 ms                                                   | 143 ms: 1.12x faster                                                     |
| deepcopy_reduce           | 4.07 us                                                  | 3.73 us: 1.09x faster                                                    |
| async_tree_none           | 497 ms                                                   | 457 ms: 1.09x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 611 ms: 1.07x faster                                                     |
| sqlalchemy_declarative    | 150 ms                                                   | 143 ms: 1.05x faster                                                     |
| generators                | 37.6 ms                                                  | 36.2 ms: 1.04x faster                                                    |
| logging_simple            | 7.07 us                                                  | 7.20 us: 1.02x slower                                                    |
| python_startup_no_site    | 8.73 ms                                                  | 8.95 ms: 1.03x slower                                                    |
| nqueens                   | 100 ms                                                   | 103 ms: 1.03x slower                                                     |
| logging_silent            | 133 ns                                                   | 137 ns: 1.03x slower                                                     |
| json_loads                | 31.7 us                                                  | 32.7 us: 1.03x slower                                                    |
| connected_components      | 533 ms                                                   | 551 ms: 1.03x slower                                                     |
| mdp                       | 3.34 sec                                                 | 3.46 sec: 1.04x slower                                                   |
| fannkuch                  | 461 ms                                                   | 478 ms: 1.04x slower                                                     |
| pprint_safe_repr          | 926 ms                                                   | 963 ms: 1.04x slower                                                     |
| scimark_sparse_mat_mult   | 6.51 ms                                                  | 6.77 ms: 1.04x slower                                                    |
| sympy_integrate           | 20.8 ms                                                  | 21.7 ms: 1.04x slower                                                    |
| scimark_sor               | 160 ms                                                   | 166 ms: 1.04x slower                                                     |
| sympy_expand              | 457 ms                                                   | 476 ms: 1.04x slower                                                     |
| sphinx                    | 1.17 sec                                                 | 1.22 sec: 1.04x slower                                                   |
| regex_v8                  | 31.8 ms                                                  | 33.3 ms: 1.05x slower                                                    |
| regex_effbot              | 4.89 ms                                                  | 5.11 ms: 1.05x slower                                                    |
| comprehensions            | 20.4 us                                                  | 21.3 us: 1.05x slower                                                    |
| django_template           | 41.6 ms                                                  | 43.6 ms: 1.05x slower                                                    |
| mako                      | 13.4 ms                                                  | 14.0 ms: 1.05x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 1.99 sec: 1.05x slower                                                   |
| nbody                     | 114 ms                                                   | 120 ms: 1.05x slower                                                     |
| python_startup            | 15.4 ms                                                  | 16.2 ms: 1.05x slower                                                    |
| chaos                     | 68.0 ms                                                  | 71.9 ms: 1.06x slower                                                    |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                                   |
| genshi_text               | 27.7 ms                                                  | 29.4 ms: 1.06x slower                                                    |
| richards_super            | 60.1 ms                                                  | 63.8 ms: 1.06x slower                                                    |
| sqlalchemy_imperative     | 15.1 ms                                                  | 16.1 ms: 1.06x slower                                                    |
| scimark_monte_carlo       | 83.6 ms                                                  | 88.8 ms: 1.06x slower                                                    |
| spectral_norm             | 143 ms                                                   | 152 ms: 1.07x slower                                                     |
| pickle_pure_python        | 357 us                                                   | 381 us: 1.07x slower                                                     |
| float                     | 93.3 ms                                                  | 99.9 ms: 1.07x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.48 ms: 1.07x slower                                                    |
| sympy_str                 | 264 ms                                                   | 283 ms: 1.07x slower                                                     |
| unpickle_pure_python      | 251 us                                                   | 269 us: 1.07x slower                                                     |
| typing_runtime_protocols  | 193 us                                                   | 208 us: 1.07x slower                                                     |
| deltablue                 | 3.82 ms                                                  | 4.11 ms: 1.08x slower                                                    |
| tomli_loads               | 2.54 sec                                                 | 2.74 sec: 1.08x slower                                                   |
| docutils                  | 2.89 sec                                                 | 3.12 sec: 1.08x slower                                                   |
| pyflate                   | 556 ms                                                   | 605 ms: 1.09x slower                                                     |
| raytrace                  | 300 ms                                                   | 327 ms: 1.09x slower                                                     |
| json_dumps                | 13.6 ms                                                  | 14.8 ms: 1.09x slower                                                    |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                                   |
| create_gc_cycles          | 3.35 ms                                                  | 3.89 ms: 1.16x slower                                                    |
| gc_traversal              | 5.77 ms                                                  | 6.88 ms: 1.19x slower                                                    |
| k_core                    | 2.96 sec                                                 | 4.56 sec: 1.54x slower                                                   |
| bench_mp_pool             | 7.68 ms                                                  | 5.50 sec: 715.33x slower                                                 |
| Geometric mean            | (ref)                                                    | 1.11x slower                                                             |

Benchmark hidden because not significant (38): pathlib, async_tree_none_tg, async_tree_cpu_io_mixed_tg, scimark_lu, xml_etree_parse, async_tree_cpu_io_mixed, meteor_contest, bpe_tokeniser, tornado_http, html5lib, bench_thread_pool, coverage, 2to3, telco, pycparser, shortest_path, thrift, xml_etree_generate, asyncio_websockets, async_generators, sympy_sum, scimark_fft, crypto_pyaes, regex_dna, json, hexiom, pidigits, regex_compile, logging_format, richards, coroutines, xml_etree_process, sqlglot_normalize, sqlglot_optimize, genshi_xml, pylint, xml_etree_iterparse, sqlglot_transpile
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2
Ignored benchmarks (2) of results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: dulwich_log, sqlite_synth

- Geometric mean (including insignificant results): 1.012x slower
# HPT report

- Reliability score: 96.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x