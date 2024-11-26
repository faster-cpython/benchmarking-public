# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-x86
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.111x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 258 ms: 1.03x faster                                                                     |
| docutils       | 1.95 sec                                                        | 1.94 sec: 1.00x faster                                                                   |
| html5lib       | 52.1 ms                                                         | 48.8 ms: 1.07x faster                                                                    |
| tornado_http   | 118 ms                                                          | 106 ms: 1.11x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 471 ms: 1.96x faster                                                                     |
| async_tree_none         | 394 ms                                                          | 226 ms: 1.74x faster                                                                     |
| async_tree_io           | 940 ms                                                          | 553 ms: 1.70x faster                                                                     |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                                     |
| Geometric mean          | (ref)                                                           | 1.77x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                                     |
| float          | 69.6 ms                                                         | 62.8 ms: 1.11x faster                                                                    |
| nbody          | 79.1 ms                                                         | 92.7 ms: 1.17x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 118 ms: 1.10x faster                                                                     |
| regex_compile  | 117 ms                                                          | 109 ms: 1.07x faster                                                                     |
| regex_v8       | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                                    |
| regex_effbot   | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.47 ms: 1.31x faster                                                                    |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                                     |
| pickle_pure_python   | 280 us                                                          | 262 us: 1.07x faster                                                                     |
| unpickle_pure_python | 189 us                                                          | 178 us: 1.06x faster                                                                     |
| json_loads           | 22.4 us                                                         | 21.3 us: 1.05x faster                                                                    |
| xml_etree_iterparse  | 70.8 ms                                                         | 69.8 ms: 1.01x faster                                                                    |
| xml_etree_process    | 48.1 ms                                                         | 51.2 ms: 1.06x slower                                                                    |
| xml_etree_generate   | 61.6 ms                                                         | 68.1 ms: 1.10x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                             |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                                    |
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.27 ms: 1.10x faster                                                                    |
| django_template | 36.0 ms                                                         | 33.2 ms: 1.09x faster                                                                    |
| genshi_xml      | 46.6 ms                                                         | 48.6 ms: 1.04x slower                                                                    |
| genshi_text     | 21.0 ms                                                         | 23.1 ms: 1.10x slower                                                                    |
| Geometric mean  | (ref)                                                           | 1.01x faster                                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 152 us: 2.60x faster                                                                     |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                                     |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 471 ms: 1.96x faster                                                                     |
| async_tree_none          | 394 ms                                                          | 226 ms: 1.74x faster                                                                     |
| async_tree_io            | 940 ms                                                          | 553 ms: 1.70x faster                                                                     |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                                     |
| pylint                   | 384 ms                                                          | 236 ms: 1.63x faster                                                                     |
| deltablue                | 4.04 ms                                                         | 2.76 ms: 1.46x faster                                                                    |
| chaos                    | 74.4 ms                                                         | 54.0 ms: 1.38x faster                                                                    |
| crypto_pyaes             | 81.3 ms                                                         | 59.5 ms: 1.37x faster                                                                    |
| raytrace                 | 303 ms                                                          | 228 ms: 1.32x faster                                                                     |
| json_dumps               | 9.82 ms                                                         | 7.47 ms: 1.31x faster                                                                    |
| logging_silent           | 97.9 ns                                                         | 75.6 ns: 1.30x faster                                                                    |
| deepcopy_memo            | 29.6 us                                                         | 23.0 us: 1.28x faster                                                                    |
| scimark_lu               | 89.8 ms                                                         | 71.0 ms: 1.26x faster                                                                    |
| comprehensions           | 17.7 us                                                         | 14.4 us: 1.24x faster                                                                    |
| deepcopy                 | 310 us                                                          | 252 us: 1.23x faster                                                                     |
| pycparser                | 1.04 sec                                                        | 857 ms: 1.22x faster                                                                     |
| sqlglot_parse            | 1.33 ms                                                         | 1.10 ms: 1.21x faster                                                                    |
| thrift                   | 902 us                                                          | 749 us: 1.20x faster                                                                     |
| go                       | 146 ms                                                          | 122 ms: 1.19x faster                                                                     |
| sqlglot_transpile        | 1.58 ms                                                         | 1.34 ms: 1.18x faster                                                                    |
| dulwich_log              | 58.5 ms                                                         | 50.0 ms: 1.17x faster                                                                    |
| generators               | 31.6 ms                                                         | 27.0 ms: 1.17x faster                                                                    |
| pyflate                  | 422 ms                                                          | 372 ms: 1.13x faster                                                                     |
| hexiom                   | 6.13 ms                                                         | 5.42 ms: 1.13x faster                                                                    |
| json                     | 4.76 ms                                                         | 4.25 ms: 1.12x faster                                                                    |
| tornado_http             | 118 ms                                                          | 106 ms: 1.11x faster                                                                     |
| scimark_sor              | 115 ms                                                          | 104 ms: 1.11x faster                                                                     |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                                     |
| richards_super           | 49.9 ms                                                         | 45.0 ms: 1.11x faster                                                                    |
| float                    | 69.6 ms                                                         | 62.8 ms: 1.11x faster                                                                    |
| regex_dna                | 131 ms                                                          | 118 ms: 1.10x faster                                                                     |
| mako                     | 9.10 ms                                                         | 8.27 ms: 1.10x faster                                                                    |
| sympy_sum                | 122 ms                                                          | 112 ms: 1.09x faster                                                                     |
| django_template          | 36.0 ms                                                         | 33.2 ms: 1.09x faster                                                                    |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.08x faster                                                                   |
| bench_thread_pool        | 1.12 ms                                                         | 1.04 ms: 1.07x faster                                                                    |
| deepcopy_reduce          | 2.68 us                                                         | 2.50 us: 1.07x faster                                                                    |
| nqueens                  | 87.1 ms                                                         | 81.6 ms: 1.07x faster                                                                    |
| pickle_pure_python       | 280 us                                                          | 262 us: 1.07x faster                                                                     |
| html5lib                 | 52.1 ms                                                         | 48.8 ms: 1.07x faster                                                                    |
| regex_compile            | 117 ms                                                          | 109 ms: 1.07x faster                                                                     |
| unpickle_pure_python     | 189 us                                                          | 178 us: 1.06x faster                                                                     |
| sympy_integrate          | 16.6 ms                                                         | 15.7 ms: 1.06x faster                                                                    |
| json_loads               | 22.4 us                                                         | 21.3 us: 1.05x faster                                                                    |
| scimark_monte_carlo      | 61.9 ms                                                         | 58.9 ms: 1.05x faster                                                                    |
| asyncio_tcp              | 744 ms                                                          | 722 ms: 1.03x faster                                                                     |
| 2to3                     | 265 ms                                                          | 258 ms: 1.03x faster                                                                     |
| sympy_str                | 229 ms                                                          | 222 ms: 1.03x faster                                                                     |
| spectral_norm            | 80.2 ms                                                         | 78.4 ms: 1.02x faster                                                                    |
| xml_etree_iterparse      | 70.8 ms                                                         | 69.8 ms: 1.01x faster                                                                    |
| sympy_expand             | 391 ms                                                          | 389 ms: 1.01x faster                                                                     |
| docutils                 | 1.95 sec                                                        | 1.94 sec: 1.00x faster                                                                   |
| sqlglot_optimize         | 44.7 ms                                                         | 45.0 ms: 1.01x slower                                                                    |
| sqlglot_normalize        | 230 ms                                                          | 233 ms: 1.01x slower                                                                     |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.01x slower                                                                   |
| meteor_contest           | 80.0 ms                                                         | 81.2 ms: 1.01x slower                                                                    |
| pprint_safe_repr         | 658 ms                                                          | 672 ms: 1.02x slower                                                                     |
| pprint_pformat           | 1.37 sec                                                        | 1.41 sec: 1.03x slower                                                                   |
| coroutines               | 17.9 ms                                                         | 18.6 ms: 1.04x slower                                                                    |
| fannkuch                 | 317 ms                                                          | 329 ms: 1.04x slower                                                                     |
| regex_v8                 | 15.8 ms                                                         | 16.4 ms: 1.04x slower                                                                    |
| genshi_xml               | 46.6 ms                                                         | 48.6 ms: 1.04x slower                                                                    |
| python_startup           | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                                    |
| xml_etree_process        | 48.1 ms                                                         | 51.2 ms: 1.06x slower                                                                    |
| pathlib                  | 81.2 ms                                                         | 86.5 ms: 1.06x slower                                                                    |
| logging_format           | 7.91 us                                                         | 8.49 us: 1.07x slower                                                                    |
| create_gc_cycles         | 694 us                                                          | 760 us: 1.10x slower                                                                     |
| logging_simple           | 7.29 us                                                         | 7.99 us: 1.10x slower                                                                    |
| genshi_text              | 21.0 ms                                                         | 23.1 ms: 1.10x slower                                                                    |
| bench_mp_pool            | 66.4 ms                                                         | 73.1 ms: 1.10x slower                                                                    |
| xml_etree_generate       | 61.6 ms                                                         | 68.1 ms: 1.10x slower                                                                    |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                                    |
| scimark_fft              | 216 ms                                                          | 241 ms: 1.11x slower                                                                     |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                                    |
| coverage                 | 46.6 ms                                                         | 54.0 ms: 1.16x slower                                                                    |
| regex_effbot             | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                                    |
| nbody                    | 79.1 ms                                                         | 92.7 ms: 1.17x slower                                                                    |
| async_generators         | 241 ms                                                          | 304 ms: 1.26x slower                                                                     |
| telco                    | 4.83 ms                                                         | 6.49 ms: 1.34x slower                                                                    |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                             |

Benchmark hidden because not significant (3): richards, scimark_sparse_mat_mult, tomli_loads
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-pythonperf1_win32-x86-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.111x faster
# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown