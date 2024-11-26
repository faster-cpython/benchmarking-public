# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-x86_64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.315x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.17x faster                                                       |
| html5lib       | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 329 ms: 2.10x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 406 ms: 2.02x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 847 ms: 1.89x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 574 ms: 1.63x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 90.4 ms: 1.48x faster                                                        |
| float          | 111 ms                                                       | 82.6 ms: 1.35x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.35x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 24.8 ms: 1.09x faster                                                        |
| regex_dna      | 261 ms                                                       | 241 ms: 1.08x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.45x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 332 us: 1.37x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.8 ms: 1.25x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.55 sec: 1.14x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.12x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 84.5 ms: 1.09x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 15.9 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.7 ms: 1.38x faster                                                        |
| django_template | 50.2 ms                                                      | 39.9 ms: 1.26x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 26.9 ms: 1.17x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.08x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.54 ms: 2.12x faster                                                        |
| async_tree_none          | 692 ms                                                       | 329 ms: 2.10x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 406 ms: 2.02x faster                                                         |
| generators               | 57.3 ms                                                      | 29.3 ms: 1.96x faster                                                        |
| go                       | 262 ms                                                       | 136 ms: 1.92x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 847 ms: 1.89x faster                                                         |
| raytrace                 | 489 ms                                                       | 276 ms: 1.77x faster                                                         |
| chaos                    | 109 ms                                                       | 62.5 ms: 1.74x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.2 us: 1.70x faster                                                        |
| scimark_lu               | 167 ms                                                       | 98.1 ms: 1.70x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 64.1 ms: 1.68x faster                                                        |
| pylint                   | 566 ms                                                       | 346 ms: 1.63x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 574 ms: 1.63x faster                                                         |
| logging_silent           | 167 ns                                                       | 103 ns: 1.63x faster                                                         |
| deepcopy                 | 468 us                                                       | 291 us: 1.61x faster                                                         |
| richards_super           | 90.6 ms                                                      | 56.7 ms: 1.60x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 75.2 ms: 1.58x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                        |
| scimark_sor              | 180 ms                                                       | 115 ms: 1.56x faster                                                         |
| pyflate                  | 733 ms                                                       | 478 ms: 1.53x faster                                                         |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.30 ms: 1.49x faster                                                        |
| richards                 | 75.1 ms                                                      | 50.6 ms: 1.48x faster                                                        |
| nbody                    | 134 ms                                                       | 90.4 ms: 1.48x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.45x faster                                                         |
| spectral_norm            | 139 ms                                                       | 96.4 ms: 1.44x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.39 us: 1.39x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.38x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.99 us: 1.38x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 332 us: 1.37x faster                                                         |
| regex_compile            | 190 ms                                                       | 140 ms: 1.35x faster                                                         |
| thrift                   | 1.18 ms                                                      | 870 us: 1.35x faster                                                         |
| float                    | 111 ms                                                       | 82.6 ms: 1.35x faster                                                        |
| fannkuch                 | 483 ms                                                       | 359 ms: 1.34x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.33x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.01 us: 1.33x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 794 ms: 1.32x faster                                                         |
| nqueens                  | 115 ms                                                       | 87.5 ms: 1.31x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                        |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 899 us: 1.27x faster                                                         |
| django_template          | 50.2 ms                                                      | 39.9 ms: 1.26x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 60.8 ms: 1.25x faster                                                        |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                         |
| scimark_fft              | 361 ms                                                       | 293 ms: 1.24x faster                                                         |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.23x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.5 ms: 1.23x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.48 sec: 1.21x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 67.4 ms: 1.20x faster                                                        |
| sympy_expand             | 600 ms                                                       | 501 ms: 1.20x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.25 ms: 1.20x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 58.8 ms: 1.19x faster                                                        |
| async_generators         | 421 ms                                                       | 357 ms: 1.18x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 26.9 ms: 1.17x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.17x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.55 sec: 1.14x faster                                                       |
| json                     | 5.86 ms                                                      | 5.14 ms: 1.14x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.12x faster                                                         |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.11x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 24.8 ms: 1.09x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.5 ms: 1.09x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.74 us: 1.09x faster                                                        |
| regex_dna                | 261 ms                                                       | 241 ms: 1.08x faster                                                         |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                         |
| telco                    | 7.23 ms                                                      | 7.95 ms: 1.10x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 81.2 ms: 1.28x slower                                                        |
| python_startup           | 11.5 ms                                                      | 15.9 ms: 1.38x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.80 ms: 1.70x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 3.02 ms: 1.72x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 2.16 sec: 338.96x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                 |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.315x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.27x