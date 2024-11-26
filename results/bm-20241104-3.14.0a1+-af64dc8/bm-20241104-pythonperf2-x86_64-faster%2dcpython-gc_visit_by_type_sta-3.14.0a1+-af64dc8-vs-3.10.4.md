# Results vs. 3.10.4

- fork: faster-cpython
- ref: gc_visit_by_type_sta
- machine: linux-x86_64
- commit hash: af64dc8
- commit date: 2024-11-04
- overall geometric mean: 1.317x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.24x faster                                                                   |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 330 ms: 2.09x faster                                                                   |
| async_tree_memoization  | 819 ms                                                       | 407 ms: 2.01x faster                                                                   |
| async_tree_io           | 1.60 sec                                                     | 835 ms: 1.91x faster                                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 570 ms: 1.64x faster                                                                   |
| Geometric mean          | (ref)                                                        | 1.91x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.7 ms: 1.49x faster                                                                  |
| float          | 111 ms                                                       | 82.3 ms: 1.35x faster                                                                  |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                                   |
| regex_dna      | 261 ms                                                       | 241 ms: 1.08x faster                                                                   |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                                  |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                                   |
| pickle_pure_python   | 455 us                                                       | 330 us: 1.38x faster                                                                   |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                                  |
| xml_etree_process    | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                                                  |
| json_loads           | 30.3 us                                                      | 24.4 us: 1.24x faster                                                                  |
| tomli_loads          | 2.92 sec                                                     | 2.47 sec: 1.18x faster                                                                 |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                                   |
| xml_etree_generate   | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                                   |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                                  |
| python_startup         | 11.5 ms                                                      | 15.8 ms: 1.38x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                                  |
| django_template | 50.2 ms                                                      | 40.7 ms: 1.23x faster                                                                  |
| genshi_text     | 31.4 ms                                                      | 26.0 ms: 1.21x faster                                                                  |
| genshi_xml      | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                                                  |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.06x faster                                                                   |
| deltablue                | 7.50 ms                                                      | 3.45 ms: 2.18x faster                                                                  |
| async_tree_none          | 692 ms                                                       | 330 ms: 2.09x faster                                                                   |
| async_tree_memoization   | 819 ms                                                       | 407 ms: 2.01x faster                                                                   |
| async_tree_io            | 1.60 sec                                                     | 835 ms: 1.91x faster                                                                   |
| go                       | 262 ms                                                       | 137 ms: 1.91x faster                                                                   |
| generators               | 57.3 ms                                                      | 30.2 ms: 1.90x faster                                                                  |
| chaos                    | 109 ms                                                       | 60.7 ms: 1.79x faster                                                                  |
| scimark_lu               | 167 ms                                                       | 95.6 ms: 1.75x faster                                                                  |
| raytrace                 | 489 ms                                                       | 285 ms: 1.72x faster                                                                   |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.69x faster                                                                  |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                                   |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 570 ms: 1.64x faster                                                                   |
| richards_super           | 90.6 ms                                                      | 55.3 ms: 1.64x faster                                                                  |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.63x faster                                                                   |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                                   |
| deepcopy                 | 468 us                                                       | 290 us: 1.61x faster                                                                   |
| scimark_monte_carlo      | 107 ms                                                       | 66.8 ms: 1.61x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 74.5 ms: 1.60x faster                                                                  |
| pyflate                  | 733 ms                                                       | 466 ms: 1.57x faster                                                                   |
| sqlglot_parse            | 2.24 ms                                                      | 1.45 ms: 1.54x faster                                                                  |
| richards                 | 75.1 ms                                                      | 49.0 ms: 1.53x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.15 ms: 1.53x faster                                                                  |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.52x faster                                                                  |
| nbody                    | 134 ms                                                       | 89.7 ms: 1.49x faster                                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 1.83 ms: 1.47x faster                                                                  |
| spectral_norm            | 139 ms                                                       | 96.0 ms: 1.45x faster                                                                  |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.44x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                                   |
| pycparser                | 1.67 sec                                                     | 1.20 sec: 1.39x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 330 us: 1.38x faster                                                                   |
| logging_format           | 9.64 us                                                      | 7.00 us: 1.38x faster                                                                  |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                                  |
| fannkuch                 | 483 ms                                                       | 352 ms: 1.37x faster                                                                   |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                                   |
| logging_simple           | 8.88 us                                                      | 6.49 us: 1.37x faster                                                                  |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                                  |
| float                    | 111 ms                                                       | 82.3 ms: 1.35x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.60 sec: 1.35x faster                                                                 |
| thrift                   | 1.18 ms                                                      | 880 us: 1.34x faster                                                                   |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.34x faster                                                                   |
| html5lib                 | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 788 ms: 1.33x faster                                                                   |
| bench_thread_pool        | 1.14 ms                                                      | 879 us: 1.30x faster                                                                   |
| nqueens                  | 115 ms                                                       | 88.9 ms: 1.29x faster                                                                  |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                                   |
| xml_etree_process        | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                                                  |
| 2to3                     | 350 ms                                                       | 281 ms: 1.24x faster                                                                   |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.3 ms: 1.24x faster                                                                  |
| json_loads               | 30.3 us                                                      | 24.4 us: 1.24x faster                                                                  |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                                   |
| django_template          | 50.2 ms                                                      | 40.7 ms: 1.23x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                                   |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                                                  |
| genshi_text              | 31.4 ms                                                      | 26.0 ms: 1.21x faster                                                                  |
| dulwich_log              | 81.1 ms                                                      | 67.1 ms: 1.21x faster                                                                  |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.21x faster                                                                   |
| sympy_expand             | 600 ms                                                       | 498 ms: 1.20x faster                                                                   |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                                 |
| sqlglot_optimize         | 70.1 ms                                                      | 58.8 ms: 1.19x faster                                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.26 ms: 1.19x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.47 sec: 1.18x faster                                                                 |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                                 |
| genshi_xml               | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.12 ms: 1.14x faster                                                                  |
| async_generators         | 421 ms                                                       | 369 ms: 1.14x faster                                                                   |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                                   |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                                   |
| sqlite_synth             | 2.99 us                                                      | 2.75 us: 1.09x faster                                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                                  |
| regex_dna                | 261 ms                                                       | 241 ms: 1.08x faster                                                                   |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                                                   |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                                                   |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                                  |
| asyncio_websockets       | 390 ms                                                       | 380 ms: 1.03x faster                                                                   |
| telco                    | 7.23 ms                                                      | 7.73 ms: 1.07x slower                                                                  |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                                  |
| coverage                 | 63.3 ms                                                      | 78.2 ms: 1.24x slower                                                                  |
| python_startup           | 11.5 ms                                                      | 15.8 ms: 1.38x slower                                                                  |
| gc_traversal             | 3.42 ms                                                      | 5.78 ms: 1.69x slower                                                                  |
| create_gc_cycles         | 1.76 ms                                                      | 3.05 ms: 1.73x slower                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 2.11 sec: 331.32x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241104-3.14.0a1+-af64dc8/bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.317x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.27x