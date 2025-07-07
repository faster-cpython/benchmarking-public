# Results vs. 3.10.4

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.284x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 225 ms: 1.18x faster                                                             |
| docutils       | 1.95 sec                                                        | 2.88 sec: 1.48x slower                                                           |
| html5lib       | 52.1 ms                                                         | 41.3 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 334 ms: 2.76x faster                                                             |
| async_tree_io           | 940 ms                                                          | 356 ms: 2.64x faster                                                             |
| async_tree_none         | 394 ms                                                          | 174 ms: 2.27x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 214 ms: 2.19x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 136 ms: 3.70x faster                                                             |
| float          | 69.6 ms                                                         | 45.9 ms: 1.52x faster                                                            |
| nbody          | 79.1 ms                                                         | 82.8 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.75x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 94.1 ms: 1.24x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.4 ms: 1.18x faster                                                            |
| regex_dna      | 131 ms                                                          | 115 ms: 1.14x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.65 ms: 1.48x faster                                                            |
| json_loads           | 22.4 us                                                         | 16.1 us: 1.39x faster                                                            |
| xml_etree_parse      | 120 ms                                                          | 90.8 ms: 1.32x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 231 us: 1.21x faster                                                             |
| xml_etree_iterparse  | 70.8 ms                                                         | 58.7 ms: 1.21x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 159 us: 1.19x faster                                                             |
| xml_etree_process    | 48.1 ms                                                         | 44.4 ms: 1.08x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.02 us: 1.07x faster                                                            |
| pickle               | 7.83 us                                                         | 7.88 us: 1.01x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 62.4 ms: 1.01x slower                                                            |
| unpickle_list        | 2.98 us                                                         | 3.05 us: 1.02x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.06x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.2 us: 1.11x slower                                                            |
| tomli_loads          | 1.91 sec                                                        | 2.71 sec: 1.42x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                            |
| python_startup         | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 27.5 ms: 1.31x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 40.5 ms: 1.15x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 19.7 ms: 1.06x faster                                                            |
| mako            | 9.10 ms                                                         | 9.74 ms: 1.07x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 2.27 sec: 7.49x faster                                                           |
| pidigits                 | 502 ms                                                          | 136 ms: 3.70x faster                                                             |
| typing_runtime_protocols | 396 us                                                          | 128 us: 3.09x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 334 ms: 2.76x faster                                                             |
| async_tree_io            | 940 ms                                                          | 356 ms: 2.64x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 32.5 ms: 2.50x faster                                                            |
| async_tree_none          | 394 ms                                                          | 174 ms: 2.27x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 214 ms: 2.19x faster                                                             |
| pylint                   | 384 ms                                                          | 214 ms: 1.79x faster                                                             |
| sqlite_synth             | 2.29 us                                                         | 1.33 us: 1.72x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.43 ms: 1.66x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.13 sec: 1.62x faster                                                           |
| chaos                    | 74.4 ms                                                         | 46.2 ms: 1.61x faster                                                            |
| thrift                   | 902 us                                                          | 570 us: 1.58x faster                                                             |
| go                       | 146 ms                                                          | 92.3 ms: 1.58x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 62.2 ns: 1.57x faster                                                            |
| deepcopy                 | 310 us                                                          | 202 us: 1.54x faster                                                             |
| json                     | 4.76 ms                                                         | 3.11 ms: 1.53x faster                                                            |
| float                    | 69.6 ms                                                         | 45.9 ms: 1.52x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 492 ms: 1.51x faster                                                             |
| json_dumps               | 9.82 ms                                                         | 6.65 ms: 1.48x faster                                                            |
| comprehensions           | 17.7 us                                                         | 12.2 us: 1.46x faster                                                            |
| raytrace                 | 303 ms                                                          | 210 ms: 1.44x faster                                                             |
| pycparser                | 1.04 sec                                                        | 725 ms: 1.44x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 20.7 us: 1.43x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 57.7 ms: 1.41x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 41.6 ms: 1.41x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 64.4 ms: 1.39x faster                                                            |
| json_loads               | 22.4 us                                                         | 16.1 us: 1.39x faster                                                            |
| generators               | 31.6 ms                                                         | 22.9 ms: 1.38x faster                                                            |
| pyflate                  | 422 ms                                                          | 312 ms: 1.35x faster                                                             |
| hexiom                   | 6.13 ms                                                         | 4.63 ms: 1.32x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 90.8 ms: 1.32x faster                                                            |
| django_template          | 36.0 ms                                                         | 27.5 ms: 1.31x faster                                                            |
| scimark_sor              | 115 ms                                                          | 88.2 ms: 1.31x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 41.3 ms: 1.26x faster                                                            |
| sympy_sum                | 122 ms                                                          | 98.0 ms: 1.25x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.15 us: 1.25x faster                                                            |
| richards_super           | 49.9 ms                                                         | 40.2 ms: 1.24x faster                                                            |
| regex_compile            | 117 ms                                                          | 94.1 ms: 1.24x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.1 ms: 1.24x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 70.7 ms: 1.23x faster                                                            |
| coroutines               | 17.9 ms                                                         | 14.7 ms: 1.22x faster                                                            |
| sympy_expand             | 391 ms                                                          | 321 ms: 1.22x faster                                                             |
| sympy_str                | 229 ms                                                          | 189 ms: 1.21x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 231 us: 1.21x faster                                                             |
| xml_etree_iterparse      | 70.8 ms                                                         | 58.7 ms: 1.21x faster                                                            |
| richards                 | 40.3 ms                                                         | 33.4 ms: 1.20x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 159 us: 1.19x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 14.1 ms: 1.18x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.4 ms: 1.18x faster                                                            |
| 2to3                     | 265 ms                                                          | 225 ms: 1.18x faster                                                             |
| pprint_safe_repr         | 658 ms                                                          | 569 ms: 1.16x faster                                                             |
| genshi_xml               | 46.6 ms                                                         | 40.5 ms: 1.15x faster                                                            |
| regex_dna                | 131 ms                                                          | 115 ms: 1.14x faster                                                             |
| spectral_norm            | 80.2 ms                                                         | 73.8 ms: 1.09x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 44.4 ms: 1.08x faster                                                            |
| logging_format           | 7.91 us                                                         | 7.31 us: 1.08x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.78 us: 1.07x faster                                                            |
| pickle_list              | 3.22 us                                                         | 3.02 us: 1.07x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 19.7 ms: 1.06x faster                                                            |
| fannkuch                 | 317 ms                                                          | 300 ms: 1.06x faster                                                             |
| regex_effbot             | 1.66 ms                                                         | 1.58 ms: 1.05x faster                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.23 ms: 1.05x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.12 ms: 1.04x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.10 ms: 1.02x faster                                                            |
| pickle                   | 7.83 us                                                         | 7.88 us: 1.01x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 62.4 ms: 1.01x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.05 us: 1.02x slower                                                            |
| nbody                    | 79.1 ms                                                         | 82.8 ms: 1.05x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.06x slower                                                            |
| mako                     | 9.10 ms                                                         | 9.74 ms: 1.07x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 85.7 ms: 1.07x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.08x slower                                                            |
| async_generators         | 241 ms                                                          | 262 ms: 1.09x slower                                                             |
| pickle_dict              | 18.2 us                                                         | 20.2 us: 1.11x slower                                                            |
| telco                    | 4.83 ms                                                         | 5.44 ms: 1.13x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.1 ms: 1.14x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 79.2 ms: 1.19x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.69 sec: 1.23x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.71 sec: 1.42x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.88 sec: 1.48x slower                                                           |
| coverage                 | 46.6 ms                                                         | 68.9 ms: 1.48x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.03 ms: 1.49x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.28x faster                                                                     |

Benchmark hidden because not significant (2): unpack_sequence, scimark_fft
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250705-3.15.0a0-1953713-NOGIL/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.284x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown