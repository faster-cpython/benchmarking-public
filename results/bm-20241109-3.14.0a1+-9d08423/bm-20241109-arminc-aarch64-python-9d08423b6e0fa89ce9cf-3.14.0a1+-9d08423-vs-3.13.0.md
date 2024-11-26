# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-aarch64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.012x slower
- HPT reliability: 95.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.89 sec                                                 | 3.13 sec: 1.08x slower                                                   |
| sphinx         | 1.17 sec                                                 | 1.24 sec: 1.06x slower                                                   |
| Geometric mean | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 552 ms: 1.18x faster                                                     |
| async_tree_none           | 497 ms                                                   | 458 ms: 1.09x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 611 ms: 1.06x faster                                                     |
| asyncio_websockets        | 659 ms                                                   | 676 ms: 1.03x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.16 sec: 1.05x slower                                                   |
| async_tree_io_tg          | 1.13 sec                                                 | 1.27 sec: 1.12x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, coroutines, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 98.6 ms: 1.06x slower                                                    |
| nbody          | 114 ms                                                   | 123 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 5.07 ms: 1.04x slower                                                    |
| regex_dna      | 253 ms                                                   | 272 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 149 ms                                                   | 152 ms: 1.02x slower                                                     |
| unpickle_pure_python | 251 us                                                   | 268 us: 1.07x slower                                                     |
| json_dumps           | 13.6 ms                                                  | 14.8 ms: 1.09x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.78 sec: 1.09x slower                                                   |
| pickle_pure_python   | 357 us                                                   | 401 us: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_parse, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.73 ms                                                  | 9.02 ms: 1.03x slower                                                    |
| python_startup         | 15.4 ms                                                  | 16.1 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.04x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 43.7 ms: 1.05x slower                                                    |
| mako            | 13.4 ms                                                  | 14.4 ms: 1.07x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                  | 447 us                                                   | 355 us: 1.26x faster                                                     |
| deepcopy_memo             | 50.4 us                                                  | 40.6 us: 1.24x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 552 ms: 1.18x faster                                                     |
| deepcopy_reduce           | 4.07 us                                                  | 3.59 us: 1.13x faster                                                    |
| go                        | 160 ms                                                   | 147 ms: 1.09x faster                                                     |
| async_tree_none           | 497 ms                                                   | 458 ms: 1.09x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 611 ms: 1.06x faster                                                     |
| generators                | 37.6 ms                                                  | 35.8 ms: 1.05x faster                                                    |
| telco                     | 9.74 ms                                                  | 9.40 ms: 1.04x faster                                                    |
| bpe_tokeniser             | 5.87 sec                                                 | 5.92 sec: 1.01x slower                                                   |
| xml_etree_iterparse       | 149 ms                                                   | 152 ms: 1.02x slower                                                     |
| connected_components      | 533 ms                                                   | 545 ms: 1.02x slower                                                     |
| sqlalchemy_imperative     | 15.1 ms                                                  | 15.5 ms: 1.03x slower                                                    |
| asyncio_websockets        | 659 ms                                                   | 676 ms: 1.03x slower                                                     |
| richards                  | 53.6 ms                                                  | 55.0 ms: 1.03x slower                                                    |
| sympy_expand              | 457 ms                                                   | 470 ms: 1.03x slower                                                     |
| scimark_sor               | 160 ms                                                   | 165 ms: 1.03x slower                                                     |
| logging_simple            | 7.07 us                                                  | 7.30 us: 1.03x slower                                                    |
| python_startup_no_site    | 8.73 ms                                                  | 9.02 ms: 1.03x slower                                                    |
| regex_effbot              | 4.89 ms                                                  | 5.07 ms: 1.04x slower                                                    |
| comprehensions            | 20.4 us                                                  | 21.2 us: 1.04x slower                                                    |
| richards_super            | 60.1 ms                                                  | 62.6 ms: 1.04x slower                                                    |
| pprint_safe_repr          | 926 ms                                                   | 966 ms: 1.04x slower                                                     |
| python_startup            | 15.4 ms                                                  | 16.1 ms: 1.05x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 1.99 sec: 1.05x slower                                                   |
| django_template           | 41.6 ms                                                  | 43.7 ms: 1.05x slower                                                    |
| chaos                     | 68.0 ms                                                  | 71.4 ms: 1.05x slower                                                    |
| sympy_integrate           | 20.8 ms                                                  | 21.9 ms: 1.05x slower                                                    |
| async_tree_io             | 1.11 sec                                                 | 1.16 sec: 1.05x slower                                                   |
| mdp                       | 3.34 sec                                                 | 3.51 sec: 1.05x slower                                                   |
| float                     | 93.3 ms                                                  | 98.6 ms: 1.06x slower                                                    |
| typing_runtime_protocols  | 193 us                                                   | 205 us: 1.06x slower                                                     |
| sphinx                    | 1.17 sec                                                 | 1.24 sec: 1.06x slower                                                   |
| fannkuch                  | 461 ms                                                   | 491 ms: 1.06x slower                                                     |
| sqlglot_parse             | 1.38 ms                                                  | 1.47 ms: 1.07x slower                                                    |
| raytrace                  | 300 ms                                                   | 320 ms: 1.07x slower                                                     |
| unpickle_pure_python      | 251 us                                                   | 268 us: 1.07x slower                                                     |
| sympy_str                 | 264 ms                                                   | 283 ms: 1.07x slower                                                     |
| mako                      | 13.4 ms                                                  | 14.4 ms: 1.07x slower                                                    |
| logging_silent            | 133 ns                                                   | 143 ns: 1.07x slower                                                     |
| regex_dna                 | 253 ms                                                   | 272 ms: 1.08x slower                                                     |
| nbody                     | 114 ms                                                   | 123 ms: 1.08x slower                                                     |
| docutils                  | 2.89 sec                                                 | 3.13 sec: 1.08x slower                                                   |
| nqueens                   | 100 ms                                                   | 108 ms: 1.08x slower                                                     |
| json_dumps                | 13.6 ms                                                  | 14.8 ms: 1.09x slower                                                    |
| tomli_loads               | 2.54 sec                                                 | 2.78 sec: 1.09x slower                                                   |
| deltablue                 | 3.82 ms                                                  | 4.20 ms: 1.10x slower                                                    |
| pyflate                   | 556 ms                                                   | 616 ms: 1.11x slower                                                     |
| async_tree_io_tg          | 1.13 sec                                                 | 1.27 sec: 1.12x slower                                                   |
| pickle_pure_python        | 357 us                                                   | 401 us: 1.12x slower                                                     |
| create_gc_cycles          | 3.35 ms                                                  | 3.83 ms: 1.14x slower                                                    |
| gc_traversal              | 5.77 ms                                                  | 6.75 ms: 1.17x slower                                                    |
| k_core                    | 2.96 sec                                                 | 4.56 sec: 1.54x slower                                                   |
| bench_mp_pool             | 7.68 ms                                                  | 6.80 sec: 884.93x slower                                                 |
| Geometric mean            | (ref)                                                    | 1.11x slower                                                             |

Benchmark hidden because not significant (38): async_tree_cpu_io_mixed_tg, async_tree_none_tg, json, sqlalchemy_declarative, pathlib, thrift, async_tree_cpu_io_mixed, coroutines, xml_etree_generate, scimark_lu, xml_etree_parse, sympy_sum, crypto_pyaes, 2to3, pycparser, regex_v8, async_generators, shortest_path, scimark_fft, bench_thread_pool, regex_compile, genshi_xml, logging_format, coverage, pidigits, sqlglot_optimize, scimark_monte_carlo, meteor_contest, json_loads, genshi_text, xml_etree_process, scimark_sparse_mat_mult, sqlglot_transpile, spectral_norm, hexiom, sqlglot_normalize, pylint, html5lib
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (2) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: dulwich_log, sqlite_synth

- Geometric mean (including insignificant results): 1.012x slower
# HPT report

- Reliability score: 95.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x