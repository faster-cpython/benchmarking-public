# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-x86
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 233 ms: 1.14x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.85 ms: 1.10x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                          |
| html5lib       | 52.1 ms                                                         | 45.1 ms: 1.15x faster                                                           |
| tornado_http   | 118 ms                                                          | 94.2 ms: 1.25x faster                                                           |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 466 ms: 1.98x faster                                                            |
| async_tree_io           | 940 ms                                                          | 532 ms: 1.77x faster                                                            |
| async_tree_none         | 394 ms                                                          | 230 ms: 1.71x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                            |
| float          | 69.6 ms                                                         | 52.6 ms: 1.32x faster                                                           |
| nbody          | 79.1 ms                                                         | 73.9 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                           | 1.53x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 100.0 ms: 1.17x faster                                                          |
| regex_dna      | 131 ms                                                          | 127 ms: 1.03x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.97 ms: 1.19x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.94 ms: 1.42x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 146 us: 1.29x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 219 us: 1.28x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 103 ms: 1.16x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 42.4 ms: 1.13x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.6 ms: 1.10x faster                                                           |
| json_loads           | 22.4 us                                                         | 21.1 us: 1.06x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.87 us: 1.04x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 60.1 ms: 1.03x faster                                                           |
| pickle               | 7.83 us                                                         | 8.01 us: 1.02x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.4 us: 1.12x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.65 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.97 ms: 1.31x faster                                                           |
| django_template | 36.0 ms                                                         | 30.6 ms: 1.18x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 19.2 ms: 1.09x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 44.4 ms: 1.05x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 139 us: 2.86x faster                                                            |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 466 ms: 1.98x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.23 ms: 1.81x faster                                                           |
| async_tree_io            | 940 ms                                                          | 532 ms: 1.77x faster                                                            |
| pylint                   | 384 ms                                                          | 218 ms: 1.76x faster                                                            |
| async_tree_none          | 394 ms                                                          | 230 ms: 1.71x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 58.2 ns: 1.68x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                            |
| raytrace                 | 303 ms                                                          | 190 ms: 1.60x faster                                                            |
| chaos                    | 74.4 ms                                                         | 47.9 ms: 1.55x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 60.0 ms: 1.50x faster                                                           |
| generators               | 31.6 ms                                                         | 21.3 ms: 1.48x faster                                                           |
| comprehensions           | 17.7 us                                                         | 12.0 us: 1.47x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 56.1 ms: 1.45x faster                                                           |
| go                       | 146 ms                                                          | 102 ms: 1.43x faster                                                            |
| richards_super           | 49.9 ms                                                         | 34.9 ms: 1.43x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.30 ms: 1.43x faster                                                           |
| scimark_sor              | 115 ms                                                          | 80.6 ms: 1.43x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 934 us: 1.42x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.94 ms: 1.42x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 45.0 ms: 1.38x faster                                                           |
| pyflate                  | 422 ms                                                          | 307 ms: 1.38x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.17 ms: 1.35x faster                                                           |
| pycparser                | 1.04 sec                                                        | 786 ms: 1.32x faster                                                            |
| float                    | 69.6 ms                                                         | 52.6 ms: 1.32x faster                                                           |
| mako                     | 9.10 ms                                                         | 6.97 ms: 1.31x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 146 us: 1.29x faster                                                            |
| richards                 | 40.3 ms                                                         | 31.2 ms: 1.29x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 219 us: 1.28x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 23.4 us: 1.27x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 69.3 ms: 1.26x faster                                                           |
| tornado_http             | 118 ms                                                          | 94.2 ms: 1.25x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 66.3 ms: 1.21x faster                                                           |
| fannkuch                 | 317 ms                                                          | 266 ms: 1.19x faster                                                            |
| django_template          | 36.0 ms                                                         | 30.6 ms: 1.18x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                                          |
| regex_compile            | 117 ms                                                          | 100.0 ms: 1.17x faster                                                          |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.16x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.4 ms: 1.16x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 103 ms: 1.16x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 969 us: 1.16x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 45.1 ms: 1.15x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 2.00 us: 1.15x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.83 ms: 1.14x faster                                                           |
| 2to3                     | 265 ms                                                          | 233 ms: 1.14x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 42.4 ms: 1.13x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 14.8 ms: 1.13x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 40.2 ms: 1.11x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 207 ms: 1.11x faster                                                            |
| deepcopy                 | 310 us                                                          | 282 us: 1.10x faster                                                            |
| chameleon                | 6.42 ms                                                         | 5.85 ms: 1.10x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.6 ms: 1.10x faster                                                           |
| sympy_str                | 229 ms                                                          | 209 ms: 1.10x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.25 sec: 1.10x faster                                                          |
| json                     | 4.76 ms                                                         | 4.36 ms: 1.09x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 19.2 ms: 1.09x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.67 sec: 1.09x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 686 ms: 1.09x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 611 ms: 1.08x faster                                                            |
| nbody                    | 79.1 ms                                                         | 73.9 ms: 1.07x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 74.7 ms: 1.07x faster                                                           |
| sympy_expand             | 391 ms                                                          | 367 ms: 1.07x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.1 us: 1.06x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 44.4 ms: 1.05x faster                                                           |
| scimark_fft              | 216 ms                                                          | 207 ms: 1.05x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.87 us: 1.04x faster                                                           |
| regex_dna                | 131 ms                                                          | 127 ms: 1.03x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 60.1 ms: 1.03x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.63 us: 1.02x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                          |
| flaskblogging            | 2.03 sec                                                        | 2.04 sec: 1.00x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.01 us: 1.02x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 83.3 ms: 1.03x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.23 us: 1.04x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.61 us: 1.04x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 69.5 ms: 1.05x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 745 us: 1.07x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.42 ms: 1.11x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.4 us: 1.12x slower                                                           |
| async_generators         | 241 ms                                                          | 271 ms: 1.12x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.65 us: 1.14x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.97 ms: 1.19x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.15 ms: 1.27x slower                                                           |
| coverage                 | 46.6 ms                                                         | 304 ms: 6.53x slower                                                            |
| thrift                   | 902 us                                                          | 9.80 ms: 10.86x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.14x faster                                                                    |

Benchmark hidden because not significant (2): regex_v8, python_startup
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown