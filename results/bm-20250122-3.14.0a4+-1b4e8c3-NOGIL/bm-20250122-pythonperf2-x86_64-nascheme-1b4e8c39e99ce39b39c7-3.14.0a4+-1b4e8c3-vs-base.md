# Results vs. base

- fork: nascheme
- ref: 1b4e8c39e99ce39b39c7
- machine: linux-x86_64
- commit hash: 1b4e8c3
- commit date: 2025-01-22
- overall geometric mean: 1.003x slower
- HPT reliability: 89.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 338 ms                                                                       | 342 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 302 ms                                                                       | 295 ms: 1.02x faster                                                           |
| async_tree_memoization     | 372 ms                                                                       | 365 ms: 1.02x faster                                                           |
| async_tree_memoization_tg  | 327 ms                                                                       | 322 ms: 1.01x faster                                                           |
| async_tree_io              | 625 ms                                                                       | 617 ms: 1.01x faster                                                           |
| asyncio_websockets         | 382 ms                                                                       | 378 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed    | 537 ms                                                                       | 533 ms: 1.01x faster                                                           |
| async_tree_none_tg         | 252 ms                                                                       | 250 ms: 1.01x faster                                                           |
| coroutines                 | 22.1 ms                                                                      | 22.0 ms: 1.00x faster                                                          |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                       | 488 ms: 1.00x faster                                                           |
| async_generators           | 471 ms                                                                       | 470 ms: 1.00x faster                                                           |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 249 ms                                                                       | 248 ms: 1.00x faster                                                           |
| nbody          | 132 ms                                                                       | 134 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 25.9 ms                                                                      | 25.8 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                   |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 240 us                                                                       | 237 us: 1.02x faster                                                           |
| json_dumps           | 13.5 ms                                                                      | 13.6 ms: 1.00x slower                                                          |
| tomli_loads          | 2.42 sec                                                                     | 2.44 sec: 1.00x slower                                                         |
| json_loads           | 27.9 us                                                                      | 28.2 us: 1.01x slower                                                          |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                                      | 18.9 ms: 1.01x slower                                                          |
| python_startup_no_site | 11.8 ms                                                                      | 12.0 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                                        | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 48.1 ms                                                                      | 46.7 ms: 1.03x faster                                                          |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                                   |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104 | bm-20250122-pythonperf2-x86_64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| go                         | 154 ms                                                                       | 149 ms: 1.03x faster                                                           |
| django_template            | 48.1 ms                                                                      | 46.7 ms: 1.03x faster                                                          |
| sqlglot_parse              | 1.70 ms                                                                      | 1.65 ms: 1.03x faster                                                          |
| scimark_monte_carlo        | 90.2 ms                                                                      | 87.8 ms: 1.03x faster                                                          |
| async_tree_none            | 302 ms                                                                       | 295 ms: 1.02x faster                                                           |
| async_tree_memoization     | 372 ms                                                                       | 365 ms: 1.02x faster                                                           |
| unpickle_pure_python       | 240 us                                                                       | 237 us: 1.02x faster                                                           |
| logging_format             | 8.17 us                                                                      | 8.05 us: 1.02x faster                                                          |
| mdp                        | 2.78 sec                                                                     | 2.74 sec: 1.01x faster                                                         |
| spectral_norm              | 102 ms                                                                       | 101 ms: 1.01x faster                                                           |
| coverage                   | 103 ms                                                                       | 102 ms: 1.01x faster                                                           |
| async_tree_memoization_tg  | 327 ms                                                                       | 322 ms: 1.01x faster                                                           |
| async_tree_io              | 625 ms                                                                       | 617 ms: 1.01x faster                                                           |
| deltablue                  | 4.63 ms                                                                      | 4.57 ms: 1.01x faster                                                          |
| sqlglot_transpile          | 2.10 ms                                                                      | 2.07 ms: 1.01x faster                                                          |
| crypto_pyaes               | 93.5 ms                                                                      | 92.4 ms: 1.01x faster                                                          |
| asyncio_websockets         | 382 ms                                                                       | 378 ms: 1.01x faster                                                           |
| deepcopy                   | 341 us                                                                       | 337 us: 1.01x faster                                                           |
| logging_simple             | 7.34 us                                                                      | 7.27 us: 1.01x faster                                                          |
| sympy_expand               | 573 ms                                                                       | 568 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult    | 5.64 ms                                                                      | 5.59 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed    | 537 ms                                                                       | 533 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 918 ms                                                                       | 910 ms: 1.01x faster                                                           |
| async_tree_none_tg         | 252 ms                                                                       | 250 ms: 1.01x faster                                                           |
| pprint_pformat             | 1.90 sec                                                                     | 1.88 sec: 1.01x faster                                                         |
| sympy_integrate            | 27.3 ms                                                                      | 27.1 ms: 1.01x faster                                                          |
| richards_super             | 67.3 ms                                                                      | 66.9 ms: 1.01x faster                                                          |
| shortest_path              | 530 ms                                                                       | 527 ms: 1.01x faster                                                           |
| regex_v8                   | 25.9 ms                                                                      | 25.8 ms: 1.01x faster                                                          |
| many_optionals             | 1.13 ms                                                                      | 1.13 ms: 1.01x faster                                                          |
| pycparser                  | 1.29 sec                                                                     | 1.29 sec: 1.00x faster                                                         |
| sqlalchemy_declarative     | 176 ms                                                                       | 175 ms: 1.00x faster                                                           |
| deepcopy_reduce            | 3.68 us                                                                      | 3.66 us: 1.00x faster                                                          |
| pathlib                    | 16.5 ms                                                                      | 16.4 ms: 1.00x faster                                                          |
| coroutines                 | 22.1 ms                                                                      | 22.0 ms: 1.00x faster                                                          |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                       | 488 ms: 1.00x faster                                                           |
| pidigits                   | 249 ms                                                                       | 248 ms: 1.00x faster                                                           |
| async_generators           | 471 ms                                                                       | 470 ms: 1.00x faster                                                           |
| k_core                     | 2.40 sec                                                                     | 2.40 sec: 1.00x slower                                                         |
| dulwich_log                | 69.1 ms                                                                      | 69.3 ms: 1.00x slower                                                          |
| thrift                     | 1.03 ms                                                                      | 1.03 ms: 1.00x slower                                                          |
| json_dumps                 | 13.5 ms                                                                      | 13.6 ms: 1.00x slower                                                          |
| tomli_loads                | 2.42 sec                                                                     | 2.44 sec: 1.00x slower                                                         |
| sqlglot_normalize          | 131 ms                                                                       | 131 ms: 1.01x slower                                                           |
| fannkuch                   | 476 ms                                                                       | 479 ms: 1.01x slower                                                           |
| pyflate                    | 495 ms                                                                       | 499 ms: 1.01x slower                                                           |
| hexiom                     | 7.24 ms                                                                      | 7.31 ms: 1.01x slower                                                          |
| json                       | 5.57 ms                                                                      | 5.62 ms: 1.01x slower                                                          |
| bpe_tokeniser              | 5.23 sec                                                                     | 5.28 sec: 1.01x slower                                                         |
| json_loads                 | 27.9 us                                                                      | 28.2 us: 1.01x slower                                                          |
| nbody                      | 132 ms                                                                       | 134 ms: 1.01x slower                                                           |
| scimark_sor                | 121 ms                                                                       | 123 ms: 1.01x slower                                                           |
| meteor_contest             | 155 ms                                                                       | 156 ms: 1.01x slower                                                           |
| deepcopy_memo              | 37.0 us                                                                      | 37.4 us: 1.01x slower                                                          |
| python_startup             | 18.7 ms                                                                      | 18.9 ms: 1.01x slower                                                          |
| sqlglot_optimize           | 66.6 ms                                                                      | 67.4 ms: 1.01x slower                                                          |
| 2to3                       | 338 ms                                                                       | 342 ms: 1.01x slower                                                           |
| typing_runtime_protocols   | 220 us                                                                       | 223 us: 1.01x slower                                                           |
| python_startup_no_site     | 11.8 ms                                                                      | 12.0 ms: 1.01x slower                                                          |
| raytrace                   | 343 ms                                                                       | 348 ms: 1.01x slower                                                           |
| sqlite_synth               | 2.58 us                                                                      | 2.63 us: 1.02x slower                                                          |
| generators                 | 30.9 ms                                                                      | 31.5 ms: 1.02x slower                                                          |
| bench_mp_pool              | 48.8 ms                                                                      | 49.7 ms: 1.02x slower                                                          |
| scimark_fft                | 346 ms                                                                       | 354 ms: 1.02x slower                                                           |
| scimark_lu                 | 120 ms                                                                       | 123 ms: 1.02x slower                                                           |
| nqueens                    | 111 ms                                                                       | 116 ms: 1.04x slower                                                           |
| gc_traversal               | 4.13 ms                                                                      | 4.64 ms: 1.12x slower                                                          |
| create_gc_cycles           | 1.95 ms                                                                      | 2.40 ms: 1.23x slower                                                          |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                                   |

Benchmark hidden because not significant (24): async_tree_io_tg, bench_thread_pool, connected_components, sqlalchemy_imperative, chaos, sympy_sum, docutils, float, sympy_str, genshi_text, subparsers, logging_silent, pickle_pure_python, regex_compile, regex_dna, telco, regex_effbot, genshi_xml, pylint, richards, mako, sphinx, html5lib, comprehensions
Ignored benchmarks (4) of results/bm-20250117-3.14.0a4+-3829104-NOGIL/bm-20250117-pythonperf2-x86_64-python-3829104ab412a47bf3f3-3.14.0a4+-3829104.json: xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 89.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x