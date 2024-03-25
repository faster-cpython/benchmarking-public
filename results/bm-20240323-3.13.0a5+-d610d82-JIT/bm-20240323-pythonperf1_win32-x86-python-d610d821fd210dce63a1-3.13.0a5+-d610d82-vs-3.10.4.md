# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-x86
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.05x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 262 ms: 1.01x faster                                                            |
| chameleon      | 6.42 ms                                                         | 6.15 ms: 1.04x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                          |
| html5lib       | 52.1 ms                                                         | 46.6 ms: 1.12x faster                                                           |
| tornado_http   | 118 ms                                                          | 99.2 ms: 1.18x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 515 ms: 1.79x faster                                                            |
| async_tree_io           | 940 ms                                                          | 559 ms: 1.68x faster                                                            |
| async_tree_none         | 394 ms                                                          | 237 ms: 1.66x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 292 ms: 1.60x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.68x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| float          | 69.6 ms                                                         | 52.7 ms: 1.32x faster                                                           |
| nbody          | 79.1 ms                                                         | 97.1 ms: 1.23x slower                                                           |
| Geometric mean | (ref)                                                           | 1.39x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                            |
| regex_compile  | 117 ms                                                          | 113 ms: 1.03x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.81 ms: 1.44x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 224 us: 1.25x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 168 us: 1.13x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.71 sec: 1.11x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.3 us: 1.10x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.72 us: 1.10x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 44.0 ms: 1.09x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.7 ms: 1.06x faster                                                           |
| pickle               | 7.83 us                                                         | 7.88 us: 1.01x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 62.4 ms: 1.01x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.0 us: 1.02x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                    |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 23.3 ms: 1.29x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.21x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.20 ms: 1.26x faster                                                           |
| django_template | 36.0 ms                                                         | 32.7 ms: 1.10x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 49.8 ms: 1.07x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 23.8 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 93.9 us: 4.21x faster                                                           |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 515 ms: 1.79x faster                                                            |
| async_tree_io            | 940 ms                                                          | 559 ms: 1.68x faster                                                            |
| async_tree_none          | 394 ms                                                          | 237 ms: 1.66x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 292 ms: 1.60x faster                                                            |
| pylint                   | 384 ms                                                          | 240 ms: 1.60x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.62 ms: 1.54x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.81 ms: 1.44x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 69.4 ns: 1.41x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 61.0 ms: 1.33x faster                                                           |
| float                    | 69.6 ms                                                         | 52.7 ms: 1.32x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.03 ms: 1.30x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.20 ms: 1.26x faster                                                           |
| generators               | 31.6 ms                                                         | 25.0 ms: 1.26x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 224 us: 1.25x faster                                                            |
| chaos                    | 74.4 ms                                                         | 59.7 ms: 1.25x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.28 ms: 1.24x faster                                                           |
| pycparser                | 1.04 sec                                                        | 854 ms: 1.22x faster                                                            |
| richards_super           | 49.9 ms                                                         | 41.3 ms: 1.21x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                           |
| coroutines               | 17.9 ms                                                         | 15.1 ms: 1.19x faster                                                           |
| tornado_http             | 118 ms                                                          | 99.2 ms: 1.18x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 634 ms: 1.17x faster                                                            |
| json                     | 4.76 ms                                                         | 4.11 ms: 1.16x faster                                                           |
| go                       | 146 ms                                                          | 127 ms: 1.15x faster                                                            |
| comprehensions           | 17.7 us                                                         | 15.6 us: 1.14x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 168 us: 1.13x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 71.6 ms: 1.12x faster                                                           |
| pyflate                  | 422 ms                                                          | 377 ms: 1.12x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 46.6 ms: 1.12x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.71 sec: 1.11x faster                                                          |
| scimark_sor              | 115 ms                                                          | 103 ms: 1.11x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| richards                 | 40.3 ms                                                         | 36.3 ms: 1.11x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.10x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.3 us: 1.10x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.7 ms: 1.10x faster                                                           |
| sympy_sum                | 122 ms                                                          | 111 ms: 1.10x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.72 us: 1.10x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 44.0 ms: 1.09x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 27.3 us: 1.08x faster                                                           |
| raytrace                 | 303 ms                                                          | 280 ms: 1.08x faster                                                            |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                            |
| create_gc_cycles         | 694 us                                                          | 646 us: 1.07x faster                                                            |
| deepcopy                 | 310 us                                                          | 289 us: 1.07x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.7 ms: 1.06x faster                                                           |
| sympy_str                | 229 ms                                                          | 217 ms: 1.06x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 85.0 ms: 1.06x faster                                                           |
| chameleon                | 6.42 ms                                                         | 6.15 ms: 1.04x faster                                                           |
| sympy_expand             | 391 ms                                                          | 375 ms: 1.04x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.59 us: 1.04x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.14 ms: 1.03x faster                                                           |
| regex_compile            | 117 ms                                                          | 113 ms: 1.03x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.79 sec: 1.02x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.7 sec: 1.02x faster                                                          |
| 2to3                     | 265 ms                                                          | 262 ms: 1.01x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 6.07 ms: 1.01x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                          |
| pickle                   | 7.83 us                                                         | 7.88 us: 1.01x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 62.4 ms: 1.01x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.0 us: 1.02x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 46.2 ms: 1.03x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 83.3 ms: 1.04x slower                                                           |
| sqlglot_normalize        | 230 ms                                                          | 240 ms: 1.04x slower                                                            |
| nqueens                  | 87.1 ms                                                         | 92.2 ms: 1.06x slower                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 65.6 ms: 1.06x slower                                                           |
| fannkuch                 | 317 ms                                                          | 337 ms: 1.06x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 86.4 ms: 1.06x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 49.8 ms: 1.07x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.38 ms: 1.08x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.09x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.50 sec: 1.10x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 44.3 ns: 1.11x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 731 ms: 1.11x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 74.1 ms: 1.12x slower                                                           |
| scimark_fft              | 216 ms                                                          | 244 ms: 1.13x slower                                                            |
| genshi_text              | 21.0 ms                                                         | 23.8 ms: 1.13x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.06 us: 1.15x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.44 us: 1.16x slower                                                           |
| async_generators         | 241 ms                                                          | 293 ms: 1.21x slower                                                            |
| nbody                    | 79.1 ms                                                         | 97.1 ms: 1.23x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 23.3 ms: 1.29x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.46 ms: 1.34x slower                                                           |
| coverage                 | 46.6 ms                                                         | 484 ms: 10.40x slower                                                           |
| thrift                   | 902 us                                                          | 11.0 ms: 12.21x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (2): sympy_integrate, pickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: unknown