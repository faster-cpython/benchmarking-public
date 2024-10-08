# Results vs. 3.10.4

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: windows-x86
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 259 ms: 1.03x faster                                                                     |
| docutils       | 1.95 sec                                                        | 1.94 sec: 1.01x faster                                                                   |
| html5lib       | 52.1 ms                                                         | 46.9 ms: 1.11x faster                                                                    |
| tornado_http   | 118 ms                                                          | 106 ms: 1.11x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 474 ms: 1.95x faster                                                                     |
| async_tree_none         | 394 ms                                                          | 226 ms: 1.75x faster                                                                     |
| async_tree_io           | 940 ms                                                          | 551 ms: 1.71x faster                                                                     |
| async_tree_memoization  | 467 ms                                                          | 275 ms: 1.70x faster                                                                     |
| Geometric mean          | (ref)                                                           | 1.77x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.52x faster                                                                     |
| float          | 69.6 ms                                                         | 43.1 ms: 1.61x faster                                                                    |
| nbody          | 79.1 ms                                                         | 52.7 ms: 1.50x faster                                                                    |
| Geometric mean | (ref)                                                           | 1.83x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 94.0 ms: 1.24x faster                                                                    |
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                                     |
| regex_v8       | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                                    |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.23 ms: 1.36x faster                                                                    |
| pickle_pure_python   | 280 us                                                          | 214 us: 1.31x faster                                                                     |
| tomli_loads          | 1.91 sec                                                        | 1.50 sec: 1.27x faster                                                                   |
| unpickle_pure_python | 189 us                                                          | 151 us: 1.26x faster                                                                     |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.16x faster                                                                     |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.8 ms: 1.13x faster                                                                    |
| xml_etree_process    | 48.1 ms                                                         | 44.6 ms: 1.08x faster                                                                    |
| xml_etree_generate   | 61.6 ms                                                         | 58.9 ms: 1.05x faster                                                                    |
| json_loads           | 22.4 us                                                         | 21.7 us: 1.03x faster                                                                    |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                                    |
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.44 ms: 1.67x faster                                                                    |
| django_template | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                                    |
| genshi_xml      | 46.6 ms                                                         | 47.9 ms: 1.03x slower                                                                    |
| genshi_text     | 21.0 ms                                                         | 22.8 ms: 1.09x slower                                                                    |
| Geometric mean  | (ref)                                                           | 1.14x faster                                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 148 us: 2.67x faster                                                                     |
| pidigits                 | 502 ms                                                          | 199 ms: 2.52x faster                                                                     |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 474 ms: 1.95x faster                                                                     |
| deepcopy_memo            | 29.6 us                                                         | 16.0 us: 1.84x faster                                                                    |
| async_tree_none          | 394 ms                                                          | 226 ms: 1.75x faster                                                                     |
| async_tree_io            | 940 ms                                                          | 551 ms: 1.71x faster                                                                     |
| crypto_pyaes             | 81.3 ms                                                         | 47.9 ms: 1.70x faster                                                                    |
| async_tree_memoization   | 467 ms                                                          | 275 ms: 1.70x faster                                                                     |
| mako                     | 9.10 ms                                                         | 5.44 ms: 1.67x faster                                                                    |
| logging_silent           | 97.9 ns                                                         | 58.7 ns: 1.67x faster                                                                    |
| spectral_norm            | 80.2 ms                                                         | 49.1 ms: 1.63x faster                                                                    |
| float                    | 69.6 ms                                                         | 43.1 ms: 1.61x faster                                                                    |
| pyflate                  | 422 ms                                                          | 271 ms: 1.56x faster                                                                     |
| comprehensions           | 17.7 us                                                         | 11.4 us: 1.55x faster                                                                    |
| pylint                   | 384 ms                                                          | 253 ms: 1.51x faster                                                                     |
| nbody                    | 79.1 ms                                                         | 52.7 ms: 1.50x faster                                                                    |
| scimark_monte_carlo      | 61.9 ms                                                         | 42.4 ms: 1.46x faster                                                                    |
| chaos                    | 74.4 ms                                                         | 51.6 ms: 1.44x faster                                                                    |
| deltablue                | 4.04 ms                                                         | 2.82 ms: 1.43x faster                                                                    |
| fannkuch                 | 317 ms                                                          | 225 ms: 1.41x faster                                                                     |
| sqlglot_parse            | 1.33 ms                                                         | 978 us: 1.36x faster                                                                     |
| json_dumps               | 9.82 ms                                                         | 7.23 ms: 1.36x faster                                                                    |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.42 ms: 1.34x faster                                                                    |
| pickle_pure_python       | 280 us                                                          | 214 us: 1.31x faster                                                                     |
| pycparser                | 1.04 sec                                                        | 798 ms: 1.31x faster                                                                     |
| raytrace                 | 303 ms                                                          | 235 ms: 1.29x faster                                                                     |
| go                       | 146 ms                                                          | 113 ms: 1.28x faster                                                                     |
| scimark_fft              | 216 ms                                                          | 169 ms: 1.28x faster                                                                     |
| deepcopy                 | 310 us                                                          | 243 us: 1.27x faster                                                                     |
| tomli_loads              | 1.91 sec                                                        | 1.50 sec: 1.27x faster                                                                   |
| sqlglot_transpile        | 1.58 ms                                                         | 1.25 ms: 1.27x faster                                                                    |
| hexiom                   | 6.13 ms                                                         | 4.86 ms: 1.26x faster                                                                    |
| unpickle_pure_python     | 189 us                                                          | 151 us: 1.26x faster                                                                     |
| richards_super           | 49.9 ms                                                         | 39.7 ms: 1.26x faster                                                                    |
| generators               | 31.6 ms                                                         | 25.2 ms: 1.25x faster                                                                    |
| regex_compile            | 117 ms                                                          | 94.0 ms: 1.24x faster                                                                    |
| thrift                   | 902 us                                                          | 759 us: 1.19x faster                                                                     |
| dulwich_log              | 58.5 ms                                                         | 49.4 ms: 1.19x faster                                                                    |
| richards                 | 40.3 ms                                                         | 34.4 ms: 1.17x faster                                                                    |
| scimark_lu               | 89.8 ms                                                         | 76.9 ms: 1.17x faster                                                                    |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.16x faster                                                                     |
| scimark_sor              | 115 ms                                                          | 101 ms: 1.14x faster                                                                     |
| pprint_pformat           | 1.37 sec                                                        | 1.20 sec: 1.14x faster                                                                   |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.8 ms: 1.13x faster                                                                    |
| bench_thread_pool        | 1.12 ms                                                         | 993 us: 1.13x faster                                                                     |
| meteor_contest           | 80.0 ms                                                         | 71.0 ms: 1.13x faster                                                                    |
| deepcopy_reduce          | 2.68 us                                                         | 2.39 us: 1.12x faster                                                                    |
| pprint_safe_repr         | 658 ms                                                          | 587 ms: 1.12x faster                                                                     |
| django_template          | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                                    |
| sympy_sum                | 122 ms                                                          | 110 ms: 1.11x faster                                                                     |
| html5lib                 | 52.1 ms                                                         | 46.9 ms: 1.11x faster                                                                    |
| tornado_http             | 118 ms                                                          | 106 ms: 1.11x faster                                                                     |
| json                     | 4.76 ms                                                         | 4.31 ms: 1.11x faster                                                                    |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                                     |
| asyncio_tcp              | 744 ms                                                          | 680 ms: 1.09x faster                                                                     |
| nqueens                  | 87.1 ms                                                         | 80.2 ms: 1.09x faster                                                                    |
| xml_etree_process        | 48.1 ms                                                         | 44.6 ms: 1.08x faster                                                                    |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                                   |
| sympy_str                | 229 ms                                                          | 218 ms: 1.05x faster                                                                     |
| xml_etree_generate       | 61.6 ms                                                         | 58.9 ms: 1.05x faster                                                                    |
| json_loads               | 22.4 us                                                         | 21.7 us: 1.03x faster                                                                    |
| 2to3                     | 265 ms                                                          | 259 ms: 1.03x faster                                                                     |
| sqlglot_optimize         | 44.7 ms                                                         | 43.7 ms: 1.02x faster                                                                    |
| sympy_integrate          | 16.6 ms                                                         | 16.3 ms: 1.02x faster                                                                    |
| sqlglot_normalize        | 230 ms                                                          | 227 ms: 1.01x faster                                                                     |
| sympy_expand             | 391 ms                                                          | 386 ms: 1.01x faster                                                                     |
| docutils                 | 1.95 sec                                                        | 1.94 sec: 1.01x faster                                                                   |
| regex_v8                 | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                                    |
| coroutines               | 17.9 ms                                                         | 18.3 ms: 1.02x slower                                                                    |
| genshi_xml               | 46.6 ms                                                         | 47.9 ms: 1.03x slower                                                                    |
| python_startup           | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                                    |
| logging_simple           | 7.29 us                                                         | 7.72 us: 1.06x slower                                                                    |
| logging_format           | 7.91 us                                                         | 8.38 us: 1.06x slower                                                                    |
| genshi_text              | 21.0 ms                                                         | 22.8 ms: 1.09x slower                                                                    |
| pathlib                  | 81.2 ms                                                         | 89.0 ms: 1.10x slower                                                                    |
| create_gc_cycles         | 694 us                                                          | 767 us: 1.10x slower                                                                     |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                                    |
| coverage                 | 46.6 ms                                                         | 52.0 ms: 1.12x slower                                                                    |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                                    |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                                    |
| bench_mp_pool            | 66.4 ms                                                         | 77.8 ms: 1.17x slower                                                                    |
| telco                    | 4.83 ms                                                         | 5.97 ms: 1.24x slower                                                                    |
| async_generators         | 241 ms                                                          | 332 ms: 1.38x slower                                                                     |
| Geometric mean           | (ref)                                                           | 1.21x faster                                                                             |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240801-3.14.0a0-dc5a9d5-JIT/bm-20240801-pythonperf1_win32-x86-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown