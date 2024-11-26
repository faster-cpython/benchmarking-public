# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-x86
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.039x faster
- HPT reliability: 52.28%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 293 ms: 1.10x slower                                                            |
| docutils       | 1.95 sec                                                        | 2.14 sec: 1.10x slower                                                          |
| html5lib       | 52.1 ms                                                         | 50.0 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 492 ms: 1.87x faster                                                            |
| async_tree_io           | 940 ms                                                          | 567 ms: 1.66x faster                                                            |
| async_tree_none         | 394 ms                                                          | 242 ms: 1.63x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 296 ms: 1.57x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.68x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 207 ms: 2.43x faster                                                            |
| float          | 69.6 ms                                                         | 56.3 ms: 1.24x faster                                                           |
| nbody          | 79.1 ms                                                         | 93.1 ms: 1.18x slower                                                           |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 115 ms: 1.13x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.7 ms: 1.01x faster                                                           |
| regex_compile  | 117 ms                                                          | 122 ms: 1.05x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.82 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps          | 9.82 ms                                                         | 8.98 ms: 1.09x faster                                                           |
| xml_etree_parse     | 120 ms                                                          | 111 ms: 1.08x faster                                                            |
| json_loads          | 22.4 us                                                         | 21.3 us: 1.05x faster                                                           |
| xml_etree_iterparse | 70.8 ms                                                         | 68.6 ms: 1.03x faster                                                           |
| tomli_loads         | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                          |
| pickle_pure_python  | 280 us                                                          | 306 us: 1.09x slower                                                            |
| xml_etree_process   | 48.1 ms                                                         | 54.0 ms: 1.12x slower                                                           |
| xml_etree_generate  | 61.6 ms                                                         | 72.0 ms: 1.17x slower                                                           |
| Geometric mean      | (ref)                                                           | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.2 ms: 1.14x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 9.10 ms                                                         | 7.39 ms: 1.23x faster                                                           |
| genshi_text    | 21.0 ms                                                         | 26.1 ms: 1.25x slower                                                           |
| genshi_xml     | 46.6 ms                                                         | 58.2 ms: 1.25x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 207 ms: 2.43x faster                                                            |
| typing_runtime_protocols | 396 us                                                          | 168 us: 2.36x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 113 ms: 2.04x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 492 ms: 1.87x faster                                                            |
| async_tree_io            | 940 ms                                                          | 567 ms: 1.66x faster                                                            |
| async_tree_none          | 394 ms                                                          | 242 ms: 1.63x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 296 ms: 1.57x faster                                                            |
| pylint                   | 384 ms                                                          | 278 ms: 1.38x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 23.2 us: 1.28x faster                                                           |
| deltablue                | 4.04 ms                                                         | 3.24 ms: 1.25x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 79.0 ns: 1.24x faster                                                           |
| float                    | 69.6 ms                                                         | 56.3 ms: 1.24x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.39 ms: 1.23x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 74.1 ms: 1.21x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 67.3 ms: 1.21x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.95 us: 1.18x faster                                                           |
| go                       | 146 ms                                                          | 125 ms: 1.17x faster                                                            |
| scimark_sor              | 115 ms                                                          | 99.1 ms: 1.16x faster                                                           |
| chaos                    | 74.4 ms                                                         | 64.2 ms: 1.16x faster                                                           |
| thrift                   | 902 us                                                          | 782 us: 1.15x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 51.1 ms: 1.14x faster                                                           |
| deepcopy                 | 310 us                                                          | 272 us: 1.14x faster                                                            |
| regex_dna                | 131 ms                                                          | 115 ms: 1.13x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.18 ms: 1.13x faster                                                           |
| pycparser                | 1.04 sec                                                        | 944 ms: 1.10x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 8.98 ms: 1.09x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 111 ms: 1.08x faster                                                            |
| json                     | 4.76 ms                                                         | 4.50 ms: 1.06x faster                                                           |
| pyflate                  | 422 ms                                                          | 400 ms: 1.05x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 1.06 ms: 1.05x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.3 us: 1.05x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.52 ms: 1.04x faster                                                           |
| raytrace                 | 303 ms                                                          | 291 ms: 1.04x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 50.0 ms: 1.04x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.6 ms: 1.03x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.4 ms: 1.03x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 78.6 ms: 1.02x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.7 ms: 1.01x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.72 us: 1.01x slower                                                           |
| mdp                      | 1.83 sec                                                        | 1.86 sec: 1.02x slower                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 63.7 ms: 1.03x slower                                                           |
| sympy_sum                | 122 ms                                                          | 126 ms: 1.03x slower                                                            |
| comprehensions           | 17.7 us                                                         | 18.3 us: 1.03x slower                                                           |
| regex_compile            | 117 ms                                                          | 122 ms: 1.05x slower                                                            |
| fannkuch                 | 317 ms                                                          | 332 ms: 1.05x slower                                                            |
| richards                 | 40.3 ms                                                         | 42.8 ms: 1.06x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 87.1 ms: 1.07x slower                                                           |
| sympy_expand             | 391 ms                                                          | 420 ms: 1.07x slower                                                            |
| sympy_str                | 229 ms                                                          | 249 ms: 1.09x slower                                                            |
| pickle_pure_python       | 280 us                                                          | 306 us: 1.09x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.82 ms: 1.09x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.50 sec: 1.10x slower                                                          |
| docutils                 | 1.95 sec                                                        | 2.14 sec: 1.10x slower                                                          |
| 2to3                     | 265 ms                                                          | 293 ms: 1.10x slower                                                            |
| meteor_contest           | 80.0 ms                                                         | 88.4 ms: 1.10x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 738 ms: 1.12x slower                                                            |
| xml_etree_process        | 48.1 ms                                                         | 54.0 ms: 1.12x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.93 us: 1.13x slower                                                           |
| nqueens                  | 87.1 ms                                                         | 98.5 ms: 1.13x slower                                                           |
| logging_simple           | 7.29 us                                                         | 8.27 us: 1.13x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.1 ms: 1.14x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.2 ms: 1.14x slower                                                           |
| generators               | 31.6 ms                                                         | 36.3 ms: 1.15x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 72.0 ms: 1.17x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 19.4 ms: 1.17x slower                                                           |
| nbody                    | 79.1 ms                                                         | 93.1 ms: 1.18x slower                                                           |
| scimark_fft              | 216 ms                                                          | 257 ms: 1.19x slower                                                            |
| hexiom                   | 6.13 ms                                                         | 7.33 ms: 1.20x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 26.1 ms: 1.25x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 58.2 ms: 1.25x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 57.2 ms: 1.28x slower                                                           |
| async_generators         | 241 ms                                                          | 323 ms: 1.34x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 94.4 ms: 1.42x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.14 ms: 1.48x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.18 ms: 1.70x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (4): django_template, unpickle_pure_python, scimark_sparse_mat_mult, richards_super
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1_win32-x86-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.039x faster
# HPT report

- Reliability score: 52.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown