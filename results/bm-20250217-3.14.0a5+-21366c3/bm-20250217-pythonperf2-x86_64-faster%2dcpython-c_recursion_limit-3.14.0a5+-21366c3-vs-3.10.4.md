# Results vs. 3.10.4

- fork: faster-cpython
- ref: c_recursion_limit
- machine: linux-x86_64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.354x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                                |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                              |
| html5lib       | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                               |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 647 ms: 2.47x faster                                                                |
| async_tree_none         | 692 ms                                                       | 288 ms: 2.40x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 351 ms: 2.33x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 519 ms: 1.80x faster                                                                |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.7 ms: 1.59x faster                                                               |
| nbody          | 134 ms                                                       | 89.1 ms: 1.50x faster                                                               |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                                |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                                |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.05 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 204 us: 1.53x faster                                                                |
| tomli_loads          | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                              |
| pickle_pure_python   | 455 us                                                       | 333 us: 1.37x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                               |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 133 ms: 1.20x faster                                                                |
| xml_etree_iterparse  | 110 ms                                                       | 94.6 ms: 1.17x faster                                                               |
| json_loads           | 30.3 us                                                      | 26.1 us: 1.16x faster                                                               |
| xml_etree_generate   | 92.3 ms                                                      | 83.0 ms: 1.11x faster                                                               |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.07 ms: 1.24x slower                                                               |
| python_startup         | 11.5 ms                                                      | 16.2 ms: 1.41x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                               |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.37x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 24.3 ms: 1.29x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 53.7 ms: 1.18x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 166 us: 3.23x faster                                                                |
| async_tree_io            | 1.60 sec                                                     | 647 ms: 2.47x faster                                                                |
| async_tree_none          | 692 ms                                                       | 288 ms: 2.40x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 351 ms: 2.33x faster                                                                |
| deltablue                | 7.50 ms                                                      | 3.31 ms: 2.27x faster                                                               |
| go                       | 262 ms                                                       | 129 ms: 2.03x faster                                                                |
| generators               | 57.3 ms                                                      | 29.3 ms: 1.96x faster                                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 519 ms: 1.80x faster                                                                |
| pylint                   | 566 ms                                                       | 314 ms: 1.80x faster                                                                |
| chaos                    | 109 ms                                                       | 60.6 ms: 1.79x faster                                                               |
| raytrace                 | 489 ms                                                       | 278 ms: 1.76x faster                                                                |
| scimark_lu               | 167 ms                                                       | 95.9 ms: 1.74x faster                                                               |
| scimark_monte_carlo      | 107 ms                                                       | 61.8 ms: 1.74x faster                                                               |
| logging_silent           | 167 ns                                                       | 96.3 ns: 1.74x faster                                                               |
| richards_super           | 90.6 ms                                                      | 52.5 ms: 1.73x faster                                                               |
| deepcopy_memo            | 49.8 us                                                      | 29.2 us: 1.70x faster                                                               |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.65x faster                                                                |
| sqlglot_parse            | 2.24 ms                                                      | 1.36 ms: 1.65x faster                                                               |
| deepcopy                 | 468 us                                                       | 284 us: 1.65x faster                                                                |
| spectral_norm            | 139 ms                                                       | 85.8 ms: 1.62x faster                                                               |
| pyflate                  | 733 ms                                                       | 453 ms: 1.62x faster                                                                |
| crypto_pyaes             | 119 ms                                                       | 73.9 ms: 1.61x faster                                                               |
| float                    | 111 ms                                                       | 69.7 ms: 1.59x faster                                                               |
| richards                 | 75.1 ms                                                      | 47.3 ms: 1.59x faster                                                               |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                               |
| sqlglot_transpile        | 2.68 ms                                                      | 1.74 ms: 1.54x faster                                                               |
| unpickle_pure_python     | 312 us                                                       | 204 us: 1.53x faster                                                                |
| hexiom                   | 9.42 ms                                                      | 6.20 ms: 1.52x faster                                                               |
| nbody                    | 134 ms                                                       | 89.1 ms: 1.50x faster                                                               |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.43x faster                                                               |
| html5lib                 | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                               |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                                |
| logging_format           | 9.64 us                                                      | 6.83 us: 1.41x faster                                                               |
| django_template          | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                               |
| logging_simple           | 8.88 us                                                      | 6.32 us: 1.40x faster                                                               |
| thrift                   | 1.18 ms                                                      | 845 us: 1.39x faster                                                                |
| tomli_loads              | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                              |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                               |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.37x faster                                                               |
| pickle_pure_python       | 455 us                                                       | 333 us: 1.37x faster                                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 778 ms: 1.35x faster                                                                |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                              |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                              |
| fannkuch                 | 483 ms                                                       | 362 ms: 1.33x faster                                                                |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.33x faster                                                                |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                               |
| xml_etree_process        | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                               |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.5 ms: 1.30x faster                                                               |
| nqueens                  | 115 ms                                                       | 88.6 ms: 1.30x faster                                                               |
| genshi_text              | 31.4 ms                                                      | 24.3 ms: 1.29x faster                                                               |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                                |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                               |
| sqlglot_normalize        | 144 ms                                                       | 114 ms: 1.26x faster                                                                |
| sympy_str                | 360 ms                                                       | 288 ms: 1.25x faster                                                                |
| sqlglot_optimize         | 70.1 ms                                                      | 56.3 ms: 1.25x faster                                                               |
| bench_thread_pool        | 1.14 ms                                                      | 925 us: 1.23x faster                                                                |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                                |
| sympy_expand             | 600 ms                                                       | 489 ms: 1.23x faster                                                                |
| mdp                      | 3.01 sec                                                     | 2.46 sec: 1.22x faster                                                              |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                                               |
| dulwich_log              | 81.1 ms                                                      | 66.5 ms: 1.22x faster                                                               |
| xml_etree_parse          | 160 ms                                                       | 133 ms: 1.20x faster                                                                |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                              |
| genshi_xml               | 63.3 ms                                                      | 53.7 ms: 1.18x faster                                                               |
| scimark_fft              | 361 ms                                                       | 309 ms: 1.17x faster                                                                |
| xml_etree_iterparse      | 110 ms                                                       | 94.6 ms: 1.17x faster                                                               |
| json_loads               | 30.3 us                                                      | 26.1 us: 1.16x faster                                                               |
| xml_etree_generate       | 92.3 ms                                                      | 83.0 ms: 1.11x faster                                                               |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.10x faster                                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.63 ms: 1.10x faster                                                               |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                                |
| sqlite_synth             | 2.99 us                                                      | 2.77 us: 1.08x faster                                                               |
| json                     | 5.86 ms                                                      | 5.47 ms: 1.07x faster                                                               |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                                |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                               |
| async_generators         | 421 ms                                                       | 414 ms: 1.02x faster                                                                |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                                |
| regex_effbot             | 3.09 ms                                                      | 3.05 ms: 1.01x faster                                                               |
| telco                    | 7.23 ms                                                      | 7.92 ms: 1.10x slower                                                               |
| python_startup_no_site   | 7.33 ms                                                      | 9.07 ms: 1.24x slower                                                               |
| coverage                 | 63.3 ms                                                      | 78.7 ms: 1.24x slower                                                               |
| python_startup           | 11.5 ms                                                      | 16.2 ms: 1.41x slower                                                               |
| create_gc_cycles         | 1.76 ms                                                      | 2.80 ms: 1.59x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 6.31 ms: 1.85x slower                                                               |
| bench_mp_pool            | 6.37 ms                                                      | 1.12 sec: 176.32x slower                                                            |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                        |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-pythonperf2-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.354x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.27x