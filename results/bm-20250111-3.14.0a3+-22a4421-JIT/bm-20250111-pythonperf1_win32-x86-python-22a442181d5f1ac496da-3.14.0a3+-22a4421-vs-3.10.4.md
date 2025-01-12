# Results vs. 3.10.4

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-x86
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.061x faster
- HPT reliability: 77.33%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.95 sec                                                        | 1.98 sec: 1.02x slower                                                          |
| html5lib       | 52.1 ms                                                         | 48.9 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 473 ms: 1.95x faster                                                            |
| async_tree_io           | 940 ms                                                          | 485 ms: 1.94x faster                                                            |
| async_tree_none         | 394 ms                                                          | 233 ms: 1.69x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 285 ms: 1.64x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| float          | 69.6 ms                                                         | 52.1 ms: 1.34x faster                                                           |
| nbody          | 79.1 ms                                                         | 100 ms: 1.27x slower                                                            |
| Geometric mean | (ref)                                                           | 1.38x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| regex_compile  | 117 ms                                                          | 114 ms: 1.02x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 8.98 ms: 1.09x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.4 ms: 1.07x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 298 us: 1.06x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 202 us: 1.07x slower                                                            |
| unpickle             | 9.82 us                                                         | 10.7 us: 1.09x slower                                                           |
| unpickle_list        | 2.98 us                                                         | 3.32 us: 1.11x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 54.4 ms: 1.13x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 21.3 us: 1.16x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.80 us: 1.18x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 76.1 ms: 1.23x slower                                                           |
| pickle               | 7.83 us                                                         | 10.2 us: 1.31x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                           |
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.42 ms: 1.23x faster                                                           |
| django_template | 36.0 ms                                                         | 36.9 ms: 1.02x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 57.1 ms: 1.22x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 26.7 ms: 1.27x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.07x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 167 us: 2.37x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 107 ms: 2.16x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 473 ms: 1.95x faster                                                            |
| async_tree_io            | 940 ms                                                          | 485 ms: 1.94x faster                                                            |
| async_tree_none          | 394 ms                                                          | 233 ms: 1.69x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 285 ms: 1.64x faster                                                            |
| pylint                   | 384 ms                                                          | 238 ms: 1.61x faster                                                            |
| float                    | 69.6 ms                                                         | 52.1 ms: 1.34x faster                                                           |
| deltablue                | 4.04 ms                                                         | 3.18 ms: 1.27x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 23.8 us: 1.24x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 79.0 ns: 1.24x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 73.0 ms: 1.23x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.42 ms: 1.23x faster                                                           |
| thrift                   | 902 us                                                          | 758 us: 1.19x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                           |
| scimark_sor              | 115 ms                                                          | 98.3 ms: 1.17x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 69.8 ms: 1.16x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.15 ms: 1.16x faster                                                           |
| go                       | 146 ms                                                          | 126 ms: 1.16x faster                                                            |
| chaos                    | 74.4 ms                                                         | 65.0 ms: 1.14x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 51.5 ms: 1.14x faster                                                           |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.42 ms: 1.11x faster                                                           |
| deepcopy                 | 310 us                                                          | 280 us: 1.11x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 72.6 ms: 1.10x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| pycparser                | 1.04 sec                                                        | 950 ms: 1.10x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 8.98 ms: 1.09x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.4 ms: 1.09x faster                                                           |
| json                     | 4.76 ms                                                         | 4.36 ms: 1.09x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 683 ms: 1.09x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.03 ms: 1.07x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.4 ms: 1.07x faster                                                           |
| sympy_sum                | 122 ms                                                          | 115 ms: 1.07x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 48.9 ms: 1.06x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.06 ms: 1.06x faster                                                           |
| pyflate                  | 422 ms                                                          | 400 ms: 1.05x faster                                                            |
| richards_super           | 49.9 ms                                                         | 48.4 ms: 1.03x faster                                                           |
| regex_compile            | 117 ms                                                          | 114 ms: 1.02x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 62.2 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                          |
| raytrace                 | 303 ms                                                          | 305 ms: 1.01x slower                                                            |
| mdp                      | 1.83 sec                                                        | 1.85 sec: 1.01x slower                                                          |
| docutils                 | 1.95 sec                                                        | 1.98 sec: 1.02x slower                                                          |
| comprehensions           | 17.7 us                                                         | 18.2 us: 1.02x slower                                                           |
| django_template          | 36.0 ms                                                         | 36.9 ms: 1.02x slower                                                           |
| sympy_str                | 229 ms                                                          | 235 ms: 1.03x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 17.4 ms: 1.05x slower                                                           |
| sympy_expand             | 391 ms                                                          | 413 ms: 1.06x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 298 us: 1.06x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 202 us: 1.07x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.87 us: 1.07x slower                                                           |
| richards                 | 40.3 ms                                                         | 43.1 ms: 1.07x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 87.1 ms: 1.07x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                           |
| fannkuch                 | 317 ms                                                          | 342 ms: 1.08x slower                                                            |
| unpickle                 | 9.82 us                                                         | 10.7 us: 1.09x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.50 sec: 1.10x slower                                                          |
| nqueens                  | 87.1 ms                                                         | 95.6 ms: 1.10x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 44.1 ns: 1.10x slower                                                           |
| scimark_fft              | 216 ms                                                          | 239 ms: 1.10x slower                                                            |
| unpickle_list            | 2.98 us                                                         | 3.32 us: 1.11x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 89.1 ms: 1.11x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 735 ms: 1.12x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 54.4 ms: 1.13x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 50.6 ms: 1.13x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.0 ms: 1.14x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 7.11 ms: 1.16x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 21.3 us: 1.16x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.23 us: 1.17x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.57 us: 1.18x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.80 us: 1.18x slower                                                           |
| generators               | 31.6 ms                                                         | 38.0 ms: 1.20x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 57.1 ms: 1.22x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 76.1 ms: 1.23x slower                                                           |
| nbody                    | 79.1 ms                                                         | 100 ms: 1.27x slower                                                            |
| genshi_text              | 21.0 ms                                                         | 26.7 ms: 1.27x slower                                                           |
| pickle                   | 7.83 us                                                         | 10.2 us: 1.31x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 88.7 ms: 1.34x slower                                                           |
| async_generators         | 241 ms                                                          | 338 ms: 1.40x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.83 ms: 1.43x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.31 ms: 1.51x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.07 ms: 1.54x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): 2to3
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 77.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown