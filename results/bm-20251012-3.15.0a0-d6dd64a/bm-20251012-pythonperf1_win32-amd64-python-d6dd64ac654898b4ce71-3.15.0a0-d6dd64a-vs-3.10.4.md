# Results vs. 3.10.4

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.430x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.62 sec: 1.20x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.7 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| async_tree_io           | 940 ms                                                          | 390 ms: 2.41x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 203 ms: 2.30x faster                                                             |
| async_tree_none         | 394 ms                                                          | 174 ms: 2.27x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.44x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 150 ms: 3.35x faster                                                             |
| float          | 69.6 ms                                                         | 46.2 ms: 1.51x faster                                                            |
| nbody          | 79.1 ms                                                         | 67.0 ms: 1.18x faster                                                            |
| Geometric mean | (ref)                                                           | 1.81x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 81.4 ms: 1.43x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 14.1 ms: 1.12x faster                                                            |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.49 ms: 1.79x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.5 us: 1.54x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 137 us: 1.38x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.40 sec: 1.37x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 89.5 ms: 1.34x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 216 us: 1.29x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 39.9 ms: 1.21x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.4 ms: 1.12x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.81 us: 1.12x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 57.1 ms: 1.08x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.94 us: 1.01x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.24 us: 1.01x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 19.8 us: 1.08x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                            |
| python_startup         | 22.9 ms                                                         | 26.0 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 25.0 ms: 1.44x faster                                                            |
| mako            | 9.10 ms                                                         | 6.76 ms: 1.35x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.9 ms: 1.32x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 35.4 ms: 1.32x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.25 sec: 13.60x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 105 us: 3.77x faster                                                             |
| pidigits                 | 502 ms                                                          | 150 ms: 3.35x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.2 ms: 2.78x faster                                                            |
| async_tree_io            | 940 ms                                                          | 390 ms: 2.41x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 203 ms: 2.30x faster                                                             |
| async_tree_none          | 394 ms                                                          | 174 ms: 2.27x faster                                                             |
| mdp                      | 1.83 sec                                                        | 826 ms: 2.21x faster                                                             |
| pylint                   | 384 ms                                                          | 197 ms: 1.95x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 383 ms: 1.94x faster                                                             |
| go                       | 146 ms                                                          | 77.3 ms: 1.88x faster                                                            |
| deepcopy                 | 310 us                                                          | 169 us: 1.83x faster                                                             |
| deltablue                | 4.04 ms                                                         | 2.24 ms: 1.80x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 5.49 ms: 1.79x faster                                                            |
| thrift                   | 902 us                                                          | 506 us: 1.78x faster                                                             |
| chaos                    | 74.4 ms                                                         | 41.7 ms: 1.78x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 48.2 ms: 1.69x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 58.4 ns: 1.68x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 17.9 us: 1.66x faster                                                            |
| json                     | 4.76 ms                                                         | 2.92 ms: 1.63x faster                                                            |
| raytrace                 | 303 ms                                                          | 186 ms: 1.63x faster                                                             |
| richards_super           | 49.9 ms                                                         | 31.0 ms: 1.61x faster                                                            |
| generators               | 31.6 ms                                                         | 19.6 ms: 1.61x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.2 us: 1.58x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.5 us: 1.54x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.9 ms: 1.51x faster                                                            |
| float                    | 69.6 ms                                                         | 46.2 ms: 1.51x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 60.1 ms: 1.49x faster                                                            |
| pyflate                  | 422 ms                                                          | 283 ms: 1.49x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.13 ms: 1.48x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.81 us: 1.48x faster                                                            |
| richards                 | 40.3 ms                                                         | 27.5 ms: 1.47x faster                                                            |
| scimark_sor              | 115 ms                                                          | 79.1 ms: 1.46x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 40.5 ms: 1.44x faster                                                            |
| django_template          | 36.0 ms                                                         | 25.0 ms: 1.44x faster                                                            |
| pycparser                | 1.04 sec                                                        | 725 ms: 1.44x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.60 us: 1.44x faster                                                            |
| regex_compile            | 117 ms                                                          | 81.4 ms: 1.43x faster                                                            |
| sympy_sum                | 122 ms                                                          | 88.0 ms: 1.39x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 62.8 ms: 1.39x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 137 us: 1.38x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.40 sec: 1.37x faster                                                           |
| sympy_str                | 229 ms                                                          | 170 ms: 1.35x faster                                                             |
| mako                     | 9.10 ms                                                         | 6.76 ms: 1.35x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 38.7 ms: 1.35x faster                                                            |
| sympy_expand             | 391 ms                                                          | 290 ms: 1.35x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 89.5 ms: 1.34x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 12.5 ms: 1.33x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.03 sec: 1.33x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 15.9 ms: 1.32x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 35.4 ms: 1.32x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 508 ms: 1.30x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 216 us: 1.29x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 867 us: 1.29x faster                                                             |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.55 ms: 1.27x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 63.3 ms: 1.27x faster                                                            |
| scimark_fft              | 216 ms                                                          | 172 ms: 1.25x faster                                                             |
| 2to3                     | 265 ms                                                          | 219 ms: 1.21x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 39.9 ms: 1.21x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.62 sec: 1.20x faster                                                           |
| coroutines               | 17.9 ms                                                         | 15.0 ms: 1.20x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.65 us: 1.19x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.15 us: 1.19x faster                                                            |
| nbody                    | 79.1 ms                                                         | 67.0 ms: 1.18x faster                                                            |
| fannkuch                 | 317 ms                                                          | 270 ms: 1.18x faster                                                             |
| telco                    | 4.83 ms                                                         | 4.22 ms: 1.15x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.4 ms: 1.12x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.81 us: 1.12x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 14.1 ms: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.53 ms: 1.09x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 73.6 ms: 1.09x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 57.1 ms: 1.08x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 37.4 ns: 1.07x faster                                                            |
| async_generators         | 241 ms                                                          | 237 ms: 1.02x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.94 us: 1.01x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.24 us: 1.01x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 19.8 us: 1.08x slower                                                            |
| coverage                 | 46.6 ms                                                         | 51.4 ms: 1.10x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.0 ms: 1.13x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 90.8 ms: 1.37x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.06 ms: 1.61x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.30 ms: 1.87x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.43x faster                                                                     |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.430x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: unknown