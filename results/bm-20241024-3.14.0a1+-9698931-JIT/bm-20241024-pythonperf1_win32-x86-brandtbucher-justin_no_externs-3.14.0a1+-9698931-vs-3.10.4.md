# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-x86
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.112x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 274 ms: 1.03x slower                                                               |
| docutils       | 1.95 sec                                                        | 2.10 sec: 1.08x slower                                                             |
| html5lib       | 52.1 ms                                                         | 48.7 ms: 1.07x faster                                                              |
| tornado_http   | 118 ms                                                          | 110 ms: 1.07x faster                                                               |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 474 ms: 1.94x faster                                                               |
| async_tree_io           | 940 ms                                                          | 540 ms: 1.74x faster                                                               |
| async_tree_none         | 394 ms                                                          | 228 ms: 1.72x faster                                                               |
| async_tree_memoization  | 467 ms                                                          | 287 ms: 1.63x faster                                                               |
| Geometric mean          | (ref)                                                           | 1.76x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 207 ms: 2.43x faster                                                               |
| float          | 69.6 ms                                                         | 52.2 ms: 1.33x faster                                                              |
| nbody          | 79.1 ms                                                         | 70.3 ms: 1.13x faster                                                              |
| Geometric mean | (ref)                                                           | 1.54x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                               |
| regex_compile  | 117 ms                                                          | 113 ms: 1.03x faster                                                               |
| regex_effbot   | 1.66 ms                                                         | 1.79 ms: 1.07x slower                                                              |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.64 sec: 1.16x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 8.50 ms: 1.16x faster                                                              |
| unpickle_pure_python | 189 us                                                          | 173 us: 1.09x faster                                                               |
| pickle_pure_python   | 280 us                                                          | 258 us: 1.09x faster                                                               |
| xml_etree_parse      | 120 ms                                                          | 113 ms: 1.06x faster                                                               |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.2 ms: 1.04x faster                                                              |
| json_loads           | 22.4 us                                                         | 21.7 us: 1.03x faster                                                              |
| xml_etree_process    | 48.1 ms                                                         | 47.7 ms: 1.01x faster                                                              |
| xml_etree_generate   | 61.6 ms                                                         | 63.8 ms: 1.04x slower                                                              |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                              |
| python_startup         | 22.9 ms                                                         | 26.4 ms: 1.15x slower                                                              |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.83 ms: 1.33x faster                                                              |
| django_template | 36.0 ms                                                         | 34.7 ms: 1.04x faster                                                              |
| genshi_text     | 21.0 ms                                                         | 24.9 ms: 1.19x slower                                                              |
| genshi_xml      | 46.6 ms                                                         | 58.0 ms: 1.24x slower                                                              |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 152 us: 2.60x faster                                                               |
| pidigits                 | 502 ms                                                          | 207 ms: 2.43x faster                                                               |
| sqlglot_normalize        | 230 ms                                                          | 102 ms: 2.26x faster                                                               |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 474 ms: 1.94x faster                                                               |
| async_tree_io            | 940 ms                                                          | 540 ms: 1.74x faster                                                               |
| async_tree_none          | 394 ms                                                          | 228 ms: 1.72x faster                                                               |
| async_tree_memoization   | 467 ms                                                          | 287 ms: 1.63x faster                                                               |
| deepcopy_memo            | 29.6 us                                                         | 19.6 us: 1.51x faster                                                              |
| deltablue                | 4.04 ms                                                         | 2.91 ms: 1.39x faster                                                              |
| scimark_sor              | 115 ms                                                          | 83.3 ms: 1.38x faster                                                              |
| scimark_lu               | 89.8 ms                                                         | 65.7 ms: 1.37x faster                                                              |
| crypto_pyaes             | 81.3 ms                                                         | 59.7 ms: 1.36x faster                                                              |
| go                       | 146 ms                                                          | 109 ms: 1.34x faster                                                               |
| float                    | 69.6 ms                                                         | 52.2 ms: 1.33x faster                                                              |
| mako                     | 9.10 ms                                                         | 6.83 ms: 1.33x faster                                                              |
| pylint                   | 384 ms                                                          | 291 ms: 1.32x faster                                                               |
| logging_silent           | 97.9 ns                                                         | 76.8 ns: 1.27x faster                                                              |
| deepcopy                 | 310 us                                                          | 244 us: 1.27x faster                                                               |
| chaos                    | 74.4 ms                                                         | 58.7 ms: 1.27x faster                                                              |
| scimark_monte_carlo      | 61.9 ms                                                         | 51.0 ms: 1.21x faster                                                              |
| sqlglot_parse            | 1.33 ms                                                         | 1.10 ms: 1.21x faster                                                              |
| pycparser                | 1.04 sec                                                        | 862 ms: 1.21x faster                                                               |
| pyflate                  | 422 ms                                                          | 358 ms: 1.18x faster                                                               |
| dulwich_log              | 58.5 ms                                                         | 50.1 ms: 1.17x faster                                                              |
| tomli_loads              | 1.91 sec                                                        | 1.64 sec: 1.16x faster                                                             |
| comprehensions           | 17.7 us                                                         | 15.3 us: 1.16x faster                                                              |
| json_dumps               | 9.82 ms                                                         | 8.50 ms: 1.16x faster                                                              |
| thrift                   | 902 us                                                          | 788 us: 1.15x faster                                                               |
| nbody                    | 79.1 ms                                                         | 70.3 ms: 1.13x faster                                                              |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.89 ms: 1.12x faster                                                              |
| generators               | 31.6 ms                                                         | 28.1 ms: 1.12x faster                                                              |
| richards_super           | 49.9 ms                                                         | 44.6 ms: 1.12x faster                                                              |
| sqlglot_transpile        | 1.58 ms                                                         | 1.42 ms: 1.12x faster                                                              |
| spectral_norm            | 80.2 ms                                                         | 72.5 ms: 1.11x faster                                                              |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                               |
| raytrace                 | 303 ms                                                          | 277 ms: 1.09x faster                                                               |
| unpickle_pure_python     | 189 us                                                          | 173 us: 1.09x faster                                                               |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                                              |
| fannkuch                 | 317 ms                                                          | 291 ms: 1.09x faster                                                               |
| pickle_pure_python       | 280 us                                                          | 258 us: 1.09x faster                                                               |
| tornado_http             | 118 ms                                                          | 110 ms: 1.07x faster                                                               |
| html5lib                 | 52.1 ms                                                         | 48.7 ms: 1.07x faster                                                              |
| deepcopy_reduce          | 2.68 us                                                         | 2.52 us: 1.06x faster                                                              |
| xml_etree_parse          | 120 ms                                                          | 113 ms: 1.06x faster                                                               |
| nqueens                  | 87.1 ms                                                         | 82.6 ms: 1.05x faster                                                              |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.2 ms: 1.04x faster                                                              |
| django_template          | 36.0 ms                                                         | 34.7 ms: 1.04x faster                                                              |
| json_loads               | 22.4 us                                                         | 21.7 us: 1.03x faster                                                              |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                             |
| regex_compile            | 117 ms                                                          | 113 ms: 1.03x faster                                                               |
| scimark_fft              | 216 ms                                                          | 210 ms: 1.03x faster                                                               |
| pprint_safe_repr         | 658 ms                                                          | 642 ms: 1.03x faster                                                               |
| mdp                      | 1.83 sec                                                        | 1.79 sec: 1.02x faster                                                             |
| richards                 | 40.3 ms                                                         | 39.5 ms: 1.02x faster                                                              |
| xml_etree_process        | 48.1 ms                                                         | 47.7 ms: 1.01x faster                                                              |
| meteor_contest           | 80.0 ms                                                         | 81.3 ms: 1.02x slower                                                              |
| 2to3                     | 265 ms                                                          | 274 ms: 1.03x slower                                                               |
| xml_etree_generate       | 61.6 ms                                                         | 63.8 ms: 1.04x slower                                                              |
| sympy_str                | 229 ms                                                          | 239 ms: 1.04x slower                                                               |
| hexiom                   | 6.13 ms                                                         | 6.40 ms: 1.04x slower                                                              |
| sympy_expand             | 391 ms                                                          | 410 ms: 1.05x slower                                                               |
| regex_effbot             | 1.66 ms                                                         | 1.79 ms: 1.07x slower                                                              |
| docutils                 | 1.95 sec                                                        | 2.10 sec: 1.08x slower                                                             |
| logging_format           | 7.91 us                                                         | 8.57 us: 1.08x slower                                                              |
| pathlib                  | 81.2 ms                                                         | 88.3 ms: 1.09x slower                                                              |
| json                     | 4.76 ms                                                         | 5.19 ms: 1.09x slower                                                              |
| logging_simple           | 7.29 us                                                         | 7.96 us: 1.09x slower                                                              |
| sympy_integrate          | 16.6 ms                                                         | 18.3 ms: 1.10x slower                                                              |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                              |
| sqlglot_optimize         | 44.7 ms                                                         | 50.6 ms: 1.13x slower                                                              |
| python_startup           | 22.9 ms                                                         | 26.4 ms: 1.15x slower                                                              |
| coverage                 | 46.6 ms                                                         | 54.3 ms: 1.17x slower                                                              |
| genshi_text              | 21.0 ms                                                         | 24.9 ms: 1.19x slower                                                              |
| genshi_xml               | 46.6 ms                                                         | 58.0 ms: 1.24x slower                                                              |
| telco                    | 4.83 ms                                                         | 6.32 ms: 1.31x slower                                                              |
| async_generators         | 241 ms                                                          | 326 ms: 1.35x slower                                                               |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.41x slower                                                              |
| bench_mp_pool            | 66.4 ms                                                         | 94.6 ms: 1.43x slower                                                              |
| create_gc_cycles         | 694 us                                                          | 1.19 ms: 1.72x slower                                                              |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                       |

Benchmark hidden because not significant (3): sympy_sum, regex_v8, coroutines
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-pythonperf1_win32-x86-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.112x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown