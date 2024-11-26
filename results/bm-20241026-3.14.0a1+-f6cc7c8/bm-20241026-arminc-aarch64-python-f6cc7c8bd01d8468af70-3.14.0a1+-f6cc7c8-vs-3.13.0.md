# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-aarch64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.014x faster
- HPT reliability: 88.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 294 ms: 1.03x faster                                                     |
| docutils       | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (3): html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 528 ms: 1.23x faster                                                     |
| async_tree_memoization     | 651 ms                                                   | 578 ms: 1.13x faster                                                     |
| async_tree_none            | 497 ms                                                   | 445 ms: 1.12x faster                                                     |
| async_tree_none_tg         | 470 ms                                                   | 438 ms: 1.07x faster                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 733 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 743 ms: 1.03x faster                                                     |
| async_generators           | 489 ms                                                   | 477 ms: 1.03x faster                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.11x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 95.1 ms: 1.02x slower                                                    |
| nbody          | 114 ms                                                   | 117 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                   | 125 ms: 1.02x faster                                                     |
| regex_effbot   | 4.89 ms                                                  | 4.96 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 186 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 149 ms                                                   | 147 ms: 1.02x faster                                                     |
| json_loads           | 31.7 us                                                  | 31.3 us: 1.01x faster                                                    |
| unpickle_pure_python | 251 us                                                   | 257 us: 1.02x slower                                                     |
| tomli_loads          | 2.54 sec                                                 | 2.63 sec: 1.03x slower                                                   |
| pickle_pure_python   | 357 us                                                   | 371 us: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 13.4 ms                                                  | 13.6 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 447 us                                                   | 336 us: 1.33x faster                                                     |
| deepcopy_memo              | 50.4 us                                                  | 38.4 us: 1.31x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 528 ms: 1.23x faster                                                     |
| go                         | 160 ms                                                   | 137 ms: 1.17x faster                                                     |
| deepcopy_reduce            | 4.07 us                                                  | 3.54 us: 1.15x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 578 ms: 1.13x faster                                                     |
| async_tree_none            | 497 ms                                                   | 445 ms: 1.12x faster                                                     |
| generators                 | 37.6 ms                                                  | 34.8 ms: 1.08x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 438 ms: 1.07x faster                                                     |
| sqlalchemy_declarative     | 150 ms                                                   | 140 ms: 1.07x faster                                                     |
| pathlib                    | 22.7 ms                                                  | 21.5 ms: 1.06x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 186 ms: 1.05x faster                                                     |
| json                       | 5.73 ms                                                  | 5.46 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 733 ms: 1.05x faster                                                     |
| 2to3                       | 304 ms                                                   | 294 ms: 1.03x faster                                                     |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 743 ms: 1.03x faster                                                     |
| telco                      | 9.74 ms                                                  | 9.45 ms: 1.03x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.24 sec: 1.03x faster                                                   |
| logging_format             | 7.82 us                                                  | 7.62 us: 1.03x faster                                                    |
| async_generators           | 489 ms                                                   | 477 ms: 1.03x faster                                                     |
| thrift                     | 968 us                                                   | 945 us: 1.02x faster                                                     |
| logging_simple             | 7.07 us                                                  | 6.91 us: 1.02x faster                                                    |
| scimark_fft                | 447 ms                                                   | 438 ms: 1.02x faster                                                     |
| coverage                   | 99.1 ms                                                  | 97.2 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 147 ms: 1.02x faster                                                     |
| regex_compile              | 127 ms                                                   | 125 ms: 1.02x faster                                                     |
| bpe_tokeniser              | 5.87 sec                                                 | 5.79 sec: 1.01x faster                                                   |
| json_loads                 | 31.7 us                                                  | 31.3 us: 1.01x faster                                                    |
| sqlglot_normalize          | 127 ms                                                   | 128 ms: 1.01x slower                                                     |
| pprint_safe_repr           | 926 ms                                                   | 939 ms: 1.01x slower                                                     |
| pprint_pformat             | 1.90 sec                                                 | 1.92 sec: 1.01x slower                                                   |
| fannkuch                   | 461 ms                                                   | 468 ms: 1.02x slower                                                     |
| regex_effbot               | 4.89 ms                                                  | 4.96 ms: 1.02x slower                                                    |
| sympy_integrate            | 20.8 ms                                                  | 21.2 ms: 1.02x slower                                                    |
| mako                       | 13.4 ms                                                  | 13.6 ms: 1.02x slower                                                    |
| float                      | 93.3 ms                                                  | 95.1 ms: 1.02x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.13 sec: 1.02x slower                                                   |
| comprehensions             | 20.4 us                                                  | 20.8 us: 1.02x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 257 us: 1.02x slower                                                     |
| nbody                      | 114 ms                                                   | 117 ms: 1.02x slower                                                     |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.03x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.94 ms: 1.03x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 2.63 sec: 1.03x slower                                                   |
| chaos                      | 68.0 ms                                                  | 70.3 ms: 1.03x slower                                                    |
| raytrace                   | 300 ms                                                   | 310 ms: 1.03x slower                                                     |
| pickle_pure_python         | 357 us                                                   | 371 us: 1.04x slower                                                     |
| docutils                   | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                   |
| pyflate                    | 556 ms                                                   | 585 ms: 1.05x slower                                                     |
| create_gc_cycles           | 3.35 ms                                                  | 3.60 ms: 1.07x slower                                                    |
| gc_traversal               | 5.77 ms                                                  | 6.31 ms: 1.09x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.11x slower                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 4.94 sec: 643.12x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (37): tornado_http, html5lib, crypto_pyaes, nqueens, sympy_sum, logging_silent, python_startup_no_site, genshi_text, genshi_xml, sqlglot_optimize, scimark_monte_carlo, xml_etree_generate, meteor_contest, asyncio_websockets, richards_super, regex_dna, sympy_str, scimark_sor, hexiom, bench_thread_pool, mdp, regex_v8, typing_runtime_protocols, coroutines, richards, sqlglot_transpile, xml_etree_process, sympy_expand, django_template, pidigits, scimark_sparse_mat_mult, python_startup, spectral_norm, sphinx, sqlalchemy_imperative, pylint, json_dumps
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path
Ignored benchmarks (1) of results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: dulwich_log

- Geometric mean (including insignificant results): 1.014x faster
# HPT report

- Reliability score: 88.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x