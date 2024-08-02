# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-x86
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 245 ms: 1.08x faster                                                            |
| chameleon      | 6.42 ms                                                         | 6.12 ms: 1.05x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                          |
| html5lib       | 52.1 ms                                                         | 45.2 ms: 1.15x faster                                                           |
| tornado_http   | 118 ms                                                          | 96.7 ms: 1.22x faster                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 472 ms: 1.95x faster                                                            |
| async_tree_io           | 940 ms                                                          | 527 ms: 1.79x faster                                                            |
| async_tree_none         | 394 ms                                                          | 225 ms: 1.75x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                            |
| float          | 69.6 ms                                                         | 41.2 ms: 1.69x faster                                                           |
| nbody          | 79.1 ms                                                         | 54.6 ms: 1.45x faster                                                           |
| Geometric mean | (ref)                                                           | 1.84x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 93.9 ms: 1.24x faster                                                           |
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.68 ms: 1.47x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 199 us: 1.41x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 135 us: 1.41x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.39 sec: 1.37x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 40.4 ms: 1.19x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 103 ms: 1.17x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.1 ms: 1.16x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 55.6 ms: 1.11x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.96 us: 1.01x faster                                                           |
| pickle               | 7.83 us                                                         | 8.05 us: 1.03x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.63 us: 1.13x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.7 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.4 ms: 1.06x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.35 ms: 1.70x faster                                                           |
| django_template | 36.0 ms                                                         | 30.7 ms: 1.17x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 21.4 ms: 1.02x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 51.7 ms: 1.11x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 141 us: 2.81x faster                                                            |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 472 ms: 1.95x faster                                                            |
| async_tree_io            | 940 ms                                                          | 527 ms: 1.79x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 55.6 ns: 1.76x faster                                                           |
| async_tree_none          | 394 ms                                                          | 225 ms: 1.75x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                            |
| mako                     | 9.10 ms                                                         | 5.35 ms: 1.70x faster                                                           |
| float                    | 69.6 ms                                                         | 41.2 ms: 1.69x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 48.3 ms: 1.68x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 48.4 ms: 1.66x faster                                                           |
| pylint                   | 384 ms                                                          | 236 ms: 1.62x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.55 ms: 1.58x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.4 us: 1.56x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.7 ms: 1.52x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.68 ms: 1.47x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 916 us: 1.45x faster                                                            |
| nbody                    | 79.1 ms                                                         | 54.6 ms: 1.45x faster                                                           |
| raytrace                 | 303 ms                                                          | 209 ms: 1.45x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 20.6 us: 1.44x faster                                                           |
| richards_super           | 49.9 ms                                                         | 34.9 ms: 1.43x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 199 us: 1.41x faster                                                            |
| chaos                    | 74.4 ms                                                         | 52.9 ms: 1.41x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 135 us: 1.41x faster                                                            |
| fannkuch                 | 317 ms                                                          | 229 ms: 1.38x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.39 sec: 1.37x faster                                                          |
| generators               | 31.6 ms                                                         | 23.0 ms: 1.37x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.57 ms: 1.34x faster                                                           |
| go                       | 146 ms                                                          | 109 ms: 1.34x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.18 ms: 1.34x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.45 ms: 1.32x faster                                                           |
| pycparser                | 1.04 sec                                                        | 789 ms: 1.32x faster                                                            |
| pyflate                  | 422 ms                                                          | 321 ms: 1.32x faster                                                            |
| richards                 | 40.3 ms                                                         | 31.0 ms: 1.30x faster                                                           |
| scimark_fft              | 216 ms                                                          | 168 ms: 1.29x faster                                                            |
| scimark_sor              | 115 ms                                                          | 90.1 ms: 1.28x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 68.4 ms: 1.27x faster                                                           |
| regex_compile            | 117 ms                                                          | 93.9 ms: 1.24x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 72.4 ms: 1.24x faster                                                           |
| tornado_http             | 118 ms                                                          | 96.7 ms: 1.22x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.90 us: 1.21x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.14 sec: 1.20x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 625 ms: 1.19x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 40.4 ms: 1.19x faster                                                           |
| django_template          | 36.0 ms                                                         | 30.7 ms: 1.17x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 563 ms: 1.17x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 103 ms: 1.17x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.1 ms: 1.16x faster                                                           |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.15x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 45.2 ms: 1.15x faster                                                           |
| coroutines               | 17.9 ms                                                         | 15.7 ms: 1.15x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.61 sec: 1.14x faster                                                          |
| json                     | 4.76 ms                                                         | 4.22 ms: 1.13x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 993 us: 1.13x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 55.6 ms: 1.11x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 72.5 ms: 1.10x faster                                                           |
| sympy_str                | 229 ms                                                          | 210 ms: 1.09x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| 2to3                     | 265 ms                                                          | 245 ms: 1.08x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 41.6 ms: 1.08x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.08x faster                                                           |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                            |
| chameleon                | 6.42 ms                                                         | 6.12 ms: 1.05x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 221 ms: 1.04x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                          |
| sympy_expand             | 391 ms                                                          | 376 ms: 1.04x faster                                                            |
| logging_simple           | 7.29 us                                                         | 7.19 us: 1.01x faster                                                           |
| deepcopy                 | 310 us                                                          | 307 us: 1.01x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.82 us: 1.01x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.96 us: 1.01x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                          |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.73 us: 1.02x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 21.4 ms: 1.02x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 83.3 ms: 1.03x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.05 us: 1.03x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                           |
| python_startup           | 22.9 ms                                                         | 24.4 ms: 1.06x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 768 us: 1.11x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 51.7 ms: 1.11x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.63 us: 1.13x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.7 us: 1.14x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.49 ms: 1.14x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 76.4 ms: 1.15x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                           |
| async_generators         | 241 ms                                                          | 291 ms: 1.21x slower                                                            |
| coverage                 | 46.6 ms                                                         | 332 ms: 7.12x slower                                                            |
| thrift                   | 902 us                                                          | 10.3 ms: 11.37x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.16x faster                                                                    |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown