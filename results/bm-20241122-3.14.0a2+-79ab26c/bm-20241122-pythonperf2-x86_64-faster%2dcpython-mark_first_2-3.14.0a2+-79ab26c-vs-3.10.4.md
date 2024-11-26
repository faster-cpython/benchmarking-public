# Results vs. 3.10.4

- fork: faster-cpython
- ref: mark_first_2
- machine: linux-x86_64
- commit hash: 79ab26c
- commit date: 2024-11-22
- overall geometric mean: 1.312x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                           |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                         |
| html5lib       | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                          |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 666 ms: 2.40x faster                                                           |
| async_tree_none         | 692 ms                                                       | 296 ms: 2.34x faster                                                           |
| async_tree_memoization  | 819 ms                                                       | 363 ms: 2.26x faster                                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 527 ms: 1.77x faster                                                           |
| Geometric mean          | (ref)                                                        | 2.18x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.7 ms: 1.50x faster                                                          |
| float          | 111 ms                                                       | 79.3 ms: 1.40x faster                                                          |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                           |
| regex_dna      | 261 ms                                                       | 250 ms: 1.04x faster                                                           |
| regex_v8       | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                          |
| regex_effbot   | 3.09 ms                                                      | 3.36 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.47x faster                                                           |
| pickle_pure_python   | 455 us                                                       | 336 us: 1.35x faster                                                           |
| xml_etree_process    | 75.9 ms                                                      | 60.2 ms: 1.26x faster                                                          |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                          |
| json_loads           | 30.3 us                                                      | 25.6 us: 1.18x faster                                                          |
| tomli_loads          | 2.92 sec                                                     | 2.52 sec: 1.15x faster                                                         |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 110 ms                                                       | 96.7 ms: 1.14x faster                                                          |
| xml_etree_generate   | 92.3 ms                                                      | 83.7 ms: 1.10x faster                                                          |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                          |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.7 ms: 1.38x faster                                                          |
| django_template | 50.2 ms                                                      | 37.9 ms: 1.33x faster                                                          |
| genshi_text     | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                          |
| genshi_xml      | 63.3 ms                                                      | 53.7 ms: 1.18x faster                                                          |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.05x faster                                                           |
| async_tree_io            | 1.60 sec                                                     | 666 ms: 2.40x faster                                                           |
| async_tree_none          | 692 ms                                                       | 296 ms: 2.34x faster                                                           |
| async_tree_memoization   | 819 ms                                                       | 363 ms: 2.26x faster                                                           |
| deltablue                | 7.50 ms                                                      | 3.55 ms: 2.11x faster                                                          |
| generators               | 57.3 ms                                                      | 29.8 ms: 1.93x faster                                                          |
| go                       | 262 ms                                                       | 138 ms: 1.90x faster                                                           |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 527 ms: 1.77x faster                                                           |
| pylint                   | 566 ms                                                       | 321 ms: 1.76x faster                                                           |
| scimark_lu               | 167 ms                                                       | 95.8 ms: 1.74x faster                                                          |
| chaos                    | 109 ms                                                       | 63.2 ms: 1.72x faster                                                          |
| raytrace                 | 489 ms                                                       | 288 ms: 1.70x faster                                                           |
| logging_silent           | 167 ns                                                       | 103 ns: 1.63x faster                                                           |
| deepcopy_memo            | 49.8 us                                                      | 30.7 us: 1.62x faster                                                          |
| richards_super           | 90.6 ms                                                      | 56.0 ms: 1.62x faster                                                          |
| crypto_pyaes             | 119 ms                                                       | 73.7 ms: 1.62x faster                                                          |
| scimark_monte_carlo      | 107 ms                                                       | 67.1 ms: 1.60x faster                                                          |
| deepcopy                 | 468 us                                                       | 297 us: 1.57x faster                                                           |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.56x faster                                                          |
| richards                 | 75.1 ms                                                      | 49.7 ms: 1.51x faster                                                          |
| comprehensions           | 26.7 us                                                      | 17.8 us: 1.50x faster                                                          |
| nbody                    | 134 ms                                                       | 89.7 ms: 1.50x faster                                                          |
| pyflate                  | 733 ms                                                       | 494 ms: 1.48x faster                                                           |
| hexiom                   | 9.42 ms                                                      | 6.36 ms: 1.48x faster                                                          |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.47x faster                                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 1.83 ms: 1.46x faster                                                          |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                          |
| spectral_norm            | 139 ms                                                       | 96.9 ms: 1.44x faster                                                          |
| scimark_sor              | 180 ms                                                       | 128 ms: 1.40x faster                                                           |
| float                    | 111 ms                                                       | 79.3 ms: 1.40x faster                                                          |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.38x faster                                                          |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.38x faster                                                         |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                           |
| thrift                   | 1.18 ms                                                      | 865 us: 1.36x faster                                                           |
| pickle_pure_python       | 455 us                                                       | 336 us: 1.35x faster                                                           |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                          |
| sqlalchemy_declarative   | 190 ms                                                       | 141 ms: 1.35x faster                                                           |
| html5lib                 | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                          |
| django_template          | 50.2 ms                                                      | 37.9 ms: 1.33x faster                                                          |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.32x faster                                                          |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 802 ms: 1.31x faster                                                           |
| genshi_text              | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                          |
| logging_format           | 9.64 us                                                      | 7.46 us: 1.29x faster                                                          |
| logging_simple           | 8.88 us                                                      | 6.88 us: 1.29x faster                                                          |
| fannkuch                 | 483 ms                                                       | 374 ms: 1.29x faster                                                           |
| nqueens                  | 115 ms                                                       | 90.0 ms: 1.28x faster                                                          |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.9 ms: 1.27x faster                                                          |
| xml_etree_process        | 75.9 ms                                                      | 60.2 ms: 1.26x faster                                                          |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                          |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.26x faster                                                           |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                           |
| sympy_str                | 360 ms                                                       | 293 ms: 1.23x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 931 us: 1.23x faster                                                           |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                           |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.21x faster                                                          |
| sympy_expand             | 600 ms                                                       | 501 ms: 1.20x faster                                                           |
| json_loads               | 30.3 us                                                      | 25.6 us: 1.18x faster                                                          |
| dulwich_log              | 81.1 ms                                                      | 68.5 ms: 1.18x faster                                                          |
| sqlglot_optimize         | 70.1 ms                                                      | 59.4 ms: 1.18x faster                                                          |
| genshi_xml               | 63.3 ms                                                      | 53.7 ms: 1.18x faster                                                          |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                         |
| scimark_fft              | 361 ms                                                       | 309 ms: 1.17x faster                                                           |
| tomli_loads              | 2.92 sec                                                     | 2.52 sec: 1.15x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                           |
| xml_etree_iterparse      | 110 ms                                                       | 96.7 ms: 1.14x faster                                                          |
| json                     | 5.86 ms                                                      | 5.22 ms: 1.12x faster                                                          |
| xml_etree_generate       | 92.3 ms                                                      | 83.7 ms: 1.10x faster                                                          |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                           |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                           |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.79 ms: 1.06x faster                                                          |
| sqlite_synth             | 2.99 us                                                      | 2.85 us: 1.05x faster                                                          |
| regex_dna                | 261 ms                                                       | 250 ms: 1.04x faster                                                           |
| regex_v8                 | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                          |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                           |
| async_generators         | 421 ms                                                       | 441 ms: 1.05x slower                                                           |
| regex_effbot             | 3.09 ms                                                      | 3.36 ms: 1.09x slower                                                          |
| telco                    | 7.23 ms                                                      | 7.88 ms: 1.09x slower                                                          |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                          |
| coverage                 | 63.3 ms                                                      | 80.9 ms: 1.28x slower                                                          |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                          |
| create_gc_cycles         | 1.76 ms                                                      | 2.66 ms: 1.51x slower                                                          |
| gc_traversal             | 3.42 ms                                                      | 6.33 ms: 1.85x slower                                                          |
| bench_mp_pool            | 6.37 ms                                                      | 1.88 sec: 295.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                   |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241122-3.14.0a2+-79ab26c/bm-20241122-pythonperf2-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.312x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.27x