# Results vs. 3.10.4

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: linux-x86_64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.300x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 290 ms: 1.21x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                                       |
| html5lib       | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 653 ms: 2.45x faster                                                         |
| async_tree_none         | 692 ms                                                       | 293 ms: 2.36x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 361 ms: 2.27x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 524 ms: 1.79x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 72.8 ms: 1.53x faster                                                        |
| nbody          | 134 ms                                                       | 90.8 ms: 1.48x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.24 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 202 us: 1.54x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 341 us: 1.34x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 56.9 ms: 1.33x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 94.0 ms: 1.18x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.7 ms: 1.14x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.38 ms: 1.57x faster                                                        |
| django_template | 50.2 ms                                                      | 39.5 ms: 1.27x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 28.7 ms: 1.09x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 62.8 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.22x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 183 us: 2.94x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 653 ms: 2.45x faster                                                         |
| async_tree_none          | 692 ms                                                       | 293 ms: 2.36x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 361 ms: 2.27x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.31 ms: 2.26x faster                                                        |
| go                       | 262 ms                                                       | 145 ms: 1.81x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 524 ms: 1.79x faster                                                         |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.74x faster                                                         |
| pylint                   | 566 ms                                                       | 331 ms: 1.71x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 62.9 ms: 1.71x faster                                                        |
| scimark_lu               | 167 ms                                                       | 98.9 ms: 1.69x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.8 us: 1.67x faster                                                        |
| logging_silent           | 167 ns                                                       | 101 ns: 1.66x faster                                                         |
| richards_super           | 90.6 ms                                                      | 54.8 ms: 1.65x faster                                                        |
| pyflate                  | 733 ms                                                       | 451 ms: 1.63x faster                                                         |
| chaos                    | 109 ms                                                       | 67.6 ms: 1.61x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 75.3 ms: 1.58x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.38 ms: 1.57x faster                                                        |
| richards                 | 75.1 ms                                                      | 48.2 ms: 1.56x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 202 us: 1.54x faster                                                         |
| float                    | 111 ms                                                       | 72.8 ms: 1.53x faster                                                        |
| deepcopy                 | 468 us                                                       | 310 us: 1.51x faster                                                         |
| spectral_norm            | 139 ms                                                       | 93.6 ms: 1.49x faster                                                        |
| nbody                    | 134 ms                                                       | 90.8 ms: 1.48x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.47x faster                                                        |
| raytrace                 | 489 ms                                                       | 338 ms: 1.45x faster                                                         |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.44x faster                                                        |
| generators               | 57.3 ms                                                      | 39.8 ms: 1.44x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                       |
| comprehensions           | 26.7 us                                                      | 19.0 us: 1.40x faster                                                        |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.60 us: 1.34x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 341 us: 1.34x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 56.9 ms: 1.33x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.23 us: 1.33x faster                                                        |
| thrift                   | 1.18 ms                                                      | 883 us: 1.33x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 7.08 ms: 1.33x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.33x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 797 ms: 1.32x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                                        |
| fannkuch                 | 483 ms                                                       | 379 ms: 1.27x faster                                                         |
| django_template          | 50.2 ms                                                      | 39.5 ms: 1.27x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.9 ms: 1.27x faster                                                        |
| sympy_sum                | 193 ms                                                       | 158 ms: 1.22x faster                                                         |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                        |
| 2to3                     | 350 ms                                                       | 290 ms: 1.21x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 67.7 ms: 1.20x faster                                                        |
| scimark_fft              | 361 ms                                                       | 305 ms: 1.19x faster                                                         |
| sympy_str                | 360 ms                                                       | 305 ms: 1.18x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 970 us: 1.18x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 94.0 ms: 1.18x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 24.0 ms: 1.17x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.16x faster                                                       |
| sympy_expand             | 600 ms                                                       | 521 ms: 1.15x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 125 ms: 1.15x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 61.3 ms: 1.14x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 80.7 ms: 1.14x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                                       |
| nqueens                  | 115 ms                                                       | 101 ms: 1.14x faster                                                         |
| json                     | 5.86 ms                                                      | 5.25 ms: 1.12x faster                                                        |
| regex_dna                | 261 ms                                                       | 234 ms: 1.12x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 28.7 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                        |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.02 ms: 1.01x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 62.8 ms: 1.01x faster                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.24 ms: 1.05x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.65 ms: 1.06x slower                                                        |
| async_generators         | 421 ms                                                       | 465 ms: 1.11x slower                                                         |
| mypy2                    | 933 ms                                                       | 1.04 sec: 1.12x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 81.5 ms: 1.29x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.69 ms: 1.53x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.31 ms: 1.85x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.10 sec: 172.99x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-pythonperf2-x86_64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.300x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.30x