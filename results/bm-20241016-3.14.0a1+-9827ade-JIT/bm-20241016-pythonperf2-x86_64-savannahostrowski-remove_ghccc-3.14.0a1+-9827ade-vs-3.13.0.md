# Results vs. 3.13.0

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.003x slower
- HPT reliability: 50.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 314 ms: 1.07x slower                                                            |
| docutils       | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                                          |
| html5lib       | 72.9 ms                                                      | 70.9 ms: 1.03x faster                                                           |
| sphinx         | 1.11 sec                                                     | 1.26 sec: 1.13x slower                                                          |
| tornado_http   | 119 ms                                                       | 121 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 377 ms: 1.22x faster                                                            |
| async_tree_none            | 370 ms                                                       | 335 ms: 1.10x faster                                                            |
| async_tree_memoization     | 447 ms                                                       | 413 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 342 ms                                                       | 323 ms: 1.06x faster                                                            |
| asyncio_websockets         | 395 ms                                                       | 384 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 582 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 566 ms: 1.01x faster                                                            |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                           |
| async_tree_io              | 832 ms                                                       | 854 ms: 1.03x slower                                                            |
| async_tree_io_tg           | 823 ms                                                       | 869 ms: 1.06x slower                                                            |
| async_generators           | 364 ms                                                       | 386 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 83.5 ms: 1.10x faster                                                           |
| float          | 81.6 ms                                                      | 79.4 ms: 1.03x faster                                                           |
| pidigits       | 252 ms                                                       | 252 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 232 ms: 1.03x faster                                                            |
| regex_effbot   | 3.51 ms                                                      | 3.47 ms: 1.01x faster                                                           |
| regex_compile  | 143 ms                                                       | 148 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.11 sec: 1.16x faster                                                          |
| xml_etree_process    | 60.7 ms                                                      | 57.8 ms: 1.05x faster                                                           |
| xml_etree_generate   | 85.2 ms                                                      | 82.0 ms: 1.04x faster                                                           |
| json_loads           | 24.7 us                                                      | 24.5 us: 1.01x faster                                                           |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                            |
| xml_etree_iterparse  | 99.8 ms                                                      | 100 ms: 1.01x slower                                                            |
| unpickle_pure_python | 216 us                                                       | 219 us: 1.01x slower                                                            |
| json_dumps           | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                           |
| pickle_pure_python   | 322 us                                                       | 335 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                           |
| python_startup_no_site | 8.93 ms                                                      | 8.99 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.44 ms: 1.09x faster                                                           |
| genshi_text     | 27.2 ms                                                      | 27.9 ms: 1.03x slower                                                           |
| genshi_xml      | 58.0 ms                                                      | 61.8 ms: 1.07x slower                                                           |
| django_template | 38.9 ms                                                      | 43.3 ms: 1.11x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 29.6 us: 1.31x faster                                                           |
| deepcopy                   | 388 us                                                       | 313 us: 1.24x faster                                                            |
| async_tree_memoization_tg  | 458 ms                                                       | 377 ms: 1.22x faster                                                            |
| scimark_sor                | 125 ms                                                       | 105 ms: 1.19x faster                                                            |
| richards_super             | 60.2 ms                                                      | 51.4 ms: 1.17x faster                                                           |
| deepcopy_reduce            | 3.49 us                                                      | 3.02 us: 1.16x faster                                                           |
| tomli_loads                | 2.43 sec                                                     | 2.11 sec: 1.16x faster                                                          |
| richards                   | 52.5 ms                                                      | 45.5 ms: 1.15x faster                                                           |
| telco                      | 8.77 ms                                                      | 7.78 ms: 1.13x faster                                                           |
| async_tree_none            | 370 ms                                                       | 335 ms: 1.10x faster                                                            |
| nbody                      | 92.1 ms                                                      | 83.5 ms: 1.10x faster                                                           |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                           |
| mako                       | 10.3 ms                                                      | 9.44 ms: 1.09x faster                                                           |
| pyflate                    | 493 ms                                                       | 452 ms: 1.09x faster                                                            |
| json                       | 5.62 ms                                                      | 5.16 ms: 1.09x faster                                                           |
| go                         | 167 ms                                                       | 154 ms: 1.09x faster                                                            |
| async_tree_memoization     | 447 ms                                                       | 413 ms: 1.08x faster                                                            |
| bpe_tokeniser              | 5.09 sec                                                     | 4.77 sec: 1.07x faster                                                          |
| coverage                   | 84.5 ms                                                      | 79.8 ms: 1.06x faster                                                           |
| logging_silent             | 97.5 ns                                                      | 92.1 ns: 1.06x faster                                                           |
| async_tree_none_tg         | 342 ms                                                       | 323 ms: 1.06x faster                                                            |
| spectral_norm              | 97.4 ms                                                      | 92.5 ms: 1.05x faster                                                           |
| xml_etree_process          | 60.7 ms                                                      | 57.8 ms: 1.05x faster                                                           |
| pprint_safe_repr           | 835 ms                                                       | 796 ms: 1.05x faster                                                            |
| python_startup             | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                           |
| xml_etree_generate         | 85.2 ms                                                      | 82.0 ms: 1.04x faster                                                           |
| scimark_fft                | 298 ms                                                       | 288 ms: 1.04x faster                                                            |
| fannkuch                   | 384 ms                                                       | 371 ms: 1.04x faster                                                            |
| crypto_pyaes               | 73.5 ms                                                      | 71.1 ms: 1.03x faster                                                           |
| regex_dna                  | 238 ms                                                       | 232 ms: 1.03x faster                                                            |
| asyncio_websockets         | 395 ms                                                       | 384 ms: 1.03x faster                                                            |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                                          |
| html5lib                   | 72.9 ms                                                      | 70.9 ms: 1.03x faster                                                           |
| float                      | 81.6 ms                                                      | 79.4 ms: 1.03x faster                                                           |
| thrift                     | 918 us                                                       | 894 us: 1.03x faster                                                            |
| deltablue                  | 3.38 ms                                                      | 3.30 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 582 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 566 ms: 1.01x faster                                                            |
| dulwich_log                | 65.5 ms                                                      | 64.6 ms: 1.01x faster                                                           |
| regex_effbot               | 3.51 ms                                                      | 3.47 ms: 1.01x faster                                                           |
| json_loads                 | 24.7 us                                                      | 24.5 us: 1.01x faster                                                           |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                            |
| pidigits                   | 252 ms                                                       | 252 ms: 1.00x faster                                                            |
| xml_etree_iterparse        | 99.8 ms                                                      | 100 ms: 1.01x slower                                                            |
| python_startup_no_site     | 8.93 ms                                                      | 8.99 ms: 1.01x slower                                                           |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                           |
| unpickle_pure_python       | 216 us                                                       | 219 us: 1.01x slower                                                            |
| pycparser                  | 1.28 sec                                                     | 1.30 sec: 1.01x slower                                                          |
| json_dumps                 | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                           |
| tornado_http               | 119 ms                                                       | 121 ms: 1.02x slower                                                            |
| meteor_contest             | 130 ms                                                       | 133 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 176 us                                                       | 180 us: 1.02x slower                                                            |
| genshi_text                | 27.2 ms                                                      | 27.9 ms: 1.03x slower                                                           |
| async_tree_io              | 832 ms                                                       | 854 ms: 1.03x slower                                                            |
| mdp                        | 2.53 sec                                                     | 2.60 sec: 1.03x slower                                                          |
| bench_thread_pool          | 929 us                                                       | 958 us: 1.03x slower                                                            |
| regex_compile              | 143 ms                                                       | 148 ms: 1.04x slower                                                            |
| logging_format             | 6.95 us                                                      | 7.22 us: 1.04x slower                                                           |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.38 ms: 1.04x slower                                                           |
| pickle_pure_python         | 322 us                                                       | 335 us: 1.04x slower                                                            |
| logging_simple             | 6.28 us                                                      | 6.59 us: 1.05x slower                                                           |
| sympy_expand               | 506 ms                                                       | 534 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 823 ms                                                       | 869 ms: 1.06x slower                                                            |
| async_generators           | 364 ms                                                       | 386 ms: 1.06x slower                                                            |
| genshi_xml                 | 58.0 ms                                                      | 61.8 ms: 1.07x slower                                                           |
| 2to3                       | 293 ms                                                       | 314 ms: 1.07x slower                                                            |
| comprehensions             | 17.3 us                                                      | 18.6 us: 1.08x slower                                                           |
| sympy_str                  | 297 ms                                                       | 319 ms: 1.08x slower                                                            |
| scimark_monte_carlo        | 65.2 ms                                                      | 70.2 ms: 1.08x slower                                                           |
| hexiom                     | 6.47 ms                                                      | 7.06 ms: 1.09x slower                                                           |
| create_gc_cycles           | 2.65 ms                                                      | 2.90 ms: 1.09x slower                                                           |
| chaos                      | 60.6 ms                                                      | 66.4 ms: 1.10x slower                                                           |
| sqlglot_parse              | 1.37 ms                                                      | 1.51 ms: 1.10x slower                                                           |
| nqueens                    | 92.3 ms                                                      | 102 ms: 1.11x slower                                                            |
| sqlglot_normalize          | 119 ms                                                       | 132 ms: 1.11x slower                                                            |
| django_template            | 38.9 ms                                                      | 43.3 ms: 1.11x slower                                                           |
| generators                 | 33.9 ms                                                      | 38.1 ms: 1.12x slower                                                           |
| sqlglot_transpile          | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                           |
| sympy_sum                  | 154 ms                                                       | 174 ms: 1.13x slower                                                            |
| sphinx                     | 1.11 sec                                                     | 1.26 sec: 1.13x slower                                                          |
| docutils                   | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                                          |
| sympy_integrate            | 23.4 ms                                                      | 27.2 ms: 1.16x slower                                                           |
| sqlglot_optimize           | 58.7 ms                                                      | 69.5 ms: 1.19x slower                                                           |
| raytrace                   | 267 ms                                                       | 324 ms: 1.21x slower                                                            |
| gc_traversal               | 4.48 ms                                                      | 5.48 ms: 1.22x slower                                                           |
| pylint                     | 345 ms                                                       | 424 ms: 1.23x slower                                                            |
| bench_mp_pool              | 4.82 ms                                                      | 1.98 sec: 410.98x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                                    |

Benchmark hidden because not significant (2): scimark_lu, regex_v8
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.003x slower
# HPT report

- Reliability score: 50.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x