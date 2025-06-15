# Results vs. 3.10.4

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.057x slower
- HPT reliability: 62.39%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 286 ms: 1.08x slower                                                             |
| docutils       | 1.95 sec                                                        | 2.11 sec: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 432 ms: 2.13x faster                                                             |
| async_tree_io           | 940 ms                                                          | 532 ms: 1.77x faster                                                             |
| async_tree_none         | 394 ms                                                          | 232 ms: 1.70x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 285 ms: 1.64x faster                                                             |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 146 ms: 3.44x faster                                                             |
| nbody          | 79.1 ms                                                         | 56.2 ms: 1.41x faster                                                            |
| float          | 69.6 ms                                                         | 78.1 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                           | 1.63x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                             |
| regex_compile  | 117 ms                                                          | 120 ms: 1.03x slower                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.74 ms: 1.05x slower                                                            |
| regex_v8       | 15.8 ms                                                         | 16.5 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.57 sec: 1.22x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 158 us: 1.20x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.14x faster                                                             |
| json_dumps           | 9.82 ms                                                         | 8.67 ms: 1.13x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 3.10 us: 1.04x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 52.2 ms: 1.08x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 71.8 ms: 1.17x slower                                                            |
| pickle_pure_python   | 280 us                                                          | 330 us: 1.18x slower                                                             |
| unpickle             | 9.82 us                                                         | 11.6 us: 1.18x slower                                                            |
| pickle_list          | 3.22 us                                                         | 3.93 us: 1.22x slower                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 86.8 ms: 1.23x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 22.6 us: 1.24x slower                                                            |
| pickle               | 7.83 us                                                         | 9.84 us: 1.26x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                            |
| python_startup         | 22.9 ms                                                         | 27.3 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.24 ms: 1.26x faster                                                            |
| django_template | 36.0 ms                                                         | 37.8 ms: 1.05x slower                                                            |
| genshi_xml      | 46.6 ms                                                         | 50.3 ms: 1.08x slower                                                            |
| genshi_text     | 21.0 ms                                                         | 24.7 ms: 1.18x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.51 sec: 11.24x faster                                                          |
| pidigits                 | 502 ms                                                          | 146 ms: 3.44x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 145 us: 2.73x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 34.7 ms: 2.34x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 432 ms: 2.13x faster                                                             |
| async_tree_io            | 940 ms                                                          | 532 ms: 1.77x faster                                                             |
| async_tree_none          | 394 ms                                                          | 232 ms: 1.70x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 285 ms: 1.64x faster                                                             |
| pylint                   | 384 ms                                                          | 250 ms: 1.54x faster                                                             |
| mdp                      | 1.83 sec                                                        | 1.20 sec: 1.53x faster                                                           |
| nbody                    | 79.1 ms                                                         | 56.2 ms: 1.41x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.74 us: 1.31x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 62.2 ms: 1.31x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 571 ms: 1.30x faster                                                             |
| mako                     | 9.10 ms                                                         | 7.24 ms: 1.26x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.57 sec: 1.22x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 158 us: 1.20x faster                                                             |
| json                     | 4.76 ms                                                         | 3.99 ms: 1.19x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.80 ms: 1.16x faster                                                            |
| scimark_fft              | 216 ms                                                          | 188 ms: 1.15x faster                                                             |
| deepcopy                 | 310 us                                                          | 270 us: 1.15x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 978 us: 1.15x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.14x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 8.67 ms: 1.13x faster                                                            |
| chaos                    | 74.4 ms                                                         | 65.9 ms: 1.13x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 51.8 ms: 1.13x faster                                                            |
| comprehensions           | 17.7 us                                                         | 15.8 us: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                             |
| fannkuch                 | 317 ms                                                          | 285 ms: 1.11x faster                                                             |
| pycparser                | 1.04 sec                                                        | 940 ms: 1.11x faster                                                             |
| pyflate                  | 422 ms                                                          | 387 ms: 1.09x faster                                                             |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                            |
| go                       | 146 ms                                                          | 137 ms: 1.06x faster                                                             |
| sympy_sum                | 122 ms                                                          | 120 ms: 1.02x faster                                                             |
| pprint_pformat           | 1.37 sec                                                        | 1.38 sec: 1.01x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 666 ms: 1.01x slower                                                             |
| raytrace                 | 303 ms                                                          | 307 ms: 1.02x slower                                                             |
| sympy_str                | 229 ms                                                          | 233 ms: 1.02x slower                                                             |
| meteor_contest           | 80.0 ms                                                         | 81.7 ms: 1.02x slower                                                            |
| regex_compile            | 117 ms                                                          | 120 ms: 1.03x slower                                                             |
| sympy_expand             | 391 ms                                                          | 404 ms: 1.03x slower                                                             |
| nqueens                  | 87.1 ms                                                         | 90.4 ms: 1.04x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.10 us: 1.04x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.79 us: 1.04x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 17.3 ms: 1.04x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.74 ms: 1.05x slower                                                            |
| regex_v8                 | 15.8 ms                                                         | 16.5 ms: 1.05x slower                                                            |
| django_template          | 36.0 ms                                                         | 37.8 ms: 1.05x slower                                                            |
| 2to3                     | 265 ms                                                          | 286 ms: 1.08x slower                                                             |
| genshi_xml               | 46.6 ms                                                         | 50.3 ms: 1.08x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.11 sec: 1.08x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 52.2 ms: 1.08x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.26 ms: 1.09x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                            |
| float                    | 69.6 ms                                                         | 78.1 ms: 1.12x slower                                                            |
| deltablue                | 4.04 ms                                                         | 4.55 ms: 1.13x slower                                                            |
| scimark_sor              | 115 ms                                                          | 134 ms: 1.16x slower                                                             |
| xml_etree_generate       | 61.6 ms                                                         | 71.8 ms: 1.17x slower                                                            |
| richards_super           | 49.9 ms                                                         | 58.6 ms: 1.17x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 330 us: 1.18x slower                                                             |
| genshi_text              | 21.0 ms                                                         | 24.7 ms: 1.18x slower                                                            |
| unpickle                 | 9.82 us                                                         | 11.6 us: 1.18x slower                                                            |
| generators               | 31.6 ms                                                         | 37.3 ms: 1.18x slower                                                            |
| deepcopy_memo            | 29.6 us                                                         | 35.0 us: 1.18x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.3 ms: 1.19x slower                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 74.0 ms: 1.19x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.93 us: 1.22x slower                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 86.8 ms: 1.23x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 22.6 us: 1.24x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.84 us: 1.26x slower                                                            |
| logging_format           | 7.91 us                                                         | 9.97 us: 1.26x slower                                                            |
| hexiom                   | 6.13 ms                                                         | 7.80 ms: 1.27x slower                                                            |
| richards                 | 40.3 ms                                                         | 51.6 ms: 1.28x slower                                                            |
| logging_simple           | 7.29 us                                                         | 9.45 us: 1.30x slower                                                            |
| scimark_lu               | 89.8 ms                                                         | 122 ms: 1.36x slower                                                             |
| coroutines               | 17.9 ms                                                         | 25.6 ms: 1.43x slower                                                            |
| spectral_norm            | 80.2 ms                                                         | 116 ms: 1.44x slower                                                             |
| async_generators         | 241 ms                                                          | 354 ms: 1.47x slower                                                             |
| bench_mp_pool            | 66.4 ms                                                         | 105 ms: 1.58x slower                                                             |
| unpack_sequence          | 40.0 ns                                                         | 77.9 ns: 1.95x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.47 ms: 2.12x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.83 ms: 2.21x slower                                                            |
| logging_silent           | 97.9 ns                                                         | 502 ns: 5.13x slower                                                             |
| coverage                 | 46.6 ms                                                         | 473 ms: 10.16x slower                                                            |
| thrift                   | 902 us                                                          | 103 ms: 113.86x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.06x slower                                                                     |

Benchmark hidden because not significant (1): html5lib
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250614-3.15.0a0-2e15a50-JIT/bm-20250614-pythonperf1_win32-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.057x slower

# HPT report

- Reliability score: 62.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown