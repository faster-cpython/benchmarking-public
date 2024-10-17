# Results vs. base

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.01x faster
- HPT reliability: 64.31%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 3.20 sec                                                                     | 3.19 sec: 1.00x faster                                                          |
| html5lib       | 69.9 ms                                                                      | 70.9 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): 2to3, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets         | 387 ms                                                                       | 384 ms: 1.01x faster                                                            |
| async_tree_io_tg           | 873 ms                                                                       | 869 ms: 1.01x faster                                                            |
| async_tree_none            | 333 ms                                                                       | 335 ms: 1.01x slower                                                            |
| coroutines                 | 21.7 ms                                                                      | 21.8 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 561 ms                                                                       | 566 ms: 1.01x slower                                                            |
| async_tree_io              | 846 ms                                                                       | 854 ms: 1.01x slower                                                            |
| async_generators           | 380 ms                                                                       | 386 ms: 1.02x slower                                                            |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                                    |

Benchmark hidden because not significant (6): async_tree_memoization_tg, asyncio_tcp, async_tree_memoization, asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.8 ms                                                                      | 79.4 ms: 1.00x faster                                                           |
| pidigits       | 252 ms                                                                       | 252 ms: 1.00x faster                                                            |
| nbody          | 81.9 ms                                                                      | 83.5 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 243 ms                                                                       | 232 ms: 1.05x faster                                                            |
| regex_effbot   | 3.44 ms                                                                      | 3.47 ms: 1.01x slower                                                           |
| regex_compile  | 147 ms                                                                       | 148 ms: 1.01x slower                                                            |
| regex_v8       | 24.6 ms                                                                      | 25.0 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 149 ms                                                                       | 143 ms: 1.04x faster                                                            |
| pickle_list          | 4.76 us                                                                      | 4.64 us: 1.02x faster                                                           |
| pickle_dict          | 34.0 us                                                                      | 33.3 us: 1.02x faster                                                           |
| json_dumps           | 11.2 ms                                                                      | 11.0 ms: 1.02x faster                                                           |
| unpickle             | 15.3 us                                                                      | 15.0 us: 1.02x faster                                                           |
| tomli_loads          | 2.13 sec                                                                     | 2.11 sec: 1.01x faster                                                          |
| unpickle_pure_python | 220 us                                                                       | 219 us: 1.01x faster                                                            |
| pickle_pure_python   | 330 us                                                                       | 335 us: 1.01x slower                                                            |
| pickle               | 10.5 us                                                                      | 10.8 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                                    |

Benchmark hidden because not significant (5): unpickle_list, json_loads, xml_etree_process, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 9.02 ms                                                                      | 8.99 ms: 1.00x faster                                                           |
| python_startup         | 15.0 ms                                                                      | 14.9 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                        | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml     | 62.6 ms                                                                      | 61.8 ms: 1.01x faster                                                           |
| mako           | 9.46 ms                                                                      | 9.44 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241016-pythonperf2-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| bench_mp_pool              | 3.28 sec                                                                     | 1.98 sec: 1.66x faster                                                          |
| deepcopy_memo              | 31.3 us                                                                      | 29.6 us: 1.06x faster                                                           |
| regex_dna                  | 243 ms                                                                       | 232 ms: 1.05x faster                                                            |
| xml_etree_parse            | 149 ms                                                                       | 143 ms: 1.04x faster                                                            |
| chaos                      | 69.1 ms                                                                      | 66.4 ms: 1.04x faster                                                           |
| unpack_sequence            | 91.0 ns                                                                      | 88.4 ns: 1.03x faster                                                           |
| richards_super             | 53.0 ms                                                                      | 51.4 ms: 1.03x faster                                                           |
| pickle_list                | 4.76 us                                                                      | 4.64 us: 1.02x faster                                                           |
| pickle_dict                | 34.0 us                                                                      | 33.3 us: 1.02x faster                                                           |
| json_dumps                 | 11.2 ms                                                                      | 11.0 ms: 1.02x faster                                                           |
| unpickle                   | 15.3 us                                                                      | 15.0 us: 1.02x faster                                                           |
| dulwich_log                | 65.7 ms                                                                      | 64.6 ms: 1.02x faster                                                           |
| typing_runtime_protocols   | 183 us                                                                       | 180 us: 1.02x faster                                                            |
| telco                      | 7.90 ms                                                                      | 7.78 ms: 1.02x faster                                                           |
| generators                 | 38.6 ms                                                                      | 38.1 ms: 1.01x faster                                                           |
| mdp                        | 2.64 sec                                                                     | 2.60 sec: 1.01x faster                                                          |
| genshi_xml                 | 62.6 ms                                                                      | 61.8 ms: 1.01x faster                                                           |
| raytrace                   | 327 ms                                                                       | 324 ms: 1.01x faster                                                            |
| tomli_loads                | 2.13 sec                                                                     | 2.11 sec: 1.01x faster                                                          |
| asyncio_websockets         | 387 ms                                                                       | 384 ms: 1.01x faster                                                            |
| sqlglot_normalize          | 132 ms                                                                       | 132 ms: 1.01x faster                                                            |
| crypto_pyaes               | 71.5 ms                                                                      | 71.1 ms: 1.01x faster                                                           |
| spectral_norm              | 93.1 ms                                                                      | 92.5 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 873 ms                                                                       | 869 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 220 us                                                                       | 219 us: 1.01x faster                                                            |
| float                      | 79.8 ms                                                                      | 79.4 ms: 1.00x faster                                                           |
| python_startup_no_site     | 9.02 ms                                                                      | 8.99 ms: 1.00x faster                                                           |
| pyflate                    | 453 ms                                                                       | 452 ms: 1.00x faster                                                            |
| python_startup             | 15.0 ms                                                                      | 14.9 ms: 1.00x faster                                                           |
| docutils                   | 3.20 sec                                                                     | 3.19 sec: 1.00x faster                                                          |
| mako                       | 9.46 ms                                                                      | 9.44 ms: 1.00x faster                                                           |
| meteor_contest             | 134 ms                                                                       | 133 ms: 1.00x faster                                                            |
| pidigits                   | 252 ms                                                                       | 252 ms: 1.00x faster                                                            |
| sympy_str                  | 318 ms                                                                       | 319 ms: 1.00x slower                                                            |
| sympy_expand               | 532 ms                                                                       | 534 ms: 1.00x slower                                                            |
| pycparser                  | 1.29 sec                                                                     | 1.30 sec: 1.01x slower                                                          |
| async_tree_none            | 333 ms                                                                       | 335 ms: 1.01x slower                                                            |
| sqlglot_transpile          | 1.97 ms                                                                      | 1.99 ms: 1.01x slower                                                           |
| coroutines                 | 21.7 ms                                                                      | 21.8 ms: 1.01x slower                                                           |
| thrift                     | 887 us                                                                       | 894 us: 1.01x slower                                                            |
| logging_silent             | 91.4 ns                                                                      | 92.1 ns: 1.01x slower                                                           |
| regex_effbot               | 3.44 ms                                                                      | 3.47 ms: 1.01x slower                                                           |
| pprint_safe_repr           | 790 ms                                                                       | 796 ms: 1.01x slower                                                            |
| regex_compile              | 147 ms                                                                       | 148 ms: 1.01x slower                                                            |
| create_gc_cycles           | 2.87 ms                                                                      | 2.90 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 561 ms                                                                       | 566 ms: 1.01x slower                                                            |
| async_tree_io              | 846 ms                                                                       | 854 ms: 1.01x slower                                                            |
| bpe_tokeniser              | 4.72 sec                                                                     | 4.77 sec: 1.01x slower                                                          |
| deepcopy                   | 308 us                                                                       | 313 us: 1.01x slower                                                            |
| regex_v8                   | 24.6 ms                                                                      | 25.0 ms: 1.01x slower                                                           |
| pprint_pformat             | 1.63 sec                                                                     | 1.65 sec: 1.01x slower                                                          |
| richards                   | 44.8 ms                                                                      | 45.5 ms: 1.01x slower                                                           |
| pickle_pure_python         | 330 us                                                                       | 335 us: 1.01x slower                                                            |
| html5lib                   | 69.9 ms                                                                      | 70.9 ms: 1.01x slower                                                           |
| scimark_sor                | 103 ms                                                                       | 105 ms: 1.02x slower                                                            |
| async_generators           | 380 ms                                                                       | 386 ms: 1.02x slower                                                            |
| go                         | 151 ms                                                                       | 154 ms: 1.02x slower                                                            |
| json                       | 5.07 ms                                                                      | 5.16 ms: 1.02x slower                                                           |
| scimark_fft                | 282 ms                                                                       | 288 ms: 1.02x slower                                                            |
| nbody                      | 81.9 ms                                                                      | 83.5 ms: 1.02x slower                                                           |
| scimark_lu                 | 95.1 ms                                                                      | 97.1 ms: 1.02x slower                                                           |
| pickle                     | 10.5 us                                                                      | 10.8 us: 1.03x slower                                                           |
| scimark_monte_carlo        | 68.2 ms                                                                      | 70.2 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                                    |

Benchmark hidden because not significant (35): deepcopy_reduce, tornado_http, sphinx, unpickle_list, coverage, async_tree_memoization_tg, json_loads, genshi_text, xml_etree_process, django_template, deltablue, logging_format, bench_thread_pool, asyncio_tcp, 2to3, sympy_integrate, gc_traversal, fannkuch, sqlglot_optimize, pylint, async_tree_memoization, logging_simple, hexiom, nqueens, asyncio_tcp_ssl, sympy_sum, xml_etree_generate, sqlite_synth, pathlib, scimark_sparse_mat_mult, async_tree_none_tg, comprehensions, xml_etree_iterparse, sqlglot_parse, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 64.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x