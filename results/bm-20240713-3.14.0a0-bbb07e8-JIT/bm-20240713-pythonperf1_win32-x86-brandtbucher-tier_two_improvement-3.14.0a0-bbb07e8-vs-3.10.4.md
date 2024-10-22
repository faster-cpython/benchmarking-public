# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_improvement
- machine: windows-x86
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 251 ms: 1.06x faster                                                                 |
| docutils       | 1.95 sec                                                        | 1.91 sec: 1.02x faster                                                               |
| html5lib       | 52.1 ms                                                         | 47.5 ms: 1.10x faster                                                                |
| tornado_http   | 118 ms                                                          | 97.0 ms: 1.21x faster                                                                |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 482 ms: 1.91x faster                                                                 |
| async_tree_none         | 394 ms                                                          | 220 ms: 1.79x faster                                                                 |
| async_tree_io           | 940 ms                                                          | 531 ms: 1.77x faster                                                                 |
| async_tree_memoization  | 467 ms                                                          | 272 ms: 1.72x faster                                                                 |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.57x faster                                                                 |
| float          | 69.6 ms                                                         | 43.0 ms: 1.62x faster                                                                |
| nbody          | 79.1 ms                                                         | 61.2 ms: 1.29x faster                                                                |
| Geometric mean | (ref)                                                           | 1.75x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 94.4 ms: 1.24x faster                                                                |
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                                 |
| regex_v8       | 15.8 ms                                                         | 15.7 ms: 1.00x faster                                                                |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                                |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.17 ms: 1.37x faster                                                                |
| pickle_pure_python   | 280 us                                                          | 212 us: 1.32x faster                                                                 |
| unpickle_pure_python | 189 us                                                          | 146 us: 1.30x faster                                                                 |
| tomli_loads          | 1.91 sec                                                        | 1.49 sec: 1.28x faster                                                               |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.15x faster                                                                 |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.0 ms: 1.14x faster                                                                |
| xml_etree_process    | 48.1 ms                                                         | 43.4 ms: 1.11x faster                                                                |
| xml_etree_generate   | 61.6 ms                                                         | 58.1 ms: 1.06x faster                                                                |
| json_loads           | 22.4 us                                                         | 21.7 us: 1.03x faster                                                                |
| Geometric mean       | (ref)                                                           | 1.19x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.1 ms: 1.01x slower                                                                |
| python_startup_no_site | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                                |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.39 ms: 1.69x faster                                                                |
| django_template | 36.0 ms                                                         | 33.6 ms: 1.07x faster                                                                |
| genshi_text     | 21.0 ms                                                         | 22.9 ms: 1.09x slower                                                                |
| genshi_xml      | 46.6 ms                                                         | 52.9 ms: 1.14x slower                                                                |
| Geometric mean  | (ref)                                                           | 1.10x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 144 us: 2.74x faster                                                                 |
| pidigits                 | 502 ms                                                          | 196 ms: 2.57x faster                                                                 |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 482 ms: 1.91x faster                                                                 |
| deepcopy_memo            | 29.6 us                                                         | 15.8 us: 1.87x faster                                                                |
| async_tree_none          | 394 ms                                                          | 220 ms: 1.79x faster                                                                 |
| async_tree_io            | 940 ms                                                          | 531 ms: 1.77x faster                                                                 |
| crypto_pyaes             | 81.3 ms                                                         | 46.8 ms: 1.74x faster                                                                |
| async_tree_memoization   | 467 ms                                                          | 272 ms: 1.72x faster                                                                 |
| logging_silent           | 97.9 ns                                                         | 57.4 ns: 1.70x faster                                                                |
| mako                     | 9.10 ms                                                         | 5.39 ms: 1.69x faster                                                                |
| spectral_norm            | 80.2 ms                                                         | 48.7 ms: 1.65x faster                                                                |
| float                    | 69.6 ms                                                         | 43.0 ms: 1.62x faster                                                                |
| pyflate                  | 422 ms                                                          | 263 ms: 1.61x faster                                                                 |
| pylint                   | 384 ms                                                          | 240 ms: 1.60x faster                                                                 |
| comprehensions           | 17.7 us                                                         | 11.2 us: 1.58x faster                                                                |
| deltablue                | 4.04 ms                                                         | 2.67 ms: 1.51x faster                                                                |
| scimark_monte_carlo      | 61.9 ms                                                         | 42.8 ms: 1.45x faster                                                                |
| sqlglot_parse            | 1.33 ms                                                         | 942 us: 1.41x faster                                                                 |
| fannkuch                 | 317 ms                                                          | 225 ms: 1.41x faster                                                                 |
| chaos                    | 74.4 ms                                                         | 53.3 ms: 1.40x faster                                                                |
| json_dumps               | 9.82 ms                                                         | 7.17 ms: 1.37x faster                                                                |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.37 ms: 1.37x faster                                                                |
| pickle_pure_python       | 280 us                                                          | 212 us: 1.32x faster                                                                 |
| raytrace                 | 303 ms                                                          | 229 ms: 1.32x faster                                                                 |
| hexiom                   | 6.13 ms                                                         | 4.68 ms: 1.31x faster                                                                |
| sqlglot_transpile        | 1.58 ms                                                         | 1.21 ms: 1.31x faster                                                                |
| richards_super           | 49.9 ms                                                         | 38.2 ms: 1.31x faster                                                                |
| scimark_fft              | 216 ms                                                          | 166 ms: 1.31x faster                                                                 |
| unpickle_pure_python     | 189 us                                                          | 146 us: 1.30x faster                                                                 |
| deepcopy                 | 310 us                                                          | 240 us: 1.29x faster                                                                 |
| nbody                    | 79.1 ms                                                         | 61.2 ms: 1.29x faster                                                                |
| go                       | 146 ms                                                          | 113 ms: 1.29x faster                                                                 |
| tomli_loads              | 1.91 sec                                                        | 1.49 sec: 1.28x faster                                                               |
| pycparser                | 1.04 sec                                                        | 826 ms: 1.26x faster                                                                 |
| generators               | 31.6 ms                                                         | 25.5 ms: 1.24x faster                                                                |
| regex_compile            | 117 ms                                                          | 94.4 ms: 1.24x faster                                                                |
| tornado_http             | 118 ms                                                          | 97.0 ms: 1.21x faster                                                                |
| richards                 | 40.3 ms                                                         | 33.7 ms: 1.19x faster                                                                |
| asyncio_tcp              | 744 ms                                                          | 623 ms: 1.19x faster                                                                 |
| thrift                   | 902 us                                                          | 760 us: 1.19x faster                                                                 |
| nqueens                  | 87.1 ms                                                         | 73.7 ms: 1.18x faster                                                                |
| pprint_pformat           | 1.37 sec                                                        | 1.16 sec: 1.18x faster                                                               |
| pprint_safe_repr         | 658 ms                                                          | 563 ms: 1.17x faster                                                                 |
| scimark_sor              | 115 ms                                                          | 99.9 ms: 1.15x faster                                                                |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.15x faster                                                                 |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.0 ms: 1.14x faster                                                                |
| bench_thread_pool        | 1.12 ms                                                         | 980 us: 1.14x faster                                                                 |
| meteor_contest           | 80.0 ms                                                         | 70.1 ms: 1.14x faster                                                                |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.14x faster                                                                 |
| scimark_lu               | 89.8 ms                                                         | 80.4 ms: 1.12x faster                                                                |
| json                     | 4.76 ms                                                         | 4.27 ms: 1.11x faster                                                                |
| mdp                      | 1.83 sec                                                        | 1.64 sec: 1.11x faster                                                               |
| deepcopy_reduce          | 2.68 us                                                         | 2.42 us: 1.11x faster                                                                |
| xml_etree_process        | 48.1 ms                                                         | 43.4 ms: 1.11x faster                                                                |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                                 |
| html5lib                 | 52.1 ms                                                         | 47.5 ms: 1.10x faster                                                                |
| django_template          | 36.0 ms                                                         | 33.6 ms: 1.07x faster                                                                |
| sympy_str                | 229 ms                                                          | 214 ms: 1.07x faster                                                                 |
| xml_etree_generate       | 61.6 ms                                                         | 58.1 ms: 1.06x faster                                                                |
| 2to3                     | 265 ms                                                          | 251 ms: 1.06x faster                                                                 |
| sympy_integrate          | 16.6 ms                                                         | 15.9 ms: 1.05x faster                                                                |
| coroutines               | 17.9 ms                                                         | 17.1 ms: 1.05x faster                                                                |
| sqlglot_optimize         | 44.7 ms                                                         | 43.1 ms: 1.04x faster                                                                |
| json_loads               | 22.4 us                                                         | 21.7 us: 1.03x faster                                                                |
| sympy_expand             | 391 ms                                                          | 379 ms: 1.03x faster                                                                 |
| docutils                 | 1.95 sec                                                        | 1.91 sec: 1.02x faster                                                               |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                               |
| regex_v8                 | 15.8 ms                                                         | 15.7 ms: 1.00x faster                                                                |
| sqlglot_normalize        | 230 ms                                                          | 232 ms: 1.01x slower                                                                 |
| python_startup           | 22.9 ms                                                         | 23.1 ms: 1.01x slower                                                                |
| logging_format           | 7.91 us                                                         | 8.06 us: 1.02x slower                                                                |
| logging_simple           | 7.29 us                                                         | 7.44 us: 1.02x slower                                                                |
| pathlib                  | 81.2 ms                                                         | 83.2 ms: 1.02x slower                                                                |
| python_startup_no_site   | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                                |
| create_gc_cycles         | 694 us                                                          | 755 us: 1.09x slower                                                                 |
| genshi_text              | 21.0 ms                                                         | 22.9 ms: 1.09x slower                                                                |
| bench_mp_pool            | 66.4 ms                                                         | 73.4 ms: 1.11x slower                                                                |
| coverage                 | 46.6 ms                                                         | 51.9 ms: 1.12x slower                                                                |
| genshi_xml               | 46.6 ms                                                         | 52.9 ms: 1.14x slower                                                                |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                                |
| gc_traversal             | 1.28 ms                                                         | 1.46 ms: 1.14x slower                                                                |
| telco                    | 4.83 ms                                                         | 5.60 ms: 1.16x slower                                                                |
| async_generators         | 241 ms                                                          | 321 ms: 1.33x slower                                                                 |
| Geometric mean           | (ref)                                                           | 1.22x faster                                                                         |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240713-3.14.0a0-bbb07e8-JIT/bm-20240713-pythonperf1_win32-x86-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown