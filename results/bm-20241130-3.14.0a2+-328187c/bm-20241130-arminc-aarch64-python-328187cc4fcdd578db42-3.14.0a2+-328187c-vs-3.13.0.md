# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-aarch64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.000x slower
- HPT reliability: 81.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.89 sec                                                 | 3.12 sec: 1.08x slower                                                   |
| sphinx         | 1.17 sec                                                 | 1.23 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 564 ms: 1.15x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 573 ms: 1.14x faster                                                     |
| async_tree_none           | 497 ms                                                   | 445 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 751 ms: 1.02x faster                                                     |
| async_generators          | 489 ms                                                   | 509 ms: 1.04x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                                   |
| async_tree_io_tg          | 1.13 sec                                                 | 1.24 sec: 1.10x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_none_tg, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 119 ms: 1.04x slower                                                     |
| float          | 93.3 ms                                                  | 99.0 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.06 ms: 1.20x faster                                                    |
| regex_dna      | 253 ms                                                   | 263 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 251 us                                                   | 265 us: 1.06x slower                                                     |
| json_dumps           | 13.6 ms                                                  | 14.4 ms: 1.06x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.74 sec: 1.08x slower                                                   |
| pickle_pure_python   | 357 us                                                   | 411 us: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_parse, json_loads, xml_etree_generate, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.73 ms                                                  | 9.05 ms: 1.04x slower                                                    |
| python_startup         | 15.4 ms                                                  | 16.2 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.05x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 13.4 ms                                                  | 14.3 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                  | 447 us                                                   | 354 us: 1.27x faster                                                     |
| deepcopy_memo             | 50.4 us                                                  | 41.0 us: 1.23x faster                                                    |
| regex_effbot              | 4.89 ms                                                  | 4.06 ms: 1.20x faster                                                    |
| pylint                    | 342 ms                                                   | 297 ms: 1.15x faster                                                     |
| async_tree_memoization_tg | 649 ms                                                   | 564 ms: 1.15x faster                                                     |
| deepcopy_reduce           | 4.07 us                                                  | 3.58 us: 1.14x faster                                                    |
| async_tree_memoization    | 651 ms                                                   | 573 ms: 1.14x faster                                                     |
| go                        | 160 ms                                                   | 142 ms: 1.13x faster                                                     |
| async_tree_none           | 497 ms                                                   | 445 ms: 1.12x faster                                                     |
| generators                | 37.6 ms                                                  | 35.6 ms: 1.06x faster                                                    |
| telco                     | 9.74 ms                                                  | 9.38 ms: 1.04x faster                                                    |
| json                      | 5.73 ms                                                  | 5.54 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 751 ms: 1.02x faster                                                     |
| logging_simple            | 7.07 us                                                  | 6.99 us: 1.01x faster                                                    |
| bpe_tokeniser             | 5.87 sec                                                 | 5.94 sec: 1.01x slower                                                   |
| pprint_safe_repr          | 926 ms                                                   | 947 ms: 1.02x slower                                                     |
| mdp                       | 3.34 sec                                                 | 3.42 sec: 1.02x slower                                                   |
| pprint_pformat            | 1.90 sec                                                 | 1.96 sec: 1.03x slower                                                   |
| python_startup_no_site    | 8.73 ms                                                  | 9.05 ms: 1.04x slower                                                    |
| nbody                     | 114 ms                                                   | 119 ms: 1.04x slower                                                     |
| regex_dna                 | 253 ms                                                   | 263 ms: 1.04x slower                                                     |
| async_generators          | 489 ms                                                   | 509 ms: 1.04x slower                                                     |
| sphinx                    | 1.17 sec                                                 | 1.23 sec: 1.05x slower                                                   |
| sympy_expand              | 457 ms                                                   | 480 ms: 1.05x slower                                                     |
| python_startup            | 15.4 ms                                                  | 16.2 ms: 1.05x slower                                                    |
| fannkuch                  | 461 ms                                                   | 486 ms: 1.05x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                                   |
| unpickle_pure_python      | 251 us                                                   | 265 us: 1.06x slower                                                     |
| chaos                     | 68.0 ms                                                  | 72.0 ms: 1.06x slower                                                    |
| sympy_integrate           | 20.8 ms                                                  | 22.1 ms: 1.06x slower                                                    |
| float                     | 93.3 ms                                                  | 99.0 ms: 1.06x slower                                                    |
| json_dumps                | 13.6 ms                                                  | 14.4 ms: 1.06x slower                                                    |
| sympy_sum                 | 144 ms                                                   | 153 ms: 1.06x slower                                                     |
| typing_runtime_protocols  | 193 us                                                   | 206 us: 1.07x slower                                                     |
| sympy_str                 | 264 ms                                                   | 283 ms: 1.07x slower                                                     |
| nqueens                   | 100 ms                                                   | 107 ms: 1.07x slower                                                     |
| sqlglot_parse             | 1.38 ms                                                  | 1.47 ms: 1.07x slower                                                    |
| mako                      | 13.4 ms                                                  | 14.3 ms: 1.07x slower                                                    |
| comprehensions            | 20.4 us                                                  | 21.8 us: 1.07x slower                                                    |
| deltablue                 | 3.82 ms                                                  | 4.09 ms: 1.07x slower                                                    |
| logging_silent            | 133 ns                                                   | 143 ns: 1.07x slower                                                     |
| raytrace                  | 300 ms                                                   | 323 ms: 1.08x slower                                                     |
| pyflate                   | 556 ms                                                   | 601 ms: 1.08x slower                                                     |
| tomli_loads               | 2.54 sec                                                 | 2.74 sec: 1.08x slower                                                   |
| docutils                  | 2.89 sec                                                 | 3.12 sec: 1.08x slower                                                   |
| sqlglot_normalize         | 127 ms                                                   | 138 ms: 1.09x slower                                                     |
| create_gc_cycles          | 3.35 ms                                                  | 3.65 ms: 1.09x slower                                                    |
| async_tree_io_tg          | 1.13 sec                                                 | 1.24 sec: 1.10x slower                                                   |
| sqlalchemy_imperative     | 15.1 ms                                                  | 16.7 ms: 1.10x slower                                                    |
| gc_traversal              | 5.77 ms                                                  | 6.36 ms: 1.10x slower                                                    |
| scimark_monte_carlo       | 83.6 ms                                                  | 92.9 ms: 1.11x slower                                                    |
| pickle_pure_python        | 357 us                                                   | 411 us: 1.15x slower                                                     |
| k_core                    | 2.96 sec                                                 | 3.55 sec: 1.20x slower                                                   |
| bench_mp_pool             | 7.68 ms                                                  | 5.89 sec: 766.30x slower                                                 |
| Geometric mean            | (ref)                                                    | 1.09x slower                                                             |

Benchmark hidden because not significant (38): sqlalchemy_declarative, django_template, html5lib, async_tree_cpu_io_mixed_tg, scimark_lu, shortest_path, logging_format, thrift, 2to3, xml_etree_parse, regex_compile, pycparser, crypto_pyaes, pathlib, connected_components, async_tree_none_tg, sqlglot_optimize, coroutines, json_loads, meteor_contest, asyncio_websockets, spectral_norm, pidigits, bench_thread_pool, regex_v8, scimark_fft, hexiom, xml_etree_generate, xml_etree_iterparse, scimark_sparse_mat_mult, scimark_sor, richards_super, xml_etree_process, genshi_xml, richards, genshi_text, coverage, sqlglot_transpile
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (5) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: djangocms, dulwich_log, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 81.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x