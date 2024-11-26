# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-x86_64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.294x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 427 ms: 1.50x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.42 sec: 1.19x slower                                                       |
| Geometric mean | (ref)                                                        | 1.34x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 897 ms: 1.17x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 371 ms: 1.16x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 478 ms: 1.13x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 944 ms: 1.10x faster                                                         |
| async_tree_none            | 452 ms                                                       | 414 ms: 1.09x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 644 ms: 1.08x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 514 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 680 ms: 1.02x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 249 ms: 1.06x faster                                                         |
| float          | 76.6 ms                                                      | 140 ms: 1.83x slower                                                         |
| nbody          | 88.0 ms                                                      | 179 ms: 2.04x slower                                                         |
| Geometric mean | (ref)                                                        | 1.52x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                        |
| regex_dna      | 239 ms                                                       | 250 ms: 1.05x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 27.2 ms: 1.15x slower                                                        |
| regex_compile  | 144 ms                                                       | 224 ms: 1.55x slower                                                         |
| Geometric mean | (ref)                                                        | 1.17x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.03x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                                         |
| json_loads           | 24.4 us                                                      | 28.6 us: 1.17x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 115 ms: 1.33x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 15.1 ms: 1.47x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 3.27 sec: 1.52x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 93.9 ms: 1.61x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 602 us: 1.89x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 399 us: 1.90x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.40x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 12.1 ms: 1.40x slower                                                        |
| python_startup         | 11.6 ms                                                      | 19.8 ms: 1.71x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.54x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 68.2 ms: 1.79x slower                                                        |
| mako            | 10.0 ms                                                      | 22.1 ms: 2.21x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.98x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 897 ms: 1.17x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 371 ms: 1.16x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 478 ms: 1.13x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 944 ms: 1.10x faster                                                         |
| async_tree_none            | 452 ms                                                       | 414 ms: 1.09x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 644 ms: 1.08x faster                                                         |
| pidigits                   | 265 ms                                                       | 249 ms: 1.06x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 514 ms: 1.06x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 680 ms: 1.02x faster                                                         |
| asyncio_websockets         | 387 ms                                                       | 381 ms: 1.02x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                        |
| pathlib                    | 18.9 ms                                                      | 19.6 ms: 1.04x slower                                                        |
| regex_dna                  | 239 ms                                                       | 250 ms: 1.05x slower                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.98 us: 1.07x slower                                                        |
| generators                 | 37.4 ms                                                      | 40.8 ms: 1.09x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 3.85 ms: 1.11x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 27.2 ms: 1.15x slower                                                        |
| json                       | 5.12 ms                                                      | 5.90 ms: 1.15x slower                                                        |
| coroutines                 | 23.0 ms                                                      | 26.7 ms: 1.16x slower                                                        |
| deepcopy                   | 368 us                                                       | 431 us: 1.17x slower                                                         |
| json_loads                 | 24.4 us                                                      | 28.6 us: 1.17x slower                                                        |
| scimark_fft                | 301 ms                                                       | 353 ms: 1.17x slower                                                         |
| docutils                   | 2.87 sec                                                     | 3.42 sec: 1.19x slower                                                       |
| async_generators           | 390 ms                                                       | 479 ms: 1.23x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.29 ms: 1.26x slower                                                        |
| mdp                        | 2.57 sec                                                     | 3.23 sec: 1.26x slower                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                      | 24.2 ms: 1.29x slower                                                        |
| meteor_contest             | 128 ms                                                       | 170 ms: 1.33x slower                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 115 ms: 1.33x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 32.8 ms: 1.37x slower                                                        |
| deepcopy_memo              | 36.8 us                                                      | 50.5 us: 1.37x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 89.8 ms: 1.37x slower                                                        |
| comprehensions             | 21.9 us                                                      | 30.4 us: 1.39x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 12.1 ms: 1.40x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 4.72 us: 1.40x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 128 ms: 1.42x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.76 sec: 1.42x slower                                                       |
| sqlalchemy_declarative     | 159 ms                                                       | 227 ms: 1.42x slower                                                         |
| telco                      | 6.96 ms                                                      | 10.1 ms: 1.46x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 15.1 ms: 1.47x slower                                                        |
| 2to3                       | 285 ms                                                       | 427 ms: 1.50x slower                                                         |
| sympy_str                  | 302 ms                                                       | 452 ms: 1.50x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 121 ms: 1.50x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 3.27 sec: 1.52x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 140 ms: 1.53x slower                                                         |
| regex_compile              | 144 ms                                                       | 224 ms: 1.55x slower                                                         |
| coverage                   | 66.7 ms                                                      | 106 ms: 1.59x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 185 ms: 1.60x slower                                                         |
| fannkuch                   | 350 ms                                                       | 560 ms: 1.60x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 92.4 ms: 1.61x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 93.9 ms: 1.61x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.58 ms: 1.62x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 263 ms: 1.62x slower                                                         |
| logging_format             | 7.48 us                                                      | 12.5 us: 1.67x slower                                                        |
| sympy_expand               | 484 ms                                                       | 814 ms: 1.68x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 1.36 sec: 1.68x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.60 ms: 1.69x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 2.82 sec: 1.71x slower                                                       |
| python_startup             | 11.6 ms                                                      | 19.8 ms: 1.71x slower                                                        |
| pyflate                    | 439 ms                                                       | 752 ms: 1.72x slower                                                         |
| logging_simple             | 6.71 us                                                      | 11.6 us: 1.73x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 266 us: 1.76x slower                                                         |
| richards                   | 45.7 ms                                                      | 81.2 ms: 1.77x slower                                                        |
| django_template            | 38.2 ms                                                      | 68.2 ms: 1.79x slower                                                        |
| float                      | 76.6 ms                                                      | 140 ms: 1.83x slower                                                         |
| chaos                      | 64.0 ms                                                      | 119 ms: 1.86x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 130 ms: 1.88x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 602 us: 1.89x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 3.38 ms: 1.90x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 399 us: 1.90x slower                                                         |
| richards_super             | 51.3 ms                                                      | 98.0 ms: 1.91x slower                                                        |
| go                         | 150 ms                                                       | 286 ms: 1.91x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 11.5 ms: 1.93x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 186 ns: 1.97x slower                                                         |
| raytrace                   | 298 ms                                                       | 595 ms: 2.00x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 2.79 ms: 2.03x slower                                                        |
| nbody                      | 88.0 ms                                                      | 179 ms: 2.04x slower                                                         |
| scimark_lu                 | 98.8 ms                                                      | 215 ms: 2.17x slower                                                         |
| scimark_sor                | 109 ms                                                       | 238 ms: 2.18x slower                                                         |
| mako                       | 10.0 ms                                                      | 22.1 ms: 2.21x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 8.35 ms: 2.58x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 53.6 ms: 11.25x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.46x slower                                                                 |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.294x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.29x
- 99% likely to have a slowdown of 1.25x

# Memory
- memory change: 1.24x