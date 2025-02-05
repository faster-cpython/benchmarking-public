# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-x86_64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.095x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 427 ms: 1.22x slower                                                         |
| docutils       | 3.41 sec                                                     | 3.42 sec: 1.00x slower                                                       |
| html5lib       | 94.6 ms                                                      | 104 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 944 ms: 1.69x faster                                                         |
| async_tree_none         | 692 ms                                                       | 414 ms: 1.67x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 514 ms: 1.59x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 680 ms: 1.38x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.58x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                         |
| float          | 111 ms                                                       | 140 ms: 1.26x slower                                                         |
| nbody          | 134 ms                                                       | 179 ms: 1.34x slower                                                         |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 250 ms: 1.05x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 27.2 ms: 1.00x slower                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                        |
| regex_compile  | 190 ms                                                       | 224 ms: 1.18x slower                                                         |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                         |
| json_loads           | 30.3 us                                                      | 28.6 us: 1.06x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 15.1 ms: 1.04x slower                                                        |
| tomli_loads          | 2.92 sec                                                     | 3.27 sec: 1.12x slower                                                       |
| xml_etree_process    | 75.9 ms                                                      | 93.9 ms: 1.24x slower                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 115 ms: 1.24x slower                                                         |
| unpickle_pure_python | 312 us                                                       | 399 us: 1.28x slower                                                         |
| pickle_pure_python   | 455 us                                                       | 602 us: 1.32x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.11x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 12.1 ms: 1.65x slower                                                        |
| python_startup         | 11.5 ms                                                      | 19.8 ms: 1.72x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.69x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                      | 80.8 ms: 1.28x slower                                                        |
| genshi_text     | 31.4 ms                                                      | 41.8 ms: 1.33x slower                                                        |
| django_template | 50.2 ms                                                      | 68.2 ms: 1.36x slower                                                        |
| mako            | 14.7 ms                                                      | 22.1 ms: 1.50x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.36x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 266 us: 2.01x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 944 ms: 1.69x faster                                                         |
| async_tree_none          | 692 ms                                                       | 414 ms: 1.67x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 514 ms: 1.59x faster                                                         |
| generators               | 57.3 ms                                                      | 40.8 ms: 1.40x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 680 ms: 1.38x faster                                                         |
| pylint                   | 566 ms                                                       | 434 ms: 1.30x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                         |
| coroutines               | 30.3 ms                                                      | 26.7 ms: 1.13x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 19.6 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                         |
| deepcopy                 | 468 us                                                       | 431 us: 1.09x faster                                                         |
| json_loads               | 30.3 us                                                      | 28.6 us: 1.06x faster                                                        |
| regex_dna                | 261 ms                                                       | 250 ms: 1.05x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.02x faster                                                         |
| scimark_fft              | 361 ms                                                       | 353 ms: 1.02x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 27.2 ms: 1.00x slower                                                        |
| docutils                 | 3.41 sec                                                     | 3.42 sec: 1.00x slower                                                       |
| json                     | 5.86 ms                                                      | 5.90 ms: 1.01x slower                                                        |
| spectral_norm            | 139 ms                                                       | 140 ms: 1.01x slower                                                         |
| crypto_pyaes             | 119 ms                                                       | 121 ms: 1.01x slower                                                         |
| deepcopy_memo            | 49.8 us                                                      | 50.5 us: 1.01x slower                                                        |
| pyflate                  | 733 ms                                                       | 752 ms: 1.03x slower                                                         |
| json_dumps               | 14.5 ms                                                      | 15.1 ms: 1.04x slower                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.29 ms: 1.04x slower                                                        |
| pycparser                | 1.67 sec                                                     | 1.76 sec: 1.05x slower                                                       |
| sqlalchemy_imperative    | 22.7 ms                                                      | 24.2 ms: 1.06x slower                                                        |
| mdp                      | 3.01 sec                                                     | 3.23 sec: 1.08x slower                                                       |
| richards_super           | 90.6 ms                                                      | 98.0 ms: 1.08x slower                                                        |
| richards                 | 75.1 ms                                                      | 81.2 ms: 1.08x slower                                                        |
| go                       | 262 ms                                                       | 286 ms: 1.09x slower                                                         |
| chaos                    | 109 ms                                                       | 119 ms: 1.10x slower                                                         |
| html5lib                 | 94.6 ms                                                      | 104 ms: 1.10x slower                                                         |
| dulwich_log              | 81.1 ms                                                      | 89.8 ms: 1.11x slower                                                        |
| nqueens                  | 115 ms                                                       | 128 ms: 1.11x slower                                                         |
| logging_silent           | 167 ns                                                       | 186 ns: 1.11x slower                                                         |
| deltablue                | 7.50 ms                                                      | 8.35 ms: 1.11x slower                                                        |
| tomli_loads              | 2.92 sec                                                     | 3.27 sec: 1.12x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 3.85 ms: 1.13x slower                                                        |
| async_generators         | 421 ms                                                       | 479 ms: 1.14x slower                                                         |
| comprehensions           | 26.7 us                                                      | 30.4 us: 1.14x slower                                                        |
| fannkuch                 | 483 ms                                                       | 560 ms: 1.16x slower                                                         |
| sympy_integrate          | 28.2 ms                                                      | 32.8 ms: 1.17x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 4.72 us: 1.18x slower                                                        |
| regex_compile            | 190 ms                                                       | 224 ms: 1.18x slower                                                         |
| thrift                   | 1.18 ms                                                      | 1.39 ms: 1.18x slower                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 227 ms: 1.20x slower                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 130 ms: 1.21x slower                                                         |
| raytrace                 | 489 ms                                                       | 595 ms: 1.22x slower                                                         |
| 2to3                     | 350 ms                                                       | 427 ms: 1.22x slower                                                         |
| hexiom                   | 9.42 ms                                                      | 11.5 ms: 1.22x slower                                                        |
| meteor_contest           | 138 ms                                                       | 170 ms: 1.23x slower                                                         |
| xml_etree_process        | 75.9 ms                                                      | 93.9 ms: 1.24x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 115 ms: 1.24x slower                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 2.79 ms: 1.25x slower                                                        |
| sympy_str                | 360 ms                                                       | 452 ms: 1.26x slower                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 3.38 ms: 1.26x slower                                                        |
| float                    | 111 ms                                                       | 140 ms: 1.26x slower                                                         |
| genshi_xml               | 63.3 ms                                                      | 80.8 ms: 1.28x slower                                                        |
| unpickle_pure_python     | 312 us                                                       | 399 us: 1.28x slower                                                         |
| sqlglot_normalize        | 144 ms                                                       | 185 ms: 1.28x slower                                                         |
| scimark_lu               | 167 ms                                                       | 215 ms: 1.29x slower                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 1.36 sec: 1.29x slower                                                       |
| logging_format           | 9.64 us                                                      | 12.5 us: 1.30x slower                                                        |
| logging_simple           | 8.88 us                                                      | 11.6 us: 1.31x slower                                                        |
| pprint_pformat           | 2.15 sec                                                     | 2.82 sec: 1.31x slower                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 92.4 ms: 1.32x slower                                                        |
| scimark_sor              | 180 ms                                                       | 238 ms: 1.32x slower                                                         |
| pickle_pure_python       | 455 us                                                       | 602 us: 1.32x slower                                                         |
| genshi_text              | 31.4 ms                                                      | 41.8 ms: 1.33x slower                                                        |
| nbody                    | 134 ms                                                       | 179 ms: 1.34x slower                                                         |
| sympy_expand             | 600 ms                                                       | 814 ms: 1.36x slower                                                         |
| django_template          | 50.2 ms                                                      | 68.2 ms: 1.36x slower                                                        |
| sympy_sum                | 193 ms                                                       | 263 ms: 1.36x slower                                                         |
| telco                    | 7.23 ms                                                      | 10.1 ms: 1.40x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.60 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.58 ms: 1.46x slower                                                        |
| mako                     | 14.7 ms                                                      | 22.1 ms: 1.50x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 12.1 ms: 1.65x slower                                                        |
| coverage                 | 63.3 ms                                                      | 106 ms: 1.67x slower                                                         |
| python_startup           | 11.5 ms                                                      | 19.8 ms: 1.72x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 53.6 ms: 8.41x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.14x slower                                                                 |

Benchmark hidden because not significant (2): sqlite_synth, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.095x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.52x