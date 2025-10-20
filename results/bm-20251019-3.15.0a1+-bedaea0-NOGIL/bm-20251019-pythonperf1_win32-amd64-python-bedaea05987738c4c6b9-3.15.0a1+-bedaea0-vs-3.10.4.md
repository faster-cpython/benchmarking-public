# Results vs. 3.10.4

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.340x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 217 ms: 1.23x faster                                                              |
| docutils       | 1.95 sec                                                        | 2.80 sec: 1.44x slower                                                            |
| html5lib       | 52.1 ms                                                         | 40.5 ms: 1.29x faster                                                             |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 339 ms: 2.77x faster                                                              |
| async_tree_cpu_io_mixed | 922 ms                                                          | 335 ms: 2.76x faster                                                              |
| async_tree_none         | 394 ms                                                          | 168 ms: 2.34x faster                                                              |
| async_tree_memoization  | 467 ms                                                          | 206 ms: 2.27x faster                                                              |
| Geometric mean          | (ref)                                                           | 2.52x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 136 ms: 3.69x faster                                                              |
| float          | 69.6 ms                                                         | 45.1 ms: 1.54x faster                                                             |
| nbody          | 79.1 ms                                                         | 76.8 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                           | 1.80x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 90.1 ms: 1.29x faster                                                             |
| regex_v8       | 15.8 ms                                                         | 12.8 ms: 1.23x faster                                                             |
| regex_dna      | 131 ms                                                          | 112 ms: 1.16x faster                                                              |
| regex_effbot   | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                             |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.16 ms: 1.59x faster                                                             |
| json_loads           | 22.4 us                                                         | 16.1 us: 1.39x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 92.7 ms: 1.29x faster                                                             |
| unpickle_pure_python | 189 us                                                          | 150 us: 1.26x faster                                                              |
| pickle_pure_python   | 280 us                                                          | 222 us: 1.26x faster                                                              |
| xml_etree_iterparse  | 70.8 ms                                                         | 58.7 ms: 1.21x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 43.3 ms: 1.11x faster                                                             |
| pickle_list          | 3.22 us                                                         | 3.11 us: 1.03x faster                                                             |
| unpickle             | 9.82 us                                                         | 9.98 us: 1.02x slower                                                             |
| unpickle_list        | 2.98 us                                                         | 3.09 us: 1.04x slower                                                             |
| pickle               | 7.83 us                                                         | 8.15 us: 1.04x slower                                                             |
| pickle_dict          | 18.2 us                                                         | 20.3 us: 1.11x slower                                                             |
| tomli_loads          | 1.91 sec                                                        | 2.24 sec: 1.17x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                      |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                             |
| python_startup         | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 25.8 ms: 1.39x faster                                                             |
| genshi_xml      | 46.6 ms                                                         | 37.7 ms: 1.24x faster                                                             |
| genshi_text     | 21.0 ms                                                         | 18.3 ms: 1.15x faster                                                             |
| mako            | 9.10 ms                                                         | 9.74 ms: 1.07x slower                                                             |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.19 sec: 7.76x faster                                                            |
| pidigits                 | 502 ms                                                          | 136 ms: 3.69x faster                                                              |
| typing_runtime_protocols | 396 us                                                          | 126 us: 3.15x faster                                                              |
| pathlib                  | 81.2 ms                                                         | 28.7 ms: 2.83x faster                                                             |
| async_tree_io            | 940 ms                                                          | 339 ms: 2.77x faster                                                              |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 335 ms: 2.76x faster                                                              |
| async_tree_none          | 394 ms                                                          | 168 ms: 2.34x faster                                                              |
| async_tree_memoization   | 467 ms                                                          | 206 ms: 2.27x faster                                                              |
| pylint                   | 384 ms                                                          | 199 ms: 1.93x faster                                                              |
| mdp                      | 1.83 sec                                                        | 1.02 sec: 1.79x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.32 ms: 1.74x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 432 ms: 1.72x faster                                                              |
| sqlite_synth             | 2.29 us                                                         | 1.34 us: 1.71x faster                                                             |
| deepcopy                 | 310 us                                                          | 185 us: 1.68x faster                                                              |
| chaos                    | 74.4 ms                                                         | 44.4 ms: 1.68x faster                                                             |
| go                       | 146 ms                                                          | 87.9 ms: 1.66x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 60.3 ns: 1.62x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 6.16 ms: 1.59x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 18.7 us: 1.58x faster                                                             |
| thrift                   | 902 us                                                          | 575 us: 1.57x faster                                                              |
| comprehensions           | 17.7 us                                                         | 11.4 us: 1.56x faster                                                             |
| generators               | 31.6 ms                                                         | 20.3 ms: 1.55x faster                                                             |
| float                    | 69.6 ms                                                         | 45.1 ms: 1.54x faster                                                             |
| json                     | 4.76 ms                                                         | 3.14 ms: 1.52x faster                                                             |
| pycparser                | 1.04 sec                                                        | 691 ms: 1.51x faster                                                              |
| raytrace                 | 303 ms                                                          | 204 ms: 1.48x faster                                                              |
| crypto_pyaes             | 81.3 ms                                                         | 55.1 ms: 1.48x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 63.2 ms: 1.42x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 41.3 ms: 1.42x faster                                                             |
| scimark_sor              | 115 ms                                                          | 82.0 ms: 1.40x faster                                                             |
| django_template          | 36.0 ms                                                         | 25.8 ms: 1.39x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.42 ms: 1.39x faster                                                             |
| json_loads               | 22.4 us                                                         | 16.1 us: 1.39x faster                                                             |
| pyflate                  | 422 ms                                                          | 304 ms: 1.39x faster                                                              |
| richards_super           | 49.9 ms                                                         | 36.6 ms: 1.36x faster                                                             |
| deepcopy_reduce          | 2.68 us                                                         | 1.97 us: 1.36x faster                                                             |
| coroutines               | 17.9 ms                                                         | 13.6 ms: 1.32x faster                                                             |
| sympy_sum                | 122 ms                                                          | 93.4 ms: 1.31x faster                                                             |
| regex_compile            | 117 ms                                                          | 90.1 ms: 1.29x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 92.7 ms: 1.29x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 48.0 ms: 1.29x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 40.5 ms: 1.29x faster                                                             |
| richards                 | 40.3 ms                                                         | 31.4 ms: 1.28x faster                                                             |
| sympy_expand             | 391 ms                                                          | 307 ms: 1.27x faster                                                              |
| unpickle_pure_python     | 189 us                                                          | 150 us: 1.26x faster                                                              |
| pickle_pure_python       | 280 us                                                          | 222 us: 1.26x faster                                                              |
| sympy_str                | 229 ms                                                          | 183 ms: 1.25x faster                                                              |
| genshi_xml               | 46.6 ms                                                         | 37.7 ms: 1.24x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 70.9 ms: 1.23x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 12.8 ms: 1.23x faster                                                             |
| 2to3                     | 265 ms                                                          | 217 ms: 1.23x faster                                                              |
| sympy_integrate          | 16.6 ms                                                         | 13.6 ms: 1.22x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 543 ms: 1.21x faster                                                              |
| xml_etree_iterparse      | 70.8 ms                                                         | 58.7 ms: 1.21x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 68.8 ms: 1.17x faster                                                             |
| regex_dna                | 131 ms                                                          | 112 ms: 1.16x faster                                                              |
| genshi_text              | 21.0 ms                                                         | 18.3 ms: 1.15x faster                                                             |
| scimark_fft              | 216 ms                                                          | 188 ms: 1.15x faster                                                              |
| logging_simple           | 7.29 us                                                         | 6.44 us: 1.13x faster                                                             |
| unpack_sequence          | 40.0 ns                                                         | 35.5 ns: 1.13x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.90 ms: 1.12x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 43.3 ms: 1.11x faster                                                             |
| logging_format           | 7.91 us                                                         | 7.21 us: 1.10x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 1.04 ms: 1.07x faster                                                             |
| fannkuch                 | 317 ms                                                          | 299 ms: 1.06x faster                                                              |
| pickle_list              | 3.22 us                                                         | 3.11 us: 1.03x faster                                                             |
| nbody                    | 79.1 ms                                                         | 76.8 ms: 1.03x faster                                                             |
| gc_traversal             | 1.28 ms                                                         | 1.25 ms: 1.03x faster                                                             |
| unpickle                 | 9.82 us                                                         | 9.98 us: 1.02x slower                                                             |
| unpickle_list            | 2.98 us                                                         | 3.09 us: 1.04x slower                                                             |
| pickle                   | 7.83 us                                                         | 8.15 us: 1.04x slower                                                             |
| telco                    | 4.83 ms                                                         | 5.07 ms: 1.05x slower                                                             |
| async_generators         | 241 ms                                                          | 256 ms: 1.06x slower                                                              |
| meteor_contest           | 80.0 ms                                                         | 85.2 ms: 1.06x slower                                                             |
| python_startup_no_site   | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                             |
| mako                     | 9.10 ms                                                         | 9.74 ms: 1.07x slower                                                             |
| pickle_dict              | 18.2 us                                                         | 20.3 us: 1.11x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 73.9 ms: 1.11x slower                                                             |
| python_startup           | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                             |
| tomli_loads              | 1.91 sec                                                        | 2.24 sec: 1.17x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.63 sec: 1.19x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.80 sec: 1.44x slower                                                            |
| coverage                 | 46.6 ms                                                         | 67.2 ms: 1.44x slower                                                             |
| create_gc_cycles         | 694 us                                                          | 1.01 ms: 1.46x slower                                                             |
| Geometric mean           | (ref)                                                           | 1.34x faster                                                                      |

Benchmark hidden because not significant (1): xml_etree_generate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251019-3.15.0a1+-bedaea0-NOGIL/bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.340x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: unknown