# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.485x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.39x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.66 sec: 1.17x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.1 ms: 1.37x faster                                                            |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 330 ms: 2.80x faster                                                             |
| async_tree_io           | 940 ms                                                          | 388 ms: 2.42x faster                                                             |
| async_tree_none         | 394 ms                                                          | 165 ms: 2.38x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 200 ms: 2.33x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.47x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.45x faster                                                             |
| float          | 69.6 ms                                                         | 43.4 ms: 1.60x faster                                                            |
| nbody          | 79.1 ms                                                         | 54.6 ms: 1.45x faster                                                            |
| Geometric mean | (ref)                                                           | 2.00x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 79.2 ms: 1.47x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.0 ms: 1.12x faster                                                            |
| regex_dna      | 131 ms                                                          | 120 ms: 1.08x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.63 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 107 us: 1.77x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.13 sec: 1.70x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 6.23 ms: 1.58x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.3 us: 1.56x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 201 us: 1.39x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 86.5 ms: 1.39x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 35.3 ms: 1.36x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 50.5 ms: 1.22x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.3 ms: 1.16x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.54 us: 1.15x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.76 us: 1.08x faster                                                            |
| pickle               | 7.83 us                                                         | 7.86 us: 1.00x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.40 us: 1.06x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.1 us: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.4 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.38 ms: 1.69x faster                                                            |
| django_template | 36.0 ms                                                         | 24.6 ms: 1.46x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.3 ms: 1.37x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.2 ms: 1.36x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.42 sec: 11.95x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 102 us: 3.89x faster                                                             |
| pidigits                 | 502 ms                                                          | 146 ms: 3.45x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 330 ms: 2.80x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 30.0 ms: 2.71x faster                                                            |
| async_tree_io            | 940 ms                                                          | 388 ms: 2.42x faster                                                             |
| async_tree_none          | 394 ms                                                          | 165 ms: 2.38x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 200 ms: 2.33x faster                                                             |
| mdp                      | 1.83 sec                                                        | 800 ms: 2.28x faster                                                             |
| pylint                   | 384 ms                                                          | 199 ms: 1.93x faster                                                             |
| go                       | 146 ms                                                          | 76.4 ms: 1.91x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.14 ms: 1.89x faster                                                            |
| chaos                    | 74.4 ms                                                         | 40.0 ms: 1.86x faster                                                            |
| thrift                   | 902 us                                                          | 490 us: 1.84x faster                                                             |
| deepcopy                 | 310 us                                                          | 171 us: 1.81x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 45.4 ms: 1.79x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 107 us: 1.77x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 56.1 ns: 1.74x faster                                                            |
| raytrace                 | 303 ms                                                          | 178 ms: 1.70x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.13 sec: 1.70x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.38 ms: 1.69x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.6 us: 1.67x faster                                                            |
| pyflate                  | 422 ms                                                          | 253 ms: 1.67x faster                                                             |
| richards_super           | 49.9 ms                                                         | 30.3 ms: 1.65x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.1 us: 1.64x faster                                                            |
| float                    | 69.6 ms                                                         | 43.4 ms: 1.60x faster                                                            |
| json                     | 4.76 ms                                                         | 3.02 ms: 1.58x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.23 ms: 1.58x faster                                                            |
| generators               | 31.6 ms                                                         | 20.2 ms: 1.57x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.3 us: 1.56x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.9 ms: 1.55x faster                                                            |
| scimark_sor              | 115 ms                                                          | 74.5 ms: 1.54x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 58.8 ms: 1.53x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 57.7 ms: 1.51x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 912 ms: 1.50x faster                                                             |
| richards                 | 40.3 ms                                                         | 26.9 ms: 1.50x faster                                                            |
| pycparser                | 1.04 sec                                                        | 696 ms: 1.50x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.11 ms: 1.49x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.80 us: 1.49x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 500 ms: 1.49x faster                                                             |
| fannkuch                 | 317 ms                                                          | 213 ms: 1.49x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.55 us: 1.47x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 447 ms: 1.47x faster                                                             |
| regex_compile            | 117 ms                                                          | 79.2 ms: 1.47x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.6 ms: 1.46x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.2 ms: 1.45x faster                                                            |
| nbody                    | 79.1 ms                                                         | 54.6 ms: 1.45x faster                                                            |
| scimark_fft              | 216 ms                                                          | 149 ms: 1.45x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.28 ms: 1.42x faster                                                            |
| sympy_sum                | 122 ms                                                          | 87.4 ms: 1.40x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 201 us: 1.39x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 86.5 ms: 1.39x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.3 ms: 1.37x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.1 ms: 1.37x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 35.3 ms: 1.36x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.2 ms: 1.36x faster                                                            |
| sympy_expand             | 391 ms                                                          | 295 ms: 1.33x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 845 us: 1.33x faster                                                             |
| sympy_str                | 229 ms                                                          | 173 ms: 1.32x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.7 ms: 1.31x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 62.0 ms: 1.29x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.2 ms: 1.26x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 50.5 ms: 1.22x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.54 us: 1.21x faster                                                            |
| 2to3                     | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| unpack_sequence          | 40.0 ns                                                         | 33.3 ns: 1.20x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.09 us: 1.20x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.66 sec: 1.17x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.3 ms: 1.16x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.54 us: 1.15x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 70.5 ms: 1.13x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.0 ms: 1.12x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.33 ms: 1.11x faster                                                            |
| regex_dna                | 131 ms                                                          | 120 ms: 1.08x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.76 us: 1.08x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.63 ms: 1.02x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.86 us: 1.00x slower                                                            |
| async_generators         | 241 ms                                                          | 248 ms: 1.03x slower                                                             |
| pickle_list              | 3.22 us                                                         | 3.40 us: 1.06x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.7 ms: 1.07x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.1 us: 1.10x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.4 ms: 1.11x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 94.7 ms: 1.43x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.13 ms: 1.66x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.32 ms: 1.90x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.47x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.485x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.44x
- 95% likely to have a speedup of 1.42x
- 99% likely to have a speedup of 1.39x

# Memory
- memory change: unknown