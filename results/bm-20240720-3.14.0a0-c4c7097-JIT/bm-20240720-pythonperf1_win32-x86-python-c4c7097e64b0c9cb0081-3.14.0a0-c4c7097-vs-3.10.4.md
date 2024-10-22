# Results vs. 3.10.4

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-x86
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 256 ms: 1.04x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                         |
| html5lib       | 52.1 ms                                                         | 47.8 ms: 1.09x faster                                                          |
| tornado_http   | 118 ms                                                          | 106 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 468 ms: 1.97x faster                                                           |
| async_tree_none         | 394 ms                                                          | 218 ms: 1.80x faster                                                           |
| async_tree_io           | 940 ms                                                          | 540 ms: 1.74x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 269 ms: 1.74x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| float          | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                          |
| nbody          | 79.1 ms                                                         | 56.7 ms: 1.40x faster                                                          |
| Geometric mean | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 94.3 ms: 1.24x faster                                                          |
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.05 ms: 1.39x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 214 us: 1.31x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.51 sec: 1.26x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 151 us: 1.26x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.8 ms: 1.13x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 44.5 ms: 1.08x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 58.6 ms: 1.05x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.43 ms: 1.68x faster                                                          |
| django_template | 36.0 ms                                                         | 33.2 ms: 1.08x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 22.9 ms: 1.09x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 52.7 ms: 1.13x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.10x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 146 us: 2.72x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 468 ms: 1.97x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 16.1 us: 1.84x faster                                                          |
| async_tree_none          | 394 ms                                                          | 218 ms: 1.80x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 46.3 ms: 1.76x faster                                                          |
| async_tree_io            | 940 ms                                                          | 540 ms: 1.74x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 269 ms: 1.74x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.43 ms: 1.68x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 47.9 ms: 1.67x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 58.7 ns: 1.67x faster                                                          |
| float                    | 69.6 ms                                                         | 43.5 ms: 1.60x faster                                                          |
| pylint                   | 384 ms                                                          | 242 ms: 1.59x faster                                                           |
| pyflate                  | 422 ms                                                          | 267 ms: 1.58x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.7 us: 1.52x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.74 ms: 1.48x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 43.1 ms: 1.44x faster                                                          |
| chaos                    | 74.4 ms                                                         | 52.3 ms: 1.42x faster                                                          |
| nbody                    | 79.1 ms                                                         | 56.7 ms: 1.40x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.05 ms: 1.39x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 959 us: 1.39x faster                                                           |
| fannkuch                 | 317 ms                                                          | 233 ms: 1.36x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.62 ms: 1.33x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.44 ms: 1.33x faster                                                          |
| deepcopy                 | 310 us                                                          | 235 us: 1.32x faster                                                           |
| raytrace                 | 303 ms                                                          | 229 ms: 1.32x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 214 us: 1.31x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.22 ms: 1.30x faster                                                          |
| scimark_fft              | 216 ms                                                          | 168 ms: 1.29x faster                                                           |
| richards_super           | 49.9 ms                                                         | 38.7 ms: 1.29x faster                                                          |
| go                       | 146 ms                                                          | 114 ms: 1.28x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.51 sec: 1.26x faster                                                         |
| unpickle_pure_python     | 189 us                                                          | 151 us: 1.26x faster                                                           |
| pycparser                | 1.04 sec                                                        | 835 ms: 1.25x faster                                                           |
| regex_compile            | 117 ms                                                          | 94.3 ms: 1.24x faster                                                          |
| thrift                   | 902 us                                                          | 751 us: 1.20x faster                                                           |
| richards                 | 40.3 ms                                                         | 33.6 ms: 1.20x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 73.5 ms: 1.18x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.17 sec: 1.17x faster                                                         |
| scimark_lu               | 89.8 ms                                                         | 77.6 ms: 1.16x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 570 ms: 1.16x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.15x faster                                                           |
| generators               | 31.6 ms                                                         | 27.5 ms: 1.15x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 989 us: 1.13x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 70.7 ms: 1.13x faster                                                          |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                                           |
| scimark_sor              | 115 ms                                                          | 102 ms: 1.13x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.8 ms: 1.13x faster                                                          |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                           |
| tornado_http             | 118 ms                                                          | 106 ms: 1.11x faster                                                           |
| json                     | 4.76 ms                                                         | 4.33 ms: 1.10x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.46 us: 1.09x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 47.8 ms: 1.09x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.68 sec: 1.09x faster                                                         |
| asyncio_tcp              | 744 ms                                                          | 685 ms: 1.09x faster                                                           |
| django_template          | 36.0 ms                                                         | 33.2 ms: 1.08x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 44.5 ms: 1.08x faster                                                          |
| sympy_str                | 229 ms                                                          | 215 ms: 1.07x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 58.6 ms: 1.05x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.9 ms: 1.05x faster                                                          |
| 2to3                     | 265 ms                                                          | 256 ms: 1.04x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 43.6 ms: 1.03x faster                                                          |
| sympy_expand             | 391 ms                                                          | 383 ms: 1.02x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                         |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                         |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| coroutines               | 17.9 ms                                                         | 18.4 ms: 1.02x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.36 us: 1.06x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.74 us: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 87.9 ms: 1.08x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.9 ms: 1.09x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 766 us: 1.10x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 52.7 ms: 1.13x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.9 ms: 1.14x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 75.4 ms: 1.14x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.53 ms: 1.15x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| async_generators         | 241 ms                                                          | 314 ms: 1.30x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.21x faster                                                                   |

Benchmark hidden because not significant (1): sqlglot_normalize
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown