# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-x86
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 241 ms: 1.10x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.93 ms: 1.08x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                          |
| html5lib       | 52.1 ms                                                         | 47.0 ms: 1.11x faster                                                           |
| tornado_http   | 118 ms                                                          | 97.5 ms: 1.21x faster                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 468 ms: 1.97x faster                                                            |
| async_tree_io           | 940 ms                                                          | 522 ms: 1.80x faster                                                            |
| async_tree_none         | 394 ms                                                          | 221 ms: 1.78x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 272 ms: 1.72x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                            |
| float          | 69.6 ms                                                         | 53.8 ms: 1.29x faster                                                           |
| nbody          | 79.1 ms                                                         | 76.4 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.50x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 126 ms: 1.04x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.85 ms: 1.43x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 211 us: 1.33x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.59 sec: 1.20x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 161 us: 1.17x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 41.4 ms: 1.16x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.4 us: 1.10x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.76 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.7 ms: 1.08x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 59.1 ms: 1.04x faster                                                           |
| pickle               | 7.83 us                                                         | 7.73 us: 1.01x faster                                                           |
| unpickle             | 9.82 us                                                         | 9.99 us: 1.02x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.30 us: 1.02x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.5 ms: 1.02x faster                                                           |
| python_startup_no_site | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.85 ms: 1.33x faster                                                           |
| django_template | 36.0 ms                                                         | 30.3 ms: 1.19x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 20.5 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 89.5 us: 4.42x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 468 ms: 1.97x faster                                                            |
| async_tree_io            | 940 ms                                                          | 522 ms: 1.80x faster                                                            |
| async_tree_none          | 394 ms                                                          | 221 ms: 1.78x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.30 ms: 1.75x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 272 ms: 1.72x faster                                                            |
| pylint                   | 384 ms                                                          | 228 ms: 1.69x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 60.8 ns: 1.61x faster                                                           |
| richards_super           | 49.9 ms                                                         | 32.8 ms: 1.52x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 54.0 ms: 1.51x faster                                                           |
| chaos                    | 74.4 ms                                                         | 51.9 ms: 1.43x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.85 ms: 1.43x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 942 us: 1.41x faster                                                            |
| raytrace                 | 303 ms                                                          | 217 ms: 1.40x faster                                                            |
| richards                 | 40.3 ms                                                         | 29.2 ms: 1.38x faster                                                           |
| comprehensions           | 17.7 us                                                         | 12.9 us: 1.37x faster                                                           |
| generators               | 31.6 ms                                                         | 23.0 ms: 1.37x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 211 us: 1.33x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.85 ms: 1.33x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.20 ms: 1.32x faster                                                           |
| go                       | 146 ms                                                          | 113 ms: 1.29x faster                                                            |
| float                    | 69.6 ms                                                         | 53.8 ms: 1.29x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 47.9 ms: 1.29x faster                                                           |
| pyflate                  | 422 ms                                                          | 329 ms: 1.28x faster                                                            |
| scimark_sor              | 115 ms                                                          | 91.6 ms: 1.26x faster                                                           |
| pycparser                | 1.04 sec                                                        | 838 ms: 1.24x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.7 ms: 1.22x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 24.4 us: 1.21x faster                                                           |
| fannkuch                 | 317 ms                                                          | 261 ms: 1.21x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 617 ms: 1.21x faster                                                            |
| tornado_http             | 118 ms                                                          | 97.5 ms: 1.21x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.59 sec: 1.20x faster                                                          |
| django_template          | 36.0 ms                                                         | 30.3 ms: 1.19x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.18x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 161 us: 1.17x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.25 ms: 1.17x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 41.4 ms: 1.16x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.18 sec: 1.16x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 574 ms: 1.15x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 76.0 ms: 1.15x faster                                                           |
| json                     | 4.76 ms                                                         | 4.17 ms: 1.14x faster                                                           |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.14x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.61 sec: 1.13x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 79.6 ms: 1.13x faster                                                           |
| deepcopy                 | 310 us                                                          | 275 us: 1.13x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 72.3 ms: 1.11x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 47.0 ms: 1.11x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.44 us: 1.10x faster                                                           |
| 2to3                     | 265 ms                                                          | 241 ms: 1.10x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.4 us: 1.10x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.09x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.2 ms: 1.09x faster                                                           |
| chameleon                | 6.42 ms                                                         | 5.93 ms: 1.08x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.76 us: 1.08x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.7 ms: 1.08x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.01 ms: 1.08x faster                                                           |
| sympy_str                | 229 ms                                                          | 213 ms: 1.07x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 215 ms: 1.07x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 42.0 ms: 1.06x faster                                                           |
| create_gc_cycles         | 694 us                                                          | 652 us: 1.06x faster                                                            |
| scimark_fft              | 216 ms                                                          | 205 ms: 1.05x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 76.5 ms: 1.05x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 59.1 ms: 1.04x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                          |
| regex_dna                | 131 ms                                                          | 126 ms: 1.04x faster                                                            |
| sympy_expand             | 391 ms                                                          | 377 ms: 1.04x faster                                                            |
| nbody                    | 79.1 ms                                                         | 76.4 ms: 1.04x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 20.5 ms: 1.03x faster                                                           |
| python_startup           | 22.9 ms                                                         | 22.5 ms: 1.02x faster                                                           |
| pickle                   | 7.83 us                                                         | 7.73 us: 1.01x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                          |
| unpickle                 | 9.82 us                                                         | 9.99 us: 1.02x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.30 us: 1.02x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 41.6 ns: 1.04x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 69.5 ms: 1.05x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 86.0 ms: 1.06x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.47 us: 1.07x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.38 ms: 1.08x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.88 us: 1.08x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                           |
| async_generators         | 241 ms                                                          | 270 ms: 1.12x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.03 ms: 1.25x slower                                                           |
| coverage                 | 46.6 ms                                                         | 469 ms: 10.08x slower                                                           |
| thrift                   | 902 us                                                          | 11.0 ms: 12.23x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                                    |

Benchmark hidden because not significant (2): genshi_xml, regex_compile
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240323-3.13.0a5+-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x


# Memory

- memory change: unknown