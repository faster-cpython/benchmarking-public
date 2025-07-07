# Results vs. 3.10.4

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.469x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 220 ms: 1.21x faster                                                             |
| docutils       | 1.95 sec                                                        | 1.66 sec: 1.18x faster                                                           |
| html5lib       | 52.1 ms                                                         | 38.9 ms: 1.34x faster                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| async_tree_io           | 940 ms                                                          | 396 ms: 2.38x faster                                                             |
| async_tree_none         | 394 ms                                                          | 170 ms: 2.32x faster                                                             |
| async_tree_memoization  | 467 ms                                                          | 206 ms: 2.27x faster                                                             |
| Geometric mean          | (ref)                                                           | 2.44x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 145 ms: 3.46x faster                                                             |
| float          | 69.6 ms                                                         | 44.7 ms: 1.56x faster                                                            |
| nbody          | 79.1 ms                                                         | 52.7 ms: 1.50x faster                                                            |
| Geometric mean | (ref)                                                           | 2.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 79.3 ms: 1.47x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 13.9 ms: 1.14x faster                                                            |
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                             |
| regex_effbot   | 1.66 ms                                                         | 1.60 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 107 us: 1.77x faster                                                             |
| tomli_loads          | 1.91 sec                                                        | 1.14 sec: 1.67x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 6.25 ms: 1.57x faster                                                            |
| json_loads           | 22.4 us                                                         | 14.6 us: 1.53x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 203 us: 1.38x faster                                                             |
| xml_etree_parse      | 120 ms                                                          | 88.4 ms: 1.36x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 35.5 ms: 1.36x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 50.8 ms: 1.21x faster                                                            |
| unpickle             | 9.82 us                                                         | 8.46 us: 1.16x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.8 ms: 1.13x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.78 us: 1.07x faster                                                            |
| pickle_list          | 3.22 us                                                         | 3.37 us: 1.05x slower                                                            |
| pickle_dict          | 18.2 us                                                         | 20.8 us: 1.14x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.26x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                            |
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.43 ms: 1.68x faster                                                            |
| django_template | 36.0 ms                                                         | 24.2 ms: 1.49x faster                                                            |
| genshi_xml      | 46.6 ms                                                         | 34.8 ms: 1.34x faster                                                            |
| genshi_text     | 21.0 ms                                                         | 15.8 ms: 1.33x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.45x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 17.0 sec                                                        | 1.44 sec: 11.83x faster                                                          |
| typing_runtime_protocols | 396 us                                                          | 102 us: 3.90x faster                                                             |
| pidigits                 | 502 ms                                                          | 145 ms: 3.46x faster                                                             |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 328 ms: 2.81x faster                                                             |
| pathlib                  | 81.2 ms                                                         | 31.9 ms: 2.55x faster                                                            |
| async_tree_io            | 940 ms                                                          | 396 ms: 2.38x faster                                                             |
| async_tree_none          | 394 ms                                                          | 170 ms: 2.32x faster                                                             |
| mdp                      | 1.83 sec                                                        | 804 ms: 2.27x faster                                                             |
| async_tree_memoization   | 467 ms                                                          | 206 ms: 2.27x faster                                                             |
| pylint                   | 384 ms                                                          | 200 ms: 1.92x faster                                                             |
| go                       | 146 ms                                                          | 78.4 ms: 1.86x faster                                                            |
| deepcopy                 | 310 us                                                          | 170 us: 1.82x faster                                                             |
| thrift                   | 902 us                                                          | 497 us: 1.82x faster                                                             |
| chaos                    | 74.4 ms                                                         | 41.3 ms: 1.80x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.26 ms: 1.79x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 107 us: 1.77x faster                                                             |
| crypto_pyaes             | 81.3 ms                                                         | 46.1 ms: 1.76x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 55.9 ns: 1.75x faster                                                            |
| raytrace                 | 303 ms                                                          | 180 ms: 1.68x faster                                                             |
| mako                     | 9.10 ms                                                         | 5.43 ms: 1.68x faster                                                            |
| comprehensions           | 17.7 us                                                         | 10.6 us: 1.67x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.14 sec: 1.67x faster                                                           |
| pyflate                  | 422 ms                                                          | 254 ms: 1.66x faster                                                             |
| deepcopy_memo            | 29.6 us                                                         | 18.3 us: 1.62x faster                                                            |
| generators               | 31.6 ms                                                         | 19.5 ms: 1.62x faster                                                            |
| json                     | 4.76 ms                                                         | 2.96 ms: 1.61x faster                                                            |
| richards_super           | 49.9 ms                                                         | 31.5 ms: 1.58x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.25 ms: 1.57x faster                                                            |
| float                    | 69.6 ms                                                         | 44.7 ms: 1.56x faster                                                            |
| json_loads               | 22.4 us                                                         | 14.6 us: 1.53x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.0 ms: 1.51x faster                                                            |
| nbody                    | 79.1 ms                                                         | 52.7 ms: 1.50x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 918 ms: 1.49x faster                                                             |
| pycparser                | 1.04 sec                                                        | 699 ms: 1.49x faster                                                             |
| django_template          | 36.0 ms                                                         | 24.2 ms: 1.49x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 58.9 ms: 1.48x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.55 us: 1.48x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.16 ms: 1.48x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 61.0 ms: 1.47x faster                                                            |
| regex_compile            | 117 ms                                                          | 79.3 ms: 1.47x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 1.83 us: 1.47x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 449 ms: 1.47x faster                                                             |
| richards                 | 40.3 ms                                                         | 27.6 ms: 1.46x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.23 ms: 1.45x faster                                                            |
| fannkuch                 | 317 ms                                                          | 219 ms: 1.45x faster                                                             |
| scimark_sor              | 115 ms                                                          | 79.9 ms: 1.44x faster                                                            |
| scimark_fft              | 216 ms                                                          | 151 ms: 1.44x faster                                                             |
| dulwich_log              | 58.5 ms                                                         | 40.9 ms: 1.43x faster                                                            |
| sympy_sum                | 122 ms                                                          | 87.4 ms: 1.40x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 534 ms: 1.39x faster                                                             |
| pickle_pure_python       | 280 us                                                          | 203 us: 1.38x faster                                                             |
| xml_etree_parse          | 120 ms                                                          | 88.4 ms: 1.36x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 35.5 ms: 1.36x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 34.8 ms: 1.34x faster                                                            |
| sympy_str                | 229 ms                                                          | 171 ms: 1.34x faster                                                             |
| html5lib                 | 52.1 ms                                                         | 38.9 ms: 1.34x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 15.8 ms: 1.33x faster                                                            |
| sympy_expand             | 391 ms                                                          | 294 ms: 1.33x faster                                                             |
| bench_thread_pool        | 1.12 ms                                                         | 850 us: 1.32x faster                                                             |
| sympy_integrate          | 16.6 ms                                                         | 12.7 ms: 1.31x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 50.8 ms: 1.21x faster                                                            |
| 2to3                     | 265 ms                                                          | 220 ms: 1.21x faster                                                             |
| logging_format           | 7.91 us                                                         | 6.61 us: 1.20x faster                                                            |
| logging_simple           | 7.29 us                                                         | 6.16 us: 1.18x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.2 ms: 1.18x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.66 sec: 1.18x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 68.3 ms: 1.17x faster                                                            |
| unpickle                 | 9.82 us                                                         | 8.46 us: 1.16x faster                                                            |
| telco                    | 4.83 ms                                                         | 4.19 ms: 1.15x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 13.9 ms: 1.14x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 70.9 ms: 1.13x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.8 ms: 1.13x faster                                                            |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                             |
| unpickle_list            | 2.98 us                                                         | 2.78 us: 1.07x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.60 ms: 1.04x faster                                                            |
| async_generators         | 241 ms                                                          | 243 ms: 1.01x slower                                                             |
| pickle_list              | 3.22 us                                                         | 3.37 us: 1.05x slower                                                            |
| coverage                 | 46.6 ms                                                         | 49.8 ms: 1.07x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.8 us: 1.14x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 95.3 ms: 1.44x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 2.12 ms: 1.65x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.33 ms: 1.91x slower                                                            |
| Geometric mean           | (ref)                                                           | 1.45x faster                                                                     |

Benchmark hidden because not significant (2): pickle, unpack_sequence
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.469x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.43x
- 95% likely to have a speedup of 1.41x
- 99% likely to have a speedup of 1.37x

# Memory
- memory change: unknown