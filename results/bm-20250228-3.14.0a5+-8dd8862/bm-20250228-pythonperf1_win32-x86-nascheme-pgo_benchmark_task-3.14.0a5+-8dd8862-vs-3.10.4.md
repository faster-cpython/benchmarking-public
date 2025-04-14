# Results vs. 3.10.4

- fork: nascheme
- ref: pgo_benchmark_task
- machine: windows-x86
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.134x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 257 ms: 1.03x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.84 sec: 1.06x faster                                                          |
| html5lib       | 52.1 ms                                                         | 48.8 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 460 ms: 2.04x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 469 ms: 1.96x faster                                                            |
| async_tree_none         | 394 ms                                                          | 220 ms: 1.79x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 262 ms: 1.78x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.89x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.52x faster                                                            |
| float          | 69.6 ms                                                         | 54.5 ms: 1.28x faster                                                           |
| nbody          | 79.1 ms                                                         | 87.3 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.43x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 115 ms: 1.14x faster                                                            |
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.90 ms: 1.24x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.73 sec: 1.10x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.9 ms: 1.07x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 182 us: 1.04x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.6 us: 1.04x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 49.3 ms: 1.02x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 287 us: 1.02x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 67.7 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 22.0 ms: 1.22x slower                                                           |
| python_startup         | 22.9 ms                                                         | 28.5 ms: 1.24x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.23x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.82 ms: 1.16x faster                                                           |
| django_template | 36.0 ms                                                         | 34.1 ms: 1.06x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 47.8 ms: 1.03x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 148 us: 2.67x faster                                                            |
| pidigits                 | 502 ms                                                          | 200 ms: 2.52x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 36.8 ms: 2.21x faster                                                           |
| async_tree_io            | 940 ms                                                          | 460 ms: 2.04x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 469 ms: 1.96x faster                                                            |
| async_tree_none          | 394 ms                                                          | 220 ms: 1.79x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 262 ms: 1.78x faster                                                            |
| pylint                   | 384 ms                                                          | 225 ms: 1.71x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.78 ms: 1.45x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 71.7 ns: 1.36x faster                                                           |
| go                       | 146 ms                                                          | 107 ms: 1.36x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 22.5 us: 1.32x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.5 us: 1.31x faster                                                           |
| deepcopy                 | 310 us                                                          | 242 us: 1.28x faster                                                            |
| float                    | 69.6 ms                                                         | 54.5 ms: 1.28x faster                                                           |
| chaos                    | 74.4 ms                                                         | 58.6 ms: 1.27x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 70.8 ms: 1.27x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 64.7 ms: 1.26x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.90 ms: 1.24x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.87 us: 1.22x faster                                                           |
| pyflate                  | 422 ms                                                          | 351 ms: 1.20x faster                                                            |
| thrift                   | 902 us                                                          | 757 us: 1.19x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.12 ms: 1.19x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.18 ms: 1.18x faster                                                           |
| generators               | 31.6 ms                                                         | 26.9 ms: 1.17x faster                                                           |
| pycparser                | 1.04 sec                                                        | 894 ms: 1.17x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.36 ms: 1.17x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.82 ms: 1.16x faster                                                           |
| scimark_sor              | 115 ms                                                          | 99.0 ms: 1.16x faster                                                           |
| raytrace                 | 303 ms                                                          | 265 ms: 1.14x faster                                                            |
| regex_dna                | 131 ms                                                          | 115 ms: 1.14x faster                                                            |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.12x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 72.3 ms: 1.11x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.9 ms: 1.11x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 53.1 ms: 1.10x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.73 sec: 1.10x faster                                                          |
| richards_super           | 49.9 ms                                                         | 45.5 ms: 1.10x faster                                                           |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 80.7 ms: 1.08x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.9 ms: 1.07x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.7 ms: 1.07x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.28 sec: 1.07x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 48.8 ms: 1.07x faster                                                           |
| json                     | 4.76 ms                                                         | 4.47 ms: 1.06x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 619 ms: 1.06x faster                                                            |
| django_template          | 36.0 ms                                                         | 34.1 ms: 1.06x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.84 sec: 1.06x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.56 us: 1.05x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 182 us: 1.04x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 16.0 ms: 1.04x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 222 ms: 1.04x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.6 us: 1.04x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 43.2 ms: 1.04x faster                                                           |
| 2to3                     | 265 ms                                                          | 257 ms: 1.03x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.14 ms: 1.03x faster                                                           |
| fannkuch                 | 317 ms                                                          | 307 ms: 1.03x faster                                                            |
| sympy_str                | 229 ms                                                          | 222 ms: 1.03x faster                                                            |
| richards                 | 40.3 ms                                                         | 39.1 ms: 1.03x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.79 sec: 1.02x faster                                                          |
| sympy_expand             | 391 ms                                                          | 384 ms: 1.02x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 81.5 ms: 1.02x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 49.3 ms: 1.02x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 287 us: 1.02x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 47.8 ms: 1.03x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                           |
| scimark_fft              | 216 ms                                                          | 236 ms: 1.09x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 67.7 ms: 1.10x slower                                                           |
| nbody                    | 79.1 ms                                                         | 87.3 ms: 1.10x slower                                                           |
| coverage                 | 46.6 ms                                                         | 51.6 ms: 1.11x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.37 us: 1.18x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.67 us: 1.19x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.35 ms: 1.20x slower                                                           |
| async_generators         | 241 ms                                                          | 290 ms: 1.20x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 22.0 ms: 1.22x slower                                                           |
| python_startup           | 22.9 ms                                                         | 28.5 ms: 1.24x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.15 ms: 1.27x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 91.6 ms: 1.38x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.04 ms: 1.49x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-pythonperf1_win32-x86-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.134x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown