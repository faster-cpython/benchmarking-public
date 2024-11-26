# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.158x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 270 ms: 1.02x slower                                                               |
| docutils       | 1.95 sec                                                        | 2.08 sec: 1.07x slower                                                             |
| html5lib       | 52.1 ms                                                         | 45.9 ms: 1.13x faster                                                              |
| tornado_http   | 118 ms                                                          | 109 ms: 1.08x faster                                                               |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 470 ms: 1.96x faster                                                               |
| async_tree_io           | 940 ms                                                          | 525 ms: 1.79x faster                                                               |
| async_tree_none         | 394 ms                                                          | 223 ms: 1.76x faster                                                               |
| async_tree_memoization  | 467 ms                                                          | 281 ms: 1.66x faster                                                               |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 203 ms: 2.48x faster                                                               |
| float          | 69.6 ms                                                         | 49.6 ms: 1.40x faster                                                              |
| nbody          | 79.1 ms                                                         | 63.0 ms: 1.26x faster                                                              |
| Geometric mean | (ref)                                                           | 1.64x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                               |
| regex_compile  | 117 ms                                                          | 110 ms: 1.06x faster                                                               |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                              |
| regex_effbot   | 1.66 ms                                                         | 1.77 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.99 ms: 1.23x faster                                                              |
| tomli_loads          | 1.91 sec                                                        | 1.59 sec: 1.20x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 245 us: 1.14x faster                                                               |
| unpickle_pure_python | 189 us                                                          | 169 us: 1.12x faster                                                               |
| xml_etree_parse      | 120 ms                                                          | 111 ms: 1.08x faster                                                               |
| xml_etree_process    | 48.1 ms                                                         | 45.4 ms: 1.06x faster                                                              |
| xml_etree_generate   | 61.6 ms                                                         | 58.2 ms: 1.06x faster                                                              |
| json_loads           | 22.4 us                                                         | 21.2 us: 1.06x faster                                                              |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.7 ms: 1.05x faster                                                              |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.13x slower                                                              |
| python_startup         | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                                              |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.44 ms: 1.41x faster                                                              |
| django_template | 36.0 ms                                                         | 33.0 ms: 1.09x faster                                                              |
| genshi_text     | 21.0 ms                                                         | 23.2 ms: 1.11x slower                                                              |
| genshi_xml      | 46.6 ms                                                         | 55.0 ms: 1.18x slower                                                              |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.77x faster                                                               |
| pidigits                 | 502 ms                                                          | 203 ms: 2.48x faster                                                               |
| sqlglot_normalize        | 230 ms                                                          | 105 ms: 2.19x faster                                                               |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 470 ms: 1.96x faster                                                               |
| async_tree_io            | 940 ms                                                          | 525 ms: 1.79x faster                                                               |
| async_tree_none          | 394 ms                                                          | 223 ms: 1.76x faster                                                               |
| async_tree_memoization   | 467 ms                                                          | 281 ms: 1.66x faster                                                               |
| deepcopy_memo            | 29.6 us                                                         | 18.0 us: 1.64x faster                                                              |
| logging_silent           | 97.9 ns                                                         | 64.9 ns: 1.51x faster                                                              |
| crypto_pyaes             | 81.3 ms                                                         | 54.0 ms: 1.51x faster                                                              |
| scimark_sor              | 115 ms                                                          | 76.9 ms: 1.50x faster                                                              |
| deltablue                | 4.04 ms                                                         | 2.73 ms: 1.48x faster                                                              |
| go                       | 146 ms                                                          | 101 ms: 1.45x faster                                                               |
| mako                     | 9.10 ms                                                         | 6.44 ms: 1.41x faster                                                              |
| float                    | 69.6 ms                                                         | 49.6 ms: 1.40x faster                                                              |
| scimark_lu               | 89.8 ms                                                         | 65.2 ms: 1.38x faster                                                              |
| chaos                    | 74.4 ms                                                         | 55.8 ms: 1.33x faster                                                              |
| pylint                   | 384 ms                                                          | 288 ms: 1.33x faster                                                               |
| scimark_monte_carlo      | 61.9 ms                                                         | 47.7 ms: 1.30x faster                                                              |
| pyflate                  | 422 ms                                                          | 330 ms: 1.28x faster                                                               |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.28x faster                                                              |
| deepcopy                 | 310 us                                                          | 245 us: 1.27x faster                                                               |
| nbody                    | 79.1 ms                                                         | 63.0 ms: 1.26x faster                                                              |
| comprehensions           | 17.7 us                                                         | 14.2 us: 1.25x faster                                                              |
| fannkuch                 | 317 ms                                                          | 256 ms: 1.24x faster                                                               |
| generators               | 31.6 ms                                                         | 25.5 ms: 1.24x faster                                                              |
| pycparser                | 1.04 sec                                                        | 845 ms: 1.23x faster                                                               |
| json_dumps               | 9.82 ms                                                         | 7.99 ms: 1.23x faster                                                              |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.65 ms: 1.22x faster                                                              |
| richards_super           | 49.9 ms                                                         | 41.0 ms: 1.22x faster                                                              |
| tomli_loads              | 1.91 sec                                                        | 1.59 sec: 1.20x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 67.5 ms: 1.19x faster                                                              |
| raytrace                 | 303 ms                                                          | 256 ms: 1.18x faster                                                               |
| thrift                   | 902 us                                                          | 766 us: 1.18x faster                                                               |
| dulwich_log              | 58.5 ms                                                         | 50.2 ms: 1.17x faster                                                              |
| sqlglot_transpile        | 1.58 ms                                                         | 1.36 ms: 1.16x faster                                                              |
| pickle_pure_python       | 280 us                                                          | 245 us: 1.14x faster                                                               |
| html5lib                 | 52.1 ms                                                         | 45.9 ms: 1.13x faster                                                              |
| unpickle_pure_python     | 189 us                                                          | 169 us: 1.12x faster                                                               |
| richards                 | 40.3 ms                                                         | 35.9 ms: 1.12x faster                                                              |
| pprint_pformat           | 1.37 sec                                                        | 1.23 sec: 1.11x faster                                                             |
| scimark_fft              | 216 ms                                                          | 195 ms: 1.11x faster                                                               |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                              |
| pprint_safe_repr         | 658 ms                                                          | 603 ms: 1.09x faster                                                               |
| django_template          | 36.0 ms                                                         | 33.0 ms: 1.09x faster                                                              |
| meteor_contest           | 80.0 ms                                                         | 73.6 ms: 1.09x faster                                                              |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                               |
| tornado_http             | 118 ms                                                          | 109 ms: 1.08x faster                                                               |
| xml_etree_parse          | 120 ms                                                          | 111 ms: 1.08x faster                                                               |
| regex_compile            | 117 ms                                                          | 110 ms: 1.06x faster                                                               |
| xml_etree_process        | 48.1 ms                                                         | 45.4 ms: 1.06x faster                                                              |
| deepcopy_reduce          | 2.68 us                                                         | 2.53 us: 1.06x faster                                                              |
| xml_etree_generate       | 61.6 ms                                                         | 58.2 ms: 1.06x faster                                                              |
| json_loads               | 22.4 us                                                         | 21.2 us: 1.06x faster                                                              |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.7 ms: 1.05x faster                                                              |
| nqueens                  | 87.1 ms                                                         | 83.7 ms: 1.04x faster                                                              |
| mdp                      | 1.83 sec                                                        | 1.76 sec: 1.04x faster                                                             |
| coroutines               | 17.9 ms                                                         | 17.3 ms: 1.04x faster                                                              |
| hexiom                   | 6.13 ms                                                         | 5.94 ms: 1.03x faster                                                              |
| sympy_sum                | 122 ms                                                          | 119 ms: 1.03x faster                                                               |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                              |
| 2to3                     | 265 ms                                                          | 270 ms: 1.02x slower                                                               |
| sympy_str                | 229 ms                                                          | 236 ms: 1.03x slower                                                               |
| sympy_expand             | 391 ms                                                          | 406 ms: 1.04x slower                                                               |
| regex_effbot             | 1.66 ms                                                         | 1.77 ms: 1.06x slower                                                              |
| docutils                 | 1.95 sec                                                        | 2.08 sec: 1.07x slower                                                             |
| logging_simple           | 7.29 us                                                         | 7.78 us: 1.07x slower                                                              |
| logging_format           | 7.91 us                                                         | 8.45 us: 1.07x slower                                                              |
| sympy_integrate          | 16.6 ms                                                         | 18.0 ms: 1.08x slower                                                              |
| pathlib                  | 81.2 ms                                                         | 87.8 ms: 1.08x slower                                                              |
| genshi_text              | 21.0 ms                                                         | 23.2 ms: 1.11x slower                                                              |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.13x slower                                                              |
| sqlglot_optimize         | 44.7 ms                                                         | 50.8 ms: 1.14x slower                                                              |
| coverage                 | 46.6 ms                                                         | 53.8 ms: 1.16x slower                                                              |
| python_startup           | 22.9 ms                                                         | 26.6 ms: 1.16x slower                                                              |
| genshi_xml               | 46.6 ms                                                         | 55.0 ms: 1.18x slower                                                              |
| telco                    | 4.83 ms                                                         | 6.01 ms: 1.24x slower                                                              |
| async_generators         | 241 ms                                                          | 332 ms: 1.38x slower                                                               |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.41x slower                                                              |
| bench_mp_pool            | 66.4 ms                                                         | 94.4 ms: 1.42x slower                                                              |
| create_gc_cycles         | 694 us                                                          | 1.18 ms: 1.70x slower                                                              |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                       |

Benchmark hidden because not significant (1): json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.158x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown