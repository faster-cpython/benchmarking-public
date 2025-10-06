# Results vs. 3.10.4

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.457x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 217 ms: 1.22x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.60 sec: 1.22x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.6 ms: 1.38x faster                                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 327 ms: 2.82x faster                                                             |
| async_tree_io           | 940 ms                                                          | 386 ms: 2.43x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| async_tree_none         | 394 ms                                                          | 175 ms: 2.25x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.44x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.45x faster                                                             |
| float          | 69.6 ms                                                         | 43.4 ms: 1.60x faster                                                            |
| nbody          | 79.1 ms                                                         | 63.5 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                           | 1.90x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 80.1 ms: 1.46x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.0 ms: 1.13x faster                                                            |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.50 ms: 1.79x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.0 us: 1.60x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 135 us: 1.40x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.37 sec: 1.39x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 86.5 ms: 1.39x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 210 us: 1.33x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 38.6 ms: 1.25x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.68 us: 1.13x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.7 ms: 1.13x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 55.2 ms: 1.12x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.84 us: 1.05x faster                                                            |
| pickle               | 7.83 us                                                         | 7.71 us: 1.02x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.24 us: 1.01x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.3 us: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.3 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 24.4 ms: 1.48x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.4 ms: 1.36x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.5 ms: 1.35x faster                                                            |
| mako            | 9.10 ms                                                         | 6.80 ms: 1.34x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.38x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.24 sec: 13.71x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 105 us: 3.78x faster                                                             |
| pidigits                 | 502 ms                                                          | 146 ms: 3.45x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 327 ms: 2.82x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.1 ms: 2.80x faster                                                            |
| async_tree_io            | 940 ms                                                          | 386 ms: 2.43x faster                                                             |
| mdp                      | 1.83 sec                                                        | 798 ms: 2.29x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 204 ms: 2.29x faster                                                             |
| async_tree_none          | 394 ms                                                          | 175 ms: 2.25x faster                                                             |
| pylint                   | 384 ms                                                          | 192 ms: 2.00x faster                                                             |
| go                       | 146 ms                                                          | 77.6 ms: 1.88x faster                                                            |
| deepcopy                 | 310 us                                                          | 167 us: 1.86x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.19 ms: 1.84x faster                                                            |
| chaos                    | 74.4 ms                                                         | 40.5 ms: 1.84x faster                                                            |
| thrift                   | 902 us                                                          | 501 us: 1.80x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 416 ms: 1.79x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 5.50 ms: 1.79x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 16.7 us: 1.77x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 55.8 ns: 1.75x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 47.7 ms: 1.70x faster                                                            |
| raytrace                 | 303 ms                                                          | 179 ms: 1.69x faster                                                             |
| json                     | 4.76 ms                                                         | 2.88 ms: 1.65x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.6 ms: 1.63x faster                                                            |
| generators               | 31.6 ms                                                         | 19.5 ms: 1.62x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.0 us: 1.61x faster                                                            |
| float                    | 69.6 ms                                                         | 43.4 ms: 1.60x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.0 us: 1.60x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.6 ms: 1.52x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 58.9 ms: 1.52x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 39.1 ms: 1.50x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.10 ms: 1.50x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.81 us: 1.48x faster                                                            |
| richards                 | 40.3 ms                                                         | 27.2 ms: 1.48x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.4 ms: 1.48x faster                                                            |
| pyflate                  | 422 ms                                                          | 287 ms: 1.47x faster                                                             |
| scimark_sor              | 115 ms                                                          | 78.3 ms: 1.47x faster                                                            |
| pycparser                | 1.04 sec                                                        | 712 ms: 1.46x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.57 us: 1.46x faster                                                            |
| regex_compile            | 117 ms                                                          | 80.1 ms: 1.46x faster                                                            |
| sympy_sum                | 122 ms                                                          | 84.9 ms: 1.44x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 135 us: 1.40x faster                                                             |
| nqueens                  | 87.1 ms                                                         | 62.3 ms: 1.40x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.37 sec: 1.39x faster                                                           |
| sympy_str                | 229 ms                                                          | 165 ms: 1.39x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 986 ms: 1.39x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 86.5 ms: 1.39x faster                                                            |
| sympy_expand             | 391 ms                                                          | 282 ms: 1.39x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 37.6 ms: 1.38x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 12.2 ms: 1.36x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.4 ms: 1.36x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.5 ms: 1.35x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 488 ms: 1.35x faster                                                             |
| mako                     | 9.10 ms                                                         | 6.80 ms: 1.34x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.43 ms: 1.33x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 210 us: 1.33x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 846 us: 1.32x faster                                                             |
| scimark_fft              | 216 ms                                                          | 168 ms: 1.29x faster                                                             |
| unpack_sequence          | 40.0 ns                                                         | 32.0 ns: 1.25x faster                                                            |
| nbody                    | 79.1 ms                                                         | 63.5 ms: 1.25x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 38.6 ms: 1.25x faster                                                            |
| logging_simple           | 7.29 us                                                         | 5.92 us: 1.23x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.43 us: 1.23x faster                                                            |
| 2to3                     | 265 ms                                                          | 217 ms: 1.22x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.60 sec: 1.22x faster                                                           |
| coroutines               | 17.9 ms                                                         | 14.8 ms: 1.21x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 66.9 ms: 1.20x faster                                                            |
| fannkuch                 | 317 ms                                                          | 267 ms: 1.19x faster                                                             |
| telco                    | 4.83 ms                                                         | 4.18 ms: 1.15x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.68 us: 1.13x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.7 ms: 1.13x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.0 ms: 1.13x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 55.2 ms: 1.12x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 72.1 ms: 1.11x faster                                                            |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.56 ms: 1.07x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.84 us: 1.05x faster                                                            |
| async_generators         | 241 ms                                                          | 230 ms: 1.05x faster                                                             |
| pickle                   | 7.83 us                                                         | 7.71 us: 1.02x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.24 us: 1.01x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.0 ms: 1.05x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.3 us: 1.06x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.3 ms: 1.10x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 89.5 ms: 1.35x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.08 ms: 1.62x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.26 ms: 1.82x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.46x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.457x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown