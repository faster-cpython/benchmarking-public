# Results vs. 3.12.0

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.08x slower
- HPT reliability: 73.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 314 ms: 1.10x slower                                                            |
| docutils       | 2.87 sec                                                     | 3.19 sec: 1.11x slower                                                          |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 377 ms: 1.43x faster                                                            |
| async_tree_none            | 452 ms                                                       | 335 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 323 ms: 1.33x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 413 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 566 ms: 1.23x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 854 ms: 1.22x faster                                                            |
| async_tree_io_tg           | 1.05 sec                                                     | 869 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 582 ms: 1.20x faster                                                            |
| Geometric mean             | (ref)                                                        | 1.28x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                           |
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                            |
| float          | 76.6 ms                                                      | 79.4 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.47 ms: 1.03x faster                                                           |
| regex_dna      | 239 ms                                                       | 232 ms: 1.03x faster                                                            |
| regex_compile  | 144 ms                                                       | 148 ms: 1.03x slower                                                            |
| regex_v8       | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.0 ms: 1.05x faster                                                           |
| tomli_loads          | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                          |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.02x faster                                                            |
| xml_etree_process    | 58.4 ms                                                      | 57.8 ms: 1.01x faster                                                           |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.01x faster                                                            |
| json_loads           | 24.4 us                                                      | 24.5 us: 1.01x slower                                                           |
| unpickle             | 14.8 us                                                      | 15.0 us: 1.01x slower                                                           |
| unpickle_list        | 4.66 us                                                      | 4.76 us: 1.02x slower                                                           |
| pickle_dict          | 32.5 us                                                      | 33.3 us: 1.02x slower                                                           |
| pickle               | 10.5 us                                                      | 10.8 us: 1.03x slower                                                           |
| unpickle_pure_python | 210 us                                                       | 219 us: 1.05x slower                                                            |
| pickle_list          | 4.43 us                                                      | 4.64 us: 1.05x slower                                                           |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                            |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                           |
| python_startup         | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.44 ms: 1.06x faster                                                           |
| django_template | 38.2 ms                                                      | 43.3 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 377 ms: 1.43x faster                                                            |
| async_tree_none            | 452 ms                                                       | 335 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 431 ms                                                       | 323 ms: 1.33x faster                                                            |
| async_tree_memoization     | 544 ms                                                       | 413 ms: 1.32x faster                                                            |
| deepcopy_memo              | 36.8 us                                                      | 29.6 us: 1.24x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 566 ms: 1.23x faster                                                            |
| async_tree_io              | 1.04 sec                                                     | 854 ms: 1.22x faster                                                            |
| async_tree_io_tg           | 1.05 sec                                                     | 869 ms: 1.21x faster                                                            |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 582 ms: 1.20x faster                                                            |
| comprehensions             | 21.9 us                                                      | 18.6 us: 1.18x faster                                                           |
| deepcopy                   | 368 us                                                       | 313 us: 1.18x faster                                                            |
| crypto_pyaes               | 80.3 ms                                                      | 71.1 ms: 1.13x faster                                                           |
| deepcopy_reduce            | 3.37 us                                                      | 3.02 us: 1.12x faster                                                           |
| mako                       | 10.0 ms                                                      | 9.44 ms: 1.06x faster                                                           |
| nbody                      | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                           |
| coroutines                 | 23.0 ms                                                      | 21.8 ms: 1.05x faster                                                           |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                            |
| xml_etree_generate         | 86.1 ms                                                      | 82.0 ms: 1.05x faster                                                           |
| scimark_fft                | 301 ms                                                       | 288 ms: 1.05x faster                                                            |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                                            |
| logging_format             | 7.48 us                                                      | 7.22 us: 1.04x faster                                                           |
| regex_effbot               | 3.57 ms                                                      | 3.47 ms: 1.03x faster                                                           |
| regex_dna                  | 239 ms                                                       | 232 ms: 1.03x faster                                                            |
| logging_silent             | 94.4 ns                                                      | 92.1 ns: 1.02x faster                                                           |
| tomli_loads                | 2.16 sec                                                     | 2.11 sec: 1.02x faster                                                          |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.77 us                                                      | 2.71 us: 1.02x faster                                                           |
| logging_simple             | 6.71 us                                                      | 6.59 us: 1.02x faster                                                           |
| scimark_lu                 | 98.8 ms                                                      | 97.1 ms: 1.02x faster                                                           |
| pprint_safe_repr           | 807 ms                                                       | 796 ms: 1.01x faster                                                            |
| dulwich_log                | 65.4 ms                                                      | 64.6 ms: 1.01x faster                                                           |
| async_generators           | 390 ms                                                       | 386 ms: 1.01x faster                                                            |
| xml_etree_process          | 58.4 ms                                                      | 57.8 ms: 1.01x faster                                                           |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                            |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                            |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                          |
| json_loads                 | 24.4 us                                                      | 24.5 us: 1.01x slower                                                           |
| json                       | 5.12 ms                                                      | 5.16 ms: 1.01x slower                                                           |
| spectral_norm              | 91.6 ms                                                      | 92.5 ms: 1.01x slower                                                           |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                          |
| unpickle                   | 14.8 us                                                      | 15.0 us: 1.01x slower                                                           |
| generators                 | 37.4 ms                                                      | 38.1 ms: 1.02x slower                                                           |
| scimark_monte_carlo        | 69.0 ms                                                      | 70.2 ms: 1.02x slower                                                           |
| deltablue                  | 3.24 ms                                                      | 3.30 ms: 1.02x slower                                                           |
| unpickle_list              | 4.66 us                                                      | 4.76 us: 1.02x slower                                                           |
| pickle_dict                | 32.5 us                                                      | 33.3 us: 1.02x slower                                                           |
| pickle                     | 10.5 us                                                      | 10.8 us: 1.03x slower                                                           |
| go                         | 150 ms                                                       | 154 ms: 1.03x slower                                                            |
| regex_compile              | 144 ms                                                       | 148 ms: 1.03x slower                                                            |
| pyflate                    | 439 ms                                                       | 452 ms: 1.03x slower                                                            |
| float                      | 76.6 ms                                                      | 79.4 ms: 1.04x slower                                                           |
| chaos                      | 64.0 ms                                                      | 66.4 ms: 1.04x slower                                                           |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.04x slower                                                            |
| python_startup_no_site     | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                           |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.38 ms: 1.04x slower                                                           |
| unpickle_pure_python       | 210 us                                                       | 219 us: 1.05x slower                                                            |
| pickle_list                | 4.43 us                                                      | 4.64 us: 1.05x slower                                                           |
| pycparser                  | 1.23 sec                                                     | 1.30 sec: 1.05x slower                                                          |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                            |
| regex_v8                   | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                                           |
| sympy_str                  | 302 ms                                                       | 319 ms: 1.06x slower                                                            |
| fannkuch                   | 350 ms                                                       | 371 ms: 1.06x slower                                                            |
| sympy_sum                  | 162 ms                                                       | 174 ms: 1.07x slower                                                            |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.08x slower                                                           |
| raytrace                   | 298 ms                                                       | 324 ms: 1.09x slower                                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.51 ms: 1.09x slower                                                           |
| 2to3                       | 285 ms                                                       | 314 ms: 1.10x slower                                                            |
| sympy_expand               | 484 ms                                                       | 534 ms: 1.10x slower                                                            |
| docutils                   | 2.87 sec                                                     | 3.19 sec: 1.11x slower                                                          |
| telco                      | 6.96 ms                                                      | 7.78 ms: 1.12x slower                                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 1.99 ms: 1.12x slower                                                           |
| django_template            | 38.2 ms                                                      | 43.3 ms: 1.13x slower                                                           |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.14x slower                                                            |
| sympy_integrate            | 23.9 ms                                                      | 27.2 ms: 1.14x slower                                                           |
| sqlglot_normalize          | 116 ms                                                       | 132 ms: 1.14x slower                                                            |
| hexiom                     | 5.96 ms                                                      | 7.06 ms: 1.19x slower                                                           |
| typing_runtime_protocols   | 152 us                                                       | 180 us: 1.19x slower                                                            |
| coverage                   | 66.7 ms                                                      | 79.8 ms: 1.20x slower                                                           |
| sqlglot_optimize           | 57.5 ms                                                      | 69.5 ms: 1.21x slower                                                           |
| python_startup             | 11.6 ms                                                      | 14.9 ms: 1.28x slower                                                           |
| gc_traversal               | 3.48 ms                                                      | 5.48 ms: 1.58x slower                                                           |
| unpack_sequence            | 53.2 ns                                                      | 88.4 ns: 1.66x slower                                                           |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                                           |
| bench_mp_pool              | 4.76 ms                                                      | 1.98 sec: 415.63x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                    |

Benchmark hidden because not significant (5): richards, pprint_pformat, richards_super, tornado_http, bench_thread_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 73.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x