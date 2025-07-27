# Results vs. 3.10.4

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.458x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 225 ms: 1.18x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.67 sec: 1.17x faster                                                           |
| html5lib       | 52.1 ms                                                         | 39.2 ms: 1.33x faster                                                            |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 338 ms: 2.73x faster                                                             |
| async_tree_io           | 940 ms                                                          | 401 ms: 2.34x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 203 ms: 2.30x faster                                                             |
| async_tree_none         | 394 ms                                                          | 178 ms: 2.22x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 149 ms: 3.38x faster                                                             |
| float          | 69.6 ms                                                         | 43.1 ms: 1.62x faster                                                            |
| nbody          | 79.1 ms                                                         | 57.7 ms: 1.37x faster                                                            |
| Geometric mean | (ref)                                                           | 1.96x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 79.7 ms: 1.46x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                            |
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 108 us: 1.76x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.13 sec: 1.69x faster                                                           |
| json_loads           | 22.4 us                                                         | 14.3 us: 1.57x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 6.36 ms: 1.54x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 88.8 ms: 1.35x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 208 us: 1.35x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 35.9 ms: 1.34x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 52.4 ms: 1.18x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.8 ms: 1.13x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.90 us: 1.10x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.94 us: 1.02x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.43 us: 1.07x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.2 us: 1.11x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.25x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.3 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.32 ms: 1.71x faster                                                            |
| django_template | 36.0 ms                                                         | 24.5 ms: 1.47x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 35.4 ms: 1.32x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 16.0 ms: 1.31x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.45x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.42 sec: 11.92x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 105 us: 3.78x faster                                                             |
| pidigits                 | 502 ms                                                          | 149 ms: 3.38x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 338 ms: 2.73x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 32.8 ms: 2.48x faster                                                            |
| async_tree_io            | 940 ms                                                          | 401 ms: 2.34x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 203 ms: 2.30x faster                                                             |
| mdp                      | 1.83 sec                                                        | 797 ms: 2.29x faster                                                             |
| async_tree_none          | 394 ms                                                          | 178 ms: 2.22x faster                                                             |
| pylint                   | 384 ms                                                          | 204 ms: 1.88x faster                                                             |
| chaos                    | 74.4 ms                                                         | 40.3 ms: 1.85x faster                                                            |
| deepcopy                 | 310 us                                                          | 169 us: 1.83x faster                                                             |
| go                       | 146 ms                                                          | 79.7 ms: 1.83x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.22 ms: 1.82x faster                                                            |
| thrift                   | 902 us                                                          | 506 us: 1.78x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 55.2 ns: 1.77x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 46.1 ms: 1.76x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 108 us: 1.76x faster                                                             |
| mako                     | 9.10 ms                                                         | 5.32 ms: 1.71x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.4 us: 1.71x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.13 sec: 1.69x faster                                                           |
| raytrace                 | 303 ms                                                          | 183 ms: 1.66x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 18.2 us: 1.62x faster                                                            |
| pyflate                  | 422 ms                                                          | 260 ms: 1.62x faster                                                             |
| float                    | 69.6 ms                                                         | 43.1 ms: 1.62x faster                                                            |
| richards_super           | 49.9 ms                                                         | 31.3 ms: 1.59x faster                                                            |
| generators               | 31.6 ms                                                         | 20.1 ms: 1.57x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.3 us: 1.57x faster                                                            |
| json                     | 4.76 ms                                                         | 3.05 ms: 1.56x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.36 ms: 1.54x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 911 ms: 1.50x faster                                                             |
| scimark_sor              | 115 ms                                                          | 77.3 ms: 1.49x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 60.4 ms: 1.49x faster                                                            |
| pycparser                | 1.04 sec                                                        | 703 ms: 1.48x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.81 us: 1.48x faster                                                            |
| fannkuch                 | 317 ms                                                          | 215 ms: 1.48x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.16 ms: 1.48x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.5 ms: 1.47x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 42.3 ms: 1.46x faster                                                            |
| regex_compile            | 117 ms                                                          | 79.7 ms: 1.46x faster                                                            |
| richards                 | 40.3 ms                                                         | 27.7 ms: 1.45x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 519 ms: 1.43x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 60.7 ms: 1.43x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 41.4 ms: 1.41x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.30 ms: 1.41x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 469 ms: 1.40x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.63 us: 1.40x faster                                                            |
| scimark_fft              | 216 ms                                                          | 154 ms: 1.40x faster                                                             |
| sympy_sum                | 122 ms                                                          | 88.3 ms: 1.39x faster                                                            |
| nbody                    | 79.1 ms                                                         | 57.7 ms: 1.37x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 88.8 ms: 1.35x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 208 us: 1.35x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 35.9 ms: 1.34x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 39.2 ms: 1.33x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 35.4 ms: 1.32x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 16.0 ms: 1.31x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 853 us: 1.31x faster                                                             |
| sympy_str                | 229 ms                                                          | 178 ms: 1.29x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.9 ms: 1.29x faster                                                            |
| sympy_expand             | 391 ms                                                          | 305 ms: 1.28x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 64.1 ms: 1.25x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.6 ms: 1.23x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.49 us: 1.22x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.10 us: 1.20x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 33.7 ns: 1.19x faster                                                            |
| 2to3                     | 265 ms                                                          | 225 ms: 1.18x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 52.4 ms: 1.18x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.67 sec: 1.17x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.8 ms: 1.13x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 71.4 ms: 1.12x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.90 us: 1.10x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.43 ms: 1.09x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                            |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.94 us: 1.02x faster                                                            |
| coverage                 | 46.6 ms                                                         | 49.0 ms: 1.05x slower                                                            |
| async_generators         | 241 ms                                                          | 255 ms: 1.06x slower                                                             |
| pickle_list              | 3.22 us                                                         | 3.43 us: 1.07x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.2 us: 1.11x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.3 ms: 1.19x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 95.9 ms: 1.45x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.16 ms: 1.68x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.33 ms: 1.91x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.44x faster                                                                     |

Benchmark hidden because not significant (2): pickle, regex_effbot
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1_win32-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.458x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.41x
- 95% likely to have a speedup of 1.39x
- 99% likely to have a speedup of 1.36x

# Memory
- memory change: unknown