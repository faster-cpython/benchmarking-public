# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.477x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 224 ms: 1.19x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.66 sec: 1.18x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.6 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 330 ms: 2.79x faster                                                             |
| async_tree_io           | 940 ms                                                          | 393 ms: 2.39x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 205 ms: 2.28x faster                                                             |
| async_tree_none         | 394 ms                                                          | 174 ms: 2.26x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.42x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.45x faster                                                             |
| float          | 69.6 ms                                                         | 43.3 ms: 1.61x faster                                                            |
| nbody          | 79.1 ms                                                         | 54.9 ms: 1.44x faster                                                            |
| Geometric mean | (ref)                                                           | 2.00x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 78.9 ms: 1.48x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.0 ms: 1.13x faster                                                            |
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.45 ms: 1.80x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 105 us: 1.80x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.10 sec: 1.73x faster                                                           |
| json_loads           | 22.4 us                                                         | 14.3 us: 1.57x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 204 us: 1.37x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 88.0 ms: 1.36x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 35.7 ms: 1.35x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 51.2 ms: 1.20x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.60 us: 1.14x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.2 ms: 1.12x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.77 us: 1.08x faster                                                            |
| pickle               | 7.83 us                                                         | 7.67 us: 1.02x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.36 us: 1.04x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.4 us: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.29x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                            |
| python_startup         | 22.9 ms                                                         | 26.5 ms: 1.15x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.28 ms: 1.73x faster                                                            |
| django_template | 36.0 ms                                                         | 24.2 ms: 1.49x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.5 ms: 1.36x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.7 ms: 1.34x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.44 sec: 11.77x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 105 us: 3.76x faster                                                             |
| pidigits                 | 502 ms                                                          | 146 ms: 3.45x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 330 ms: 2.79x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 32.2 ms: 2.52x faster                                                            |
| async_tree_io            | 940 ms                                                          | 393 ms: 2.39x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 205 ms: 2.28x faster                                                             |
| mdp                      | 1.83 sec                                                        | 807 ms: 2.26x faster                                                             |
| async_tree_none          | 394 ms                                                          | 174 ms: 2.26x faster                                                             |
| go                       | 146 ms                                                          | 75.6 ms: 1.93x faster                                                            |
| pylint                   | 384 ms                                                          | 199 ms: 1.92x faster                                                             |
| thrift                   | 902 us                                                          | 489 us: 1.85x faster                                                             |
| chaos                    | 74.4 ms                                                         | 41.0 ms: 1.81x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 5.45 ms: 1.80x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 105 us: 1.80x faster                                                             |
| deepcopy                 | 310 us                                                          | 174 us: 1.79x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.26 ms: 1.78x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 46.4 ms: 1.75x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.10 sec: 1.73x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.28 ms: 1.73x faster                                                            |
| raytrace                 | 303 ms                                                          | 178 ms: 1.70x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.5 us: 1.68x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.2 ms: 1.65x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.3 us: 1.62x faster                                                            |
| float                    | 69.6 ms                                                         | 43.3 ms: 1.61x faster                                                            |
| generators               | 31.6 ms                                                         | 19.7 ms: 1.60x faster                                                            |
| pyflate                  | 422 ms                                                          | 265 ms: 1.59x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 61.9 ns: 1.58x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.3 us: 1.57x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.0 ms: 1.55x faster                                                            |
| fannkuch                 | 317 ms                                                          | 206 ms: 1.54x faster                                                             |
| json                     | 4.76 ms                                                         | 3.10 ms: 1.53x faster                                                            |
| richards                 | 40.3 ms                                                         | 26.4 ms: 1.52x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 59.0 ms: 1.52x faster                                                            |
| scimark_sor              | 115 ms                                                          | 75.8 ms: 1.52x faster                                                            |
| pycparser                | 1.04 sec                                                        | 690 ms: 1.51x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 907 ms: 1.51x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.10 ms: 1.49x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 442 ms: 1.49x faster                                                             |
| django_template          | 36.0 ms                                                         | 24.2 ms: 1.49x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.55 us: 1.48x faster                                                            |
| regex_compile            | 117 ms                                                          | 78.9 ms: 1.48x faster                                                            |
| scimark_fft              | 216 ms                                                          | 148 ms: 1.46x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.84 us: 1.46x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 512 ms: 1.45x faster                                                             |
| nbody                    | 79.1 ms                                                         | 54.9 ms: 1.44x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.25 ms: 1.44x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.9 ms: 1.43x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 61.3 ms: 1.42x faster                                                            |
| sympy_sum                | 122 ms                                                          | 87.0 ms: 1.41x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 204 us: 1.37x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 88.0 ms: 1.36x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.5 ms: 1.36x faster                                                            |
| sympy_str                | 229 ms                                                          | 169 ms: 1.35x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 38.6 ms: 1.35x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 35.7 ms: 1.35x faster                                                            |
| sympy_expand             | 391 ms                                                          | 290 ms: 1.34x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 34.7 ms: 1.34x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 12.7 ms: 1.31x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 864 us: 1.30x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 65.5 ms: 1.23x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.7 ms: 1.22x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.52 us: 1.21x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.04 us: 1.21x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 33.2 ns: 1.21x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 51.2 ms: 1.20x faster                                                            |
| 2to3                     | 265 ms                                                          | 224 ms: 1.19x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.66 sec: 1.18x faster                                                           |
| unpickle                 | 9.82 us                                                         | 8.60 us: 1.14x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.24 ms: 1.14x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.0 ms: 1.13x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.2 ms: 1.12x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 72.4 ms: 1.10x faster                                                            |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.77 us: 1.08x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.67 us: 1.02x faster                                                            |
| async_generators         | 241 ms                                                          | 251 ms: 1.04x slower                                                             |
| pickle_list              | 3.22 us                                                         | 3.36 us: 1.04x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.4 us: 1.06x slower                                                            |
| coverage                 | 46.6 ms                                                         | 51.1 ms: 1.10x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.5 ms: 1.15x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 96.2 ms: 1.45x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.21 ms: 1.73x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.32 ms: 1.90x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.46x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.477x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.44x
- 95% likely to have a speedup of 1.42x
- 99% likely to have a speedup of 1.38x

# Memory
- memory change: unknown