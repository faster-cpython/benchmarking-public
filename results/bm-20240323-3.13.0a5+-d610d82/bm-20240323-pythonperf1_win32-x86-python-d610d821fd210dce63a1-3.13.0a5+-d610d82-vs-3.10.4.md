# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-x86
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 228 ms: 1.16x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.65 ms: 1.14x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.75 sec: 1.12x faster                                                          |
| html5lib       | 52.1 ms                                                         | 42.6 ms: 1.22x faster                                                           |
| tornado_http   | 118 ms                                                          | 93.9 ms: 1.25x faster                                                           |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 461 ms: 2.00x faster                                                            |
| async_tree_none         | 394 ms                                                          | 215 ms: 1.83x faster                                                            |
| async_tree_io           | 940 ms                                                          | 520 ms: 1.81x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 265 ms: 1.76x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.85x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                            |
| float          | 69.6 ms                                                         | 51.5 ms: 1.35x faster                                                           |
| nbody          | 79.1 ms                                                         | 77.3 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.52x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 94.4 ms: 1.24x faster                                                           |
| regex_dna      | 131 ms                                                          | 118 ms: 1.10x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.60 ms: 1.49x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 139 us: 1.36x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 211 us: 1.33x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 40.8 ms: 1.18x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.0 us: 1.12x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.7 ms: 1.09x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.81 us: 1.06x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 59.1 ms: 1.04x faster                                                           |
| unpickle             | 9.82 us                                                         | 9.75 us: 1.01x faster                                                           |
| pickle_list          | 3.22 us                                                         | 3.34 us: 1.04x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.2 us: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.3 ms: 1.03x faster                                                           |
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.83 ms: 1.33x faster                                                           |
| django_template | 36.0 ms                                                         | 28.6 ms: 1.26x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 40.1 ms: 1.16x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 18.4 ms: 1.14x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.22x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 89.9 us: 4.40x faster                                                           |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 461 ms: 2.00x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.13 ms: 1.89x faster                                                           |
| async_tree_none          | 394 ms                                                          | 215 ms: 1.83x faster                                                            |
| async_tree_io            | 940 ms                                                          | 520 ms: 1.81x faster                                                            |
| pylint                   | 384 ms                                                          | 216 ms: 1.78x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 265 ms: 1.76x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 57.3 ns: 1.71x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 52.1 ms: 1.56x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.4 us: 1.55x faster                                                           |
| chaos                    | 74.4 ms                                                         | 48.0 ms: 1.55x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 859 us: 1.55x faster                                                            |
| richards_super           | 49.9 ms                                                         | 32.4 ms: 1.54x faster                                                           |
| raytrace                 | 303 ms                                                          | 198 ms: 1.53x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 59.8 ms: 1.50x faster                                                           |
| go                       | 146 ms                                                          | 97.5 ms: 1.49x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.60 ms: 1.49x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.19 ms: 1.46x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.08 ms: 1.46x faster                                                           |
| generators               | 31.6 ms                                                         | 22.3 ms: 1.41x faster                                                           |
| scimark_sor              | 115 ms                                                          | 82.2 ms: 1.40x faster                                                           |
| richards                 | 40.3 ms                                                         | 28.9 ms: 1.39x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 45.4 ms: 1.36x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 139 us: 1.36x faster                                                            |
| pyflate                  | 422 ms                                                          | 312 ms: 1.35x faster                                                            |
| float                    | 69.6 ms                                                         | 51.5 ms: 1.35x faster                                                           |
| pycparser                | 1.04 sec                                                        | 776 ms: 1.34x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.83 ms: 1.33x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 211 us: 1.33x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 23.0 us: 1.28x faster                                                           |
| django_template          | 36.0 ms                                                         | 28.6 ms: 1.26x faster                                                           |
| tornado_http             | 118 ms                                                          | 93.9 ms: 1.25x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 69.8 ms: 1.25x faster                                                           |
| sympy_sum                | 122 ms                                                          | 98.9 ms: 1.24x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.11 sec: 1.24x faster                                                          |
| regex_compile            | 117 ms                                                          | 94.4 ms: 1.24x faster                                                           |
| coroutines               | 17.9 ms                                                         | 14.6 ms: 1.23x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 42.6 ms: 1.22x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 540 ms: 1.22x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 66.6 ms: 1.20x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 13.9 ms: 1.19x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 629 ms: 1.18x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 40.8 ms: 1.18x faster                                                           |
| deepcopy                 | 310 us                                                          | 263 us: 1.18x faster                                                            |
| sympy_str                | 229 ms                                                          | 194 ms: 1.18x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 196 ms: 1.18x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 38.1 ms: 1.17x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.56 sec: 1.17x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 963 us: 1.16x faster                                                            |
| 2to3                     | 265 ms                                                          | 228 ms: 1.16x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 40.1 ms: 1.16x faster                                                           |
| fannkuch                 | 317 ms                                                          | 276 ms: 1.15x faster                                                            |
| json                     | 4.76 ms                                                         | 4.16 ms: 1.14x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 18.4 ms: 1.14x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.35 us: 1.14x faster                                                           |
| sympy_expand             | 391 ms                                                          | 342 ms: 1.14x faster                                                            |
| chameleon                | 6.42 ms                                                         | 5.65 ms: 1.14x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.0 us: 1.12x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.89 ms: 1.12x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.75 sec: 1.12x faster                                                          |
| regex_dna                | 131 ms                                                          | 118 ms: 1.10x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.7 ms: 1.09x faster                                                           |
| create_gc_cycles         | 694 us                                                          | 646 us: 1.07x faster                                                            |
| scimark_fft              | 216 ms                                                          | 202 ms: 1.07x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 75.1 ms: 1.07x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.81 us: 1.06x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 59.1 ms: 1.04x faster                                                           |
| python_startup           | 22.9 ms                                                         | 22.3 ms: 1.03x faster                                                           |
| nbody                    | 79.1 ms                                                         | 77.3 ms: 1.02x faster                                                           |
| unpack_sequence          | 40.0 ns                                                         | 39.3 ns: 1.02x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.7 sec: 1.01x faster                                                          |
| unpickle                 | 9.82 us                                                         | 9.75 us: 1.01x faster                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 68.1 ms: 1.03x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.34 us: 1.04x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.28 us: 1.05x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.64 us: 1.05x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 86.3 ms: 1.06x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.40 ms: 1.09x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.2 us: 1.11x slower                                                           |
| async_generators         | 241 ms                                                          | 267 ms: 1.11x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.17 ms: 1.28x slower                                                           |
| coverage                 | 46.6 ms                                                         | 476 ms: 10.22x slower                                                           |
| thrift                   | 902 us                                                          | 9.78 ms: 10.84x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.18x faster                                                                    |

Benchmark hidden because not significant (2): pickle, regex_v8
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x


# Memory

- memory change: unknown