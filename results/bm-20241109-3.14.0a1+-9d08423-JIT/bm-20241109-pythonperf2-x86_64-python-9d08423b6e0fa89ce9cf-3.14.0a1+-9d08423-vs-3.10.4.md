# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-x86_64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.277x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 319 ms: 1.10x faster                                                         |
| docutils       | 3.41 sec                                                     | 3.19 sec: 1.07x faster                                                       |
| html5lib       | 94.6 ms                                                      | 72.9 ms: 1.30x faster                                                        |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 336 ms: 2.06x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 409 ms: 2.00x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 827 ms: 1.93x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 579 ms: 1.62x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 82.8 ms: 1.62x faster                                                        |
| float          | 111 ms                                                       | 79.4 ms: 1.40x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 149 ms: 1.27x faster                                                         |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 218 us: 1.43x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.39x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 342 us: 1.33x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 57.5 ms: 1.32x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.2 us: 1.25x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.9 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                         |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                         |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 15.8 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.24 ms: 1.59x faster                                                        |
| django_template | 50.2 ms                                                      | 42.4 ms: 1.18x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 29.0 ms: 1.08x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 66.1 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 183 us: 2.94x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.29 ms: 2.28x faster                                                        |
| async_tree_none          | 692 ms                                                       | 336 ms: 2.06x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 409 ms: 2.00x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 827 ms: 1.93x faster                                                         |
| logging_silent           | 167 ns                                                       | 92.0 ns: 1.82x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.8 ms: 1.75x faster                                                        |
| scimark_lu               | 167 ms                                                       | 97.0 ms: 1.72x faster                                                        |
| richards                 | 75.1 ms                                                      | 44.3 ms: 1.70x faster                                                        |
| go                       | 262 ms                                                       | 155 ms: 1.69x faster                                                         |
| scimark_sor              | 180 ms                                                       | 107 ms: 1.69x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 30.1 us: 1.65x faster                                                        |
| chaos                    | 109 ms                                                       | 66.7 ms: 1.63x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.5 ms: 1.62x faster                                                        |
| nbody                    | 134 ms                                                       | 82.8 ms: 1.62x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 579 ms: 1.62x faster                                                         |
| mako                     | 14.7 ms                                                      | 9.24 ms: 1.59x faster                                                        |
| pyflate                  | 733 ms                                                       | 466 ms: 1.57x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 69.2 ms: 1.55x faster                                                        |
| deepcopy                 | 468 us                                                       | 309 us: 1.52x faster                                                         |
| raytrace                 | 489 ms                                                       | 323 ms: 1.51x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.51 ms: 1.48x faster                                                        |
| pylint                   | 566 ms                                                       | 384 ms: 1.47x faster                                                         |
| spectral_norm            | 139 ms                                                       | 94.7 ms: 1.47x faster                                                        |
| generators               | 57.3 ms                                                      | 39.1 ms: 1.47x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 218 us: 1.43x faster                                                         |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                        |
| float                    | 111 ms                                                       | 79.4 ms: 1.40x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.39x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.54 us: 1.36x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.12 us: 1.35x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.8 us: 1.35x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.99 ms: 1.35x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 342 us: 1.33x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 57.5 ms: 1.32x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.17 ms: 1.31x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.05 us: 1.31x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 800 ms: 1.31x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 72.9 ms: 1.30x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                       |
| fannkuch                 | 483 ms                                                       | 372 ms: 1.30x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.30 sec: 1.29x faster                                                       |
| thrift                   | 1.18 ms                                                      | 914 us: 1.29x faster                                                         |
| regex_compile            | 190 ms                                                       | 149 ms: 1.27x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 64.6 ms: 1.25x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.2 us: 1.25x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.6 ms: 1.22x faster                                                        |
| scimark_fft              | 361 ms                                                       | 297 ms: 1.22x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 961 us: 1.19x faster                                                         |
| django_template          | 50.2 ms                                                      | 42.4 ms: 1.18x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.58 sec: 1.17x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 80.9 ms: 1.14x faster                                                        |
| json                     | 5.86 ms                                                      | 5.15 ms: 1.14x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 167 ms: 1.13x faster                                                         |
| sympy_expand             | 600 ms                                                       | 530 ms: 1.13x faster                                                         |
| sympy_str                | 360 ms                                                       | 321 ms: 1.12x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.54 ms: 1.12x faster                                                        |
| nqueens                  | 115 ms                                                       | 103 ms: 1.11x faster                                                         |
| sympy_sum                | 193 ms                                                       | 174 ms: 1.11x faster                                                         |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.72 us: 1.10x faster                                                        |
| 2to3                     | 350 ms                                                       | 319 ms: 1.10x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 132 ms: 1.09x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 29.0 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.19 sec: 1.07x faster                                                       |
| async_generators         | 421 ms                                                       | 398 ms: 1.06x faster                                                         |
| meteor_contest           | 138 ms                                                       | 132 ms: 1.05x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 27.3 ms: 1.03x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 68.6 ms: 1.02x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 66.1 ms: 1.04x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.63 ms: 1.06x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 81.7 ms: 1.29x slower                                                        |
| python_startup           | 11.5 ms                                                      | 15.8 ms: 1.38x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.21 ms: 1.53x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.88 ms: 1.64x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 2.44 sec: 383.26x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.277x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.35x