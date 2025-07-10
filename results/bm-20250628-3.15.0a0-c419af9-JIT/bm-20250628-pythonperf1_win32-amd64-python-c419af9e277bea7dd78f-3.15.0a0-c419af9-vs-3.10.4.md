# Results vs. 3.10.4

- fork: python
- ref: c419af9e277bea7dd78f
- machine: windows-amd64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.481x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.65 sec: 1.18x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.1 ms: 1.37x faster                                                            |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 331 ms: 2.79x faster                                                             |
| async_tree_io           | 940 ms                                                          | 390 ms: 2.41x faster                                                             |
| async_tree_none         | 394 ms                                                          | 170 ms: 2.32x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.44x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.43x faster                                                             |
| float          | 69.6 ms                                                         | 44.5 ms: 1.56x faster                                                            |
| nbody          | 79.1 ms                                                         | 53.3 ms: 1.49x faster                                                            |
| Geometric mean | (ref)                                                           | 2.00x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.9 ms: 1.48x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.4 ms: 1.09x faster                                                            |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 109 us: 1.73x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.12 sec: 1.70x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 6.15 ms: 1.60x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.6 us: 1.54x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 203 us: 1.38x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 87.1 ms: 1.38x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 35.7 ms: 1.35x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 50.9 ms: 1.21x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.4 ms: 1.13x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.43x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.4 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.45 ms: 1.67x faster                                                            |
| django_template | 36.0 ms                                                         | 24.2 ms: 1.49x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.3 ms: 1.37x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.2 ms: 1.36x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 104 us: 3.80x faster                                                             |
| pidigits                 | 502 ms                                                          | 146 ms: 3.43x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 28.7 ms: 2.83x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 331 ms: 2.79x faster                                                             |
| async_tree_io            | 940 ms                                                          | 390 ms: 2.41x faster                                                             |
| async_tree_none          | 394 ms                                                          | 170 ms: 2.32x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| mdp                      | 1.83 sec                                                        | 810 ms: 2.25x faster                                                             |
| pylint                   | 384 ms                                                          | 198 ms: 1.94x faster                                                             |
| go                       | 146 ms                                                          | 75.9 ms: 1.92x faster                                                            |
| deepcopy                 | 310 us                                                          | 169 us: 1.83x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.21 ms: 1.83x faster                                                            |
| thrift                   | 902 us                                                          | 495 us: 1.82x faster                                                             |
| chaos                    | 74.4 ms                                                         | 40.9 ms: 1.82x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 54.3 ns: 1.80x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 45.7 ms: 1.78x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 109 us: 1.73x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.12 sec: 1.70x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 17.5 us: 1.69x faster                                                            |
| raytrace                 | 303 ms                                                          | 181 ms: 1.67x faster                                                             |
| mako                     | 9.10 ms                                                         | 5.45 ms: 1.67x faster                                                            |
| pyflate                  | 422 ms                                                          | 253 ms: 1.67x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.7 us: 1.66x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.6 ms: 1.63x faster                                                            |
| generators               | 31.6 ms                                                         | 19.4 ms: 1.62x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.15 ms: 1.60x faster                                                            |
| json                     | 4.76 ms                                                         | 3.02 ms: 1.58x faster                                                            |
| float                    | 69.6 ms                                                         | 44.5 ms: 1.56x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.6 us: 1.54x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.7 ms: 1.51x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 59.5 ms: 1.51x faster                                                            |
| scimark_sor              | 115 ms                                                          | 76.6 ms: 1.50x faster                                                            |
| pycparser                | 1.04 sec                                                        | 697 ms: 1.50x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.5 ms: 1.49x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.11 ms: 1.49x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.2 ms: 1.49x faster                                                            |
| nbody                    | 79.1 ms                                                         | 53.3 ms: 1.49x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 922 ms: 1.48x faster                                                             |
| regex_compile            | 117 ms                                                          | 78.9 ms: 1.48x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.56 us: 1.46x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 450 ms: 1.46x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 59.9 ms: 1.45x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.85 us: 1.45x faster                                                            |
| scimark_fft              | 216 ms                                                          | 150 ms: 1.44x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 40.7 ms: 1.44x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.26 ms: 1.44x faster                                                            |
| fannkuch                 | 317 ms                                                          | 224 ms: 1.41x faster                                                             |
| sympy_sum                | 122 ms                                                          | 87.7 ms: 1.40x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 203 us: 1.38x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 87.1 ms: 1.38x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.3 ms: 1.37x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.1 ms: 1.37x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.2 ms: 1.36x faster                                                            |
| sympy_str                | 229 ms                                                          | 170 ms: 1.35x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 35.7 ms: 1.35x faster                                                            |
| sympy_expand             | 391 ms                                                          | 293 ms: 1.33x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.8 ms: 1.30x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.2 ms: 1.26x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 64.9 ms: 1.24x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 50.9 ms: 1.21x faster                                                            |
| 2to3                     | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.64 us: 1.19x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.65 sec: 1.18x faster                                                           |
| logging_simple           | 7.29 us                                                         | 6.18 us: 1.18x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 70.3 ms: 1.14x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.4 ms: 1.13x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.32 ms: 1.12x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.4 ms: 1.09x faster                                                            |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                            |
| async_generators         | 241 ms                                                          | 250 ms: 1.04x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.6 ms: 1.07x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.4 ms: 1.11x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.11 ms: 1.65x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.32 ms: 1.90x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.48x faster                                                                     |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-pythonperf1_win32-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.481x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.43x
- 95% likely to have a speedup of 1.41x
- 99% likely to have a speedup of 1.38x

# Memory
- memory change: unknown