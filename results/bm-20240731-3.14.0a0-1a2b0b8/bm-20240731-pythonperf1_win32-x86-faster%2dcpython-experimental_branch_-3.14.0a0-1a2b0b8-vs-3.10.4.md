# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-x86
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.11x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 258 ms: 1.03x faster                                                                     |
| docutils       | 1.95 sec                                                        | 1.92 sec: 1.01x faster                                                                   |
| html5lib       | 52.1 ms                                                         | 49.5 ms: 1.05x faster                                                                    |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 474 ms: 1.95x faster                                                                     |
| async_tree_none         | 394 ms                                                          | 230 ms: 1.71x faster                                                                     |
| async_tree_io           | 940 ms                                                          | 559 ms: 1.68x faster                                                                     |
| async_tree_memoization  | 467 ms                                                          | 280 ms: 1.67x faster                                                                     |
| Geometric mean          | (ref)                                                           | 1.75x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                                     |
| float          | 69.6 ms                                                         | 61.5 ms: 1.13x faster                                                                    |
| nbody          | 79.1 ms                                                         | 93.6 ms: 1.18x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                                     |
| regex_compile  | 117 ms                                                          | 110 ms: 1.06x faster                                                                     |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                                    |
| regex_effbot   | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.63 ms: 1.29x faster                                                                    |
| xml_etree_parse      | 120 ms                                                          | 106 ms: 1.13x faster                                                                     |
| json_loads           | 22.4 us                                                         | 20.2 us: 1.11x faster                                                                    |
| pickle_pure_python   | 280 us                                                          | 257 us: 1.09x faster                                                                     |
| unpickle_pure_python | 189 us                                                          | 181 us: 1.05x faster                                                                     |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.7 ms: 1.03x faster                                                                    |
| xml_etree_process    | 48.1 ms                                                         | 50.2 ms: 1.04x slower                                                                    |
| xml_etree_generate   | 61.6 ms                                                         | 66.8 ms: 1.08x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                             |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                                    |
| python_startup_no_site | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.15 ms: 1.12x faster                                                                    |
| django_template | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                                    |
| genshi_xml      | 46.6 ms                                                         | 49.3 ms: 1.06x slower                                                                    |
| genshi_text     | 21.0 ms                                                         | 23.5 ms: 1.12x slower                                                                    |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 151 us: 2.62x faster                                                                     |
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                                     |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 474 ms: 1.95x faster                                                                     |
| async_tree_none          | 394 ms                                                          | 230 ms: 1.71x faster                                                                     |
| async_tree_io            | 940 ms                                                          | 559 ms: 1.68x faster                                                                     |
| async_tree_memoization   | 467 ms                                                          | 280 ms: 1.67x faster                                                                     |
| pylint                   | 384 ms                                                          | 236 ms: 1.63x faster                                                                     |
| deltablue                | 4.04 ms                                                         | 2.75 ms: 1.47x faster                                                                    |
| chaos                    | 74.4 ms                                                         | 52.2 ms: 1.43x faster                                                                    |
| crypto_pyaes             | 81.3 ms                                                         | 58.6 ms: 1.39x faster                                                                    |
| raytrace                 | 303 ms                                                          | 226 ms: 1.34x faster                                                                     |
| scimark_lu               | 89.8 ms                                                         | 68.4 ms: 1.31x faster                                                                    |
| json_dumps               | 9.82 ms                                                         | 7.63 ms: 1.29x faster                                                                    |
| logging_silent           | 97.9 ns                                                         | 76.2 ns: 1.28x faster                                                                    |
| deepcopy_memo            | 29.6 us                                                         | 23.4 us: 1.27x faster                                                                    |
| sqlglot_parse            | 1.33 ms                                                         | 1.07 ms: 1.24x faster                                                                    |
| comprehensions           | 17.7 us                                                         | 14.3 us: 1.24x faster                                                                    |
| deepcopy                 | 310 us                                                          | 256 us: 1.21x faster                                                                     |
| pycparser                | 1.04 sec                                                        | 873 ms: 1.19x faster                                                                     |
| sqlglot_transpile        | 1.58 ms                                                         | 1.33 ms: 1.19x faster                                                                    |
| scimark_sor              | 115 ms                                                          | 98.0 ms: 1.17x faster                                                                    |
| thrift                   | 902 us                                                          | 769 us: 1.17x faster                                                                     |
| go                       | 146 ms                                                          | 125 ms: 1.17x faster                                                                     |
| dulwich_log              | 58.5 ms                                                         | 50.5 ms: 1.16x faster                                                                    |
| pyflate                  | 422 ms                                                          | 364 ms: 1.16x faster                                                                     |
| richards_super           | 49.9 ms                                                         | 43.3 ms: 1.15x faster                                                                    |
| hexiom                   | 6.13 ms                                                         | 5.36 ms: 1.14x faster                                                                    |
| generators               | 31.6 ms                                                         | 27.7 ms: 1.14x faster                                                                    |
| json                     | 4.76 ms                                                         | 4.19 ms: 1.14x faster                                                                    |
| nqueens                  | 87.1 ms                                                         | 76.8 ms: 1.13x faster                                                                    |
| xml_etree_parse          | 120 ms                                                          | 106 ms: 1.13x faster                                                                     |
| float                    | 69.6 ms                                                         | 61.5 ms: 1.13x faster                                                                    |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                                     |
| mako                     | 9.10 ms                                                         | 8.15 ms: 1.12x faster                                                                    |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                                    |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.8 ms: 1.11x faster                                                                    |
| sympy_sum                | 122 ms                                                          | 110 ms: 1.11x faster                                                                     |
| json_loads               | 22.4 us                                                         | 20.2 us: 1.11x faster                                                                    |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                                     |
| pickle_pure_python       | 280 us                                                          | 257 us: 1.09x faster                                                                     |
| mdp                      | 1.83 sec                                                        | 1.69 sec: 1.08x faster                                                                   |
| sympy_integrate          | 16.6 ms                                                         | 15.7 ms: 1.06x faster                                                                    |
| regex_compile            | 117 ms                                                          | 110 ms: 1.06x faster                                                                     |
| asyncio_tcp              | 744 ms                                                          | 702 ms: 1.06x faster                                                                     |
| django_template          | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                                    |
| html5lib                 | 52.1 ms                                                         | 49.5 ms: 1.05x faster                                                                    |
| richards                 | 40.3 ms                                                         | 38.3 ms: 1.05x faster                                                                    |
| unpickle_pure_python     | 189 us                                                          | 181 us: 1.05x faster                                                                     |
| coroutines               | 17.9 ms                                                         | 17.4 ms: 1.03x faster                                                                    |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.7 ms: 1.03x faster                                                                    |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.14 ms: 1.03x faster                                                                    |
| deepcopy_reduce          | 2.68 us                                                         | 2.60 us: 1.03x faster                                                                    |
| 2to3                     | 265 ms                                                          | 258 ms: 1.03x faster                                                                     |
| sympy_str                | 229 ms                                                          | 225 ms: 1.02x faster                                                                     |
| fannkuch                 | 317 ms                                                          | 311 ms: 1.02x faster                                                                     |
| docutils                 | 1.95 sec                                                        | 1.92 sec: 1.01x faster                                                                   |
| sqlglot_optimize         | 44.7 ms                                                         | 45.0 ms: 1.01x slower                                                                    |
| sympy_expand             | 391 ms                                                          | 395 ms: 1.01x slower                                                                     |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                                    |
| sqlglot_normalize        | 230 ms                                                          | 236 ms: 1.02x slower                                                                     |
| pprint_pformat           | 1.37 sec                                                        | 1.41 sec: 1.03x slower                                                                   |
| python_startup           | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                                    |
| meteor_contest           | 80.0 ms                                                         | 83.2 ms: 1.04x slower                                                                    |
| xml_etree_process        | 48.1 ms                                                         | 50.2 ms: 1.04x slower                                                                    |
| pprint_safe_repr         | 658 ms                                                          | 693 ms: 1.05x slower                                                                     |
| genshi_xml               | 46.6 ms                                                         | 49.3 ms: 1.06x slower                                                                    |
| scimark_fft              | 216 ms                                                          | 230 ms: 1.06x slower                                                                     |
| create_gc_cycles         | 694 us                                                          | 746 us: 1.08x slower                                                                     |
| python_startup_no_site   | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                                    |
| xml_etree_generate       | 61.6 ms                                                         | 66.8 ms: 1.08x slower                                                                    |
| pathlib                  | 81.2 ms                                                         | 88.5 ms: 1.09x slower                                                                    |
| logging_format           | 7.91 us                                                         | 8.72 us: 1.10x slower                                                                    |
| bench_mp_pool            | 66.4 ms                                                         | 73.8 ms: 1.11x slower                                                                    |
| logging_simple           | 7.29 us                                                         | 8.13 us: 1.12x slower                                                                    |
| coverage                 | 46.6 ms                                                         | 52.1 ms: 1.12x slower                                                                    |
| genshi_text              | 21.0 ms                                                         | 23.5 ms: 1.12x slower                                                                    |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.13x slower                                                                    |
| regex_effbot             | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                                    |
| nbody                    | 79.1 ms                                                         | 93.6 ms: 1.18x slower                                                                    |
| telco                    | 4.83 ms                                                         | 6.21 ms: 1.29x slower                                                                    |
| async_generators         | 241 ms                                                          | 311 ms: 1.29x slower                                                                     |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                             |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, tomli_loads, spectral_norm
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-pythonperf1_win32-x86-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown