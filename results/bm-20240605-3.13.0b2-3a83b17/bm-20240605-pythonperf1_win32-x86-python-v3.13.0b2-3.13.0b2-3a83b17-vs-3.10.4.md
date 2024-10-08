# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b2
- machine: windows-x86
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 233 ms: 1.14x faster                                                |
| chameleon      | 6.42 ms                                                         | 5.71 ms: 1.12x faster                                               |
| docutils       | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                              |
| html5lib       | 52.1 ms                                                         | 45.4 ms: 1.15x faster                                               |
| tornado_http   | 118 ms                                                          | 94.3 ms: 1.25x faster                                               |
| Geometric mean | (ref)                                                           | 1.14x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 471 ms: 1.96x faster                                                |
| async_tree_io           | 940 ms                                                          | 530 ms: 1.77x faster                                                |
| async_tree_none         | 394 ms                                                          | 228 ms: 1.73x faster                                                |
| async_tree_memoization  | 467 ms                                                          | 275 ms: 1.70x faster                                                |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                |
| float          | 69.6 ms                                                         | 52.4 ms: 1.33x faster                                               |
| nbody          | 79.1 ms                                                         | 76.9 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                           | 1.51x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 99.9 ms: 1.17x faster                                               |
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                |
| regex_effbot   | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                           | 1.03x faster                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.84 ms: 1.44x faster                                               |
| pickle_pure_python   | 280 us                                                          | 213 us: 1.31x faster                                                |
| unpickle_pure_python | 189 us                                                          | 147 us: 1.29x faster                                                |
| tomli_loads          | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                              |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                |
| xml_etree_process    | 48.1 ms                                                         | 42.1 ms: 1.14x faster                                               |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.2 ms: 1.10x faster                                               |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                               |
| xml_etree_generate   | 61.6 ms                                                         | 59.6 ms: 1.03x faster                                               |
| unpickle_list        | 2.98 us                                                         | 2.93 us: 1.02x faster                                               |
| pickle               | 7.83 us                                                         | 8.07 us: 1.03x slower                                               |
| pickle_list          | 3.22 us                                                         | 3.57 us: 1.11x slower                                               |
| pickle_dict          | 18.2 us                                                         | 20.8 us: 1.14x slower                                               |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.2 ms: 1.03x faster                                               |
| python_startup_no_site | 18.1 ms                                                         | 18.2 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.94 ms: 1.31x faster                                               |
| django_template | 36.0 ms                                                         | 30.1 ms: 1.20x faster                                               |
| genshi_xml      | 46.6 ms                                                         | 44.3 ms: 1.05x faster                                               |
| genshi_text     | 21.0 ms                                                         | 20.1 ms: 1.04x faster                                               |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 136 us: 2.92x faster                                                |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 471 ms: 1.96x faster                                                |
| deltablue                | 4.04 ms                                                         | 2.23 ms: 1.81x faster                                               |
| async_tree_io            | 940 ms                                                          | 530 ms: 1.77x faster                                                |
| pylint                   | 384 ms                                                          | 217 ms: 1.77x faster                                                |
| async_tree_none          | 394 ms                                                          | 228 ms: 1.73x faster                                                |
| async_tree_memoization   | 467 ms                                                          | 275 ms: 1.70x faster                                                |
| logging_silent           | 97.9 ns                                                         | 57.9 ns: 1.69x faster                                               |
| raytrace                 | 303 ms                                                          | 189 ms: 1.60x faster                                                |
| chaos                    | 74.4 ms                                                         | 48.0 ms: 1.55x faster                                               |
| scimark_lu               | 89.8 ms                                                         | 59.4 ms: 1.51x faster                                               |
| comprehensions           | 17.7 us                                                         | 11.9 us: 1.50x faster                                               |
| generators               | 31.6 ms                                                         | 21.2 ms: 1.49x faster                                               |
| crypto_pyaes             | 81.3 ms                                                         | 55.8 ms: 1.46x faster                                               |
| hexiom                   | 6.13 ms                                                         | 4.23 ms: 1.45x faster                                               |
| go                       | 146 ms                                                          | 101 ms: 1.45x faster                                                |
| json_dumps               | 9.82 ms                                                         | 6.84 ms: 1.44x faster                                               |
| scimark_sor              | 115 ms                                                          | 81.0 ms: 1.42x faster                                               |
| richards_super           | 49.9 ms                                                         | 35.5 ms: 1.41x faster                                               |
| sqlglot_parse            | 1.33 ms                                                         | 964 us: 1.38x faster                                                |
| scimark_monte_carlo      | 61.9 ms                                                         | 45.2 ms: 1.37x faster                                               |
| pyflate                  | 422 ms                                                          | 308 ms: 1.37x faster                                                |
| pycparser                | 1.04 sec                                                        | 777 ms: 1.34x faster                                                |
| sqlglot_transpile        | 1.58 ms                                                         | 1.19 ms: 1.33x faster                                               |
| float                    | 69.6 ms                                                         | 52.4 ms: 1.33x faster                                               |
| pickle_pure_python       | 280 us                                                          | 213 us: 1.31x faster                                                |
| mako                     | 9.10 ms                                                         | 6.94 ms: 1.31x faster                                               |
| richards                 | 40.3 ms                                                         | 31.2 ms: 1.29x faster                                               |
| unpickle_pure_python     | 189 us                                                          | 147 us: 1.29x faster                                                |
| nqueens                  | 87.1 ms                                                         | 68.7 ms: 1.27x faster                                               |
| deepcopy_memo            | 29.6 us                                                         | 23.5 us: 1.26x faster                                               |
| tornado_http             | 118 ms                                                          | 94.3 ms: 1.25x faster                                               |
| django_template          | 36.0 ms                                                         | 30.1 ms: 1.20x faster                                               |
| spectral_norm            | 80.2 ms                                                         | 68.0 ms: 1.18x faster                                               |
| fannkuch                 | 317 ms                                                          | 270 ms: 1.17x faster                                                |
| regex_compile            | 117 ms                                                          | 99.9 ms: 1.17x faster                                               |
| sqlite_synth             | 2.29 us                                                         | 1.96 us: 1.17x faster                                               |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.17x faster                                                |
| json                     | 4.76 ms                                                         | 4.10 ms: 1.16x faster                                               |
| tomli_loads              | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                              |
| coroutines               | 17.9 ms                                                         | 15.5 ms: 1.16x faster                                               |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                |
| html5lib                 | 52.1 ms                                                         | 45.4 ms: 1.15x faster                                               |
| xml_etree_process        | 48.1 ms                                                         | 42.1 ms: 1.14x faster                                               |
| mdp                      | 1.83 sec                                                        | 1.60 sec: 1.14x faster                                              |
| 2to3                     | 265 ms                                                          | 233 ms: 1.14x faster                                                |
| bench_thread_pool        | 1.12 ms                                                         | 985 us: 1.14x faster                                                |
| sympy_integrate          | 16.6 ms                                                         | 14.6 ms: 1.14x faster                                               |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.87 ms: 1.13x faster                                               |
| sqlglot_optimize         | 44.7 ms                                                         | 39.7 ms: 1.13x faster                                               |
| asyncio_tcp              | 744 ms                                                          | 662 ms: 1.12x faster                                                |
| chameleon                | 6.42 ms                                                         | 5.71 ms: 1.12x faster                                               |
| sqlglot_normalize        | 230 ms                                                          | 206 ms: 1.12x faster                                                |
| deepcopy                 | 310 us                                                          | 280 us: 1.11x faster                                                |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.2 ms: 1.10x faster                                               |
| pprint_pformat           | 1.37 sec                                                        | 1.24 sec: 1.10x faster                                              |
| scimark_fft              | 216 ms                                                          | 198 ms: 1.09x faster                                                |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                               |
| sympy_str                | 229 ms                                                          | 211 ms: 1.09x faster                                                |
| pprint_safe_repr         | 658 ms                                                          | 607 ms: 1.09x faster                                                |
| meteor_contest           | 80.0 ms                                                         | 74.1 ms: 1.08x faster                                               |
| docutils                 | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                              |
| genshi_xml               | 46.6 ms                                                         | 44.3 ms: 1.05x faster                                               |
| genshi_text              | 21.0 ms                                                         | 20.1 ms: 1.04x faster                                               |
| sympy_expand             | 391 ms                                                          | 375 ms: 1.04x faster                                                |
| deepcopy_reduce          | 2.68 us                                                         | 2.59 us: 1.04x faster                                               |
| xml_etree_generate       | 61.6 ms                                                         | 59.6 ms: 1.03x faster                                               |
| python_startup           | 22.9 ms                                                         | 22.2 ms: 1.03x faster                                               |
| nbody                    | 79.1 ms                                                         | 76.9 ms: 1.03x faster                                               |
| unpickle_list            | 2.98 us                                                         | 2.93 us: 1.02x faster                                               |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                              |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                              |
| python_startup_no_site   | 18.1 ms                                                         | 18.2 ms: 1.01x slower                                               |
| logging_simple           | 7.29 us                                                         | 7.47 us: 1.02x slower                                               |
| logging_format           | 7.91 us                                                         | 8.13 us: 1.03x slower                                               |
| pickle                   | 7.83 us                                                         | 8.07 us: 1.03x slower                                               |
| pathlib                  | 81.2 ms                                                         | 83.9 ms: 1.03x slower                                               |
| bench_mp_pool            | 66.4 ms                                                         | 69.4 ms: 1.05x slower                                               |
| create_gc_cycles         | 694 us                                                          | 756 us: 1.09x slower                                                |
| async_generators         | 241 ms                                                          | 266 ms: 1.10x slower                                                |
| pickle_list              | 3.22 us                                                         | 3.57 us: 1.11x slower                                               |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                               |
| regex_effbot             | 1.66 ms                                                         | 1.88 ms: 1.13x slower                                               |
| pickle_dict              | 18.2 us                                                         | 20.8 us: 1.14x slower                                               |
| telco                    | 4.83 ms                                                         | 6.03 ms: 1.25x slower                                               |
| coverage                 | 46.6 ms                                                         | 307 ms: 6.60x slower                                                |
| thrift                   | 902 us                                                          | 9.73 ms: 10.78x slower                                              |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                        |

Benchmark hidden because not significant (2): unpickle, regex_v8
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown