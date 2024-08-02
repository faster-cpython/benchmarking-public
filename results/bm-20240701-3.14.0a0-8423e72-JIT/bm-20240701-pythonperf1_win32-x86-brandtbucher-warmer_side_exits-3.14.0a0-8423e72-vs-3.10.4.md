# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmer_side_exits
- machine: windows-x86
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| docutils       | 1.95 sec                                                        | 2.00 sec: 1.03x slower                                                            |
| html5lib       | 52.1 ms                                                         | 51.6 ms: 1.01x faster                                                             |
| tornado_http   | 118 ms                                                          | 101 ms: 1.16x faster                                                              |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 490 ms: 1.88x faster                                                              |
| async_tree_none         | 394 ms                                                          | 240 ms: 1.64x faster                                                              |
| async_tree_io           | 940 ms                                                          | 575 ms: 1.64x faster                                                              |
| async_tree_memoization  | 467 ms                                                          | 295 ms: 1.58x faster                                                              |
| Geometric mean          | (ref)                                                           | 1.68x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.54x faster                                                              |
| nbody          | 79.1 ms                                                         | 51.5 ms: 1.54x faster                                                             |
| float          | 69.6 ms                                                         | 45.6 ms: 1.53x faster                                                             |
| Geometric mean | (ref)                                                           | 1.81x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 101 ms: 1.16x faster                                                              |
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                              |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                             |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 130 us: 1.45x faster                                                              |
| json_dumps           | 9.82 ms                                                         | 7.39 ms: 1.33x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 223 us: 1.25x faster                                                              |
| tomli_loads          | 1.91 sec                                                        | 1.63 sec: 1.17x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 106 ms: 1.14x faster                                                              |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.5 ms: 1.12x faster                                                             |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 48.5 ms: 1.01x slower                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 63.0 ms: 1.02x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.2 ms: 1.01x slower                                                             |
| python_startup_no_site | 18.1 ms                                                         | 19.2 ms: 1.07x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 9.10 ms                                                         | 5.43 ms: 1.68x faster                                                             |
| genshi_xml     | 46.6 ms                                                         | 57.1 ms: 1.23x slower                                                             |
| genshi_text    | 21.0 ms                                                         | 25.8 ms: 1.23x slower                                                             |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 197 ms: 2.54x faster                                                              |
| typing_runtime_protocols | 396 us                                                          | 160 us: 2.47x faster                                                              |
| sqlglot_normalize        | 230 ms                                                          | 101 ms: 2.28x faster                                                              |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 490 ms: 1.88x faster                                                              |
| deepcopy_memo            | 29.6 us                                                         | 16.5 us: 1.79x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 48.3 ms: 1.68x faster                                                             |
| mako                     | 9.10 ms                                                         | 5.43 ms: 1.68x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 59.0 ns: 1.66x faster                                                             |
| async_tree_none          | 394 ms                                                          | 240 ms: 1.64x faster                                                              |
| async_tree_io            | 940 ms                                                          | 575 ms: 1.64x faster                                                              |
| spectral_norm            | 80.2 ms                                                         | 49.3 ms: 1.63x faster                                                             |
| comprehensions           | 17.7 us                                                         | 11.1 us: 1.59x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 295 ms: 1.58x faster                                                              |
| nbody                    | 79.1 ms                                                         | 51.5 ms: 1.54x faster                                                             |
| float                    | 69.6 ms                                                         | 45.6 ms: 1.53x faster                                                             |
| pylint                   | 384 ms                                                          | 256 ms: 1.50x faster                                                              |
| pyflate                  | 422 ms                                                          | 283 ms: 1.49x faster                                                              |
| fannkuch                 | 317 ms                                                          | 216 ms: 1.47x faster                                                              |
| unpickle_pure_python     | 189 us                                                          | 130 us: 1.45x faster                                                              |
| scimark_monte_carlo      | 61.9 ms                                                         | 42.9 ms: 1.44x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.82 ms: 1.43x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.37 ms: 1.37x faster                                                             |
| chaos                    | 74.4 ms                                                         | 55.7 ms: 1.34x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 7.39 ms: 1.33x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.68 ms: 1.31x faster                                                             |
| sqlglot_parse            | 1.33 ms                                                         | 1.02 ms: 1.31x faster                                                             |
| scimark_fft              | 216 ms                                                          | 166 ms: 1.30x faster                                                              |
| pickle_pure_python       | 280 us                                                          | 223 us: 1.25x faster                                                              |
| deepcopy                 | 310 us                                                          | 250 us: 1.24x faster                                                              |
| sqlglot_transpile        | 1.58 ms                                                         | 1.29 ms: 1.23x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 71.6 ms: 1.22x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 622 ms: 1.20x faster                                                              |
| go                       | 146 ms                                                          | 122 ms: 1.19x faster                                                              |
| tomli_loads              | 1.91 sec                                                        | 1.63 sec: 1.17x faster                                                            |
| tornado_http             | 118 ms                                                          | 101 ms: 1.16x faster                                                              |
| richards_super           | 49.9 ms                                                         | 42.9 ms: 1.16x faster                                                             |
| regex_compile            | 117 ms                                                          | 101 ms: 1.16x faster                                                              |
| thrift                   | 902 us                                                          | 786 us: 1.15x faster                                                              |
| json                     | 4.76 ms                                                         | 4.16 ms: 1.15x faster                                                             |
| pycparser                | 1.04 sec                                                        | 917 ms: 1.14x faster                                                              |
| xml_etree_parse          | 120 ms                                                          | 106 ms: 1.14x faster                                                              |
| bench_thread_pool        | 1.12 ms                                                         | 989 us: 1.13x faster                                                              |
| raytrace                 | 303 ms                                                          | 268 ms: 1.13x faster                                                              |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.5 ms: 1.12x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 1.23 sec: 1.11x faster                                                            |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                              |
| pprint_safe_repr         | 658 ms                                                          | 602 ms: 1.09x faster                                                              |
| richards                 | 40.3 ms                                                         | 37.5 ms: 1.07x faster                                                             |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 84.2 ms: 1.07x faster                                                             |
| sympy_sum                | 122 ms                                                          | 115 ms: 1.06x faster                                                              |
| mdp                      | 1.83 sec                                                        | 1.73 sec: 1.06x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 76.5 ms: 1.05x faster                                                             |
| generators               | 31.6 ms                                                         | 30.2 ms: 1.04x faster                                                             |
| scimark_sor              | 115 ms                                                          | 110 ms: 1.04x faster                                                              |
| deepcopy_reduce          | 2.68 us                                                         | 2.59 us: 1.03x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 51.6 ms: 1.01x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 16.6 ms: 1.01x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 48.5 ms: 1.01x slower                                                             |
| python_startup           | 22.9 ms                                                         | 23.2 ms: 1.01x slower                                                             |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 63.0 ms: 1.02x slower                                                             |
| docutils                 | 1.95 sec                                                        | 2.00 sec: 1.03x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 83.5 ms: 1.03x slower                                                             |
| sqlglot_optimize         | 44.7 ms                                                         | 46.6 ms: 1.04x slower                                                             |
| sympy_expand             | 391 ms                                                          | 413 ms: 1.06x slower                                                              |
| python_startup_no_site   | 18.1 ms                                                         | 19.2 ms: 1.07x slower                                                             |
| coroutines               | 17.9 ms                                                         | 19.3 ms: 1.08x slower                                                             |
| create_gc_cycles         | 694 us                                                          | 761 us: 1.10x slower                                                              |
| logging_format           | 7.91 us                                                         | 8.69 us: 1.10x slower                                                             |
| logging_simple           | 7.29 us                                                         | 8.05 us: 1.10x slower                                                             |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                             |
| coverage                 | 46.6 ms                                                         | 52.4 ms: 1.13x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 74.9 ms: 1.13x slower                                                             |
| telco                    | 4.83 ms                                                         | 5.61 ms: 1.16x slower                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                             |
| genshi_xml               | 46.6 ms                                                         | 57.1 ms: 1.23x slower                                                             |
| genshi_text              | 21.0 ms                                                         | 25.8 ms: 1.23x slower                                                             |
| async_generators         | 241 ms                                                          | 338 ms: 1.40x slower                                                              |
| Geometric mean           | (ref)                                                           | 1.18x faster                                                                      |

Benchmark hidden because not significant (4): 2to3, django_template, asyncio_tcp_ssl, sympy_str
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-pythonperf1_win32-x86-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown