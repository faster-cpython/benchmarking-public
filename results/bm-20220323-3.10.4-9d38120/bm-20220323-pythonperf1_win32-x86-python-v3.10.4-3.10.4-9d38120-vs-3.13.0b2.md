# Results vs. 3.13.0b2

- fork: python
- ref: v3.10.4
- machine: windows-x86
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 265 ms: 1.14x slower                                            |
| chameleon      | 5.71 ms                                                             | 6.42 ms: 1.12x slower                                           |
| docutils       | 1.81 sec                                                            | 1.95 sec: 1.08x slower                                          |
| html5lib       | 45.4 ms                                                             | 52.1 ms: 1.15x slower                                           |
| tornado_http   | 94.3 ms                                                             | 118 ms: 1.25x slower                                            |
| Geometric mean | (ref)                                                               | 1.14x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization  | 275 ms                                                              | 467 ms: 1.70x slower                                            |
| async_tree_none         | 228 ms                                                              | 394 ms: 1.73x slower                                            |
| async_tree_io           | 530 ms                                                              | 940 ms: 1.77x slower                                            |
| async_tree_cpu_io_mixed | 471 ms                                                              | 922 ms: 1.96x slower                                            |
| Geometric mean          | (ref)                                                               | 1.79x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 79.1 ms: 1.03x slower                                           |
| float          | 52.4 ms                                                             | 69.6 ms: 1.33x slower                                           |
| pidigits       | 199 ms                                                              | 502 ms: 2.53x slower                                            |
| Geometric mean | (ref)                                                               | 1.51x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.66 ms: 1.13x faster                                           |
| regex_dna      | 118 ms                                                              | 131 ms: 1.11x slower                                            |
| regex_compile  | 99.9 ms                                                             | 117 ms: 1.17x slower                                            |
| Geometric mean | (ref)                                                               | 1.03x slower                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_dict          | 20.8 us                                                             | 18.2 us: 1.14x faster                                           |
| pickle_list          | 3.57 us                                                             | 3.22 us: 1.11x faster                                           |
| pickle               | 8.07 us                                                             | 7.83 us: 1.03x faster                                           |
| unpickle_list        | 2.93 us                                                             | 2.98 us: 1.02x slower                                           |
| xml_etree_generate   | 59.6 ms                                                             | 61.6 ms: 1.03x slower                                           |
| json_loads           | 20.5 us                                                             | 22.4 us: 1.09x slower                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 70.8 ms: 1.10x slower                                           |
| xml_etree_process    | 42.1 ms                                                             | 48.1 ms: 1.14x slower                                           |
| xml_etree_parse      | 104 ms                                                              | 120 ms: 1.15x slower                                            |
| tomli_loads          | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                          |
| unpickle_pure_python | 147 us                                                              | 189 us: 1.29x slower                                            |
| pickle_pure_python   | 213 us                                                              | 280 us: 1.31x slower                                            |
| json_dumps           | 6.84 ms                                                             | 9.82 ms: 1.44x slower                                           |
| Geometric mean       | (ref)                                                               | 1.10x slower                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 18.1 ms: 1.01x faster                                           |
| python_startup         | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                           |
| Geometric mean         | (ref)                                                               | 1.01x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 21.0 ms: 1.04x slower                                           |
| genshi_xml      | 44.3 ms                                                             | 46.6 ms: 1.05x slower                                           |
| django_template | 30.1 ms                                                             | 36.0 ms: 1.20x slower                                           |
| mako            | 6.94 ms                                                             | 9.10 ms: 1.31x slower                                           |
| Geometric mean  | (ref)                                                               | 1.15x slower                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| thrift                   | 9.73 ms                                                             | 902 us: 10.78x faster                                           |
| coverage                 | 307 ms                                                              | 46.6 ms: 6.60x faster                                           |
| telco                    | 6.03 ms                                                             | 4.83 ms: 1.25x faster                                           |
| pickle_dict              | 20.8 us                                                             | 18.2 us: 1.14x faster                                           |
| regex_effbot             | 1.88 ms                                                             | 1.66 ms: 1.13x faster                                           |
| gc_traversal             | 1.43 ms                                                             | 1.28 ms: 1.12x faster                                           |
| pickle_list              | 3.57 us                                                             | 3.22 us: 1.11x faster                                           |
| async_generators         | 266 ms                                                              | 241 ms: 1.10x faster                                            |
| create_gc_cycles         | 756 us                                                              | 694 us: 1.09x faster                                            |
| bench_mp_pool            | 69.4 ms                                                             | 66.4 ms: 1.05x faster                                           |
| pathlib                  | 83.9 ms                                                             | 81.2 ms: 1.03x faster                                           |
| pickle                   | 8.07 us                                                             | 7.83 us: 1.03x faster                                           |
| logging_format           | 8.13 us                                                             | 7.91 us: 1.03x faster                                           |
| logging_simple           | 7.47 us                                                             | 7.29 us: 1.02x faster                                           |
| python_startup_no_site   | 18.2 ms                                                             | 18.1 ms: 1.01x faster                                           |
| flaskblogging            | 2.03 sec                                                            | 2.03 sec: 1.00x faster                                          |
| asyncio_tcp_ssl          | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                          |
| unpickle_list            | 2.93 us                                                             | 2.98 us: 1.02x slower                                           |
| nbody                    | 76.9 ms                                                             | 79.1 ms: 1.03x slower                                           |
| python_startup           | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                           |
| xml_etree_generate       | 59.6 ms                                                             | 61.6 ms: 1.03x slower                                           |
| deepcopy_reduce          | 2.59 us                                                             | 2.68 us: 1.04x slower                                           |
| sympy_expand             | 375 ms                                                              | 391 ms: 1.04x slower                                            |
| genshi_text              | 20.1 ms                                                             | 21.0 ms: 1.04x slower                                           |
| genshi_xml               | 44.3 ms                                                             | 46.6 ms: 1.05x slower                                           |
| docutils                 | 1.81 sec                                                            | 1.95 sec: 1.08x slower                                          |
| meteor_contest           | 74.1 ms                                                             | 80.0 ms: 1.08x slower                                           |
| pprint_safe_repr         | 607 ms                                                              | 658 ms: 1.09x slower                                            |
| sympy_str                | 211 ms                                                              | 229 ms: 1.09x slower                                            |
| json_loads               | 20.5 us                                                             | 22.4 us: 1.09x slower                                           |
| scimark_fft              | 198 ms                                                              | 216 ms: 1.09x slower                                            |
| pprint_pformat           | 1.24 sec                                                            | 1.37 sec: 1.10x slower                                          |
| xml_etree_iterparse      | 64.2 ms                                                             | 70.8 ms: 1.10x slower                                           |
| regex_dna                | 118 ms                                                              | 131 ms: 1.11x slower                                            |
| deepcopy                 | 280 us                                                              | 310 us: 1.11x slower                                            |
| sqlglot_normalize        | 206 ms                                                              | 230 ms: 1.12x slower                                            |
| chameleon                | 5.71 ms                                                             | 6.42 ms: 1.12x slower                                           |
| asyncio_tcp              | 662 ms                                                              | 744 ms: 1.12x slower                                            |
| sqlglot_optimize         | 39.7 ms                                                             | 44.7 ms: 1.13x slower                                           |
| scimark_sparse_mat_mult  | 2.87 ms                                                             | 3.24 ms: 1.13x slower                                           |
| sympy_integrate          | 14.6 ms                                                             | 16.6 ms: 1.14x slower                                           |
| bench_thread_pool        | 985 us                                                              | 1.12 ms: 1.14x slower                                           |
| 2to3                     | 233 ms                                                              | 265 ms: 1.14x slower                                            |
| mdp                      | 1.60 sec                                                            | 1.83 sec: 1.14x slower                                          |
| xml_etree_process        | 42.1 ms                                                             | 48.1 ms: 1.14x slower                                           |
| html5lib                 | 45.4 ms                                                             | 52.1 ms: 1.15x slower                                           |
| xml_etree_parse          | 104 ms                                                              | 120 ms: 1.15x slower                                            |
| coroutines               | 15.5 ms                                                             | 17.9 ms: 1.16x slower                                           |
| tomli_loads              | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                          |
| json                     | 4.10 ms                                                             | 4.76 ms: 1.16x slower                                           |
| sympy_sum                | 105 ms                                                              | 122 ms: 1.17x slower                                            |
| sqlite_synth             | 1.96 us                                                             | 2.29 us: 1.17x slower                                           |
| regex_compile            | 99.9 ms                                                             | 117 ms: 1.17x slower                                            |
| fannkuch                 | 270 ms                                                              | 317 ms: 1.17x slower                                            |
| spectral_norm            | 68.0 ms                                                             | 80.2 ms: 1.18x slower                                           |
| django_template          | 30.1 ms                                                             | 36.0 ms: 1.20x slower                                           |
| tornado_http             | 94.3 ms                                                             | 118 ms: 1.25x slower                                            |
| deepcopy_memo            | 23.5 us                                                             | 29.6 us: 1.26x slower                                           |
| nqueens                  | 68.7 ms                                                             | 87.1 ms: 1.27x slower                                           |
| unpickle_pure_python     | 147 us                                                              | 189 us: 1.29x slower                                            |
| richards                 | 31.2 ms                                                             | 40.3 ms: 1.29x slower                                           |
| mako                     | 6.94 ms                                                             | 9.10 ms: 1.31x slower                                           |
| pickle_pure_python       | 213 us                                                              | 280 us: 1.31x slower                                            |
| float                    | 52.4 ms                                                             | 69.6 ms: 1.33x slower                                           |
| sqlglot_transpile        | 1.19 ms                                                             | 1.58 ms: 1.33x slower                                           |
| pycparser                | 777 ms                                                              | 1.04 sec: 1.34x slower                                          |
| pyflate                  | 308 ms                                                              | 422 ms: 1.37x slower                                            |
| scimark_monte_carlo      | 45.2 ms                                                             | 61.9 ms: 1.37x slower                                           |
| sqlglot_parse            | 964 us                                                              | 1.33 ms: 1.38x slower                                           |
| richards_super           | 35.5 ms                                                             | 49.9 ms: 1.41x slower                                           |
| scimark_sor              | 81.0 ms                                                             | 115 ms: 1.42x slower                                            |
| json_dumps               | 6.84 ms                                                             | 9.82 ms: 1.44x slower                                           |
| go                       | 101 ms                                                              | 146 ms: 1.45x slower                                            |
| hexiom                   | 4.23 ms                                                             | 6.13 ms: 1.45x slower                                           |
| crypto_pyaes             | 55.8 ms                                                             | 81.3 ms: 1.46x slower                                           |
| generators               | 21.2 ms                                                             | 31.6 ms: 1.49x slower                                           |
| comprehensions           | 11.9 us                                                             | 17.7 us: 1.50x slower                                           |
| scimark_lu               | 59.4 ms                                                             | 89.8 ms: 1.51x slower                                           |
| chaos                    | 48.0 ms                                                             | 74.4 ms: 1.55x slower                                           |
| raytrace                 | 189 ms                                                              | 303 ms: 1.60x slower                                            |
| logging_silent           | 57.9 ns                                                             | 97.9 ns: 1.69x slower                                           |
| async_tree_memoization   | 275 ms                                                              | 467 ms: 1.70x slower                                            |
| async_tree_none          | 228 ms                                                              | 394 ms: 1.73x slower                                            |
| pylint                   | 217 ms                                                              | 384 ms: 1.77x slower                                            |
| async_tree_io            | 530 ms                                                              | 940 ms: 1.77x slower                                            |
| deltablue                | 2.23 ms                                                             | 4.04 ms: 1.81x slower                                           |
| async_tree_cpu_io_mixed  | 471 ms                                                              | 922 ms: 1.96x slower                                            |
| pidigits                 | 199 ms                                                              | 502 ms: 2.53x slower                                            |
| typing_runtime_protocols | 136 us                                                              | 396 us: 2.92x slower                                            |
| Geometric mean           | (ref)                                                               | 1.15x slower                                                    |

Benchmark hidden because not significant (2): regex_v8, unpickle
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: unknown