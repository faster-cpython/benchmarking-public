# Results vs. 3.10.4

- fork: eendebakpt
- ref: int_freelist
- machine: linux-x86_64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                     |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                   |
| html5lib       | 94.6 ms                                                      | 71.0 ms: 1.33x faster                                                    |
| Geometric mean | (ref)                                                        | 1.24x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 334 ms: 2.07x faster                                                     |
| async_tree_memoization  | 819 ms                                                       | 413 ms: 1.98x faster                                                     |
| async_tree_io           | 1.60 sec                                                     | 850 ms: 1.88x faster                                                     |
| async_tree_cpu_io_mixed | 936 ms                                                       | 580 ms: 1.61x faster                                                     |
| Geometric mean          | (ref)                                                        | 1.88x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 91.3 ms: 1.47x faster                                                    |
| float          | 111 ms                                                       | 80.5 ms: 1.38x faster                                                    |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                        | 1.30x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                     |
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                     |
| regex_v8       | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                                    |
| regex_effbot   | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                        | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 215 us: 1.45x faster                                                     |
| pickle_pure_python   | 455 us                                                       | 333 us: 1.37x faster                                                     |
| xml_etree_process    | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                                    |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                    |
| tomli_loads          | 2.92 sec                                                     | 2.42 sec: 1.21x faster                                                   |
| json_loads           | 30.3 us                                                      | 25.6 us: 1.19x faster                                                    |
| xml_etree_parse      | 160 ms                                                       | 150 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.07x faster                                                     |
| xml_etree_generate   | 92.3 ms                                                      | 87.3 ms: 1.06x faster                                                    |
| Geometric mean       | (ref)                                                        | 1.21x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                    |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                    |
| django_template | 50.2 ms                                                      | 37.3 ms: 1.34x faster                                                    |
| genshi_text     | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                    |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                    |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 177 us: 3.03x faster                                                     |
| deltablue                | 7.50 ms                                                      | 3.52 ms: 2.13x faster                                                    |
| async_tree_none          | 692 ms                                                       | 334 ms: 2.07x faster                                                     |
| async_tree_memoization   | 819 ms                                                       | 413 ms: 1.98x faster                                                     |
| generators               | 57.3 ms                                                      | 29.3 ms: 1.96x faster                                                    |
| go                       | 262 ms                                                       | 136 ms: 1.92x faster                                                     |
| async_tree_io            | 1.60 sec                                                     | 850 ms: 1.88x faster                                                     |
| raytrace                 | 489 ms                                                       | 278 ms: 1.76x faster                                                     |
| chaos                    | 109 ms                                                       | 61.9 ms: 1.75x faster                                                    |
| scimark_lu               | 167 ms                                                       | 98.4 ms: 1.70x faster                                                    |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.69x faster                                                    |
| logging_silent           | 167 ns                                                       | 100.0 ns: 1.67x faster                                                   |
| deepcopy                 | 468 us                                                       | 286 us: 1.64x faster                                                     |
| richards_super           | 90.6 ms                                                      | 55.6 ms: 1.63x faster                                                    |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                     |
| scimark_monte_carlo      | 107 ms                                                       | 66.5 ms: 1.62x faster                                                    |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 580 ms: 1.61x faster                                                     |
| spectral_norm            | 139 ms                                                       | 87.3 ms: 1.59x faster                                                    |
| crypto_pyaes             | 119 ms                                                       | 75.1 ms: 1.59x faster                                                    |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.58x faster                                                    |
| richards                 | 75.1 ms                                                      | 49.3 ms: 1.52x faster                                                    |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.52x faster                                                    |
| pyflate                  | 733 ms                                                       | 488 ms: 1.50x faster                                                     |
| hexiom                   | 9.42 ms                                                      | 6.28 ms: 1.50x faster                                                    |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                    |
| nbody                    | 134 ms                                                       | 91.3 ms: 1.47x faster                                                    |
| unpickle_pure_python     | 312 us                                                       | 215 us: 1.45x faster                                                     |
| scimark_sor              | 180 ms                                                       | 126 ms: 1.43x faster                                                     |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                    |
| float                    | 111 ms                                                       | 80.5 ms: 1.38x faster                                                    |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                   |
| logging_format           | 9.64 us                                                      | 7.03 us: 1.37x faster                                                    |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                     |
| thrift                   | 1.18 ms                                                      | 858 us: 1.37x faster                                                     |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                    |
| pickle_pure_python       | 455 us                                                       | 333 us: 1.37x faster                                                     |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                    |
| logging_simple           | 8.88 us                                                      | 6.54 us: 1.36x faster                                                    |
| django_template          | 50.2 ms                                                      | 37.3 ms: 1.34x faster                                                    |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.33x faster                                                     |
| html5lib                 | 94.6 ms                                                      | 71.0 ms: 1.33x faster                                                    |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                   |
| pprint_safe_repr         | 1.05 sec                                                     | 798 ms: 1.31x faster                                                     |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                    |
| nqueens                  | 115 ms                                                       | 88.6 ms: 1.30x faster                                                    |
| fannkuch                 | 483 ms                                                       | 376 ms: 1.28x faster                                                     |
| xml_etree_process        | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                                    |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                    |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.26x faster                                                     |
| genshi_text              | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                    |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.2 ms: 1.25x faster                                                    |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                     |
| bench_thread_pool        | 1.14 ms                                                      | 924 us: 1.24x faster                                                     |
| sympy_str                | 360 ms                                                       | 294 ms: 1.22x faster                                                     |
| mdp                      | 3.01 sec                                                     | 2.47 sec: 1.22x faster                                                   |
| dulwich_log              | 81.1 ms                                                      | 66.7 ms: 1.22x faster                                                    |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                     |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                                    |
| tomli_loads              | 2.92 sec                                                     | 2.42 sec: 1.21x faster                                                   |
| sympy_expand             | 600 ms                                                       | 504 ms: 1.19x faster                                                     |
| sqlglot_optimize         | 70.1 ms                                                      | 59.0 ms: 1.19x faster                                                    |
| json_loads               | 30.3 us                                                      | 25.6 us: 1.19x faster                                                    |
| scimark_fft              | 361 ms                                                       | 306 ms: 1.18x faster                                                     |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                   |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                    |
| json                     | 5.86 ms                                                      | 5.17 ms: 1.14x faster                                                    |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                     |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.61 ms: 1.10x faster                                                    |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                     |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                     |
| xml_etree_parse          | 160 ms                                                       | 150 ms: 1.07x faster                                                     |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.07x faster                                                     |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                    |
| xml_etree_generate       | 92.3 ms                                                      | 87.3 ms: 1.06x faster                                                    |
| regex_v8                 | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                                    |
| async_generators         | 421 ms                                                       | 436 ms: 1.04x slower                                                     |
| telco                    | 7.23 ms                                                      | 7.88 ms: 1.09x slower                                                    |
| regex_effbot             | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                    |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                    |
| coverage                 | 63.3 ms                                                      | 83.7 ms: 1.32x slower                                                    |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                    |
| create_gc_cycles         | 1.76 ms                                                      | 3.00 ms: 1.70x slower                                                    |
| gc_traversal             | 3.42 ms                                                      | 6.15 ms: 1.80x slower                                                    |
| bench_mp_pool            | 6.37 ms                                                      | 1.22 sec: 191.78x slower                                                 |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.305x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.27x