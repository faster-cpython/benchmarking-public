# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-x86
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.286x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 235 ms: 1.13x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.72 sec: 1.13x faster                                                          |
| html5lib       | 52.1 ms                                                         | 40.9 ms: 1.27x faster                                                           |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 376 ms: 2.50x faster                                                            |
| async_tree_none         | 394 ms                                                          | 174 ms: 2.27x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 213 ms: 2.19x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 441 ms: 2.09x faster                                                            |
| Geometric mean          | (ref)                                                           | 2.26x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 217 ms: 2.31x faster                                                            |
| float          | 69.6 ms                                                         | 46.3 ms: 1.50x faster                                                           |
| nbody          | 79.1 ms                                                         | 69.2 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                           | 1.58x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 88.8 ms: 1.31x faster                                                           |
| regex_dna      | 131 ms                                                          | 132 ms: 1.01x slower                                                            |
| regex_v8       | 15.8 ms                                                         | 17.4 ms: 1.10x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.39 sec: 1.37x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 7.49 ms: 1.31x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 224 us: 1.25x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 154 us: 1.23x faster                                                            |
| pickle_list          | 3.22 us                                                         | 2.70 us: 1.19x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.57 us: 1.16x faster                                                           |
| pickle_dict          | 18.2 us                                                         | 17.0 us: 1.07x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 113 ms: 1.06x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.4 us: 1.05x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 46.8 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 72.6 ms: 1.02x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.05x slower                                                           |
| pickle               | 7.83 us                                                         | 8.31 us: 1.06x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 67.3 ms: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.1 ms: 1.22x slower                                                           |
| python_startup         | 22.9 ms                                                         | 28.7 ms: 1.25x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.24x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.0 ms: 1.33x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 16.1 ms: 1.31x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 36.3 ms: 1.29x faster                                                           |
| mako            | 9.10 ms                                                         | 7.79 ms: 1.17x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.27x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 124 us: 3.20x faster                                                            |
| async_tree_io            | 940 ms                                                          | 376 ms: 2.50x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 32.7 ms: 2.49x faster                                                           |
| pidigits                 | 502 ms                                                          | 217 ms: 2.31x faster                                                            |
| async_tree_none          | 394 ms                                                          | 174 ms: 2.27x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 213 ms: 2.19x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 441 ms: 2.09x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.01 ms: 2.01x faster                                                           |
| pylint                   | 384 ms                                                          | 205 ms: 1.87x faster                                                            |
| generators               | 31.6 ms                                                         | 17.0 ms: 1.85x faster                                                           |
| go                       | 146 ms                                                          | 79.1 ms: 1.84x faster                                                           |
| chaos                    | 74.4 ms                                                         | 44.9 ms: 1.66x faster                                                           |
| deepcopy                 | 310 us                                                          | 187 us: 1.66x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.2 us: 1.63x faster                                                           |
| raytrace                 | 303 ms                                                          | 192 ms: 1.57x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 63.4 ns: 1.54x faster                                                           |
| scimark_sor              | 115 ms                                                          | 75.5 ms: 1.52x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 873 us: 1.52x faster                                                            |
| float                    | 69.6 ms                                                         | 46.3 ms: 1.50x faster                                                           |
| unpack_sequence          | 40.0 ns                                                         | 27.7 ns: 1.44x faster                                                           |
| comprehensions           | 17.7 us                                                         | 12.3 us: 1.44x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.10 ms: 1.44x faster                                                           |
| thrift                   | 902 us                                                          | 628 us: 1.44x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 43.8 ms: 1.41x faster                                                           |
| pyflate                  | 422 ms                                                          | 300 ms: 1.41x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.38 ms: 1.40x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 58.4 ms: 1.39x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 1.94 us: 1.38x faster                                                           |
| richards_super           | 49.9 ms                                                         | 36.0 ms: 1.38x faster                                                           |
| pycparser                | 1.04 sec                                                        | 757 ms: 1.38x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.39 sec: 1.37x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 551 ms: 1.35x faster                                                            |
| coroutines               | 17.9 ms                                                         | 13.5 ms: 1.33x faster                                                           |
| django_template          | 36.0 ms                                                         | 27.0 ms: 1.33x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 60.6 ms: 1.32x faster                                                           |
| regex_compile            | 117 ms                                                          | 88.8 ms: 1.31x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.49 ms: 1.31x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 16.1 ms: 1.31x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 36.3 ms: 1.29x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 45.8 ms: 1.28x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 40.9 ms: 1.27x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.08 sec: 1.27x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.57 ms: 1.26x faster                                                           |
| richards                 | 40.3 ms                                                         | 32.0 ms: 1.26x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 69.5 ms: 1.25x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 224 us: 1.25x faster                                                            |
| sympy_sum                | 122 ms                                                          | 98.1 ms: 1.25x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.85 us: 1.24x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 532 ms: 1.24x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 154 us: 1.23x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 74.1 ms: 1.21x faster                                                           |
| sympy_str                | 229 ms                                                          | 190 ms: 1.20x faster                                                            |
| sympy_expand             | 391 ms                                                          | 328 ms: 1.19x faster                                                            |
| pickle_list              | 3.22 us                                                         | 2.70 us: 1.19x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 195 ms: 1.18x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 14.2 ms: 1.17x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.79 ms: 1.17x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 38.4 ms: 1.16x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.57 us: 1.16x faster                                                           |
| nbody                    | 79.1 ms                                                         | 69.2 ms: 1.14x faster                                                           |
| fannkuch                 | 317 ms                                                          | 280 ms: 1.13x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.72 sec: 1.13x faster                                                          |
| 2to3                     | 265 ms                                                          | 235 ms: 1.13x faster                                                            |
| json                     | 4.76 ms                                                         | 4.26 ms: 1.12x faster                                                           |
| scimark_fft              | 216 ms                                                          | 197 ms: 1.10x faster                                                            |
| pickle_dict              | 18.2 us                                                         | 17.0 us: 1.07x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 113 ms: 1.06x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.4 us: 1.05x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 76.8 ms: 1.04x faster                                                           |
| async_generators         | 241 ms                                                          | 233 ms: 1.03x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.65 us: 1.03x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 46.8 ms: 1.03x faster                                                           |
| logging_simple           | 7.29 us                                                         | 7.10 us: 1.03x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.79 sec: 1.02x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                          |
| regex_dna                | 131 ms                                                          | 132 ms: 1.01x slower                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 72.6 ms: 1.02x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.05x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.31 us: 1.06x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 67.3 ms: 1.09x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 17.4 ms: 1.10x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.93 ms: 1.16x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.32 ms: 1.18x slower                                                           |
| coverage                 | 46.6 ms                                                         | 55.0 ms: 1.18x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 22.1 ms: 1.22x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.98 ms: 1.24x slower                                                           |
| python_startup           | 22.9 ms                                                         | 28.7 ms: 1.25x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 92.4 ms: 1.39x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.17 ms: 1.68x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 2.45 ms: 1.91x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.26x faster                                                                    |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.286x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown