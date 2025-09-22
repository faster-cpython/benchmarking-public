# Results vs. 3.10.4

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.490x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.39x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 222 ms: 1.20x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.66 sec: 1.18x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.7 ms: 1.38x faster                                                            |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 331 ms: 2.78x faster                                                             |
| async_tree_io           | 940 ms                                                          | 386 ms: 2.44x faster                                                             |
| async_tree_none         | 394 ms                                                          | 173 ms: 2.28x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 206 ms: 2.27x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.43x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 148 ms: 3.39x faster                                                             |
| float          | 69.6 ms                                                         | 39.7 ms: 1.76x faster                                                            |
| nbody          | 79.1 ms                                                         | 55.0 ms: 1.44x faster                                                            |
| Geometric mean | (ref)                                                           | 2.05x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 77.8 ms: 1.50x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.2 ms: 1.11x faster                                                            |
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.38 ms: 1.82x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 107 us: 1.78x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.10 sec: 1.74x faster                                                           |
| json_loads           | 22.4 us                                                         | 14.0 us: 1.60x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 199 us: 1.41x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 86.2 ms: 1.39x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 35.2 ms: 1.37x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 49.8 ms: 1.24x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.47 us: 1.16x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.7 ms: 1.15x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.72 us: 1.10x faster                                                            |
| pickle               | 7.83 us                                                         | 7.98 us: 1.02x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.38 us: 1.05x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.30x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.26 ms: 1.73x faster                                                            |
| django_template | 36.0 ms                                                         | 24.1 ms: 1.49x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.5 ms: 1.35x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 35.1 ms: 1.33x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.38 sec: 12.28x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 102 us: 3.89x faster                                                             |
| pidigits                 | 502 ms                                                          | 148 ms: 3.39x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 331 ms: 2.78x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.6 ms: 2.74x faster                                                            |
| async_tree_io            | 940 ms                                                          | 386 ms: 2.44x faster                                                             |
| async_tree_none          | 394 ms                                                          | 173 ms: 2.28x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 206 ms: 2.27x faster                                                             |
| mdp                      | 1.83 sec                                                        | 820 ms: 2.23x faster                                                             |
| pylint                   | 384 ms                                                          | 199 ms: 1.93x faster                                                             |
| go                       | 146 ms                                                          | 76.4 ms: 1.91x faster                                                            |
| deepcopy                 | 310 us                                                          | 167 us: 1.85x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.38 ms: 1.82x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.22 ms: 1.82x faster                                                            |
| chaos                    | 74.4 ms                                                         | 41.1 ms: 1.81x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 54.2 ns: 1.81x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 107 us: 1.78x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 46.0 ms: 1.77x faster                                                            |
| float                    | 69.6 ms                                                         | 39.7 ms: 1.76x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 16.9 us: 1.75x faster                                                            |
| thrift                   | 902 us                                                          | 517 us: 1.74x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.10 sec: 1.74x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.26 ms: 1.73x faster                                                            |
| raytrace                 | 303 ms                                                          | 177 ms: 1.71x faster                                                             |
| pyflate                  | 422 ms                                                          | 253 ms: 1.67x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.7 us: 1.65x faster                                                            |
| json                     | 4.76 ms                                                         | 2.91 ms: 1.64x faster                                                            |
| generators               | 31.6 ms                                                         | 19.5 ms: 1.62x faster                                                            |
| richards_super           | 49.9 ms                                                         | 31.0 ms: 1.61x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.0 us: 1.60x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 472 ms: 1.58x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 873 ms: 1.57x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 57.8 ms: 1.55x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 430 ms: 1.53x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.5 ms: 1.53x faster                                                            |
| regex_compile            | 117 ms                                                          | 77.8 ms: 1.50x faster                                                            |
| fannkuch                 | 317 ms                                                          | 212 ms: 1.50x faster                                                             |
| django_template          | 36.0 ms                                                         | 24.1 ms: 1.49x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.12 ms: 1.49x faster                                                            |
| pycparser                | 1.04 sec                                                        | 701 ms: 1.49x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.55 us: 1.48x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.81 us: 1.48x faster                                                            |
| scimark_sor              | 115 ms                                                          | 78.5 ms: 1.47x faster                                                            |
| richards                 | 40.3 ms                                                         | 27.5 ms: 1.46x faster                                                            |
| scimark_fft              | 216 ms                                                          | 149 ms: 1.45x faster                                                             |
| nbody                    | 79.1 ms                                                         | 55.0 ms: 1.44x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.8 ms: 1.44x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 61.3 ms: 1.42x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 199 us: 1.41x faster                                                             |
| sympy_sum                | 122 ms                                                          | 87.4 ms: 1.40x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.32 ms: 1.40x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 86.2 ms: 1.39x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 37.7 ms: 1.38x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 35.2 ms: 1.37x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.5 ms: 1.35x faster                                                            |
| sympy_str                | 229 ms                                                          | 171 ms: 1.34x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 35.1 ms: 1.33x faster                                                            |
| sympy_expand             | 391 ms                                                          | 296 ms: 1.32x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 851 us: 1.32x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.7 ms: 1.31x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.4 ms: 1.24x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 49.8 ms: 1.24x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 32.4 ns: 1.24x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.47 us: 1.22x faster                                                            |
| telco                    | 4.83 ms                                                         | 3.98 ms: 1.21x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.03 us: 1.21x faster                                                            |
| 2to3                     | 265 ms                                                          | 222 ms: 1.20x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 67.2 ms: 1.19x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.66 sec: 1.18x faster                                                           |
| unpickle                 | 9.82 us                                                         | 8.47 us: 1.16x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.7 ms: 1.15x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.2 ms: 1.11x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 72.7 ms: 1.10x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.72 us: 1.10x faster                                                            |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.98 us: 1.02x slower                                                            |
| async_generators         | 241 ms                                                          | 246 ms: 1.02x slower                                                             |
| pickle_list              | 3.22 us                                                         | 3.38 us: 1.05x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.1 ms: 1.05x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 91.1 ms: 1.37x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.14 ms: 1.67x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.29 ms: 1.86x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.48x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1_win32-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.490x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.44x
- 95% likely to have a speedup of 1.42x
- 99% likely to have a speedup of 1.39x

# Memory
- memory change: unknown