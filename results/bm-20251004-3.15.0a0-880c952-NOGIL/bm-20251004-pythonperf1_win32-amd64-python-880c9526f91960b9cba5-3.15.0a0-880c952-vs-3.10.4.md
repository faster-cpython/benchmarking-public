# Results vs. 3.10.4

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.331x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 222 ms: 1.20x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.79 sec: 1.43x slower                                                           |
| html5lib       | 52.1 ms                                                         | 40.7 ms: 1.28x faster                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 327 ms: 2.82x faster                                                             |
| async_tree_io           | 940 ms                                                          | 347 ms: 2.71x faster                                                             |
| async_tree_none         | 394 ms                                                          | 168 ms: 2.34x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 209 ms: 2.23x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.51x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 137 ms: 3.67x faster                                                             |
| float          | 69.6 ms                                                         | 46.2 ms: 1.51x faster                                                            |
| Geometric mean | (ref)                                                           | 1.77x faster                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 91.3 ms: 1.28x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 12.7 ms: 1.24x faster                                                            |
| regex_dna      | 131 ms                                                          | 111 ms: 1.17x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.11 ms: 1.61x faster                                                            |
| json_loads           | 22.4 us                                                         | 15.9 us: 1.41x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 90.6 ms: 1.32x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 149 us: 1.27x faster                                                             |
| pickle_pure_python   | 280 us                                                          | 224 us: 1.25x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 58.6 ms: 1.21x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 44.6 ms: 1.08x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.06 us: 1.05x faster                                                            |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.03x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.17 us: 1.06x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.08x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.29 sec: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                                     |

Benchmark hidden because not significant (2): pickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 26.2 ms: 1.38x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 38.3 ms: 1.22x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 18.6 ms: 1.13x faster                                                            |
| mako            | 9.10 ms                                                         | 9.70 ms: 1.07x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.36 sec: 7.21x faster                                                           |
| pidigits                 | 502 ms                                                          | 137 ms: 3.67x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 128 us: 3.09x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 327 ms: 2.82x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 28.9 ms: 2.81x faster                                                            |
| async_tree_io            | 940 ms                                                          | 347 ms: 2.71x faster                                                             |
| async_tree_none          | 394 ms                                                          | 168 ms: 2.34x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 209 ms: 2.23x faster                                                             |
| pylint                   | 384 ms                                                          | 205 ms: 1.87x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.05 sec: 1.74x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.34 ms: 1.72x faster                                                            |
| deepcopy                 | 310 us                                                          | 184 us: 1.68x faster                                                             |
| logging_silent           | 97.9 ns                                                         | 58.9 ns: 1.66x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.38 us: 1.66x faster                                                            |
| go                       | 146 ms                                                          | 89.4 ms: 1.63x faster                                                            |
| chaos                    | 74.4 ms                                                         | 46.0 ms: 1.62x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.11 ms: 1.61x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 18.5 us: 1.60x faster                                                            |
| thrift                   | 902 us                                                          | 572 us: 1.58x faster                                                             |
| json                     | 4.76 ms                                                         | 3.04 ms: 1.57x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.5 us: 1.54x faster                                                            |
| generators               | 31.6 ms                                                         | 20.9 ms: 1.51x faster                                                            |
| float                    | 69.6 ms                                                         | 46.2 ms: 1.51x faster                                                            |
| pycparser                | 1.04 sec                                                        | 694 ms: 1.50x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 55.7 ms: 1.46x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 61.5 ms: 1.46x faster                                                            |
| raytrace                 | 303 ms                                                          | 207 ms: 1.46x faster                                                             |
| json_loads               | 22.4 us                                                         | 15.9 us: 1.41x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 41.8 ms: 1.40x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 536 ms: 1.39x faster                                                             |
| pyflate                  | 422 ms                                                          | 304 ms: 1.39x faster                                                             |
| django_template          | 36.0 ms                                                         | 26.2 ms: 1.38x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.46 ms: 1.38x faster                                                            |
| scimark_sor              | 115 ms                                                          | 84.8 ms: 1.36x faster                                                            |
| richards_super           | 49.9 ms                                                         | 37.6 ms: 1.33x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 90.6 ms: 1.32x faster                                                            |
| sympy_sum                | 122 ms                                                          | 93.7 ms: 1.31x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.06 us: 1.31x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 40.7 ms: 1.28x faster                                                            |
| regex_compile            | 117 ms                                                          | 91.3 ms: 1.28x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 149 us: 1.27x faster                                                             |
| sympy_str                | 229 ms                                                          | 182 ms: 1.26x faster                                                             |
| richards                 | 40.3 ms                                                         | 32.1 ms: 1.26x faster                                                            |
| sympy_expand             | 391 ms                                                          | 312 ms: 1.25x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 224 us: 1.25x faster                                                             |
| regex_v8                 | 15.8 ms                                                         | 12.7 ms: 1.24x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.0 ms: 1.24x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 542 ms: 1.22x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 38.3 ms: 1.22x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 13.7 ms: 1.22x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.8 ms: 1.21x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 72.0 ms: 1.21x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 58.6 ms: 1.21x faster                                                            |
| 2to3                     | 265 ms                                                          | 222 ms: 1.20x faster                                                             |
| regex_dna                | 131 ms                                                          | 111 ms: 1.17x faster                                                             |
| scimark_fft              | 216 ms                                                          | 188 ms: 1.15x faster                                                             |
| logging_simple           | 7.29 us                                                         | 6.43 us: 1.13x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 18.6 ms: 1.13x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.05 us: 1.12x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 36.1 ns: 1.11x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.96 ms: 1.09x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 73.6 ms: 1.09x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 44.6 ms: 1.08x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.20 ms: 1.07x faster                                                            |
| fannkuch                 | 317 ms                                                          | 301 ms: 1.05x faster                                                             |
| pickle_list              | 3.22 us                                                         | 3.06 us: 1.05x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.91 ms: 1.02x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.03x slower                                                            |
| async_generators         | 241 ms                                                          | 251 ms: 1.04x slower                                                             |
| unpickle_list            | 2.98 us                                                         | 3.17 us: 1.06x slower                                                            |
| mako                     | 9.10 ms                                                         | 9.70 ms: 1.07x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.3 ms: 1.07x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.08x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 87.7 ms: 1.10x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 74.3 ms: 1.12x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.12x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.60 sec: 1.17x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.29 sec: 1.20x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.79 sec: 1.43x slower                                                           |
| coverage                 | 46.6 ms                                                         | 67.7 ms: 1.45x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.02 ms: 1.47x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.32x faster                                                                     |

Benchmark hidden because not significant (3): nbody, pickle, xml_etree_generate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251004-3.15.0a0-880c952-NOGIL/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.331x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown