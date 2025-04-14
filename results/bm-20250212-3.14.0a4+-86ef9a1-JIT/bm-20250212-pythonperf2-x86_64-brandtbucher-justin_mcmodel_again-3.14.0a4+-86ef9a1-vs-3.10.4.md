# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.341x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                               |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                             |
| html5lib       | 94.6 ms                                                      | 67.8 ms: 1.40x faster                                                              |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 647 ms: 2.47x faster                                                               |
| async_tree_none         | 692 ms                                                       | 292 ms: 2.37x faster                                                               |
| async_tree_memoization  | 819 ms                                                       | 355 ms: 2.31x faster                                                               |
| async_tree_cpu_io_mixed | 936 ms                                                       | 522 ms: 1.79x faster                                                               |
| Geometric mean          | (ref)                                                        | 2.22x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.0 ms: 1.59x faster                                                              |
| nbody          | 134 ms                                                       | 89.9 ms: 1.49x faster                                                              |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                               |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 136 ms: 1.40x faster                                                               |
| regex_dna      | 261 ms                                                       | 243 ms: 1.08x faster                                                               |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                       |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 198 us: 1.57x faster                                                               |
| tomli_loads          | 2.92 sec                                                     | 2.00 sec: 1.46x faster                                                             |
| pickle_pure_python   | 455 us                                                       | 328 us: 1.39x faster                                                               |
| xml_etree_process    | 75.9 ms                                                      | 55.7 ms: 1.36x faster                                                              |
| json_dumps           | 14.5 ms                                                      | 11.7 ms: 1.25x faster                                                              |
| xml_etree_generate   | 92.3 ms                                                      | 79.1 ms: 1.17x faster                                                              |
| json_loads           | 30.3 us                                                      | 26.5 us: 1.14x faster                                                              |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                               |
| xml_etree_iterparse  | 110 ms                                                       | 97.3 ms: 1.14x faster                                                              |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                              |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.40 ms: 1.56x faster                                                              |
| django_template | 50.2 ms                                                      | 36.2 ms: 1.39x faster                                                              |
| genshi_text     | 31.4 ms                                                      | 23.8 ms: 1.32x faster                                                              |
| genshi_xml      | 63.3 ms                                                      | 54.3 ms: 1.17x faster                                                              |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.14x faster                                                               |
| async_tree_io            | 1.60 sec                                                     | 647 ms: 2.47x faster                                                               |
| async_tree_none          | 692 ms                                                       | 292 ms: 2.37x faster                                                               |
| async_tree_memoization   | 819 ms                                                       | 355 ms: 2.31x faster                                                               |
| deltablue                | 7.50 ms                                                      | 3.42 ms: 2.19x faster                                                              |
| generators               | 57.3 ms                                                      | 28.7 ms: 1.99x faster                                                              |
| go                       | 262 ms                                                       | 143 ms: 1.82x faster                                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 522 ms: 1.79x faster                                                               |
| pylint                   | 566 ms                                                       | 319 ms: 1.78x faster                                                               |
| scimark_monte_carlo      | 107 ms                                                       | 61.0 ms: 1.76x faster                                                              |
| chaos                    | 109 ms                                                       | 61.7 ms: 1.76x faster                                                              |
| richards_super           | 90.6 ms                                                      | 51.6 ms: 1.76x faster                                                              |
| scimark_lu               | 167 ms                                                       | 96.6 ms: 1.73x faster                                                              |
| pyflate                  | 733 ms                                                       | 425 ms: 1.73x faster                                                               |
| logging_silent           | 167 ns                                                       | 98.0 ns: 1.71x faster                                                              |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.69x faster                                                              |
| raytrace                 | 489 ms                                                       | 292 ms: 1.68x faster                                                               |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                               |
| spectral_norm            | 139 ms                                                       | 84.3 ms: 1.65x faster                                                              |
| richards                 | 75.1 ms                                                      | 45.5 ms: 1.65x faster                                                              |
| sqlglot_parse            | 2.24 ms                                                      | 1.36 ms: 1.65x faster                                                              |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.62x faster                                                               |
| crypto_pyaes             | 119 ms                                                       | 74.5 ms: 1.60x faster                                                              |
| float                    | 111 ms                                                       | 70.0 ms: 1.59x faster                                                              |
| unpickle_pure_python     | 312 us                                                       | 198 us: 1.57x faster                                                               |
| mako                     | 14.7 ms                                                      | 9.40 ms: 1.56x faster                                                              |
| sqlglot_transpile        | 2.68 ms                                                      | 1.75 ms: 1.53x faster                                                              |
| nbody                    | 134 ms                                                       | 89.9 ms: 1.49x faster                                                              |
| tomli_loads              | 2.92 sec                                                     | 2.00 sec: 1.46x faster                                                             |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.45x faster                                                              |
| comprehensions           | 26.7 us                                                      | 18.5 us: 1.44x faster                                                              |
| logging_simple           | 8.88 us                                                      | 6.23 us: 1.42x faster                                                              |
| logging_format           | 9.64 us                                                      | 6.80 us: 1.42x faster                                                              |
| pycparser                | 1.67 sec                                                     | 1.20 sec: 1.40x faster                                                             |
| regex_compile            | 190 ms                                                       | 136 ms: 1.40x faster                                                               |
| html5lib                 | 94.6 ms                                                      | 67.8 ms: 1.40x faster                                                              |
| django_template          | 50.2 ms                                                      | 36.2 ms: 1.39x faster                                                              |
| pickle_pure_python       | 455 us                                                       | 328 us: 1.39x faster                                                               |
| hexiom                   | 9.42 ms                                                      | 6.80 ms: 1.39x faster                                                              |
| thrift                   | 1.18 ms                                                      | 851 us: 1.38x faster                                                               |
| deepcopy_reduce          | 4.01 us                                                      | 2.92 us: 1.38x faster                                                              |
| xml_etree_process        | 75.9 ms                                                      | 55.7 ms: 1.36x faster                                                              |
| pprint_pformat           | 2.15 sec                                                     | 1.59 sec: 1.36x faster                                                             |
| pprint_safe_repr         | 1.05 sec                                                     | 783 ms: 1.34x faster                                                               |
| genshi_text              | 31.4 ms                                                      | 23.8 ms: 1.32x faster                                                              |
| sqlalchemy_declarative   | 190 ms                                                       | 145 ms: 1.31x faster                                                               |
| pathlib                  | 21.4 ms                                                      | 16.4 ms: 1.30x faster                                                              |
| fannkuch                 | 483 ms                                                       | 374 ms: 1.29x faster                                                               |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.1 ms: 1.26x faster                                                              |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                               |
| json_dumps               | 14.5 ms                                                      | 11.7 ms: 1.25x faster                                                              |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                               |
| dulwich_log              | 81.1 ms                                                      | 66.6 ms: 1.22x faster                                                              |
| sympy_str                | 360 ms                                                       | 296 ms: 1.22x faster                                                               |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.21x faster                                                               |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                               |
| sympy_integrate          | 28.2 ms                                                      | 23.6 ms: 1.19x faster                                                              |
| bench_thread_pool        | 1.14 ms                                                      | 961 us: 1.19x faster                                                               |
| sympy_expand             | 600 ms                                                       | 505 ms: 1.19x faster                                                               |
| nqueens                  | 115 ms                                                       | 97.4 ms: 1.18x faster                                                              |
| sqlglot_optimize         | 70.1 ms                                                      | 59.7 ms: 1.18x faster                                                              |
| xml_etree_generate       | 92.3 ms                                                      | 79.1 ms: 1.17x faster                                                              |
| genshi_xml               | 63.3 ms                                                      | 54.3 ms: 1.17x faster                                                              |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                             |
| mdp                      | 3.01 sec                                                     | 2.58 sec: 1.16x faster                                                             |
| json_loads               | 30.3 us                                                      | 26.5 us: 1.14x faster                                                              |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                                               |
| xml_etree_iterparse      | 110 ms                                                       | 97.3 ms: 1.14x faster                                                              |
| regex_dna                | 261 ms                                                       | 243 ms: 1.08x faster                                                               |
| json                     | 5.86 ms                                                      | 5.46 ms: 1.07x faster                                                              |
| sqlite_synth             | 2.99 us                                                      | 2.79 us: 1.07x faster                                                              |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                               |
| meteor_contest           | 138 ms                                                       | 133 ms: 1.04x faster                                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.92 ms: 1.03x faster                                                              |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                               |
| telco                    | 7.23 ms                                                      | 7.59 ms: 1.05x slower                                                              |
| async_generators         | 421 ms                                                       | 448 ms: 1.07x slower                                                               |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                              |
| coverage                 | 63.3 ms                                                      | 78.5 ms: 1.24x slower                                                              |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                              |
| create_gc_cycles         | 1.76 ms                                                      | 2.75 ms: 1.56x slower                                                              |
| gc_traversal             | 3.42 ms                                                      | 6.52 ms: 1.91x slower                                                              |
| bench_mp_pool            | 6.37 ms                                                      | 1.63 sec: 255.92x slower                                                           |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                                       |

Benchmark hidden because not significant (2): regex_v8, regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250212-3.14.0a4+-86ef9a1-JIT/bm-20250212-pythonperf2-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.341x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.29x