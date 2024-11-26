# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-x86
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.191x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| docutils       | 1.95 sec                                                        | 2.05 sec: 1.05x slower                                                           |
| html5lib       | 52.1 ms                                                         | 46.6 ms: 1.12x faster                                                            |
| tornado_http   | 118 ms                                                          | 110 ms: 1.07x faster                                                             |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 462 ms: 1.99x faster                                                             |
| async_tree_none         | 394 ms                                                          | 218 ms: 1.80x faster                                                             |
| async_tree_io           | 940 ms                                                          | 527 ms: 1.78x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                             |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.52x faster                                                             |
| float          | 69.6 ms                                                         | 46.5 ms: 1.50x faster                                                            |
| nbody          | 79.1 ms                                                         | 57.1 ms: 1.39x faster                                                            |
| Geometric mean | (ref)                                                           | 1.73x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 113 ms: 1.15x faster                                                             |
| regex_compile  | 117 ms                                                          | 105 ms: 1.11x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 15.0 ms: 1.05x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.80 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.49 sec: 1.29x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 7.95 ms: 1.24x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 156 us: 1.22x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 41.5 ms: 1.16x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 244 us: 1.15x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.0 ms: 1.12x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 55.0 ms: 1.12x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                             |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.40 us: 1.06x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.06x slower                                                            |
| pickle               | 7.83 us                                                         | 8.55 us: 1.09x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 21.2 us: 1.16x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                     |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                            |
| python_startup         | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.82 ms: 1.57x faster                                                            |
| django_template | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 24.6 ms: 1.17x slower                                                            |
| genshi_xml      | 46.6 ms                                                         | 55.2 ms: 1.18x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 139 us: 2.84x faster                                                             |
| pidigits                 | 502 ms                                                          | 200 ms: 2.52x faster                                                             |
| sqlglot_normalize        | 230 ms                                                          | 103 ms: 2.24x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 462 ms: 1.99x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 15.9 us: 1.85x faster                                                            |
| async_tree_none          | 394 ms                                                          | 218 ms: 1.80x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 54.6 ns: 1.79x faster                                                            |
| async_tree_io            | 940 ms                                                          | 527 ms: 1.78x faster                                                             |
| scimark_sor              | 115 ms                                                          | 68.1 ms: 1.69x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 50.0 ms: 1.63x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.57 ms: 1.57x faster                                                            |
| mako                     | 9.10 ms                                                         | 5.82 ms: 1.57x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.6 ms: 1.56x faster                                                            |
| go                       | 146 ms                                                          | 94.8 ms: 1.54x faster                                                            |
| float                    | 69.6 ms                                                         | 46.5 ms: 1.50x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 60.6 ms: 1.48x faster                                                            |
| nbody                    | 79.1 ms                                                         | 57.1 ms: 1.39x faster                                                            |
| deepcopy                 | 310 us                                                          | 225 us: 1.38x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 58.3 ms: 1.37x faster                                                            |
| pyflate                  | 422 ms                                                          | 311 ms: 1.36x faster                                                             |
| comprehensions           | 17.7 us                                                         | 13.2 us: 1.35x faster                                                            |
| chaos                    | 74.4 ms                                                         | 55.2 ms: 1.35x faster                                                            |
| pylint                   | 384 ms                                                          | 286 ms: 1.34x faster                                                             |
| generators               | 31.6 ms                                                         | 24.3 ms: 1.30x faster                                                            |
| fannkuch                 | 317 ms                                                          | 244 ms: 1.30x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.49 sec: 1.29x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.55 ms: 1.27x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.05 ms: 1.26x faster                                                            |
| pycparser                | 1.04 sec                                                        | 833 ms: 1.25x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 7.95 ms: 1.24x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 156 us: 1.22x faster                                                             |
| scimark_fft              | 216 ms                                                          | 183 ms: 1.18x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 49.5 ms: 1.18x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.28 us: 1.18x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.17 sec: 1.17x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 564 ms: 1.17x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.97 us: 1.17x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 41.5 ms: 1.16x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.37 ms: 1.16x faster                                                            |
| regex_dna                | 131 ms                                                          | 113 ms: 1.15x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 244 us: 1.15x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 5.39 ms: 1.14x faster                                                            |
| thrift                   | 902 us                                                          | 794 us: 1.14x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 77.4 ms: 1.13x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.0 ms: 1.12x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 55.0 ms: 1.12x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 46.6 ms: 1.12x faster                                                            |
| raytrace                 | 303 ms                                                          | 273 ms: 1.11x faster                                                             |
| regex_compile            | 117 ms                                                          | 105 ms: 1.11x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.11x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                             |
| meteor_contest           | 80.0 ms                                                         | 73.1 ms: 1.10x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                                            |
| django_template          | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                            |
| richards_super           | 49.9 ms                                                         | 46.2 ms: 1.08x faster                                                            |
| tornado_http             | 118 ms                                                          | 110 ms: 1.07x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 15.0 ms: 1.05x faster                                                            |
| sympy_sum                | 122 ms                                                          | 119 ms: 1.03x faster                                                             |
| coroutines               | 17.9 ms                                                         | 17.4 ms: 1.03x faster                                                            |
| richards                 | 40.3 ms                                                         | 39.3 ms: 1.02x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 39.5 ns: 1.01x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.80 sec: 1.01x faster                                                           |
| sympy_str                | 229 ms                                                          | 231 ms: 1.01x slower                                                             |
| sympy_expand             | 391 ms                                                          | 397 ms: 1.02x slower                                                             |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.5 sec: 1.03x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 17.4 ms: 1.04x slower                                                            |
| logging_simple           | 7.29 us                                                         | 7.65 us: 1.05x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.05 sec: 1.05x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.40 us: 1.06x slower                                                            |
| logging_format           | 7.91 us                                                         | 8.37 us: 1.06x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.06x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 87.7 ms: 1.08x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.80 ms: 1.08x slower                                                            |
| pickle                   | 7.83 us                                                         | 8.55 us: 1.09x slower                                                            |
| asyncio_tcp              | 744 ms                                                          | 832 ms: 1.12x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 50.3 ms: 1.13x slower                                                            |
| coverage                 | 46.6 ms                                                         | 53.8 ms: 1.15x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 21.2 us: 1.16x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                            |
| genshi_text              | 21.0 ms                                                         | 24.6 ms: 1.17x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 55.2 ms: 1.18x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.95 ms: 1.23x slower                                                            |
| async_generators         | 241 ms                                                          | 314 ms: 1.30x slower                                                             |
| gc_traversal             | 1.28 ms                                                         | 1.83 ms: 1.43x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 95.5 ms: 1.44x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.19 ms: 1.71x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.16x faster                                                                     |

Benchmark hidden because not significant (3): 2to3, unpickle_list, json
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.191x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown