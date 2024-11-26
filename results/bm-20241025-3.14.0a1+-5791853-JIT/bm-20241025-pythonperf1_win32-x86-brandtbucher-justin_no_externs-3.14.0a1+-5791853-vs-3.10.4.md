# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.154x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 267 ms: 1.01x slower                                                               |
| docutils       | 1.95 sec                                                        | 2.05 sec: 1.05x slower                                                             |
| html5lib       | 52.1 ms                                                         | 46.9 ms: 1.11x faster                                                              |
| tornado_http   | 118 ms                                                          | 110 ms: 1.07x faster                                                               |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 465 ms: 1.98x faster                                                               |
| async_tree_io           | 940 ms                                                          | 521 ms: 1.81x faster                                                               |
| async_tree_none         | 394 ms                                                          | 218 ms: 1.80x faster                                                               |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                               |
| Geometric mean          | (ref)                                                           | 1.82x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 207 ms: 2.43x faster                                                               |
| float          | 69.6 ms                                                         | 49.7 ms: 1.40x faster                                                              |
| nbody          | 79.1 ms                                                         | 67.2 ms: 1.18x faster                                                              |
| Geometric mean | (ref)                                                           | 1.59x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                               |
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                               |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                              |
| regex_effbot   | 1.66 ms                                                         | 1.80 ms: 1.08x slower                                                              |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.56 sec: 1.22x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 8.11 ms: 1.21x faster                                                              |
| pickle_pure_python   | 280 us                                                          | 244 us: 1.15x faster                                                               |
| unpickle_pure_python | 189 us                                                          | 166 us: 1.14x faster                                                               |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                              |
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                               |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.6 ms: 1.06x faster                                                              |
| xml_etree_process    | 48.1 ms                                                         | 47.2 ms: 1.02x faster                                                              |
| xml_etree_generate   | 61.6 ms                                                         | 60.5 ms: 1.02x faster                                                              |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                              |
| python_startup         | 22.9 ms                                                         | 26.9 ms: 1.17x slower                                                              |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.29 ms: 1.45x faster                                                              |
| django_template | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                              |
| genshi_text     | 21.0 ms                                                         | 23.2 ms: 1.11x slower                                                              |
| genshi_xml      | 46.6 ms                                                         | 56.3 ms: 1.21x slower                                                              |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 142 us: 2.79x faster                                                               |
| pidigits                 | 502 ms                                                          | 207 ms: 2.43x faster                                                               |
| sqlglot_normalize        | 230 ms                                                          | 102 ms: 2.25x faster                                                               |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 465 ms: 1.98x faster                                                               |
| async_tree_io            | 940 ms                                                          | 521 ms: 1.81x faster                                                               |
| async_tree_none          | 394 ms                                                          | 218 ms: 1.80x faster                                                               |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                               |
| deepcopy_memo            | 29.6 us                                                         | 18.0 us: 1.64x faster                                                              |
| logging_silent           | 97.9 ns                                                         | 63.6 ns: 1.54x faster                                                              |
| crypto_pyaes             | 81.3 ms                                                         | 54.6 ms: 1.49x faster                                                              |
| deltablue                | 4.04 ms                                                         | 2.71 ms: 1.49x faster                                                              |
| scimark_sor              | 115 ms                                                          | 78.0 ms: 1.48x faster                                                              |
| go                       | 146 ms                                                          | 99.8 ms: 1.46x faster                                                              |
| mako                     | 9.10 ms                                                         | 6.29 ms: 1.45x faster                                                              |
| float                    | 69.6 ms                                                         | 49.7 ms: 1.40x faster                                                              |
| scimark_monte_carlo      | 61.9 ms                                                         | 45.2 ms: 1.37x faster                                                              |
| pylint                   | 384 ms                                                          | 285 ms: 1.35x faster                                                               |
| scimark_lu               | 89.8 ms                                                         | 68.9 ms: 1.30x faster                                                              |
| deepcopy                 | 310 us                                                          | 244 us: 1.27x faster                                                               |
| pycparser                | 1.04 sec                                                        | 823 ms: 1.27x faster                                                               |
| comprehensions           | 17.7 us                                                         | 14.0 us: 1.26x faster                                                              |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.26x faster                                                              |
| chaos                    | 74.4 ms                                                         | 59.1 ms: 1.26x faster                                                              |
| pyflate                  | 422 ms                                                          | 335 ms: 1.26x faster                                                               |
| richards_super           | 49.9 ms                                                         | 40.0 ms: 1.25x faster                                                              |
| tomli_loads              | 1.91 sec                                                        | 1.56 sec: 1.22x faster                                                             |
| raytrace                 | 303 ms                                                          | 250 ms: 1.21x faster                                                               |
| json_dumps               | 9.82 ms                                                         | 8.11 ms: 1.21x faster                                                              |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.73 ms: 1.19x faster                                                              |
| generators               | 31.6 ms                                                         | 26.6 ms: 1.18x faster                                                              |
| nbody                    | 79.1 ms                                                         | 67.2 ms: 1.18x faster                                                              |
| thrift                   | 902 us                                                          | 767 us: 1.18x faster                                                               |
| spectral_norm            | 80.2 ms                                                         | 68.5 ms: 1.17x faster                                                              |
| dulwich_log              | 58.5 ms                                                         | 50.4 ms: 1.16x faster                                                              |
| sqlglot_transpile        | 1.58 ms                                                         | 1.37 ms: 1.15x faster                                                              |
| pickle_pure_python       | 280 us                                                          | 244 us: 1.15x faster                                                               |
| unpickle_pure_python     | 189 us                                                          | 166 us: 1.14x faster                                                               |
| richards                 | 40.3 ms                                                         | 35.4 ms: 1.14x faster                                                              |
| django_template          | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                              |
| pprint_pformat           | 1.37 sec                                                        | 1.23 sec: 1.11x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 46.9 ms: 1.11x faster                                                              |
| fannkuch                 | 317 ms                                                          | 286 ms: 1.11x faster                                                               |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                              |
| pprint_safe_repr         | 658 ms                                                          | 602 ms: 1.09x faster                                                               |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                               |
| nqueens                  | 87.1 ms                                                         | 80.3 ms: 1.08x faster                                                              |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                               |
| deepcopy_reduce          | 2.68 us                                                         | 2.50 us: 1.07x faster                                                              |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                              |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                               |
| tornado_http             | 118 ms                                                          | 110 ms: 1.07x faster                                                               |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.6 ms: 1.06x faster                                                              |
| meteor_contest           | 80.0 ms                                                         | 75.3 ms: 1.06x faster                                                              |
| scimark_fft              | 216 ms                                                          | 206 ms: 1.05x faster                                                               |
| mdp                      | 1.83 sec                                                        | 1.75 sec: 1.04x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 5.90 ms: 1.04x faster                                                              |
| sympy_sum                | 122 ms                                                          | 118 ms: 1.04x faster                                                               |
| coroutines               | 17.9 ms                                                         | 17.5 ms: 1.02x faster                                                              |
| xml_etree_process        | 48.1 ms                                                         | 47.2 ms: 1.02x faster                                                              |
| xml_etree_generate       | 61.6 ms                                                         | 60.5 ms: 1.02x faster                                                              |
| 2to3                     | 265 ms                                                          | 267 ms: 1.01x slower                                                               |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                              |
| sympy_str                | 229 ms                                                          | 232 ms: 1.01x slower                                                               |
| sympy_expand             | 391 ms                                                          | 400 ms: 1.02x slower                                                               |
| docutils                 | 1.95 sec                                                        | 2.05 sec: 1.05x slower                                                             |
| logging_simple           | 7.29 us                                                         | 7.70 us: 1.06x slower                                                              |
| logging_format           | 7.91 us                                                         | 8.40 us: 1.06x slower                                                              |
| pathlib                  | 81.2 ms                                                         | 87.9 ms: 1.08x slower                                                              |
| regex_effbot             | 1.66 ms                                                         | 1.80 ms: 1.08x slower                                                              |
| sympy_integrate          | 16.6 ms                                                         | 18.1 ms: 1.09x slower                                                              |
| genshi_text              | 21.0 ms                                                         | 23.2 ms: 1.11x slower                                                              |
| coverage                 | 46.6 ms                                                         | 52.0 ms: 1.12x slower                                                              |
| python_startup_no_site   | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                              |
| sqlglot_optimize         | 44.7 ms                                                         | 50.3 ms: 1.13x slower                                                              |
| python_startup           | 22.9 ms                                                         | 26.9 ms: 1.17x slower                                                              |
| genshi_xml               | 46.6 ms                                                         | 56.3 ms: 1.21x slower                                                              |
| telco                    | 4.83 ms                                                         | 6.14 ms: 1.27x slower                                                              |
| async_generators         | 241 ms                                                          | 320 ms: 1.33x slower                                                               |
| gc_traversal             | 1.28 ms                                                         | 1.82 ms: 1.42x slower                                                              |
| bench_mp_pool            | 66.4 ms                                                         | 94.4 ms: 1.42x slower                                                              |
| create_gc_cycles         | 694 us                                                          | 1.19 ms: 1.72x slower                                                              |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                       |

Benchmark hidden because not significant (1): json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241025-3.14.0a1+-5791853-JIT/bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-5791853.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.154x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown