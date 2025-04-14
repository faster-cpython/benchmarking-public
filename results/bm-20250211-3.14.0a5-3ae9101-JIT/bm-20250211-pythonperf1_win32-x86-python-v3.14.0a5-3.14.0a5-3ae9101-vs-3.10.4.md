# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a5
- machine: windows-x86
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.075x faster
- HPT reliability: 87.35%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 269 ms: 1.01x slower                                                |
| docutils       | 1.95 sec                                                        | 2.03 sec: 1.04x slower                                              |
| html5lib       | 52.1 ms                                                         | 49.0 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                           | 1.00x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 489 ms: 1.92x faster                                                |
| async_tree_cpu_io_mixed | 922 ms                                                          | 506 ms: 1.82x faster                                                |
| async_tree_none         | 394 ms                                                          | 233 ms: 1.69x faster                                                |
| async_tree_memoization  | 467 ms                                                          | 285 ms: 1.64x faster                                                |
| Geometric mean          | (ref)                                                           | 1.76x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                |
| float          | 69.6 ms                                                         | 53.9 ms: 1.29x faster                                               |
| nbody          | 79.1 ms                                                         | 110 ms: 1.39x slower                                                |
| Geometric mean | (ref)                                                           | 1.32x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                |
| regex_effbot   | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                               |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                               |
| regex_compile  | 117 ms                                                          | 119 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                           | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                |
| json_dumps           | 9.82 ms                                                         | 9.18 ms: 1.07x faster                                               |
| tomli_loads          | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                              |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.8 ms: 1.03x faster                                               |
| json_loads           | 22.4 us                                                         | 22.8 us: 1.02x slower                                               |
| xml_etree_process    | 48.1 ms                                                         | 55.9 ms: 1.16x slower                                               |
| pickle_pure_python   | 280 us                                                          | 327 us: 1.17x slower                                                |
| unpickle_pure_python | 189 us                                                          | 227 us: 1.20x slower                                                |
| xml_etree_generate   | 61.6 ms                                                         | 75.0 ms: 1.22x slower                                               |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 21.6 ms: 1.20x slower                                               |
| python_startup         | 22.9 ms                                                         | 28.1 ms: 1.23x slower                                               |
| Geometric mean         | (ref)                                                           | 1.21x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.91 ms: 1.15x faster                                               |
| django_template | 36.0 ms                                                         | 36.8 ms: 1.02x slower                                               |
| genshi_xml      | 46.6 ms                                                         | 50.7 ms: 1.09x slower                                               |
| genshi_text     | 21.0 ms                                                         | 24.3 ms: 1.16x slower                                               |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                |
| pathlib                  | 81.2 ms                                                         | 35.0 ms: 2.32x faster                                               |
| typing_runtime_protocols | 396 us                                                          | 171 us: 2.31x faster                                                |
| sqlglot_normalize        | 230 ms                                                          | 108 ms: 2.14x faster                                                |
| async_tree_io            | 940 ms                                                          | 489 ms: 1.92x faster                                                |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 506 ms: 1.82x faster                                                |
| async_tree_none          | 394 ms                                                          | 233 ms: 1.69x faster                                                |
| pylint                   | 384 ms                                                          | 232 ms: 1.66x faster                                                |
| async_tree_memoization   | 467 ms                                                          | 285 ms: 1.64x faster                                                |
| deltablue                | 4.04 ms                                                         | 2.89 ms: 1.40x faster                                               |
| deepcopy_memo            | 29.6 us                                                         | 21.3 us: 1.39x faster                                               |
| logging_silent           | 97.9 ns                                                         | 72.0 ns: 1.36x faster                                               |
| generators               | 31.6 ms                                                         | 23.3 ms: 1.36x faster                                               |
| scimark_lu               | 89.8 ms                                                         | 68.6 ms: 1.31x faster                                               |
| float                    | 69.6 ms                                                         | 53.9 ms: 1.29x faster                                               |
| go                       | 146 ms                                                          | 117 ms: 1.25x faster                                                |
| spectral_norm            | 80.2 ms                                                         | 65.5 ms: 1.22x faster                                               |
| sqlite_synth             | 2.29 us                                                         | 1.88 us: 1.22x faster                                               |
| chaos                    | 74.4 ms                                                         | 61.3 ms: 1.21x faster                                               |
| pyflate                  | 422 ms                                                          | 348 ms: 1.21x faster                                                |
| deepcopy                 | 310 us                                                          | 258 us: 1.20x faster                                                |
| thrift                   | 902 us                                                          | 768 us: 1.17x faster                                                |
| scimark_monte_carlo      | 61.9 ms                                                         | 52.8 ms: 1.17x faster                                               |
| mako                     | 9.10 ms                                                         | 7.91 ms: 1.15x faster                                               |
| coroutines               | 17.9 ms                                                         | 15.8 ms: 1.13x faster                                               |
| raytrace                 | 303 ms                                                          | 268 ms: 1.13x faster                                                |
| scimark_sor              | 115 ms                                                          | 103 ms: 1.12x faster                                                |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                |
| dulwich_log              | 58.5 ms                                                         | 52.8 ms: 1.11x faster                                               |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                |
| sqlglot_parse            | 1.33 ms                                                         | 1.21 ms: 1.10x faster                                               |
| regex_effbot             | 1.66 ms                                                         | 1.54 ms: 1.08x faster                                               |
| pycparser                | 1.04 sec                                                        | 974 ms: 1.07x faster                                                |
| json_dumps               | 9.82 ms                                                         | 9.18 ms: 1.07x faster                                               |
| sqlglot_transpile        | 1.58 ms                                                         | 1.49 ms: 1.06x faster                                               |
| html5lib                 | 52.1 ms                                                         | 49.0 ms: 1.06x faster                                               |
| richards_super           | 49.9 ms                                                         | 47.0 ms: 1.06x faster                                               |
| crypto_pyaes             | 81.3 ms                                                         | 76.8 ms: 1.06x faster                                               |
| comprehensions           | 17.7 us                                                         | 16.9 us: 1.05x faster                                               |
| sympy_sum                | 122 ms                                                          | 117 ms: 1.05x faster                                                |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.12 ms: 1.04x faster                                               |
| tomli_loads              | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                              |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.8 ms: 1.03x faster                                               |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                               |
| 2to3                     | 265 ms                                                          | 269 ms: 1.01x slower                                                |
| json_loads               | 22.4 us                                                         | 22.8 us: 1.02x slower                                               |
| regex_compile            | 117 ms                                                          | 119 ms: 1.02x slower                                                |
| deepcopy_reduce          | 2.68 us                                                         | 2.74 us: 1.02x slower                                               |
| hexiom                   | 6.13 ms                                                         | 6.27 ms: 1.02x slower                                               |
| django_template          | 36.0 ms                                                         | 36.8 ms: 1.02x slower                                               |
| mdp                      | 1.83 sec                                                        | 1.87 sec: 1.02x slower                                              |
| richards                 | 40.3 ms                                                         | 41.3 ms: 1.03x slower                                               |
| sympy_integrate          | 16.6 ms                                                         | 17.2 ms: 1.04x slower                                               |
| sympy_str                | 229 ms                                                          | 238 ms: 1.04x slower                                                |
| docutils                 | 1.95 sec                                                        | 2.03 sec: 1.04x slower                                              |
| sympy_expand             | 391 ms                                                          | 422 ms: 1.08x slower                                                |
| genshi_xml               | 46.6 ms                                                         | 50.7 ms: 1.09x slower                                               |
| logging_simple           | 7.29 us                                                         | 8.39 us: 1.15x slower                                               |
| genshi_text              | 21.0 ms                                                         | 24.3 ms: 1.16x slower                                               |
| sqlglot_optimize         | 44.7 ms                                                         | 51.8 ms: 1.16x slower                                               |
| xml_etree_process        | 48.1 ms                                                         | 55.9 ms: 1.16x slower                                               |
| meteor_contest           | 80.0 ms                                                         | 93.2 ms: 1.16x slower                                               |
| pprint_pformat           | 1.37 sec                                                        | 1.60 sec: 1.17x slower                                              |
| pickle_pure_python       | 280 us                                                          | 327 us: 1.17x slower                                                |
| logging_format           | 7.91 us                                                         | 9.24 us: 1.17x slower                                               |
| pprint_safe_repr         | 658 ms                                                          | 776 ms: 1.18x slower                                                |
| scimark_fft              | 216 ms                                                          | 257 ms: 1.19x slower                                                |
| nqueens                  | 87.1 ms                                                         | 104 ms: 1.20x slower                                                |
| python_startup_no_site   | 18.1 ms                                                         | 21.6 ms: 1.20x slower                                               |
| fannkuch                 | 317 ms                                                          | 380 ms: 1.20x slower                                                |
| unpickle_pure_python     | 189 us                                                          | 227 us: 1.20x slower                                                |
| coverage                 | 46.6 ms                                                         | 55.9 ms: 1.20x slower                                               |
| bench_thread_pool        | 1.12 ms                                                         | 1.35 ms: 1.21x slower                                               |
| xml_etree_generate       | 61.6 ms                                                         | 75.0 ms: 1.22x slower                                               |
| python_startup           | 22.9 ms                                                         | 28.1 ms: 1.23x slower                                               |
| bench_mp_pool            | 66.4 ms                                                         | 89.8 ms: 1.35x slower                                               |
| async_generators         | 241 ms                                                          | 334 ms: 1.38x slower                                                |
| nbody                    | 79.1 ms                                                         | 110 ms: 1.39x slower                                                |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.42x slower                                               |
| create_gc_cycles         | 694 us                                                          | 1.04 ms: 1.50x slower                                               |
| telco                    | 4.83 ms                                                         | 7.55 ms: 1.56x slower                                               |
| Geometric mean           | (ref)                                                           | 1.07x faster                                                        |

Benchmark hidden because not significant (1): json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250211-3.14.0a5-3ae9101-JIT/bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.075x faster

# HPT report

- Reliability score: 87.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown