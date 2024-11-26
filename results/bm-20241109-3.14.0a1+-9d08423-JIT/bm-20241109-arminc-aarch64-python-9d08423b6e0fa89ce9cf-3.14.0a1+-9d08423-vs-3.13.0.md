# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-aarch64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.099x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 398 ms: 1.31x slower                                                     |
| docutils       | 2.89 sec                                                 | 3.76 sec: 1.30x slower                                                   |
| html5lib       | 66.4 ms                                                  | 74.6 ms: 1.12x slower                                                    |
| sphinx         | 1.17 sec                                                 | 1.53 sec: 1.31x slower                                                   |
| Geometric mean | (ref)                                                    | 1.26x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 553 ms: 1.17x faster                                                     |
| async_tree_none           | 497 ms                                                   | 471 ms: 1.05x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 618 ms: 1.05x faster                                                     |
| asyncio_websockets        | 659 ms                                                   | 677 ms: 1.03x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.19 sec: 1.07x slower                                                   |
| async_generators          | 489 ms                                                   | 532 ms: 1.09x slower                                                     |
| async_tree_io_tg          | 1.13 sec                                                 | 1.29 sec: 1.14x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 234 ms                                                   | 249 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 33.0 ms: 1.04x slower                                                    |
| regex_effbot   | 4.89 ms                                                  | 5.08 ms: 1.04x slower                                                    |
| regex_compile  | 127 ms                                                   | 183 ms: 1.44x slower                                                     |
| Geometric mean | (ref)                                                    | 1.12x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 149 ms                                                   | 154 ms: 1.03x slower                                                     |
| tomli_loads          | 2.54 sec                                                 | 2.63 sec: 1.03x slower                                                   |
| json_dumps           | 13.6 ms                                                  | 14.5 ms: 1.07x slower                                                    |
| unpickle_pure_python | 251 us                                                   | 273 us: 1.09x slower                                                     |
| pickle_pure_python   | 357 us                                                   | 422 us: 1.18x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_generate, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.73 ms                                                  | 9.14 ms: 1.05x slower                                                    |
| python_startup         | 15.4 ms                                                  | 16.2 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.05x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 34.0 ms: 1.23x slower                                                    |
| django_template | 41.6 ms                                                  | 51.2 ms: 1.23x slower                                                    |
| genshi_xml      | 60.3 ms                                                  | 81.4 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo             | 50.4 us                                                  | 40.7 us: 1.24x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 553 ms: 1.17x faster                                                     |
| deepcopy                  | 447 us                                                   | 412 us: 1.08x faster                                                     |
| async_tree_none           | 497 ms                                                   | 471 ms: 1.05x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 618 ms: 1.05x faster                                                     |
| pathlib                   | 22.7 ms                                                  | 22.1 ms: 1.03x faster                                                    |
| shortest_path             | 565 ms                                                   | 580 ms: 1.03x slower                                                     |
| asyncio_websockets        | 659 ms                                                   | 677 ms: 1.03x slower                                                     |
| xml_etree_iterparse       | 149 ms                                                   | 154 ms: 1.03x slower                                                     |
| tomli_loads               | 2.54 sec                                                 | 2.63 sec: 1.03x slower                                                   |
| regex_v8                  | 31.8 ms                                                  | 33.0 ms: 1.04x slower                                                    |
| regex_effbot              | 4.89 ms                                                  | 5.08 ms: 1.04x slower                                                    |
| spectral_norm             | 143 ms                                                   | 149 ms: 1.04x slower                                                     |
| connected_components      | 533 ms                                                   | 557 ms: 1.05x slower                                                     |
| python_startup_no_site    | 8.73 ms                                                  | 9.14 ms: 1.05x slower                                                    |
| crypto_pyaes              | 83.7 ms                                                  | 87.8 ms: 1.05x slower                                                    |
| python_startup            | 15.4 ms                                                  | 16.2 ms: 1.05x slower                                                    |
| pidigits                  | 234 ms                                                   | 249 ms: 1.06x slower                                                     |
| json_dumps                | 13.6 ms                                                  | 14.5 ms: 1.07x slower                                                    |
| scimark_monte_carlo       | 83.6 ms                                                  | 89.4 ms: 1.07x slower                                                    |
| mdp                       | 3.34 sec                                                 | 3.58 sec: 1.07x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.19 sec: 1.07x slower                                                   |
| logging_format            | 7.82 us                                                  | 8.44 us: 1.08x slower                                                    |
| scimark_lu                | 139 ms                                                   | 151 ms: 1.09x slower                                                     |
| async_generators          | 489 ms                                                   | 532 ms: 1.09x slower                                                     |
| unpickle_pure_python      | 251 us                                                   | 273 us: 1.09x slower                                                     |
| pyflate                   | 556 ms                                                   | 609 ms: 1.09x slower                                                     |
| bench_thread_pool         | 1.27 ms                                                  | 1.40 ms: 1.09x slower                                                    |
| logging_simple            | 7.07 us                                                  | 7.79 us: 1.10x slower                                                    |
| gc_traversal              | 5.77 ms                                                  | 6.42 ms: 1.11x slower                                                    |
| fannkuch                  | 461 ms                                                   | 513 ms: 1.11x slower                                                     |
| meteor_contest            | 114 ms                                                   | 127 ms: 1.12x slower                                                     |
| create_gc_cycles          | 3.35 ms                                                  | 3.75 ms: 1.12x slower                                                    |
| html5lib                  | 66.4 ms                                                  | 74.6 ms: 1.12x slower                                                    |
| scimark_sparse_mat_mult   | 6.51 ms                                                  | 7.38 ms: 1.13x slower                                                    |
| async_tree_io_tg          | 1.13 sec                                                 | 1.29 sec: 1.14x slower                                                   |
| deltablue                 | 3.82 ms                                                  | 4.38 ms: 1.15x slower                                                    |
| typing_runtime_protocols  | 193 us                                                   | 224 us: 1.16x slower                                                     |
| richards_super            | 60.1 ms                                                  | 69.9 ms: 1.16x slower                                                    |
| go                        | 160 ms                                                   | 187 ms: 1.17x slower                                                     |
| richards                  | 53.6 ms                                                  | 63.3 ms: 1.18x slower                                                    |
| pycparser                 | 1.27 sec                                                 | 1.50 sec: 1.18x slower                                                   |
| pickle_pure_python        | 357 us                                                   | 422 us: 1.18x slower                                                     |
| sqlglot_parse             | 1.38 ms                                                  | 1.66 ms: 1.20x slower                                                    |
| raytrace                  | 300 ms                                                   | 362 ms: 1.21x slower                                                     |
| comprehensions            | 20.4 us                                                  | 24.8 us: 1.22x slower                                                    |
| genshi_text               | 27.7 ms                                                  | 34.0 ms: 1.23x slower                                                    |
| django_template           | 41.6 ms                                                  | 51.2 ms: 1.23x slower                                                    |
| chaos                     | 68.0 ms                                                  | 83.8 ms: 1.23x slower                                                    |
| sqlglot_transpile         | 1.73 ms                                                  | 2.18 ms: 1.26x slower                                                    |
| nqueens                   | 100 ms                                                   | 127 ms: 1.27x slower                                                     |
| docutils                  | 2.89 sec                                                 | 3.76 sec: 1.30x slower                                                   |
| sphinx                    | 1.17 sec                                                 | 1.53 sec: 1.31x slower                                                   |
| 2to3                      | 304 ms                                                   | 398 ms: 1.31x slower                                                     |
| generators                | 37.6 ms                                                  | 49.3 ms: 1.31x slower                                                    |
| sqlalchemy_declarative    | 150 ms                                                   | 198 ms: 1.32x slower                                                     |
| sqlglot_normalize         | 127 ms                                                   | 167 ms: 1.32x slower                                                     |
| sqlglot_optimize          | 62.2 ms                                                  | 83.6 ms: 1.34x slower                                                    |
| sympy_expand              | 457 ms                                                   | 616 ms: 1.35x slower                                                     |
| genshi_xml                | 60.3 ms                                                  | 81.4 ms: 1.35x slower                                                    |
| sqlalchemy_imperative     | 15.1 ms                                                  | 20.6 ms: 1.36x slower                                                    |
| pprint_safe_repr          | 926 ms                                                   | 1.26 sec: 1.36x slower                                                   |
| sympy_str                 | 264 ms                                                   | 363 ms: 1.37x slower                                                     |
| pprint_pformat            | 1.90 sec                                                 | 2.63 sec: 1.38x slower                                                   |
| sympy_integrate           | 20.8 ms                                                  | 29.3 ms: 1.41x slower                                                    |
| hexiom                    | 7.11 ms                                                  | 10.1 ms: 1.42x slower                                                    |
| regex_compile             | 127 ms                                                   | 183 ms: 1.44x slower                                                     |
| sympy_sum                 | 144 ms                                                   | 212 ms: 1.48x slower                                                     |
| pylint                    | 342 ms                                                   | 509 ms: 1.49x slower                                                     |
| k_core                    | 2.96 sec                                                 | 4.54 sec: 1.53x slower                                                   |
| bench_mp_pool             | 7.68 ms                                                  | 1.91 sec: 248.38x slower                                                 |
| Geometric mean            | (ref)                                                    | 1.19x slower                                                             |

Benchmark hidden because not significant (21): async_tree_none_tg, scimark_sor, async_tree_cpu_io_mixed_tg, mako, xml_etree_parse, json, bpe_tokeniser, scimark_fft, xml_etree_generate, async_tree_cpu_io_mixed, logging_silent, telco, thrift, regex_dna, deepcopy_reduce, xml_etree_process, json_loads, coverage, coroutines, nbody, float
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (2) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-arminc-aarch64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: dulwich_log, sqlite_synth

- Geometric mean (including insignificant results): 1.099x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.08x