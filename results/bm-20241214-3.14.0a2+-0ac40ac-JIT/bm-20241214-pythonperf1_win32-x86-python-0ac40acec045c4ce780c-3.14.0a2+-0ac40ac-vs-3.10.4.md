# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-x86
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.063x faster
- HPT reliability: 87.66%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 260 ms: 1.02x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.92 sec: 1.02x faster                                                          |
| html5lib       | 52.1 ms                                                         | 49.7 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 473 ms: 1.95x faster                                                            |
| async_tree_io           | 940 ms                                                          | 483 ms: 1.95x faster                                                            |
| async_tree_none         | 394 ms                                                          | 227 ms: 1.73x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 279 ms: 1.68x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.82x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| float          | 69.6 ms                                                         | 56.2 ms: 1.24x faster                                                           |
| nbody          | 79.1 ms                                                         | 104 ms: 1.32x slower                                                            |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 111 ms: 1.17x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                           |
| regex_compile  | 117 ms                                                          | 114 ms: 1.03x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.4 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 9.05 ms: 1.09x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.4 ms: 1.07x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 296 us: 1.06x slower                                                            |
| unpickle_pure_python | 189 us                                                          | 207 us: 1.09x slower                                                            |
| xml_etree_process    | 48.1 ms                                                         | 53.0 ms: 1.10x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 71.0 ms: 1.15x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                           |
| python_startup         | 22.9 ms                                                         | 25.9 ms: 1.13x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.36 ms: 1.24x faster                                                           |
| django_template | 36.0 ms                                                         | 37.3 ms: 1.03x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 56.4 ms: 1.21x slower                                                           |
| genshi_text     | 21.0 ms                                                         | 26.4 ms: 1.26x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 160 us: 2.47x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 106 ms: 2.17x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 473 ms: 1.95x faster                                                            |
| async_tree_io            | 940 ms                                                          | 483 ms: 1.95x faster                                                            |
| async_tree_none          | 394 ms                                                          | 227 ms: 1.73x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 279 ms: 1.68x faster                                                            |
| pylint                   | 384 ms                                                          | 231 ms: 1.66x faster                                                            |
| deltablue                | 4.04 ms                                                         | 3.16 ms: 1.28x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 23.4 us: 1.26x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 78.4 ns: 1.25x faster                                                           |
| float                    | 69.6 ms                                                         | 56.2 ms: 1.24x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.36 ms: 1.24x faster                                                           |
| go                       | 146 ms                                                          | 121 ms: 1.20x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 67.6 ms: 1.20x faster                                                           |
| scimark_sor              | 115 ms                                                          | 96.6 ms: 1.19x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.18x faster                                                           |
| regex_dna                | 131 ms                                                          | 111 ms: 1.17x faster                                                            |
| chaos                    | 74.4 ms                                                         | 63.6 ms: 1.17x faster                                                           |
| thrift                   | 902 us                                                          | 777 us: 1.16x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.15 ms: 1.15x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 50.8 ms: 1.15x faster                                                           |
| deepcopy                 | 310 us                                                          | 271 us: 1.15x faster                                                            |
| pycparser                | 1.04 sec                                                        | 912 ms: 1.14x faster                                                            |
| scimark_lu               | 89.8 ms                                                         | 78.8 ms: 1.14x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.43 ms: 1.11x faster                                                           |
| pyflate                  | 422 ms                                                          | 384 ms: 1.10x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.75 sec: 1.09x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 9.05 ms: 1.09x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.04 ms: 1.08x faster                                                           |
| json                     | 4.76 ms                                                         | 4.44 ms: 1.07x faster                                                           |
| sympy_sum                | 122 ms                                                          | 114 ms: 1.07x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.4 ms: 1.07x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 75.4 ms: 1.06x faster                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                           |
| richards_super           | 49.9 ms                                                         | 47.6 ms: 1.05x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 49.7 ms: 1.05x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.2 ms: 1.04x faster                                                           |
| regex_compile            | 117 ms                                                          | 114 ms: 1.03x faster                                                            |
| regex_v8                 | 15.8 ms                                                         | 15.4 ms: 1.02x faster                                                           |
| 2to3                     | 265 ms                                                          | 260 ms: 1.02x faster                                                            |
| raytrace                 | 303 ms                                                          | 297 ms: 1.02x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.92 sec: 1.02x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.22 ms: 1.01x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.84 sec: 1.01x slower                                                          |
| sympy_str                | 229 ms                                                          | 233 ms: 1.02x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 83.2 ms: 1.02x slower                                                           |
| sympy_expand             | 391 ms                                                          | 404 ms: 1.03x slower                                                            |
| comprehensions           | 17.7 us                                                         | 18.3 us: 1.03x slower                                                           |
| django_template          | 36.0 ms                                                         | 37.3 ms: 1.03x slower                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 64.1 ms: 1.03x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.79 us: 1.04x slower                                                           |
| richards                 | 40.3 ms                                                         | 42.0 ms: 1.04x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 17.4 ms: 1.05x slower                                                           |
| pickle_pure_python       | 280 us                                                          | 296 us: 1.06x slower                                                            |
| fannkuch                 | 317 ms                                                          | 338 ms: 1.06x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                           |
| unpickle_pure_python     | 189 us                                                          | 207 us: 1.09x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 53.0 ms: 1.10x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.51 sec: 1.11x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 89.3 ms: 1.12x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 97.4 ms: 1.12x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 740 ms: 1.12x slower                                                            |
| python_startup           | 22.9 ms                                                         | 25.9 ms: 1.13x slower                                                           |
| scimark_fft              | 216 ms                                                          | 244 ms: 1.13x slower                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 51.0 ms: 1.14x slower                                                           |
| generators               | 31.6 ms                                                         | 36.1 ms: 1.15x slower                                                           |
| logging_format           | 7.91 us                                                         | 9.07 us: 1.15x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 71.0 ms: 1.15x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.40 us: 1.15x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.8 ms: 1.16x slower                                                           |
| hexiom                   | 6.13 ms                                                         | 7.14 ms: 1.16x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 56.4 ms: 1.21x slower                                                           |
| mypy2                    | 590 ms                                                          | 726 ms: 1.23x slower                                                            |
| genshi_text              | 21.0 ms                                                         | 26.4 ms: 1.26x slower                                                           |
| async_generators         | 241 ms                                                          | 307 ms: 1.27x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 87.3 ms: 1.31x slower                                                           |
| nbody                    | 79.1 ms                                                         | 104 ms: 1.32x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.81 ms: 1.41x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.24 ms: 1.50x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.51x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.06x faster                                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 87.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown