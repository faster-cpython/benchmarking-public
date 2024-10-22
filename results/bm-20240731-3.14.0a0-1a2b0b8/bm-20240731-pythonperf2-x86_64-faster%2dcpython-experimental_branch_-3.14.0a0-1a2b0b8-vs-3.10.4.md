# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 288 ms: 1.22x faster                                                                  |
| docutils       | 3.41 sec                                                     | 3.01 sec: 1.13x faster                                                                |
| html5lib       | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                                                 |
| tornado_http   | 157 ms                                                       | 118 ms: 1.33x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 336 ms: 2.06x faster                                                                  |
| async_tree_memoization  | 819 ms                                                       | 409 ms: 2.00x faster                                                                  |
| async_tree_io           | 1.60 sec                                                     | 818 ms: 1.95x faster                                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 582 ms: 1.61x faster                                                                  |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.6 ms: 1.57x faster                                                                 |
| float          | 111 ms                                                       | 80.2 ms: 1.39x faster                                                                 |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                                                  |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                                  |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                                 |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 210 us: 1.49x faster                                                                  |
| pickle_pure_python   | 455 us                                                       | 321 us: 1.42x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.21 sec: 1.32x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                                 |
| json_loads           | 30.3 us                                                      | 25.8 us: 1.17x faster                                                                 |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 85.3 ms: 1.08x faster                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.07x faster                                                                  |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                                 |
| python_startup_no_site | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.6 ms: 1.39x faster                                                                 |
| django_template | 50.2 ms                                                      | 40.7 ms: 1.23x faster                                                                 |
| genshi_text     | 31.4 ms                                                      | 27.1 ms: 1.16x faster                                                                 |
| genshi_xml      | 63.3 ms                                                      | 54.7 ms: 1.16x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.23x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.05x faster                                                                  |
| deltablue                | 7.50 ms                                                      | 3.36 ms: 2.23x faster                                                                 |
| asyncio_tcp              | 779 ms                                                       | 375 ms: 2.08x faster                                                                  |
| async_tree_none          | 692 ms                                                       | 336 ms: 2.06x faster                                                                  |
| async_tree_memoization   | 819 ms                                                       | 409 ms: 2.00x faster                                                                  |
| generators               | 57.3 ms                                                      | 28.7 ms: 2.00x faster                                                                 |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                                |
| async_tree_io            | 1.60 sec                                                     | 818 ms: 1.95x faster                                                                  |
| raytrace                 | 489 ms                                                       | 266 ms: 1.84x faster                                                                  |
| chaos                    | 109 ms                                                       | 62.5 ms: 1.74x faster                                                                 |
| logging_silent           | 167 ns                                                       | 97.4 ns: 1.72x faster                                                                 |
| scimark_lu               | 167 ms                                                       | 99.2 ms: 1.68x faster                                                                 |
| crypto_pyaes             | 119 ms                                                       | 71.0 ms: 1.68x faster                                                                 |
| go                       | 262 ms                                                       | 160 ms: 1.64x faster                                                                  |
| deepcopy_memo            | 49.8 us                                                      | 30.5 us: 1.63x faster                                                                 |
| scimark_monte_carlo      | 107 ms                                                       | 66.5 ms: 1.61x faster                                                                 |
| deepcopy                 | 468 us                                                       | 290 us: 1.61x faster                                                                  |
| pylint                   | 566 ms                                                       | 351 ms: 1.61x faster                                                                  |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 582 ms: 1.61x faster                                                                  |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.60x faster                                                                 |
| richards_super           | 90.6 ms                                                      | 57.3 ms: 1.58x faster                                                                 |
| scimark_sor              | 180 ms                                                       | 115 ms: 1.57x faster                                                                  |
| nbody                    | 134 ms                                                       | 85.6 ms: 1.57x faster                                                                 |
| comprehensions           | 26.7 us                                                      | 17.6 us: 1.51x faster                                                                 |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.51x faster                                                                 |
| pyflate                  | 733 ms                                                       | 491 ms: 1.49x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 210 us: 1.49x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.39 ms: 1.47x faster                                                                 |
| richards                 | 75.1 ms                                                      | 51.0 ms: 1.47x faster                                                                 |
| spectral_norm            | 139 ms                                                       | 96.1 ms: 1.45x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 321 us: 1.42x faster                                                                  |
| logging_simple           | 8.88 us                                                      | 6.25 us: 1.42x faster                                                                 |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                                 |
| logging_format           | 9.64 us                                                      | 6.91 us: 1.39x faster                                                                 |
| mako                     | 14.7 ms                                                      | 10.6 ms: 1.39x faster                                                                 |
| float                    | 111 ms                                                       | 80.2 ms: 1.39x faster                                                                 |
| bench_mp_pool            | 6.37 ms                                                      | 4.67 ms: 1.36x faster                                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                                 |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                                 |
| fannkuch                 | 483 ms                                                       | 360 ms: 1.34x faster                                                                  |
| tornado_http             | 157 ms                                                       | 118 ms: 1.33x faster                                                                  |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                                                  |
| thrift                   | 1.18 ms                                                      | 886 us: 1.33x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                                 |
| tomli_loads              | 2.92 sec                                                     | 2.21 sec: 1.32x faster                                                                |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                                                |
| bench_thread_pool        | 1.14 ms                                                      | 874 us: 1.31x faster                                                                  |
| xml_etree_process        | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                                 |
| html5lib                 | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                                                 |
| nqueens                  | 115 ms                                                       | 90.7 ms: 1.27x faster                                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 829 ms: 1.27x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.70 sec: 1.27x faster                                                                |
| sympy_sum                | 193 ms                                                       | 156 ms: 1.24x faster                                                                  |
| django_template          | 50.2 ms                                                      | 40.7 ms: 1.23x faster                                                                 |
| dask                     | 472 ms                                                       | 386 ms: 1.22x faster                                                                  |
| 2to3                     | 350 ms                                                       | 288 ms: 1.22x faster                                                                  |
| sympy_str                | 360 ms                                                       | 299 ms: 1.20x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                                  |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                                |
| sympy_integrate          | 28.2 ms                                                      | 23.5 ms: 1.20x faster                                                                 |
| sqlglot_optimize         | 70.1 ms                                                      | 59.3 ms: 1.18x faster                                                                 |
| sympy_expand             | 600 ms                                                       | 511 ms: 1.18x faster                                                                  |
| json_loads               | 30.3 us                                                      | 25.8 us: 1.17x faster                                                                 |
| scimark_fft              | 361 ms                                                       | 310 ms: 1.17x faster                                                                  |
| genshi_text              | 31.4 ms                                                      | 27.1 ms: 1.16x faster                                                                 |
| genshi_xml               | 63.3 ms                                                      | 54.7 ms: 1.16x faster                                                                 |
| async_generators         | 421 ms                                                       | 365 ms: 1.15x faster                                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.44 ms: 1.14x faster                                                                 |
| docutils                 | 3.41 sec                                                     | 3.01 sec: 1.13x faster                                                                |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                                  |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 85.3 ms: 1.08x faster                                                                 |
| json                     | 5.86 ms                                                      | 5.48 ms: 1.07x faster                                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.07x faster                                                                  |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                                 |
| telco                    | 7.23 ms                                                      | 8.09 ms: 1.12x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 2.04 ms: 1.16x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                                 |
| coverage                 | 63.3 ms                                                      | 78.8 ms: 1.25x slower                                                                 |
| gc_traversal             | 3.42 ms                                                      | 4.75 ms: 1.39x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x