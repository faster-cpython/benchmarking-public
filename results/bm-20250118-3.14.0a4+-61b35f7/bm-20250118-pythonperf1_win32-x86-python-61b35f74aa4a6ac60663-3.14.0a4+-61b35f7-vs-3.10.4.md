# Results vs. 3.10.4

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-x86
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.025x faster
- HPT reliability: 91.42%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 282 ms: 1.06x slower                                                            |
| docutils       | 1.95 sec                                                        | 2.06 sec: 1.06x slower                                                          |
| html5lib       | 52.1 ms                                                         | 52.8 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 468 ms: 1.97x faster                                                            |
| async_tree_io           | 940 ms                                                          | 490 ms: 1.92x faster                                                            |
| async_tree_none         | 394 ms                                                          | 228 ms: 1.73x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.82x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| float          | 69.6 ms                                                         | 66.7 ms: 1.04x faster                                                           |
| nbody          | 79.1 ms                                                         | 119 ms: 1.50x slower                                                            |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.6 ms: 1.05x slower                                                           |
| regex_compile  | 117 ms                                                          | 127 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.11x faster                                                            |
| json_loads           | 22.4 us                                                         | 22.0 us: 1.02x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 9.68 ms: 1.02x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 71.4 ms: 1.01x slower                                                           |
| unpickle_list        | 2.98 us                                                         | 3.02 us: 1.01x slower                                                           |
| tomli_loads          | 1.91 sec                                                        | 2.02 sec: 1.06x slower                                                          |
| pickle_pure_python   | 280 us                                                          | 305 us: 1.09x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 212 us: 1.12x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 54.8 ms: 1.14x slower                                                           |
| unpickle             | 9.82 us                                                         | 11.2 us: 1.14x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 21.0 us: 1.15x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.74 us: 1.16x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 73.6 ms: 1.19x slower                                                           |
| pickle               | 7.83 us                                                         | 9.51 us: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.9 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.96 ms: 1.02x faster                                                           |
| django_template | 36.0 ms                                                         | 37.7 ms: 1.05x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 54.0 ms: 1.16x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 25.0 ms: 1.19x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.09x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 165 us: 2.39x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 103 ms: 2.23x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 468 ms: 1.97x faster                                                            |
| async_tree_io            | 940 ms                                                          | 490 ms: 1.92x faster                                                            |
| async_tree_none          | 394 ms                                                          | 228 ms: 1.73x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                            |
| pylint                   | 384 ms                                                          | 256 ms: 1.50x faster                                                            |
| deltablue                | 4.04 ms                                                         | 3.25 ms: 1.24x faster                                                           |
| go                       | 146 ms                                                          | 122 ms: 1.19x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 68.7 ms: 1.18x faster                                                           |
| chaos                    | 74.4 ms                                                         | 64.3 ms: 1.16x faster                                                           |
| thrift                   | 902 us                                                          | 783 us: 1.15x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 2.04 us: 1.13x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 26.3 us: 1.12x faster                                                           |
| deepcopy                 | 310 us                                                          | 276 us: 1.12x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.11x faster                                                            |
| pyflate                  | 422 ms                                                          | 385 ms: 1.09x faster                                                            |
| comprehensions           | 17.7 us                                                         | 16.5 us: 1.07x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 83.9 ms: 1.07x faster                                                           |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                           |
| raytrace                 | 303 ms                                                          | 289 ms: 1.05x faster                                                            |
| float                    | 69.6 ms                                                         | 66.7 ms: 1.04x faster                                                           |
| pycparser                | 1.04 sec                                                        | 1.00 sec: 1.04x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.28 ms: 1.04x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.08 ms: 1.03x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 57.0 ms: 1.03x faster                                                           |
| richards_super           | 49.9 ms                                                         | 48.6 ms: 1.03x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 95.4 ns: 1.03x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.96 ms: 1.02x faster                                                           |
| json_loads               | 22.4 us                                                         | 22.0 us: 1.02x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.68 ms: 1.02x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 71.4 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.01x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.02 us: 1.01x slower                                                           |
| html5lib                 | 52.1 ms                                                         | 52.8 ms: 1.01x slower                                                           |
| sympy_sum                | 122 ms                                                          | 125 ms: 1.02x slower                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 63.3 ms: 1.02x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 6.28 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.33 ms: 1.03x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 89.8 ms: 1.03x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 83.2 ms: 1.04x slower                                                           |
| scimark_sor              | 115 ms                                                          | 120 ms: 1.04x slower                                                            |
| django_template          | 36.0 ms                                                         | 37.7 ms: 1.05x slower                                                           |
| spectral_norm            | 80.2 ms                                                         | 84.5 ms: 1.05x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.6 ms: 1.05x slower                                                           |
| tomli_loads              | 1.91 sec                                                        | 2.02 sec: 1.06x slower                                                          |
| docutils                 | 1.95 sec                                                        | 2.06 sec: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 86.2 ms: 1.06x slower                                                           |
| 2to3                     | 265 ms                                                          | 282 ms: 1.06x slower                                                            |
| generators               | 31.6 ms                                                         | 33.6 ms: 1.06x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.87 us: 1.07x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 17.9 ms: 1.07x slower                                                           |
| richards                 | 40.3 ms                                                         | 43.3 ms: 1.08x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.49 sec: 1.09x slower                                                          |
| sympy_str                | 229 ms                                                          | 249 ms: 1.09x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 305 us: 1.09x slower                                                            |
| regex_compile            | 117 ms                                                          | 127 ms: 1.09x slower                                                            |
| asyncio_tcp              | 744 ms                                                          | 811 ms: 1.09x slower                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 48.9 ms: 1.09x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 722 ms: 1.10x slower                                                            |
| sympy_expand             | 391 ms                                                          | 434 ms: 1.11x slower                                                            |
| unpickle_pure_python     | 189 us                                                          | 212 us: 1.12x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                           |
| fannkuch                 | 317 ms                                                          | 358 ms: 1.13x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 54.8 ms: 1.14x slower                                                           |
| unpickle                 | 9.82 us                                                         | 11.2 us: 1.14x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 21.0 us: 1.15x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.8 ms: 1.16x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 54.0 ms: 1.16x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.74 us: 1.16x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.9 ms: 1.17x slower                                                           |
| coroutines               | 17.9 ms                                                         | 21.2 ms: 1.18x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 25.0 ms: 1.19x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 73.6 ms: 1.19x slower                                                           |
| pickle                   | 7.83 us                                                         | 9.51 us: 1.21x slower                                                           |
| scimark_fft              | 216 ms                                                          | 264 ms: 1.22x slower                                                            |
| logging_format           | 7.91 us                                                         | 9.77 us: 1.24x slower                                                           |
| logging_simple           | 7.29 us                                                         | 9.09 us: 1.25x slower                                                           |
| async_generators         | 241 ms                                                          | 323 ms: 1.34x slower                                                            |
| unpack_sequence          | 40.0 ns                                                         | 54.5 ns: 1.36x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.80 ms: 1.40x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 96.8 ms: 1.46x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.21 ms: 1.49x slower                                                           |
| nbody                    | 79.1 ms                                                         | 119 ms: 1.50x slower                                                            |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.52x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): json, mdp
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 91.42% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown