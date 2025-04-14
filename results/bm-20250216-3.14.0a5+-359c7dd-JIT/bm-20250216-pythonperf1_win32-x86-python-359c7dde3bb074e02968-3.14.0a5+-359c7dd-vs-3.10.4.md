# Results vs. 3.10.4

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-x86
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.064x faster
- HPT reliability: 92.10%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 276 ms: 1.04x slower                                                            |
| docutils       | 1.95 sec                                                        | 2.06 sec: 1.06x slower                                                          |
| html5lib       | 52.1 ms                                                         | 49.8 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 506 ms: 1.86x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 500 ms: 1.84x faster                                                            |
| async_tree_none         | 394 ms                                                          | 245 ms: 1.61x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 295 ms: 1.58x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.72x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 203 ms: 2.48x faster                                                            |
| float          | 69.6 ms                                                         | 54.5 ms: 1.28x faster                                                           |
| nbody          | 79.1 ms                                                         | 113 ms: 1.43x slower                                                            |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| regex_compile  | 117 ms                                                          | 122 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.6 ms: 1.08x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 9.21 ms: 1.07x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                          |
| json_loads           | 22.4 us                                                         | 22.7 us: 1.01x slower                                                           |
| unpickle_list        | 2.98 us                                                         | 3.04 us: 1.02x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.8 us: 1.14x slower                                                           |
| xml_etree_process    | 48.1 ms                                                         | 56.0 ms: 1.16x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.80 us: 1.18x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 73.1 ms: 1.19x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 334 us: 1.19x slower                                                            |
| pickle               | 7.83 us                                                         | 9.37 us: 1.20x slower                                                           |
| unpickle_pure_python | 189 us                                                          | 244 us: 1.29x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 21.3 ms: 1.18x slower                                                           |
| python_startup         | 22.9 ms                                                         | 27.8 ms: 1.21x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.20x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.78 ms: 1.17x faster                                                           |
| django_template | 36.0 ms                                                         | 38.8 ms: 1.08x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 23.2 ms: 1.11x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 53.5 ms: 1.15x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 203 ms: 2.48x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 34.8 ms: 2.34x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 181 us: 2.19x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 108 ms: 2.13x faster                                                            |
| async_tree_io            | 940 ms                                                          | 506 ms: 1.86x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 500 ms: 1.84x faster                                                            |
| pylint                   | 384 ms                                                          | 233 ms: 1.64x faster                                                            |
| async_tree_none          | 394 ms                                                          | 245 ms: 1.61x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 295 ms: 1.58x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 71.1 ns: 1.38x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.99 ms: 1.35x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 22.2 us: 1.33x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 67.5 ms: 1.33x faster                                                           |
| generators               | 31.6 ms                                                         | 24.1 ms: 1.31x faster                                                           |
| float                    | 69.6 ms                                                         | 54.5 ms: 1.28x faster                                                           |
| go                       | 146 ms                                                          | 116 ms: 1.25x faster                                                            |
| chaos                    | 74.4 ms                                                         | 60.0 ms: 1.24x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                                           |
| pyflate                  | 422 ms                                                          | 358 ms: 1.18x faster                                                            |
| mako                     | 9.10 ms                                                         | 7.78 ms: 1.17x faster                                                           |
| scimark_sor              | 115 ms                                                          | 98.4 ms: 1.17x faster                                                           |
| thrift                   | 902 us                                                          | 777 us: 1.16x faster                                                            |
| deepcopy                 | 310 us                                                          | 272 us: 1.14x faster                                                            |
| raytrace                 | 303 ms                                                          | 266 ms: 1.14x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 54.4 ms: 1.14x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| richards_super           | 49.9 ms                                                         | 45.0 ms: 1.11x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 672 ms: 1.11x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 72.5 ms: 1.11x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 53.0 ms: 1.10x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.59 ms: 1.10x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.5 ms: 1.08x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.6 ms: 1.08x faster                                                           |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.55 ms: 1.07x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 9.21 ms: 1.07x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.05 ms: 1.06x faster                                                           |
| pycparser                | 1.04 sec                                                        | 982 ms: 1.06x faster                                                            |
| sympy_sum                | 122 ms                                                          | 116 ms: 1.06x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 49.8 ms: 1.04x faster                                                           |
| comprehensions           | 17.7 us                                                         | 17.2 us: 1.03x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.19 ms: 1.02x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.31 ms: 1.02x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                          |
| json_loads               | 22.4 us                                                         | 22.7 us: 1.01x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| unpickle_list            | 2.98 us                                                         | 3.04 us: 1.02x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 17.1 ms: 1.03x slower                                                           |
| 2to3                     | 265 ms                                                          | 276 ms: 1.04x slower                                                            |
| sympy_str                | 229 ms                                                          | 238 ms: 1.04x slower                                                            |
| regex_compile            | 117 ms                                                          | 122 ms: 1.04x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.06 sec: 1.06x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.84 us: 1.06x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 93.5 ms: 1.07x slower                                                           |
| django_template          | 36.0 ms                                                         | 38.8 ms: 1.08x slower                                                           |
| sympy_expand             | 391 ms                                                          | 423 ms: 1.08x slower                                                            |
| genshi_text              | 21.0 ms                                                         | 23.2 ms: 1.11x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.8 us: 1.14x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 91.5 ms: 1.14x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 51.2 ms: 1.15x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 53.5 ms: 1.15x slower                                                           |
| xml_etree_process        | 48.1 ms                                                         | 56.0 ms: 1.16x slower                                                           |
| coverage                 | 46.6 ms                                                         | 54.2 ms: 1.17x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 21.3 ms: 1.18x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.80 us: 1.18x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 73.1 ms: 1.19x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 334 us: 1.19x slower                                                            |
| fannkuch                 | 317 ms                                                          | 379 ms: 1.19x slower                                                            |
| pickle                   | 7.83 us                                                         | 9.37 us: 1.20x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.65 sec: 1.20x slower                                                          |
| python_startup           | 22.9 ms                                                         | 27.8 ms: 1.21x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.83 us: 1.21x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.60 us: 1.21x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 801 ms: 1.22x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 49.9 ns: 1.25x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 244 us: 1.29x slower                                                            |
| scimark_fft              | 216 ms                                                          | 279 ms: 1.29x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 89.6 ms: 1.35x slower                                                           |
| async_generators         | 241 ms                                                          | 338 ms: 1.40x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.83 ms: 1.43x slower                                                           |
| nbody                    | 79.1 ms                                                         | 113 ms: 1.43x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.04 ms: 1.49x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.81 ms: 1.62x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (5): json, richards, crypto_pyaes, sqlglot_transpile, asyncio_tcp_ssl
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 92.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown