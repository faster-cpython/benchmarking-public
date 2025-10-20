# Results vs. 3.10.4

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.515x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.42x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 217 ms: 1.22x faster                                                              |
| docutils       | 1.95 sec                                                        | 1.60 sec: 1.22x faster                                                            |
| html5lib       | 52.1 ms                                                         | 37.2 ms: 1.40x faster                                                             |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 327 ms: 2.82x faster                                                              |
| async_tree_io           | 940 ms                                                          | 387 ms: 2.43x faster                                                              |
| async_tree_memoization  | 467 ms                                                          | 198 ms: 2.36x faster                                                              |
| async_tree_none         | 394 ms                                                          | 170 ms: 2.32x faster                                                              |
| Geometric mean          | (ref)                                                           | 2.47x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.44x faster                                                              |
| float          | 69.6 ms                                                         | 41.0 ms: 1.70x faster                                                             |
| nbody          | 79.1 ms                                                         | 54.2 ms: 1.46x faster                                                             |
| Geometric mean | (ref)                                                           | 2.04x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 76.8 ms: 1.52x faster                                                             |
| regex_dna      | 131 ms                                                          | 117 ms: 1.12x faster                                                              |
| regex_v8       | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.36 ms: 1.83x faster                                                             |
| unpickle_pure_python | 189 us                                                          | 106 us: 1.79x faster                                                              |
| tomli_loads          | 1.91 sec                                                        | 1.09 sec: 1.75x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.0 us: 1.59x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 196 us: 1.43x faster                                                              |
| xml_etree_process    | 48.1 ms                                                         | 35.3 ms: 1.37x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 88.0 ms: 1.36x faster                                                             |
| xml_etree_generate   | 61.6 ms                                                         | 49.5 ms: 1.25x faster                                                             |
| unpickle             | 9.82 us                                                         | 8.62 us: 1.14x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.1 ms: 1.12x faster                                                             |
| unpickle_list        | 2.98 us                                                         | 2.78 us: 1.08x faster                                                             |
| pickle               | 7.83 us                                                         | 7.40 us: 1.06x faster                                                             |
| pickle_list          | 3.22 us                                                         | 3.18 us: 1.01x faster                                                             |
| pickle_dict          | 18.2 us                                                         | 18.6 us: 1.02x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.31x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.8 ms: 1.04x slower                                                             |
| python_startup         | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.28 ms: 1.72x faster                                                             |
| django_template | 36.0 ms                                                         | 23.7 ms: 1.52x faster                                                             |
| genshi_text     | 21.0 ms                                                         | 15.5 ms: 1.35x faster                                                             |
| genshi_xml      | 46.6 ms                                                         | 35.0 ms: 1.33x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.34 sec: 12.67x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 101 us: 3.92x faster                                                              |
| pidigits                 | 502 ms                                                          | 146 ms: 3.44x faster                                                              |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 327 ms: 2.82x faster                                                              |
| pathlib                  | 81.2 ms                                                         | 29.1 ms: 2.79x faster                                                             |
| async_tree_io            | 940 ms                                                          | 387 ms: 2.43x faster                                                              |
| async_tree_memoization   | 467 ms                                                          | 198 ms: 2.36x faster                                                              |
| mdp                      | 1.83 sec                                                        | 785 ms: 2.33x faster                                                              |
| async_tree_none          | 394 ms                                                          | 170 ms: 2.32x faster                                                              |
| pylint                   | 384 ms                                                          | 193 ms: 1.99x faster                                                              |
| go                       | 146 ms                                                          | 75.8 ms: 1.92x faster                                                             |
| deepcopy                 | 310 us                                                          | 166 us: 1.87x faster                                                              |
| json_dumps               | 9.82 ms                                                         | 5.36 ms: 1.83x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.22 ms: 1.82x faster                                                             |
| chaos                    | 74.4 ms                                                         | 40.9 ms: 1.82x faster                                                             |
| thrift                   | 902 us                                                          | 498 us: 1.81x faster                                                              |
| crypto_pyaes             | 81.3 ms                                                         | 44.9 ms: 1.81x faster                                                             |
| unpickle_pure_python     | 189 us                                                          | 106 us: 1.79x faster                                                              |
| logging_silent           | 97.9 ns                                                         | 55.2 ns: 1.77x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.09 sec: 1.75x faster                                                            |
| raytrace                 | 303 ms                                                          | 174 ms: 1.74x faster                                                              |
| deepcopy_memo            | 29.6 us                                                         | 17.1 us: 1.73x faster                                                             |
| mako                     | 9.10 ms                                                         | 5.28 ms: 1.72x faster                                                             |
| pyflate                  | 422 ms                                                          | 247 ms: 1.71x faster                                                              |
| float                    | 69.6 ms                                                         | 41.0 ms: 1.70x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.5 us: 1.68x faster                                                             |
| json                     | 4.76 ms                                                         | 2.83 ms: 1.68x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 450 ms: 1.65x faster                                                              |
| generators               | 31.6 ms                                                         | 19.1 ms: 1.65x faster                                                             |
| richards_super           | 49.9 ms                                                         | 30.6 ms: 1.63x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 856 ms: 1.60x faster                                                              |
| json_loads               | 22.4 us                                                         | 14.0 us: 1.59x faster                                                             |
| scimark_fft              | 216 ms                                                          | 136 ms: 1.59x faster                                                              |
| pprint_safe_repr         | 658 ms                                                          | 423 ms: 1.56x faster                                                              |
| pycparser                | 1.04 sec                                                        | 680 ms: 1.53x faster                                                              |
| fannkuch                 | 317 ms                                                          | 208 ms: 1.52x faster                                                              |
| hexiom                   | 6.13 ms                                                         | 4.03 ms: 1.52x faster                                                             |
| regex_compile            | 117 ms                                                          | 76.8 ms: 1.52x faster                                                             |
| django_template          | 36.0 ms                                                         | 23.7 ms: 1.52x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.9 ms: 1.52x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 38.7 ms: 1.51x faster                                                             |
| richards                 | 40.3 ms                                                         | 26.7 ms: 1.51x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 59.7 ms: 1.50x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.55 us: 1.48x faster                                                             |
| scimark_sor              | 115 ms                                                          | 77.8 ms: 1.48x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 59.0 ms: 1.48x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.83 us: 1.47x faster                                                             |
| nbody                    | 79.1 ms                                                         | 54.2 ms: 1.46x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.22 ms: 1.46x faster                                                             |
| sympy_sum                | 122 ms                                                          | 84.7 ms: 1.45x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 196 us: 1.43x faster                                                              |
| html5lib                 | 52.1 ms                                                         | 37.2 ms: 1.40x faster                                                             |
| sympy_str                | 229 ms                                                          | 166 ms: 1.38x faster                                                              |
| xml_etree_process        | 48.1 ms                                                         | 35.3 ms: 1.37x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 88.0 ms: 1.36x faster                                                             |
| sympy_expand             | 391 ms                                                          | 288 ms: 1.36x faster                                                              |
| genshi_text              | 21.0 ms                                                         | 15.5 ms: 1.35x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 831 us: 1.35x faster                                                              |
| sympy_integrate          | 16.6 ms                                                         | 12.5 ms: 1.33x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 35.0 ms: 1.33x faster                                                             |
| coroutines               | 17.9 ms                                                         | 14.3 ms: 1.26x faster                                                             |
| telco                    | 4.83 ms                                                         | 3.86 ms: 1.25x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 64.3 ms: 1.25x faster                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 49.5 ms: 1.25x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.44 us: 1.23x faster                                                             |
| 2to3                     | 265 ms                                                          | 217 ms: 1.22x faster                                                              |
| docutils                 | 1.95 sec                                                        | 1.60 sec: 1.22x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.00 us: 1.21x faster                                                             |
| unpack_sequence          | 40.0 ns                                                         | 33.2 ns: 1.21x faster                                                             |
| unpickle                 | 9.82 us                                                         | 8.62 us: 1.14x faster                                                             |
| meteor_contest           | 80.0 ms                                                         | 70.6 ms: 1.13x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.1 ms: 1.12x faster                                                             |
| regex_dna                | 131 ms                                                          | 117 ms: 1.12x faster                                                              |
| regex_v8                 | 15.8 ms                                                         | 14.5 ms: 1.09x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.78 us: 1.08x faster                                                             |
| pickle                   | 7.83 us                                                         | 7.40 us: 1.06x faster                                                             |
| pickle_list              | 3.22 us                                                         | 3.18 us: 1.01x faster                                                             |
| async_generators         | 241 ms                                                          | 239 ms: 1.01x faster                                                              |
| pickle_dict              | 18.2 us                                                         | 18.6 us: 1.02x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 18.8 ms: 1.04x slower                                                             |
| coverage                 | 46.6 ms                                                         | 50.3 ms: 1.08x slower                                                             |
| python_startup           | 22.9 ms                                                         | 25.2 ms: 1.10x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 89.0 ms: 1.34x slower                                                             |
| gc_traversal             | 1.28 ms                                                         | 2.08 ms: 1.62x slower                                                             |
| create_gc_cycles         | 694 us                                                          | 1.26 ms: 1.82x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.50x faster                                                                      |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.515x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.47x
- 95% likely to have a speedup of 1.46x
- 99% likely to have a speedup of 1.42x

# Memory
- memory change: unknown