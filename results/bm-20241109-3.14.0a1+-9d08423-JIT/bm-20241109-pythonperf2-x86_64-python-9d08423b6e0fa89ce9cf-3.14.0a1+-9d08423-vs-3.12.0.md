# Results vs. 3.12.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-x86_64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.010x slower
- HPT reliability: 84.42%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 319 ms: 1.12x slower                                                         |
| docutils       | 2.87 sec                                                     | 3.19 sec: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 372 ms: 1.45x faster                                                         |
| async_tree_none            | 452 ms                                                       | 336 ms: 1.35x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 321 ms: 1.34x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 409 ms: 1.33x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 827 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 556 ms: 1.25x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 861 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 579 ms: 1.20x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 82.8 ms: 1.06x faster                                                        |
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                         |
| float          | 76.6 ms                                                      | 79.4 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.59 ms: 1.00x slower                                                        |
| regex_compile  | 144 ms                                                       | 149 ms: 1.04x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 80.9 ms: 1.07x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.02x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 57.5 ms: 1.01x faster                                                        |
| json_loads           | 24.4 us                                                      | 24.2 us: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 218 us: 1.04x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 342 us: 1.07x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 15.8 ms: 1.36x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.24 ms: 1.08x faster                                                        |
| django_template | 38.2 ms                                                      | 42.4 ms: 1.11x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 372 ms: 1.45x faster                                                         |
| async_tree_none            | 452 ms                                                       | 336 ms: 1.35x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 321 ms: 1.34x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 409 ms: 1.33x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 827 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 556 ms: 1.25x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 861 ms: 1.22x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 30.1 us: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 579 ms: 1.20x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                        |
| deepcopy                   | 368 us                                                       | 309 us: 1.19x faster                                                         |
| comprehensions             | 21.9 us                                                      | 19.8 us: 1.11x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.05 us: 1.10x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.5 ms: 1.09x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.24 ms: 1.08x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 80.9 ms: 1.07x faster                                                        |
| nbody                      | 88.0 ms                                                      | 82.8 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.12 us: 1.05x faster                                                        |
| richards                   | 45.7 ms                                                      | 44.3 ms: 1.03x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.54 us: 1.03x faster                                                        |
| logging_silent             | 94.4 ns                                                      | 92.0 ns: 1.03x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.02x faster                                                         |
| scimark_sor                | 109 ms                                                       | 107 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.72 us: 1.02x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 97.0 ms: 1.02x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 57.5 ms: 1.01x faster                                                        |
| scimark_fft                | 301 ms                                                       | 297 ms: 1.01x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 64.6 ms: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 800 ms: 1.01x faster                                                         |
| json_loads                 | 24.4 us                                                      | 24.2 us: 1.01x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.58 sec: 1.00x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 69.2 ms: 1.00x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.59 ms: 1.00x slower                                                        |
| richards_super             | 51.3 ms                                                      | 51.8 ms: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.29 ms: 1.02x slower                                                        |
| async_generators           | 390 ms                                                       | 398 ms: 1.02x slower                                                         |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                                         |
| spectral_norm              | 91.6 ms                                                      | 94.7 ms: 1.03x slower                                                        |
| go                         | 150 ms                                                       | 155 ms: 1.03x slower                                                         |
| float                      | 76.6 ms                                                      | 79.4 ms: 1.04x slower                                                        |
| regex_compile              | 144 ms                                                       | 149 ms: 1.04x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 218 us: 1.04x slower                                                         |
| chaos                      | 64.0 ms                                                      | 66.7 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| generators                 | 37.4 ms                                                      | 39.1 ms: 1.04x slower                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 167 ms: 1.05x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.30 sec: 1.05x slower                                                       |
| sympy_str                  | 302 ms                                                       | 321 ms: 1.06x slower                                                         |
| pyflate                    | 439 ms                                                       | 466 ms: 1.06x slower                                                         |
| fannkuch                   | 350 ms                                                       | 372 ms: 1.06x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 342 us: 1.07x slower                                                         |
| sympy_sum                  | 162 ms                                                       | 174 ms: 1.07x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.54 ms: 1.08x slower                                                        |
| raytrace                   | 298 ms                                                       | 323 ms: 1.09x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                        |
| sympy_expand               | 484 ms                                                       | 530 ms: 1.10x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.63 ms: 1.10x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.51 ms: 1.10x slower                                                        |
| django_template            | 38.2 ms                                                      | 42.4 ms: 1.11x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.19 sec: 1.11x slower                                                       |
| 2to3                       | 285 ms                                                       | 319 ms: 1.12x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.99 ms: 1.12x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 27.3 ms: 1.14x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 132 ms: 1.14x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 103 ms: 1.15x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 68.6 ms: 1.19x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.17 ms: 1.20x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 183 us: 1.21x slower                                                         |
| coverage                   | 66.7 ms                                                      | 81.7 ms: 1.22x slower                                                        |
| python_startup             | 11.6 ms                                                      | 15.8 ms: 1.36x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 5.21 ms: 1.50x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.88 ms: 1.81x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 2.44 sec: 512.74x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (4): sqlalchemy_imperative, pprint_pformat, json, bench_thread_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.010x slower
# HPT report

- Reliability score: 84.42% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x