# Results vs. 3.10.4

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.521x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.42x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 218 ms: 1.22x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| html5lib       | 52.1 ms                                                         | 37.3 ms: 1.40x faster                                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 331 ms: 2.78x faster                                                             |
| async_tree_io           | 940 ms                                                          | 393 ms: 2.39x faster                                                             |
| async_tree_none         | 394 ms                                                          | 171 ms: 2.31x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 203 ms: 2.30x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.44x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 147 ms: 3.42x faster                                                             |
| float          | 69.6 ms                                                         | 43.8 ms: 1.59x faster                                                            |
| nbody          | 79.1 ms                                                         | 55.9 ms: 1.42x faster                                                            |
| Geometric mean | (ref)                                                           | 1.97x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 77.7 ms: 1.50x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.2 ms: 1.19x faster                                                            |
| regex_dna      | 131 ms                                                          | 114 ms: 1.15x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 5.42 ms: 1.81x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 105 us: 1.81x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.09 sec: 1.76x faster                                                           |
| json_loads           | 22.4 us                                                         | 13.9 us: 1.61x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 86.3 ms: 1.39x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 202 us: 1.38x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 35.3 ms: 1.36x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 49.0 ms: 1.26x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.45 us: 1.16x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.7 ms: 1.13x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.71 us: 1.10x faster                                                            |
| pickle               | 7.83 us                                                         | 7.32 us: 1.07x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.18 us: 1.01x faster                                                            |
| pickle_dict          | 18.2 us                                                         | 19.0 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.31x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.1 ms: 1.09x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.27 ms: 1.73x faster                                                            |
| django_template | 36.0 ms                                                         | 24.4 ms: 1.48x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 35.0 ms: 1.33x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.9 ms: 1.32x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.46x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.26 sec: 13.46x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 103 us: 3.85x faster                                                             |
| pidigits                 | 502 ms                                                          | 147 ms: 3.42x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 29.2 ms: 2.79x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 331 ms: 2.78x faster                                                             |
| async_tree_io            | 940 ms                                                          | 393 ms: 2.39x faster                                                             |
| mdp                      | 1.83 sec                                                        | 786 ms: 2.32x faster                                                             |
| async_tree_none          | 394 ms                                                          | 171 ms: 2.31x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 203 ms: 2.30x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 13.8 us: 2.14x faster                                                            |
| pylint                   | 384 ms                                                          | 193 ms: 1.99x faster                                                             |
| asyncio_tcp              | 744 ms                                                          | 374 ms: 1.99x faster                                                             |
| deepcopy                 | 310 us                                                          | 159 us: 1.95x faster                                                             |
| go                       | 146 ms                                                          | 76.9 ms: 1.89x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 44.1 ms: 1.84x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 43.6 ms: 1.84x faster                                                            |
| chaos                    | 74.4 ms                                                         | 40.6 ms: 1.83x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.21 ms: 1.83x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 5.42 ms: 1.81x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 54.1 ns: 1.81x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 105 us: 1.81x faster                                                             |
| thrift                   | 902 us                                                          | 511 us: 1.76x faster                                                             |
| tomli_loads              | 1.91 sec                                                        | 1.09 sec: 1.76x faster                                                           |
| raytrace                 | 303 ms                                                          | 174 ms: 1.74x faster                                                             |
| mako                     | 9.10 ms                                                         | 5.27 ms: 1.73x faster                                                            |
| pyflate                  | 422 ms                                                          | 252 ms: 1.68x faster                                                             |
| comprehensions           | 17.7 us                                                         | 10.7 us: 1.66x faster                                                            |
| json                     | 4.76 ms                                                         | 2.92 ms: 1.63x faster                                                            |
| richards_super           | 49.9 ms                                                         | 30.7 ms: 1.62x faster                                                            |
| generators               | 31.6 ms                                                         | 19.6 ms: 1.61x faster                                                            |
| json_loads               | 22.4 us                                                         | 13.9 us: 1.61x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 857 ms: 1.60x faster                                                             |
| float                    | 69.6 ms                                                         | 43.8 ms: 1.59x faster                                                            |
| scimark_fft              | 216 ms                                                          | 136 ms: 1.59x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 426 ms: 1.55x faster                                                             |
| scimark_lu               | 89.8 ms                                                         | 58.3 ms: 1.54x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.75 us: 1.53x faster                                                            |
| pycparser                | 1.04 sec                                                        | 682 ms: 1.53x faster                                                             |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.7 ms: 1.52x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 38.9 ms: 1.51x faster                                                            |
| fannkuch                 | 317 ms                                                          | 211 ms: 1.50x faster                                                             |
| regex_compile            | 117 ms                                                          | 77.7 ms: 1.50x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.53 us: 1.50x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.11 ms: 1.49x faster                                                            |
| django_template          | 36.0 ms                                                         | 24.4 ms: 1.48x faster                                                            |
| richards                 | 40.3 ms                                                         | 27.3 ms: 1.47x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.20 ms: 1.47x faster                                                            |
| scimark_sor              | 115 ms                                                          | 79.1 ms: 1.46x faster                                                            |
| sympy_sum                | 122 ms                                                          | 84.3 ms: 1.45x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 60.3 ms: 1.44x faster                                                            |
| nbody                    | 79.1 ms                                                         | 55.9 ms: 1.42x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 37.3 ms: 1.40x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 86.3 ms: 1.39x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 202 us: 1.38x faster                                                             |
| sympy_str                | 229 ms                                                          | 166 ms: 1.38x faster                                                             |
| xml_etree_process        | 48.1 ms                                                         | 35.3 ms: 1.36x faster                                                            |
| sympy_expand             | 391 ms                                                          | 288 ms: 1.36x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 829 us: 1.35x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.4 ms: 1.34x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 35.0 ms: 1.33x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.9 ms: 1.32x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 49.0 ms: 1.26x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.3 ms: 1.25x faster                                                            |
| logging_simple           | 7.29 us                                                         | 5.82 us: 1.25x faster                                                            |
| telco                    | 4.83 ms                                                         | 3.86 ms: 1.25x faster                                                            |
| logging_format           | 7.91 us                                                         | 6.37 us: 1.24x faster                                                            |
| unpack_sequence          | 40.0 ns                                                         | 32.7 ns: 1.23x faster                                                            |
| 2to3                     | 265 ms                                                          | 218 ms: 1.22x faster                                                             |
| docutils                 | 1.95 sec                                                        | 1.61 sec: 1.21x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 13.2 ms: 1.19x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.45 us: 1.16x faster                                                            |
| regex_dna                | 131 ms                                                          | 114 ms: 1.15x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.7 ms: 1.13x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 71.1 ms: 1.13x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.71 us: 1.10x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.08x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.32 us: 1.07x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.18 us: 1.01x faster                                                            |
| async_generators         | 241 ms                                                          | 239 ms: 1.01x faster                                                             |
| pickle_dict              | 18.2 us                                                         | 19.0 us: 1.04x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.4 ms: 1.06x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.1 ms: 1.09x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 88.8 ms: 1.34x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.14 ms: 1.67x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.27 ms: 1.83x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.52x faster                                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.521x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.47x
- 95% likely to have a speedup of 1.45x
- 99% likely to have a speedup of 1.42x

# Memory
- memory change: unknown