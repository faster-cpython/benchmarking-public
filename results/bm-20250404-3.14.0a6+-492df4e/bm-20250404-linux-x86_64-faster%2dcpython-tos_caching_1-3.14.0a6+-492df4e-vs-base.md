# Results vs. base

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-x86_64
- commit hash: 492df4e
- commit date: 2025-04-04
- overall geometric mean: 1.004x slower
- HPT reliability: 99.42%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 248 ms: 1.00x faster                                                      |
| docutils       | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                    |
| html5lib       | 60.8 ms                                                                | 62.1 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization    | 312 ms                                                                 | 314 ms: 1.01x slower                                                      |
| async_generators          | 391 ms                                                                 | 395 ms: 1.01x slower                                                      |
| async_tree_memoization_tg | 315 ms                                                                 | 321 ms: 1.02x slower                                                      |
| async_tree_none_tg        | 249 ms                                                                 | 254 ms: 1.02x slower                                                      |
| coroutines                | 23.0 ms                                                                | 24.2 ms: 1.05x slower                                                     |
| Geometric mean            | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 70.2 ms                                                                | 67.4 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 24.0 ms                                                                | 23.3 ms: 1.03x faster                                                     |
| regex_dna      | 214 ms                                                                 | 216 ms: 1.01x slower                                                      |
| regex_compile  | 124 ms                                                                 | 126 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 29.8 us                                                                | 29.7 us: 1.00x faster                                                     |
| xml_etree_parse      | 140 ms                                                                 | 141 ms: 1.00x slower                                                      |
| pickle_pure_python   | 313 us                                                                 | 316 us: 1.01x slower                                                      |
| xml_etree_generate   | 83.8 ms                                                                | 84.9 ms: 1.01x slower                                                     |
| xml_etree_process    | 58.9 ms                                                                | 59.7 ms: 1.01x slower                                                     |
| unpickle_pure_python | 217 us                                                                 | 221 us: 1.02x slower                                                      |
| json_dumps           | 11.3 ms                                                                | 11.6 ms: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                     |
| python_startup_no_site | 8.17 ms                                                                | 8.18 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 11.3 ms                                                                | 11.5 ms: 1.02x slower                                                     |
| genshi_xml     | 48.7 ms                                                                | 49.6 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal              | 5.02 ms                                                                | 4.76 ms: 1.05x faster                                                     |
| float                     | 70.2 ms                                                                | 67.4 ms: 1.04x faster                                                     |
| typing_runtime_protocols  | 166 us                                                                 | 160 us: 1.04x faster                                                      |
| deepcopy_reduce           | 2.76 us                                                                | 2.66 us: 1.04x faster                                                     |
| regex_v8                  | 24.0 ms                                                                | 23.3 ms: 1.03x faster                                                     |
| pyflate                   | 445 ms                                                                 | 437 ms: 1.02x faster                                                      |
| fannkuch                  | 413 ms                                                                 | 405 ms: 1.02x faster                                                      |
| connected_components      | 453 ms                                                                 | 445 ms: 1.02x faster                                                      |
| scimark_monte_carlo       | 66.2 ms                                                                | 65.1 ms: 1.02x faster                                                     |
| many_optionals            | 933 us                                                                 | 925 us: 1.01x faster                                                      |
| shortest_path             | 495 ms                                                                 | 491 ms: 1.01x faster                                                      |
| sympy_sum                 | 150 ms                                                                 | 149 ms: 1.01x faster                                                      |
| json                      | 5.33 ms                                                                | 5.29 ms: 1.01x faster                                                     |
| telco                     | 7.80 ms                                                                | 7.75 ms: 1.01x faster                                                     |
| crypto_pyaes              | 73.0 ms                                                                | 72.5 ms: 1.01x faster                                                     |
| dulwich_log               | 59.5 ms                                                                | 59.1 ms: 1.01x faster                                                     |
| comprehensions            | 16.9 us                                                                | 16.8 us: 1.01x faster                                                     |
| mdp                       | 1.22 sec                                                               | 1.22 sec: 1.00x faster                                                    |
| docutils                  | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                    |
| sqlglot_v2_parse          | 1.24 ms                                                                | 1.24 ms: 1.00x faster                                                     |
| sqlalchemy_declarative    | 132 ms                                                                 | 131 ms: 1.00x faster                                                      |
| json_loads                | 29.8 us                                                                | 29.7 us: 1.00x faster                                                     |
| sqlglot_v2_transpile      | 1.56 ms                                                                | 1.55 ms: 1.00x faster                                                     |
| 2to3                      | 249 ms                                                                 | 248 ms: 1.00x faster                                                      |
| python_startup            | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                     |
| python_startup_no_site    | 8.17 ms                                                                | 8.18 ms: 1.00x slower                                                     |
| xml_etree_parse           | 140 ms                                                                 | 141 ms: 1.00x slower                                                      |
| bpe_tokeniser             | 4.51 sec                                                               | 4.53 sec: 1.00x slower                                                    |
| chaos                     | 56.5 ms                                                                | 56.8 ms: 1.01x slower                                                     |
| bench_thread_pool         | 877 us                                                                 | 881 us: 1.01x slower                                                      |
| regex_dna                 | 214 ms                                                                 | 216 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult   | 4.64 ms                                                                | 4.67 ms: 1.01x slower                                                     |
| async_tree_memoization    | 312 ms                                                                 | 314 ms: 1.01x slower                                                      |
| scimark_lu                | 116 ms                                                                 | 117 ms: 1.01x slower                                                      |
| pickle_pure_python        | 313 us                                                                 | 316 us: 1.01x slower                                                      |
| nqueens                   | 81.7 ms                                                                | 82.4 ms: 1.01x slower                                                     |
| async_generators          | 391 ms                                                                 | 395 ms: 1.01x slower                                                      |
| sqlglot_v2_optimize       | 52.7 ms                                                                | 53.3 ms: 1.01x slower                                                     |
| pprint_pformat            | 1.48 sec                                                               | 1.49 sec: 1.01x slower                                                    |
| sqlglot_v2_normalize      | 106 ms                                                                 | 107 ms: 1.01x slower                                                      |
| scimark_fft               | 340 ms                                                                 | 344 ms: 1.01x slower                                                      |
| xml_etree_generate        | 83.8 ms                                                                | 84.9 ms: 1.01x slower                                                     |
| xml_etree_process         | 58.9 ms                                                                | 59.7 ms: 1.01x slower                                                     |
| regex_compile             | 124 ms                                                                 | 126 ms: 1.01x slower                                                      |
| richards_super            | 49.3 ms                                                                | 50.0 ms: 1.01x slower                                                     |
| logging_format            | 6.12 us                                                                | 6.21 us: 1.02x slower                                                     |
| pathlib                   | 16.5 ms                                                                | 16.7 ms: 1.02x slower                                                     |
| raytrace                  | 258 ms                                                                 | 262 ms: 1.02x slower                                                      |
| mako                      | 11.3 ms                                                                | 11.5 ms: 1.02x slower                                                     |
| genshi_xml                | 48.7 ms                                                                | 49.6 ms: 1.02x slower                                                     |
| generators                | 29.9 ms                                                                | 30.5 ms: 1.02x slower                                                     |
| async_tree_memoization_tg | 315 ms                                                                 | 321 ms: 1.02x slower                                                      |
| sqlite_synth              | 2.77 us                                                                | 2.83 us: 1.02x slower                                                     |
| unpickle_pure_python      | 217 us                                                                 | 221 us: 1.02x slower                                                      |
| html5lib                  | 60.8 ms                                                                | 62.1 ms: 1.02x slower                                                     |
| go                        | 111 ms                                                                 | 113 ms: 1.02x slower                                                      |
| async_tree_none_tg        | 249 ms                                                                 | 254 ms: 1.02x slower                                                      |
| richards                  | 43.0 ms                                                                | 44.0 ms: 1.02x slower                                                     |
| hexiom                    | 6.14 ms                                                                | 6.29 ms: 1.02x slower                                                     |
| pycparser                 | 1.12 sec                                                               | 1.15 sec: 1.03x slower                                                    |
| deepcopy_memo             | 29.3 us                                                                | 30.1 us: 1.03x slower                                                     |
| logging_simple            | 5.51 us                                                                | 5.67 us: 1.03x slower                                                     |
| json_dumps                | 11.3 ms                                                                | 11.6 ms: 1.03x slower                                                     |
| scimark_sor               | 115 ms                                                                 | 119 ms: 1.04x slower                                                      |
| deltablue                 | 3.31 ms                                                                | 3.43 ms: 1.04x slower                                                     |
| spectral_norm             | 101 ms                                                                 | 105 ms: 1.04x slower                                                      |
| logging_silent            | 94.4 ns                                                                | 99.0 ns: 1.05x slower                                                     |
| coroutines                | 23.0 ms                                                                | 24.2 ms: 1.05x slower                                                     |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (27): k_core, meteor_contest, sympy_str, pprint_safe_repr, deepcopy, tomli_loads, regex_effbot, asyncio_websockets, sqlalchemy_imperative, bench_mp_pool, pidigits, sphinx, pylint, xml_etree_iterparse, create_gc_cycles, genshi_text, async_tree_cpu_io_mixed, coverage, sympy_integrate, sympy_expand, nbody, django_template, async_tree_cpu_io_mixed_tg, subparsers, async_tree_none, async_tree_io_tg, async_tree_io

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.42% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x