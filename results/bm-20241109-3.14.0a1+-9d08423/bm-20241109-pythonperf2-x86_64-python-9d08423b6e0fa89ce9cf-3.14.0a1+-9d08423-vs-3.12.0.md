# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-x86_64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.013x faster
- HPT reliability: 94.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 376 ms: 1.44x faster                                                         |
| async_tree_none            | 452 ms                                                       | 329 ms: 1.37x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 406 ms: 1.34x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 324 ms: 1.33x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 847 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 872 ms: 1.21x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 90.4 ms: 1.03x slower                                                        |
| float          | 76.6 ms                                                      | 82.6 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 24.8 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 84.5 ms: 1.02x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                         |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                         |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                         |
| xml_etree_process    | 58.4 ms                                                      | 60.8 ms: 1.04x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 332 us: 1.04x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.55 sec: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 15.9 ms: 1.36x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.9 ms: 1.05x slower                                                        |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 376 ms: 1.44x faster                                                         |
| async_tree_none            | 452 ms                                                       | 329 ms: 1.37x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 406 ms: 1.34x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 324 ms: 1.33x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.3 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 291 us: 1.27x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.2 us: 1.26x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 847 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 872 ms: 1.21x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.01 us: 1.12x faster                                                        |
| go                         | 150 ms                                                       | 136 ms: 1.10x faster                                                         |
| async_generators           | 390 ms                                                       | 357 ms: 1.09x faster                                                         |
| raytrace                   | 298 ms                                                       | 276 ms: 1.08x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.08x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.1 ms: 1.08x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.99 us: 1.07x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 75.2 ms: 1.07x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 899 us: 1.06x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.39 us: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.48 sec: 1.04x faster                                                       |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                         |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.03x faster                                                         |
| scimark_fft                | 301 ms                                                       | 293 ms: 1.03x faster                                                         |
| nqueens                    | 89.9 ms                                                      | 87.5 ms: 1.03x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                         |
| chaos                      | 64.0 ms                                                      | 62.5 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 84.5 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 794 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.5 ms: 1.02x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 98.1 ms: 1.01x faster                                                        |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.25 ms: 1.01x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                        |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 58.8 ms: 1.02x slower                                                        |
| fannkuch                   | 350 ms                                                       | 359 ms: 1.03x slower                                                         |
| nbody                      | 88.0 ms                                                      | 90.4 ms: 1.03x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 67.4 ms: 1.03x slower                                                        |
| sympy_expand               | 484 ms                                                       | 501 ms: 1.03x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 60.8 ms: 1.04x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 332 us: 1.04x slower                                                         |
| django_template            | 38.2 ms                                                      | 39.9 ms: 1.05x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 24.8 ms: 1.05x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 96.4 ms: 1.05x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.30 ms: 1.06x slower                                                        |
| scimark_sor                | 109 ms                                                       | 115 ms: 1.06x slower                                                         |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| float                      | 76.6 ms                                                      | 82.6 ms: 1.08x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 103 ns: 1.09x slower                                                         |
| pyflate                    | 439 ms                                                       | 478 ms: 1.09x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.54 ms: 1.09x slower                                                        |
| richards_super             | 51.3 ms                                                      | 56.7 ms: 1.10x slower                                                        |
| richards                   | 45.7 ms                                                      | 50.6 ms: 1.11x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.95 ms: 1.14x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.55 sec: 1.18x slower                                                       |
| coverage                   | 66.7 ms                                                      | 81.2 ms: 1.22x slower                                                        |
| python_startup             | 11.6 ms                                                      | 15.9 ms: 1.36x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.80 ms: 1.67x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 3.02 ms: 1.90x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 2.16 sec: 453.47x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                 |

Benchmark hidden because not significant (2): regex_effbot, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.013x faster
# HPT report

- Reliability score: 94.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x