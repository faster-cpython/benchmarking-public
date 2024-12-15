# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-x86
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.160x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 240 ms: 1.11x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                                          |
| html5lib       | 52.1 ms                                                         | 45.3 ms: 1.15x faster                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 433 ms: 2.17x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 442 ms: 2.09x faster                                                            |
| async_tree_none         | 394 ms                                                          | 199 ms: 1.98x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 246 ms: 1.89x faster                                                            |
| Geometric mean          | (ref)                                                           | 2.03x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| float          | 69.6 ms                                                         | 58.2 ms: 1.20x faster                                                           |
| nbody          | 79.1 ms                                                         | 86.0 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 103 ms: 1.13x faster                                                            |
| regex_dna      | 131 ms                                                          | 126 ms: 1.04x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.65 ms: 1.01x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 189 us                                                          | 167 us: 1.14x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.68 sec: 1.13x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 8.69 ms: 1.13x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.4 us: 1.10x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.6 ms: 1.06x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 274 us: 1.02x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 47.6 ms: 1.01x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 67.1 ms: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                           |
| python_startup         | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.61 ms: 1.20x faster                                                           |
| django_template | 36.0 ms                                                         | 31.6 ms: 1.14x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 45.2 ms: 1.03x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 20.7 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 139 us: 2.84x faster                                                            |
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| async_tree_io            | 940 ms                                                          | 433 ms: 2.17x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 442 ms: 2.09x faster                                                            |
| async_tree_none          | 394 ms                                                          | 199 ms: 1.98x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 246 ms: 1.89x faster                                                            |
| pylint                   | 384 ms                                                          | 217 ms: 1.77x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.57 ms: 1.57x faster                                                           |
| go                       | 146 ms                                                          | 94.8 ms: 1.54x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 20.7 us: 1.43x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 70.2 ns: 1.39x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 58.8 ms: 1.38x faster                                                           |
| chaos                    | 74.4 ms                                                         | 54.1 ms: 1.37x faster                                                           |
| deepcopy                 | 310 us                                                          | 229 us: 1.35x faster                                                            |
| generators               | 31.6 ms                                                         | 23.7 ms: 1.33x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 67.6 ms: 1.33x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.4 us: 1.33x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.74 ms: 1.29x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.28x faster                                                           |
| raytrace                 | 303 ms                                                          | 241 ms: 1.26x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.28 ms: 1.24x faster                                                           |
| pycparser                | 1.04 sec                                                        | 840 ms: 1.24x faster                                                            |
| pyflate                  | 422 ms                                                          | 345 ms: 1.22x faster                                                            |
| scimark_sor              | 115 ms                                                          | 95.1 ms: 1.21x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.61 ms: 1.20x faster                                                           |
| float                    | 69.6 ms                                                         | 58.2 ms: 1.20x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 52.1 ms: 1.19x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                           |
| thrift                   | 902 us                                                          | 767 us: 1.18x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 68.4 ms: 1.17x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 50.0 ms: 1.17x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 74.9 ms: 1.16x faster                                                           |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.16x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 45.3 ms: 1.15x faster                                                           |
| json                     | 4.76 ms                                                         | 4.15 ms: 1.15x faster                                                           |
| django_template          | 36.0 ms                                                         | 31.6 ms: 1.14x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 167 us: 1.14x faster                                                            |
| richards_super           | 49.9 ms                                                         | 43.9 ms: 1.14x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.68 sec: 1.13x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 8.69 ms: 1.13x faster                                                           |
| regex_compile            | 117 ms                                                          | 103 ms: 1.13x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 995 us: 1.13x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.90 ms: 1.12x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.40 us: 1.12x faster                                                           |
| 2to3                     | 265 ms                                                          | 240 ms: 1.11x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.4 us: 1.10x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.1 ms: 1.10x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.5 ms: 1.09x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 41.3 ms: 1.08x faster                                                           |
| sympy_str                | 229 ms                                                          | 212 ms: 1.08x faster                                                            |
| fannkuch                 | 317 ms                                                          | 295 ms: 1.08x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 216 ms: 1.07x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.6 ms: 1.06x faster                                                           |
| sympy_expand             | 391 ms                                                          | 374 ms: 1.04x faster                                                            |
| regex_dna                | 131 ms                                                          | 126 ms: 1.04x faster                                                            |
| richards                 | 40.3 ms                                                         | 38.8 ms: 1.04x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 636 ms: 1.03x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 45.2 ms: 1.03x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 274 us: 1.02x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 20.7 ms: 1.01x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 47.6 ms: 1.01x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.65 ms: 1.01x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 79.6 ms: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.8 ms: 1.00x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 82.6 ms: 1.02x slower                                                           |
| scimark_fft              | 216 ms                                                          | 227 ms: 1.05x slower                                                            |
| logging_simple           | 7.29 us                                                         | 7.71 us: 1.06x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.46 us: 1.07x slower                                                           |
| nbody                    | 79.1 ms                                                         | 86.0 ms: 1.09x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 67.1 ms: 1.09x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                           |
| coverage                 | 46.6 ms                                                         | 52.5 ms: 1.13x slower                                                           |
| mypy2                    | 590 ms                                                          | 681 ms: 1.15x slower                                                            |
| python_startup           | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                           |
| async_generators         | 241 ms                                                          | 287 ms: 1.19x slower                                                            |
| telco                    | 4.83 ms                                                         | 6.51 ms: 1.35x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 93.0 ms: 1.40x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.52x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.160x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown