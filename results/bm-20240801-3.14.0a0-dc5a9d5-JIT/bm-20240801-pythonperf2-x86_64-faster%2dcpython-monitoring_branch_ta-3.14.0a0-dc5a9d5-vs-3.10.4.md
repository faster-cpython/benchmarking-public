# Results vs. 3.10.4

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-x86_64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 306 ms: 1.14x faster                                                                  |
| docutils       | 3.41 sec                                                     | 3.12 sec: 1.10x faster                                                                |
| html5lib       | 94.6 ms                                                      | 70.5 ms: 1.34x faster                                                                 |
| tornado_http   | 157 ms                                                       | 119 ms: 1.31x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 335 ms: 2.06x faster                                                                  |
| async_tree_memoization  | 819 ms                                                       | 404 ms: 2.03x faster                                                                  |
| async_tree_io           | 1.60 sec                                                     | 788 ms: 2.03x faster                                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 578 ms: 1.62x faster                                                                  |
| Geometric mean          | (ref)                                                        | 1.93x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 91.2 ms: 1.47x faster                                                                 |
| float          | 111 ms                                                       | 76.1 ms: 1.46x faster                                                                 |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                                  |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                                                  |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                                 |
| regex_effbot   | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 214 us: 1.46x faster                                                                  |
| pickle_pure_python   | 455 us                                                       | 317 us: 1.44x faster                                                                  |
| tomli_loads          | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                                |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                                 |
| xml_etree_process    | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                                                 |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                                 |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 97.7 ms: 1.13x faster                                                                 |
| xml_etree_generate   | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                                 |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| python_startup_no_site | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.05 ms: 1.63x faster                                                                 |
| django_template | 50.2 ms                                                      | 41.2 ms: 1.22x faster                                                                 |
| genshi_text     | 31.4 ms                                                      | 26.3 ms: 1.20x faster                                                                 |
| genshi_xml      | 63.3 ms                                                      | 60.1 ms: 1.05x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 184 us: 2.91x faster                                                                  |
| deltablue                | 7.50 ms                                                      | 3.60 ms: 2.08x faster                                                                 |
| asyncio_tcp              | 779 ms                                                       | 377 ms: 2.07x faster                                                                  |
| async_tree_none          | 692 ms                                                       | 335 ms: 2.06x faster                                                                  |
| async_tree_memoization   | 819 ms                                                       | 404 ms: 2.03x faster                                                                  |
| async_tree_io            | 1.60 sec                                                     | 788 ms: 2.03x faster                                                                  |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                                |
| richards_super           | 90.6 ms                                                      | 52.8 ms: 1.72x faster                                                                 |
| spectral_norm            | 139 ms                                                       | 81.4 ms: 1.71x faster                                                                 |
| crypto_pyaes             | 119 ms                                                       | 70.5 ms: 1.69x faster                                                                 |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.69x faster                                                                 |
| richards                 | 75.1 ms                                                      | 45.2 ms: 1.66x faster                                                                 |
| scimark_monte_carlo      | 107 ms                                                       | 64.7 ms: 1.66x faster                                                                 |
| pyflate                  | 733 ms                                                       | 442 ms: 1.66x faster                                                                  |
| raytrace                 | 489 ms                                                       | 297 ms: 1.65x faster                                                                  |
| chaos                    | 109 ms                                                       | 66.5 ms: 1.63x faster                                                                 |
| mako                     | 14.7 ms                                                      | 9.05 ms: 1.63x faster                                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 578 ms: 1.62x faster                                                                  |
| logging_silent           | 167 ns                                                       | 104 ns: 1.61x faster                                                                  |
| go                       | 262 ms                                                       | 165 ms: 1.59x faster                                                                  |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.56x faster                                                                 |
| generators               | 57.3 ms                                                      | 36.9 ms: 1.55x faster                                                                 |
| deepcopy                 | 468 us                                                       | 306 us: 1.53x faster                                                                  |
| scimark_lu               | 167 ms                                                       | 110 ms: 1.52x faster                                                                  |
| nbody                    | 134 ms                                                       | 91.2 ms: 1.47x faster                                                                 |
| pylint                   | 566 ms                                                       | 386 ms: 1.47x faster                                                                  |
| float                    | 111 ms                                                       | 76.1 ms: 1.46x faster                                                                 |
| unpickle_pure_python     | 312 us                                                       | 214 us: 1.46x faster                                                                  |
| comprehensions           | 26.7 us                                                      | 18.4 us: 1.45x faster                                                                 |
| sqlglot_transpile        | 2.68 ms                                                      | 1.86 ms: 1.44x faster                                                                 |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.44x faster                                                                  |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                                  |
| logging_simple           | 8.88 us                                                      | 6.23 us: 1.42x faster                                                                 |
| scimark_sor              | 180 ms                                                       | 127 ms: 1.42x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                                |
| logging_format           | 9.64 us                                                      | 6.88 us: 1.40x faster                                                                 |
| fannkuch                 | 483 ms                                                       | 345 ms: 1.40x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.74 ms: 1.40x faster                                                                 |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                                 |
| html5lib                 | 94.6 ms                                                      | 70.5 ms: 1.34x faster                                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 3.00 us: 1.34x faster                                                                 |
| bench_mp_pool            | 6.37 ms                                                      | 4.81 ms: 1.32x faster                                                                 |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 3.85 ms: 1.32x faster                                                                 |
| xml_etree_process        | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                                                 |
| thrift                   | 1.18 ms                                                      | 894 us: 1.31x faster                                                                  |
| tornado_http             | 157 ms                                                       | 119 ms: 1.31x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 819 ms: 1.28x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                                                 |
| scimark_fft              | 361 ms                                                       | 284 ms: 1.27x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.70 sec: 1.26x faster                                                                |
| bench_thread_pool        | 1.14 ms                                                      | 905 us: 1.26x faster                                                                  |
| django_template          | 50.2 ms                                                      | 41.2 ms: 1.22x faster                                                                 |
| dask                     | 472 ms                                                       | 391 ms: 1.21x faster                                                                  |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                                 |
| genshi_text              | 31.4 ms                                                      | 26.3 ms: 1.20x faster                                                                 |
| nqueens                  | 115 ms                                                       | 98.2 ms: 1.17x faster                                                                 |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.15x faster                                                                |
| sympy_str                | 360 ms                                                       | 312 ms: 1.15x faster                                                                  |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 168 ms: 1.15x faster                                                                  |
| 2to3                     | 350 ms                                                       | 306 ms: 1.14x faster                                                                  |
| async_generators         | 421 ms                                                       | 372 ms: 1.13x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 97.7 ms: 1.13x faster                                                                 |
| sympy_expand             | 600 ms                                                       | 531 ms: 1.13x faster                                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                                 |
| sqlglot_optimize         | 70.1 ms                                                      | 62.6 ms: 1.12x faster                                                                 |
| sqlglot_normalize        | 144 ms                                                       | 129 ms: 1.12x faster                                                                  |
| regex_dna                | 261 ms                                                       | 235 ms: 1.11x faster                                                                  |
| docutils                 | 3.41 sec                                                     | 3.12 sec: 1.10x faster                                                                |
| sympy_integrate          | 28.2 ms                                                      | 26.0 ms: 1.08x faster                                                                 |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.43 ms: 1.08x faster                                                                 |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                                 |
| genshi_xml               | 63.3 ms                                                      | 60.1 ms: 1.05x faster                                                                 |
| telco                    | 7.23 ms                                                      | 7.82 ms: 1.08x slower                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                                 |
| coverage                 | 63.3 ms                                                      | 79.5 ms: 1.26x slower                                                                 |
| gc_traversal             | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240801-3.14.0a0-dc5a9d5-JIT/bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.22x