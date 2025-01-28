# Results vs. 3.10.4

- fork: eendebakpt
- ref: iterator_freelists
- machine: linux-x86_64
- commit hash: b2dd84b
- commit date: 2025-01-27
- overall geometric mean: 1.368x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 279 ms: 1.25x faster                                                           |
| docutils       | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                         |
| html5lib       | 94.6 ms                                                      | 65.0 ms: 1.46x faster                                                          |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 640 ms: 2.50x faster                                                           |
| async_tree_none         | 692 ms                                                       | 287 ms: 2.41x faster                                                           |
| async_tree_memoization  | 819 ms                                                       | 346 ms: 2.37x faster                                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 514 ms: 1.82x faster                                                           |
| Geometric mean          | (ref)                                                        | 2.26x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.2 ms: 1.61x faster                                                          |
| nbody          | 134 ms                                                       | 86.9 ms: 1.54x faster                                                          |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.42x faster                                                           |
| regex_dna      | 261 ms                                                       | 231 ms: 1.13x faster                                                           |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                          |
| regex_effbot   | 3.09 ms                                                      | 3.10 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 207 us: 1.51x faster                                                           |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 324 us: 1.41x faster                                                           |
| xml_etree_process    | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                          |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.27x faster                                                          |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                           |
| json_loads           | 30.3 us                                                      | 26.0 us: 1.17x faster                                                          |
| xml_etree_iterparse  | 110 ms                                                       | 96.1 ms: 1.15x faster                                                          |
| xml_etree_generate   | 92.3 ms                                                      | 82.7 ms: 1.12x faster                                                          |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.93 ms: 1.22x slower                                                          |
| python_startup         | 11.5 ms                                                      | 15.9 ms: 1.38x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.0 ms: 1.44x faster                                                          |
| genshi_text     | 31.4 ms                                                      | 23.0 ms: 1.36x faster                                                          |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                          |
| genshi_xml      | 63.3 ms                                                      | 51.7 ms: 1.23x faster                                                          |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 164 us: 3.27x faster                                                           |
| async_tree_io            | 1.60 sec                                                     | 640 ms: 2.50x faster                                                           |
| async_tree_none          | 692 ms                                                       | 287 ms: 2.41x faster                                                           |
| async_tree_memoization   | 819 ms                                                       | 346 ms: 2.37x faster                                                           |
| deltablue                | 7.50 ms                                                      | 3.25 ms: 2.31x faster                                                          |
| go                       | 262 ms                                                       | 122 ms: 2.14x faster                                                           |
| generators               | 57.3 ms                                                      | 28.3 ms: 2.03x faster                                                          |
| chaos                    | 109 ms                                                       | 59.5 ms: 1.82x faster                                                          |
| pylint                   | 566 ms                                                       | 311 ms: 1.82x faster                                                           |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 514 ms: 1.82x faster                                                           |
| scimark_lu               | 167 ms                                                       | 93.2 ms: 1.79x faster                                                          |
| raytrace                 | 489 ms                                                       | 277 ms: 1.76x faster                                                           |
| richards_super           | 90.6 ms                                                      | 51.7 ms: 1.75x faster                                                          |
| logging_silent           | 167 ns                                                       | 97.1 ns: 1.72x faster                                                          |
| deepcopy_memo            | 49.8 us                                                      | 29.2 us: 1.70x faster                                                          |
| sqlglot_parse            | 2.24 ms                                                      | 1.32 ms: 1.70x faster                                                          |
| pyflate                  | 733 ms                                                       | 432 ms: 1.70x faster                                                           |
| deepcopy                 | 468 us                                                       | 278 us: 1.68x faster                                                           |
| spectral_norm            | 139 ms                                                       | 83.6 ms: 1.66x faster                                                          |
| scimark_monte_carlo      | 107 ms                                                       | 66.1 ms: 1.63x faster                                                          |
| crypto_pyaes             | 119 ms                                                       | 73.3 ms: 1.63x faster                                                          |
| richards                 | 75.1 ms                                                      | 46.2 ms: 1.63x faster                                                          |
| float                    | 111 ms                                                       | 69.2 ms: 1.61x faster                                                          |
| comprehensions           | 26.7 us                                                      | 16.7 us: 1.59x faster                                                          |
| scimark_sor              | 180 ms                                                       | 114 ms: 1.58x faster                                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 1.70 ms: 1.58x faster                                                          |
| hexiom                   | 9.42 ms                                                      | 6.07 ms: 1.55x faster                                                          |
| nbody                    | 134 ms                                                       | 86.9 ms: 1.54x faster                                                          |
| unpickle_pure_python     | 312 us                                                       | 207 us: 1.51x faster                                                           |
| logging_simple           | 8.88 us                                                      | 6.06 us: 1.47x faster                                                          |
| html5lib                 | 94.6 ms                                                      | 65.0 ms: 1.46x faster                                                          |
| coroutines               | 30.3 ms                                                      | 20.8 ms: 1.45x faster                                                          |
| logging_format           | 9.64 us                                                      | 6.66 us: 1.45x faster                                                          |
| django_template          | 50.2 ms                                                      | 35.0 ms: 1.44x faster                                                          |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                         |
| regex_compile            | 190 ms                                                       | 134 ms: 1.42x faster                                                           |
| pickle_pure_python       | 455 us                                                       | 324 us: 1.41x faster                                                           |
| thrift                   | 1.18 ms                                                      | 843 us: 1.39x faster                                                           |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.93 us: 1.37x faster                                                          |
| genshi_text              | 31.4 ms                                                      | 23.0 ms: 1.36x faster                                                          |
| pprint_safe_repr         | 1.05 sec                                                     | 770 ms: 1.36x faster                                                           |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                          |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                          |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.34x faster                                                           |
| fannkuch                 | 483 ms                                                       | 368 ms: 1.31x faster                                                           |
| xml_etree_process        | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                          |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.5 ms: 1.30x faster                                                          |
| sympy_sum                | 193 ms                                                       | 149 ms: 1.29x faster                                                           |
| sqlglot_normalize        | 144 ms                                                       | 113 ms: 1.28x faster                                                           |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.27x faster                                                          |
| sympy_str                | 360 ms                                                       | 285 ms: 1.26x faster                                                           |
| sqlglot_optimize         | 70.1 ms                                                      | 55.7 ms: 1.26x faster                                                          |
| nqueens                  | 115 ms                                                       | 91.4 ms: 1.26x faster                                                          |
| 2to3                     | 350 ms                                                       | 279 ms: 1.25x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 911 us: 1.25x faster                                                           |
| mdp                      | 3.01 sec                                                     | 2.42 sec: 1.24x faster                                                         |
| sympy_expand             | 600 ms                                                       | 485 ms: 1.24x faster                                                           |
| sympy_integrate          | 28.2 ms                                                      | 22.8 ms: 1.23x faster                                                          |
| dulwich_log              | 81.1 ms                                                      | 66.0 ms: 1.23x faster                                                          |
| genshi_xml               | 63.3 ms                                                      | 51.7 ms: 1.23x faster                                                          |
| docutils                 | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                           |
| scimark_fft              | 361 ms                                                       | 309 ms: 1.17x faster                                                           |
| json_loads               | 30.3 us                                                      | 26.0 us: 1.17x faster                                                          |
| xml_etree_iterparse      | 110 ms                                                       | 96.1 ms: 1.15x faster                                                          |
| regex_dna                | 261 ms                                                       | 231 ms: 1.13x faster                                                           |
| xml_etree_generate       | 92.3 ms                                                      | 82.7 ms: 1.12x faster                                                          |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                           |
| json                     | 5.86 ms                                                      | 5.41 ms: 1.08x faster                                                          |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.69 ms: 1.08x faster                                                          |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                          |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                           |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                          |
| async_generators         | 421 ms                                                       | 410 ms: 1.03x faster                                                           |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                           |
| regex_effbot             | 3.09 ms                                                      | 3.10 ms: 1.00x slower                                                          |
| telco                    | 7.23 ms                                                      | 7.97 ms: 1.10x slower                                                          |
| python_startup_no_site   | 7.33 ms                                                      | 8.93 ms: 1.22x slower                                                          |
| coverage                 | 63.3 ms                                                      | 81.3 ms: 1.28x slower                                                          |
| python_startup           | 11.5 ms                                                      | 15.9 ms: 1.38x slower                                                          |
| create_gc_cycles         | 1.76 ms                                                      | 2.72 ms: 1.54x slower                                                          |
| gc_traversal             | 3.42 ms                                                      | 6.32 ms: 1.85x slower                                                          |
| bench_mp_pool            | 6.37 ms                                                      | 1.16 sec: 182.06x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                   |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250127-3.14.0a4+-b2dd84b/bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.368x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.27x