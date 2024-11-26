# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: windows-x86
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 248 ms: 1.07x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                          |
| html5lib       | 52.1 ms                                                         | 45.9 ms: 1.13x faster                                                           |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                            |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 477 ms: 1.93x faster                                                            |
| async_tree_io           | 940 ms                                                          | 534 ms: 1.76x faster                                                            |
| async_tree_none         | 394 ms                                                          | 226 ms: 1.74x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 281 ms: 1.66x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.77x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 204 ms: 2.46x faster                                                            |
| float          | 69.6 ms                                                         | 61.5 ms: 1.13x faster                                                           |
| nbody          | 79.1 ms                                                         | 88.2 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 113 ms: 1.15x faster                                                            |
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.8 ms: 1.01x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.81 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 9.04 ms: 1.09x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.0 us: 1.07x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 179 us: 1.06x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 266 us: 1.06x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.82 sec: 1.05x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.7 ms: 1.03x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 47.6 ms: 1.01x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 65.8 ms: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.78 ms: 1.17x faster                                                           |
| django_template | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 46.2 ms: 1.01x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 21.1 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.77x faster                                                            |
| pidigits                 | 502 ms                                                          | 204 ms: 2.46x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 477 ms: 1.93x faster                                                            |
| async_tree_io            | 940 ms                                                          | 534 ms: 1.76x faster                                                            |
| async_tree_none          | 394 ms                                                          | 226 ms: 1.74x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 281 ms: 1.66x faster                                                            |
| pylint                   | 384 ms                                                          | 236 ms: 1.63x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.65 ms: 1.52x faster                                                           |
| go                       | 146 ms                                                          | 100 ms: 1.46x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 69.7 ns: 1.41x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 59.8 ms: 1.36x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 21.9 us: 1.35x faster                                                           |
| generators               | 31.6 ms                                                         | 24.1 ms: 1.31x faster                                                           |
| deepcopy                 | 310 us                                                          | 238 us: 1.30x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 69.2 ms: 1.30x faster                                                           |
| chaos                    | 74.4 ms                                                         | 57.7 ms: 1.29x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.0 us: 1.26x faster                                                           |
| pycparser                | 1.04 sec                                                        | 850 ms: 1.23x faster                                                            |
| thrift                   | 902 us                                                          | 740 us: 1.22x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.10 ms: 1.21x faster                                                           |
| raytrace                 | 303 ms                                                          | 250 ms: 1.21x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.16 ms: 1.19x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.35 ms: 1.17x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.78 ms: 1.17x faster                                                           |
| regex_dna                | 131 ms                                                          | 113 ms: 1.15x faster                                                            |
| pyflate                  | 422 ms                                                          | 368 ms: 1.15x faster                                                            |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 45.9 ms: 1.13x faster                                                           |
| richards_super           | 49.9 ms                                                         | 44.1 ms: 1.13x faster                                                           |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                            |
| float                    | 69.6 ms                                                         | 61.5 ms: 1.13x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 52.1 ms: 1.12x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.12x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 79.6 ms: 1.09x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.46 us: 1.09x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.04 ms: 1.09x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 57.0 ms: 1.09x faster                                                           |
| scimark_sor              | 115 ms                                                          | 106 ms: 1.08x faster                                                            |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                            |
| 2to3                     | 265 ms                                                          | 248 ms: 1.07x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.0 us: 1.07x faster                                                           |
| django_template          | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 179 us: 1.06x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 15.7 ms: 1.06x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 266 us: 1.06x faster                                                            |
| sympy_str                | 229 ms                                                          | 218 ms: 1.05x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.82 sec: 1.05x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 77.4 ms: 1.04x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.7 ms: 1.03x faster                                                           |
| richards                 | 40.3 ms                                                         | 39.2 ms: 1.03x faster                                                           |
| sympy_expand             | 391 ms                                                          | 383 ms: 1.02x faster                                                            |
| coroutines               | 17.9 ms                                                         | 17.6 ms: 1.02x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 44.1 ms: 1.01x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 47.6 ms: 1.01x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 651 ms: 1.01x faster                                                            |
| fannkuch                 | 317 ms                                                          | 314 ms: 1.01x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 46.2 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.21 ms: 1.01x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.81 sec: 1.01x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.36 sec: 1.01x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 80.4 ms: 1.01x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.8 ms: 1.01x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 21.1 ms: 1.01x slower                                                           |
| sqlglot_normalize        | 230 ms                                                          | 234 ms: 1.02x slower                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 65.8 ms: 1.07x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.58 us: 1.08x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.81 ms: 1.09x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.98 us: 1.10x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 89.6 ms: 1.10x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.1 ms: 1.11x slower                                                           |
| nbody                    | 79.1 ms                                                         | 88.2 ms: 1.11x slower                                                           |
| scimark_fft              | 216 ms                                                          | 246 ms: 1.14x slower                                                            |
| python_startup           | 22.9 ms                                                         | 26.8 ms: 1.17x slower                                                           |
| coverage                 | 46.6 ms                                                         | 56.4 ms: 1.21x slower                                                           |
| async_generators         | 241 ms                                                          | 295 ms: 1.22x slower                                                            |
| json                     | 4.76 ms                                                         | 5.89 ms: 1.24x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 88.8 ms: 1.34x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.80 ms: 1.41x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.00 ms: 1.45x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.18 ms: 1.71x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                    |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf1_win32-x86-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.111x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown