# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.441x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 224 ms: 1.19x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.67 sec: 1.17x faster                                                           |
| html5lib       | 52.1 ms                                                         | 41.9 ms: 1.24x faster                                                            |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 340 ms: 2.71x faster                                                             |
| async_tree_io           | 940 ms                                                          | 401 ms: 2.34x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 210 ms: 2.22x faster                                                             |
| async_tree_none         | 394 ms                                                          | 181 ms: 2.17x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 149 ms: 3.38x faster                                                             |
| float          | 69.6 ms                                                         | 44.3 ms: 1.57x faster                                                            |
| nbody          | 79.1 ms                                                         | 55.3 ms: 1.43x faster                                                            |
| Geometric mean | (ref)                                                           | 1.97x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 82.4 ms: 1.42x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.4 ms: 1.09x faster                                                            |
| regex_dna      | 131 ms                                                          | 124 ms: 1.05x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.70 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 108 us: 1.76x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.14 sec: 1.67x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 6.38 ms: 1.54x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.7 us: 1.53x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 89.3 ms: 1.34x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 35.9 ms: 1.34x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 210 us: 1.33x faster                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 51.0 ms: 1.21x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.4 ms: 1.12x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.85 us: 1.11x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.90 us: 1.03x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.37 us: 1.05x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.25x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                            |
| python_startup         | 22.9 ms                                                         | 26.5 ms: 1.16x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.34 ms: 1.71x faster                                                            |
| django_template | 36.0 ms                                                         | 26.0 ms: 1.38x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.7 ms: 1.35x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.9 ms: 1.32x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.43x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.44 sec: 11.76x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 107 us: 3.70x faster                                                             |
| pidigits                 | 502 ms                                                          | 149 ms: 3.38x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 340 ms: 2.71x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 33.5 ms: 2.42x faster                                                            |
| async_tree_io            | 940 ms                                                          | 401 ms: 2.34x faster                                                             |
| mdp                      | 1.83 sec                                                        | 807 ms: 2.26x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 210 ms: 2.22x faster                                                             |
| async_tree_none          | 394 ms                                                          | 181 ms: 2.17x faster                                                             |
| pylint                   | 384 ms                                                          | 206 ms: 1.86x faster                                                             |
| go                       | 146 ms                                                          | 79.5 ms: 1.83x faster                                                            |
| thrift                   | 902 us                                                          | 505 us: 1.79x faster                                                             |
| chaos                    | 74.4 ms                                                         | 41.9 ms: 1.77x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 108 us: 1.76x faster                                                             |
| deepcopy                 | 310 us                                                          | 179 us: 1.74x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 56.4 ns: 1.73x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.34 ms: 1.72x faster                                                            |
| mako                     | 9.10 ms                                                         | 5.34 ms: 1.71x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 47.8 ms: 1.70x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.14 sec: 1.67x faster                                                           |
| comprehensions           | 17.7 us                                                         | 10.7 us: 1.66x faster                                                            |
| generators               | 31.6 ms                                                         | 19.8 ms: 1.60x faster                                                            |
| raytrace                 | 303 ms                                                          | 189 ms: 1.60x faster                                                             |
| richards_super           | 49.9 ms                                                         | 31.5 ms: 1.59x faster                                                            |
| pyflate                  | 422 ms                                                          | 267 ms: 1.58x faster                                                             |
| float                    | 69.6 ms                                                         | 44.3 ms: 1.57x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 19.2 us: 1.54x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.38 ms: 1.54x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.7 us: 1.53x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.7 ms: 1.52x faster                                                            |
| json                     | 4.76 ms                                                         | 3.17 ms: 1.50x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 59.9 ms: 1.50x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 919 ms: 1.49x faster                                                             |
| fannkuch                 | 317 ms                                                          | 214 ms: 1.48x faster                                                             |
| pycparser                | 1.04 sec                                                        | 703 ms: 1.48x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 502 ms: 1.48x faster                                                             |
| scimark_sor              | 115 ms                                                          | 78.5 ms: 1.47x faster                                                            |
| scimark_fft              | 216 ms                                                          | 149 ms: 1.45x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 456 ms: 1.44x faster                                                             |
| richards                 | 40.3 ms                                                         | 27.9 ms: 1.44x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.28 ms: 1.43x faster                                                            |
| nbody                    | 79.1 ms                                                         | 55.3 ms: 1.43x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.60 us: 1.43x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.28 ms: 1.42x faster                                                            |
| regex_compile            | 117 ms                                                          | 82.4 ms: 1.42x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 62.1 ms: 1.40x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.92 us: 1.40x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 42.2 ms: 1.39x faster                                                            |
| django_template          | 36.0 ms                                                         | 26.0 ms: 1.38x faster                                                            |
| sympy_sum                | 122 ms                                                          | 89.8 ms: 1.36x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.7 ms: 1.35x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 89.3 ms: 1.34x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 35.9 ms: 1.34x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 210 us: 1.33x faster                                                             |
| genshi_text              | 21.0 ms                                                         | 15.9 ms: 1.32x faster                                                            |
| sympy_str                | 229 ms                                                          | 175 ms: 1.31x faster                                                             |
| sympy_expand             | 391 ms                                                          | 303 ms: 1.29x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 870 us: 1.29x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 13.0 ms: 1.28x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 41.9 ms: 1.24x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 65.0 ms: 1.23x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.8 ms: 1.21x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 51.0 ms: 1.21x faster                                                            |
| 2to3                     | 265 ms                                                          | 224 ms: 1.19x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.67 sec: 1.17x faster                                                           |
| logging_format           | 7.91 us                                                         | 6.85 us: 1.15x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.32 us: 1.15x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.4 ms: 1.12x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.85 us: 1.11x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 73.1 ms: 1.09x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.4 ms: 1.09x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 37.4 ns: 1.07x faster                                                            |
| regex_dna                | 131 ms                                                          | 124 ms: 1.05x faster                                                             |
| telco                    | 4.83 ms                                                         | 4.68 ms: 1.03x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.90 us: 1.03x faster                                                            |
| async_generators         | 241 ms                                                          | 244 ms: 1.01x slower                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.70 ms: 1.02x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.37 us: 1.05x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                            |
| coverage                 | 46.6 ms                                                         | 51.5 ms: 1.11x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.5 ms: 1.16x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 96.6 ms: 1.46x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.21 ms: 1.73x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.36 ms: 1.95x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.42x faster                                                                     |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.441x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.41x
- 95% likely to have a speedup of 1.39x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown