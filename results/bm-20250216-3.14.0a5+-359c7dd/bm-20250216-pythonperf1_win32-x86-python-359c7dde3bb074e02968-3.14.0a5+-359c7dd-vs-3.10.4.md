# Results vs. 3.10.4

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-x86
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.099x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 263 ms: 1.01x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.89 sec: 1.03x faster                                                          |
| html5lib       | 52.1 ms                                                         | 48.4 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 502 ms: 1.88x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 503 ms: 1.84x faster                                                            |
| async_tree_none         | 394 ms                                                          | 235 ms: 1.68x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 284 ms: 1.64x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.75x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| float          | 69.6 ms                                                         | 58.2 ms: 1.20x faster                                                           |
| nbody          | 79.1 ms                                                         | 88.2 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                           | 1.39x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.60 ms: 1.04x faster                                                           |
| regex_compile  | 117 ms                                                          | 113 ms: 1.03x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.13x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.1 ms: 1.06x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 9.33 ms: 1.05x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 3.01 us: 1.01x slower                                                           |
| json_loads           | 22.4 us                                                         | 22.8 us: 1.02x slower                                                           |
| unpickle_pure_python | 189 us                                                          | 193 us: 1.02x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 51.9 ms: 1.08x slower                                                           |
| pickle_pure_python   | 280 us                                                          | 305 us: 1.09x slower                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 69.3 ms: 1.12x slower                                                           |
| unpickle             | 9.82 us                                                         | 11.2 us: 1.14x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.9 us: 1.15x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.71 us: 1.15x slower                                                           |
| pickle               | 7.83 us                                                         | 9.27 us: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 21.4 ms: 1.19x slower                                                           |
| python_startup         | 22.9 ms                                                         | 27.7 ms: 1.21x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.20x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.48 ms: 1.07x faster                                                           |
| django_template | 36.0 ms                                                         | 37.1 ms: 1.03x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 23.1 ms: 1.10x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 52.3 ms: 1.12x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 160 us: 2.47x faster                                                            |
| pathlib                  | 81.2 ms                                                         | 34.6 ms: 2.35x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 103 ms: 2.23x faster                                                            |
| async_tree_io            | 940 ms                                                          | 502 ms: 1.88x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 503 ms: 1.84x faster                                                            |
| pylint                   | 384 ms                                                          | 228 ms: 1.68x faster                                                            |
| async_tree_none          | 394 ms                                                          | 235 ms: 1.68x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 284 ms: 1.64x faster                                                            |
| deltablue                | 4.04 ms                                                         | 3.05 ms: 1.33x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 61.7 ms: 1.32x faster                                                           |
| go                       | 146 ms                                                          | 112 ms: 1.30x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 22.8 us: 1.30x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.3 us: 1.24x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 72.5 ms: 1.24x faster                                                           |
| chaos                    | 74.4 ms                                                         | 60.4 ms: 1.23x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 80.3 ns: 1.22x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 620 ms: 1.20x faster                                                            |
| float                    | 69.6 ms                                                         | 58.2 ms: 1.20x faster                                                           |
| deepcopy                 | 310 us                                                          | 262 us: 1.18x faster                                                            |
| pyflate                  | 422 ms                                                          | 366 ms: 1.15x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.13x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.19 ms: 1.12x faster                                                           |
| thrift                   | 902 us                                                          | 806 us: 1.12x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.4 ms: 1.12x faster                                                           |
| generators               | 31.6 ms                                                         | 28.4 ms: 1.11x faster                                                           |
| scimark_sor              | 115 ms                                                          | 104 ms: 1.11x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.92 ms: 1.11x faster                                                           |
| pycparser                | 1.04 sec                                                        | 940 ms: 1.11x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.43 ms: 1.10x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.58 ms: 1.10x faster                                                           |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 54.1 ms: 1.08x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                          |
| sympy_sum                | 122 ms                                                          | 114 ms: 1.08x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 48.4 ms: 1.08x faster                                                           |
| richards_super           | 49.9 ms                                                         | 46.4 ms: 1.08x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.48 ms: 1.07x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.05 ms: 1.06x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 81.9 ms: 1.06x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.1 ms: 1.06x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.33 ms: 1.05x faster                                                           |
| raytrace                 | 303 ms                                                          | 288 ms: 1.05x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.74 sec: 1.05x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.1 ms: 1.05x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.60 ms: 1.04x faster                                                           |
| regex_compile            | 117 ms                                                          | 113 ms: 1.03x faster                                                            |
| fannkuch                 | 317 ms                                                          | 308 ms: 1.03x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.89 sec: 1.03x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 78.6 ms: 1.02x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.4 ms: 1.01x faster                                                           |
| 2to3                     | 265 ms                                                          | 263 ms: 1.01x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 80.5 ms: 1.01x slower                                                           |
| unpickle_list            | 2.98 us                                                         | 3.01 us: 1.01x slower                                                           |
| sympy_str                | 229 ms                                                          | 232 ms: 1.01x slower                                                            |
| json_loads               | 22.4 us                                                         | 22.8 us: 1.02x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 193 us: 1.02x slower                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.74 us: 1.02x slower                                                           |
| django_template          | 36.0 ms                                                         | 37.1 ms: 1.03x slower                                                           |
| richards                 | 40.3 ms                                                         | 42.1 ms: 1.05x slower                                                           |
| sympy_expand             | 391 ms                                                          | 412 ms: 1.05x slower                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 47.1 ms: 1.05x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 42.4 ns: 1.06x slower                                                           |
| scimark_fft              | 216 ms                                                          | 230 ms: 1.06x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 51.9 ms: 1.08x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 305 us: 1.09x slower                                                            |
| pprint_safe_repr         | 658 ms                                                          | 722 ms: 1.10x slower                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.51 sec: 1.10x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 23.1 ms: 1.10x slower                                                           |
| nbody                    | 79.1 ms                                                         | 88.2 ms: 1.11x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 52.3 ms: 1.12x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 69.3 ms: 1.12x slower                                                           |
| unpickle                 | 9.82 us                                                         | 11.2 us: 1.14x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.9 us: 1.15x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.6 ms: 1.15x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.71 us: 1.15x slower                                                           |
| pickle                   | 7.83 us                                                         | 9.27 us: 1.18x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 21.4 ms: 1.19x slower                                                           |
| python_startup           | 22.9 ms                                                         | 27.7 ms: 1.21x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.73 us: 1.23x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.98 us: 1.23x slower                                                           |
| async_generators         | 241 ms                                                          | 325 ms: 1.35x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 89.7 ms: 1.35x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.80 ms: 1.41x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.90 ms: 1.43x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.08x faster                                                                    |

Benchmark hidden because not significant (2): json, asyncio_tcp_ssl
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1_win32-x86-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.099x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown