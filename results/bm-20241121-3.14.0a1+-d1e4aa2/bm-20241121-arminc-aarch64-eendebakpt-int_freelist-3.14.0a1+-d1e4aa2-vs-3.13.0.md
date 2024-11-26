# Results vs. 3.13.0

- fork: eendebakpt
- ref: int_freelist
- machine: linux-aarch64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.004x slower
- HPT reliability: 52.16%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 2.89 sec                                                 | 3.11 sec: 1.08x slower                                               |
| sphinx         | 1.17 sec                                                 | 1.22 sec: 1.04x slower                                               |
| Geometric mean | (ref)                                                    | 1.03x slower                                                         |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 545 ms: 1.19x faster                                                 |
| async_tree_none           | 497 ms                                                   | 448 ms: 1.11x faster                                                 |
| async_tree_memoization    | 651 ms                                                   | 603 ms: 1.08x faster                                                 |
| async_tree_none_tg        | 470 ms                                                   | 452 ms: 1.04x faster                                                 |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                               |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                               |
| Geometric mean            | (ref)                                                    | 1.02x faster                                                         |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 234 ms                                                   | 241 ms: 1.03x slower                                                 |
| float          | 93.3 ms                                                  | 96.8 ms: 1.04x slower                                                |
| nbody          | 114 ms                                                   | 120 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                    | 1.04x slower                                                         |

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_dna, regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.54 sec                                                 | 2.66 sec: 1.05x slower                                               |
| unpickle_pure_python | 251 us                                                   | 277 us: 1.11x slower                                                 |
| pickle_pure_python   | 357 us                                                   | 396 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                    | 1.05x slower                                                         |

Benchmark hidden because not significant (6): xml_etree_iterparse, json_loads, xml_etree_process, xml_etree_parse, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 16.0 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                    | 1.03x slower                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 60.3 ms                                                  | 62.2 ms: 1.03x slower                                                |
| mako           | 13.4 ms                                                  | 14.1 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                    | 1.03x slower                                                         |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|---------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                  | 447 us                                                   | 353 us: 1.27x faster                                                 |
| deepcopy_memo             | 50.4 us                                                  | 40.6 us: 1.24x faster                                                |
| async_tree_memoization_tg | 649 ms                                                   | 545 ms: 1.19x faster                                                 |
| go                        | 160 ms                                                   | 143 ms: 1.11x faster                                                 |
| deepcopy_reduce           | 4.07 us                                                  | 3.66 us: 1.11x faster                                                |
| async_tree_none           | 497 ms                                                   | 448 ms: 1.11x faster                                                 |
| spectral_norm             | 143 ms                                                   | 130 ms: 1.10x faster                                                 |
| async_tree_memoization    | 651 ms                                                   | 603 ms: 1.08x faster                                                 |
| scimark_fft               | 447 ms                                                   | 422 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult   | 6.51 ms                                                  | 6.22 ms: 1.05x faster                                                |
| pathlib                   | 22.7 ms                                                  | 21.7 ms: 1.04x faster                                                |
| async_tree_none_tg        | 470 ms                                                   | 452 ms: 1.04x faster                                                 |
| generators                | 37.6 ms                                                  | 36.2 ms: 1.04x faster                                                |
| bpe_tokeniser             | 5.87 sec                                                 | 5.91 sec: 1.01x slower                                               |
| sympy_str                 | 264 ms                                                   | 266 ms: 1.01x slower                                                 |
| connected_components      | 533 ms                                                   | 545 ms: 1.02x slower                                                 |
| pprint_safe_repr          | 926 ms                                                   | 955 ms: 1.03x slower                                                 |
| mdp                       | 3.34 sec                                                 | 3.44 sec: 1.03x slower                                               |
| genshi_xml                | 60.3 ms                                                  | 62.2 ms: 1.03x slower                                                |
| pidigits                  | 234 ms                                                   | 241 ms: 1.03x slower                                                 |
| bench_thread_pool         | 1.27 ms                                                  | 1.32 ms: 1.03x slower                                                |
| pprint_pformat            | 1.90 sec                                                 | 1.96 sec: 1.03x slower                                               |
| python_startup            | 15.4 ms                                                  | 16.0 ms: 1.04x slower                                                |
| float                     | 93.3 ms                                                  | 96.8 ms: 1.04x slower                                                |
| logging_format            | 7.82 us                                                  | 8.15 us: 1.04x slower                                                |
| deltablue                 | 3.82 ms                                                  | 3.99 ms: 1.04x slower                                                |
| sphinx                    | 1.17 sec                                                 | 1.22 sec: 1.04x slower                                               |
| pyflate                   | 556 ms                                                   | 582 ms: 1.05x slower                                                 |
| tomli_loads               | 2.54 sec                                                 | 2.66 sec: 1.05x slower                                               |
| chaos                     | 68.0 ms                                                  | 71.3 ms: 1.05x slower                                                |
| sympy_expand              | 457 ms                                                   | 479 ms: 1.05x slower                                                 |
| nbody                     | 114 ms                                                   | 120 ms: 1.05x slower                                                 |
| mako                      | 13.4 ms                                                  | 14.1 ms: 1.05x slower                                                |
| typing_runtime_protocols  | 193 us                                                   | 204 us: 1.06x slower                                                 |
| comprehensions            | 20.4 us                                                  | 21.6 us: 1.06x slower                                                |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                               |
| sympy_integrate           | 20.8 ms                                                  | 22.1 ms: 1.06x slower                                                |
| logging_simple            | 7.07 us                                                  | 7.52 us: 1.06x slower                                                |
| fannkuch                  | 461 ms                                                   | 491 ms: 1.07x slower                                                 |
| sqlalchemy_imperative     | 15.1 ms                                                  | 16.2 ms: 1.07x slower                                                |
| sqlglot_normalize         | 127 ms                                                   | 135 ms: 1.07x slower                                                 |
| sqlglot_parse             | 1.38 ms                                                  | 1.47 ms: 1.07x slower                                                |
| raytrace                  | 300 ms                                                   | 321 ms: 1.07x slower                                                 |
| sqlglot_transpile         | 1.73 ms                                                  | 1.86 ms: 1.07x slower                                                |
| docutils                  | 2.89 sec                                                 | 3.11 sec: 1.08x slower                                               |
| unpickle_pure_python      | 251 us                                                   | 277 us: 1.11x slower                                                 |
| pickle_pure_python        | 357 us                                                   | 396 us: 1.11x slower                                                 |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                               |
| gc_traversal              | 5.77 ms                                                  | 6.66 ms: 1.15x slower                                                |
| create_gc_cycles          | 3.35 ms                                                  | 3.93 ms: 1.17x slower                                                |
| k_core                    | 2.96 sec                                                 | 4.53 sec: 1.53x slower                                               |
| bench_mp_pool             | 7.68 ms                                                  | 6.73 sec: 875.17x slower                                             |
| Geometric mean            | (ref)                                                    | 1.10x slower                                                         |

Benchmark hidden because not significant (40): async_tree_cpu_io_mixed_tg, sqlalchemy_declarative, django_template, scimark_lu, async_tree_cpu_io_mixed, scimark_sor, html5lib, json, sympy_sum, richards, scimark_monte_carlo, 2to3, pycparser, regex_dna, shortest_path, regex_v8, xml_etree_iterparse, thrift, sqlglot_optimize, regex_compile, python_startup_no_site, crypto_pyaes, telco, asyncio_websockets, async_generators, json_loads, xml_etree_process, xml_etree_parse, coroutines, nqueens, hexiom, xml_etree_generate, logging_silent, genshi_text, richards_super, coverage, meteor_contest, json_dumps, regex_effbot, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (5) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-arminc-aarch64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: djangocms, dulwich_log, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.004x slower
# HPT report

- Reliability score: 52.16% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x