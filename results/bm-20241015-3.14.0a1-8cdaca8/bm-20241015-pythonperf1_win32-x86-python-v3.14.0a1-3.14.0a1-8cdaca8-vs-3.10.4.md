# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a1
- machine: windows-x86
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.119x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 246 ms: 1.08x faster                                                |
| docutils       | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                              |
| html5lib       | 52.1 ms                                                         | 44.9 ms: 1.16x faster                                               |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                |
| Geometric mean | (ref)                                                           | 1.11x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 467 ms: 1.97x faster                                                |
| async_tree_none         | 394 ms                                                          | 223 ms: 1.77x faster                                                |
| async_tree_io           | 940 ms                                                          | 534 ms: 1.76x faster                                                |
| async_tree_memoization  | 467 ms                                                          | 280 ms: 1.67x faster                                                |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                |
| float          | 69.6 ms                                                         | 61.9 ms: 1.12x faster                                               |
| nbody          | 79.1 ms                                                         | 87.2 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                           | 1.37x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                |
| regex_compile  | 117 ms                                                          | 105 ms: 1.11x faster                                                |
| regex_effbot   | 1.66 ms                                                         | 1.82 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                           | 1.03x faster                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                               |
| json_dumps           | 9.82 ms                                                         | 9.09 ms: 1.08x faster                                               |
| unpickle_pure_python | 189 us                                                          | 178 us: 1.07x faster                                                |
| xml_etree_parse      | 120 ms                                                          | 113 ms: 1.06x faster                                                |
| pickle_pure_python   | 280 us                                                          | 265 us: 1.06x faster                                                |
| tomli_loads          | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                              |
| xml_etree_iterparse  | 70.8 ms                                                         | 69.5 ms: 1.02x faster                                               |
| xml_etree_process    | 48.1 ms                                                         | 47.6 ms: 1.01x faster                                               |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.04x slower                                               |
| xml_etree_generate   | 61.6 ms                                                         | 66.5 ms: 1.08x slower                                               |
| pickle_list          | 3.22 us                                                         | 3.49 us: 1.09x slower                                               |
| pickle               | 7.83 us                                                         | 8.56 us: 1.09x slower                                               |
| pickle_dict          | 18.2 us                                                         | 21.6 us: 1.18x slower                                               |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                               |
| python_startup         | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                               |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.83 ms: 1.16x faster                                               |
| django_template | 36.0 ms                                                         | 32.5 ms: 1.11x faster                                               |
| genshi_text     | 21.0 ms                                                         | 20.6 ms: 1.02x faster                                               |
| genshi_xml      | 46.6 ms                                                         | 45.9 ms: 1.02x faster                                               |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.76x faster                                                |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 467 ms: 1.97x faster                                                |
| async_tree_none          | 394 ms                                                          | 223 ms: 1.77x faster                                                |
| async_tree_io            | 940 ms                                                          | 534 ms: 1.76x faster                                                |
| async_tree_memoization   | 467 ms                                                          | 280 ms: 1.67x faster                                                |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                |
| deltablue                | 4.04 ms                                                         | 2.68 ms: 1.51x faster                                               |
| go                       | 146 ms                                                          | 99.5 ms: 1.46x faster                                               |
| logging_silent           | 97.9 ns                                                         | 69.5 ns: 1.41x faster                                               |
| crypto_pyaes             | 81.3 ms                                                         | 60.0 ms: 1.36x faster                                               |
| chaos                    | 74.4 ms                                                         | 55.4 ms: 1.34x faster                                               |
| scimark_lu               | 89.8 ms                                                         | 67.6 ms: 1.33x faster                                               |
| comprehensions           | 17.7 us                                                         | 13.4 us: 1.33x faster                                               |
| deepcopy_memo            | 29.6 us                                                         | 22.3 us: 1.33x faster                                               |
| generators               | 31.6 ms                                                         | 24.1 ms: 1.31x faster                                               |
| deepcopy                 | 310 us                                                          | 242 us: 1.28x faster                                                |
| raytrace                 | 303 ms                                                          | 236 ms: 1.28x faster                                                |
| pycparser                | 1.04 sec                                                        | 825 ms: 1.26x faster                                                |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.25x faster                                               |
| hexiom                   | 6.13 ms                                                         | 5.05 ms: 1.21x faster                                               |
| sqlglot_transpile        | 1.58 ms                                                         | 1.32 ms: 1.20x faster                                               |
| thrift                   | 902 us                                                          | 762 us: 1.18x faster                                                |
| nqueens                  | 87.1 ms                                                         | 74.5 ms: 1.17x faster                                               |
| mako                     | 9.10 ms                                                         | 7.83 ms: 1.16x faster                                               |
| html5lib                 | 52.1 ms                                                         | 44.9 ms: 1.16x faster                                               |
| sqlite_synth             | 2.29 us                                                         | 1.99 us: 1.15x faster                                               |
| pyflate                  | 422 ms                                                          | 368 ms: 1.15x faster                                                |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                |
| float                    | 69.6 ms                                                         | 61.9 ms: 1.12x faster                                               |
| bench_thread_pool        | 1.12 ms                                                         | 997 us: 1.12x faster                                                |
| dulwich_log              | 58.5 ms                                                         | 52.5 ms: 1.11x faster                                               |
| scimark_sor              | 115 ms                                                          | 103 ms: 1.11x faster                                                |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                |
| django_template          | 36.0 ms                                                         | 32.5 ms: 1.11x faster                                               |
| regex_compile            | 117 ms                                                          | 105 ms: 1.11x faster                                                |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                               |
| json_dumps               | 9.82 ms                                                         | 9.09 ms: 1.08x faster                                               |
| 2to3                     | 265 ms                                                          | 246 ms: 1.08x faster                                                |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.07x faster                                               |
| unpickle_pure_python     | 189 us                                                          | 178 us: 1.07x faster                                                |
| scimark_monte_carlo      | 61.9 ms                                                         | 58.2 ms: 1.06x faster                                               |
| xml_etree_parse          | 120 ms                                                          | 113 ms: 1.06x faster                                                |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                              |
| pickle_pure_python       | 280 us                                                          | 265 us: 1.06x faster                                                |
| richards_super           | 49.9 ms                                                         | 47.3 ms: 1.06x faster                                               |
| docutils                 | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                              |
| sympy_str                | 229 ms                                                          | 218 ms: 1.05x faster                                                |
| deepcopy_reduce          | 2.68 us                                                         | 2.55 us: 1.05x faster                                               |
| coroutines               | 17.9 ms                                                         | 17.1 ms: 1.05x faster                                               |
| spectral_norm            | 80.2 ms                                                         | 77.3 ms: 1.04x faster                                               |
| sqlglot_normalize        | 230 ms                                                          | 224 ms: 1.03x faster                                                |
| sqlglot_optimize         | 44.7 ms                                                         | 43.6 ms: 1.03x faster                                               |
| tomli_loads              | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                              |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.17 ms: 1.02x faster                                               |
| xml_etree_iterparse      | 70.8 ms                                                         | 69.5 ms: 1.02x faster                                               |
| genshi_text              | 21.0 ms                                                         | 20.6 ms: 1.02x faster                                               |
| genshi_xml               | 46.6 ms                                                         | 45.9 ms: 1.02x faster                                               |
| xml_etree_process        | 48.1 ms                                                         | 47.6 ms: 1.01x faster                                               |
| sympy_expand             | 391 ms                                                          | 387 ms: 1.01x faster                                                |
| meteor_contest           | 80.0 ms                                                         | 80.3 ms: 1.00x slower                                               |
| pprint_safe_repr         | 658 ms                                                          | 662 ms: 1.01x slower                                                |
| fannkuch                 | 317 ms                                                          | 325 ms: 1.03x slower                                                |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.4 sec: 1.03x slower                                              |
| richards                 | 40.3 ms                                                         | 41.5 ms: 1.03x slower                                               |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                               |
| scimark_fft              | 216 ms                                                          | 230 ms: 1.06x slower                                                |
| xml_etree_generate       | 61.6 ms                                                         | 66.5 ms: 1.08x slower                                               |
| pathlib                  | 81.2 ms                                                         | 88.2 ms: 1.09x slower                                               |
| pickle_list              | 3.22 us                                                         | 3.49 us: 1.09x slower                                               |
| logging_simple           | 7.29 us                                                         | 7.95 us: 1.09x slower                                               |
| pickle                   | 7.83 us                                                         | 8.56 us: 1.09x slower                                               |
| regex_effbot             | 1.66 ms                                                         | 1.82 ms: 1.10x slower                                               |
| logging_format           | 7.91 us                                                         | 8.70 us: 1.10x slower                                               |
| asyncio_tcp              | 744 ms                                                          | 819 ms: 1.10x slower                                                |
| nbody                    | 79.1 ms                                                         | 87.2 ms: 1.10x slower                                               |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                               |
| coverage                 | 46.6 ms                                                         | 51.9 ms: 1.11x slower                                               |
| python_startup           | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                               |
| pickle_dict              | 18.2 us                                                         | 21.6 us: 1.18x slower                                               |
| unpack_sequence          | 40.0 ns                                                         | 49.8 ns: 1.24x slower                                               |
| json                     | 4.76 ms                                                         | 5.97 ms: 1.25x slower                                               |
| async_generators         | 241 ms                                                          | 306 ms: 1.27x slower                                                |
| bench_mp_pool            | 66.4 ms                                                         | 89.0 ms: 1.34x slower                                               |
| telco                    | 4.83 ms                                                         | 6.58 ms: 1.36x slower                                               |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.41x slower                                               |
| create_gc_cycles         | 694 us                                                          | 1.19 ms: 1.72x slower                                               |
| Geometric mean           | (ref)                                                           | 1.10x faster                                                        |

Benchmark hidden because not significant (3): unpickle_list, regex_v8, pprint_pformat
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.119x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown