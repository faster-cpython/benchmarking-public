# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: windows-x86
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 250 ms: 1.06x faster                                            |
| chameleon      | 6.42 ms                                                         | 6.08 ms: 1.06x faster                                           |
| docutils       | 1.95 sec                                                        | 1.78 sec: 1.10x faster                                          |
| html5lib       | 52.1 ms                                                         | 47.5 ms: 1.10x faster                                           |
| tornado_http   | 118 ms                                                          | 94.1 ms: 1.25x faster                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 484 ms: 1.91x faster                                            |
| async_tree_io           | 940 ms                                                          | 526 ms: 1.79x faster                                            |
| async_tree_none         | 394 ms                                                          | 245 ms: 1.61x faster                                            |
| async_tree_memoization  | 467 ms                                                          | 297 ms: 1.57x faster                                            |
| Geometric mean          | (ref)                                                           | 1.71x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                            |
| float          | 69.6 ms                                                         | 54.6 ms: 1.27x faster                                           |
| nbody          | 79.1 ms                                                         | 80.0 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                           | 1.47x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 101 ms: 1.15x faster                                            |
| regex_dna      | 131 ms                                                          | 114 ms: 1.15x faster                                            |
| regex_effbot   | 1.66 ms                                                         | 1.80 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.30 ms: 1.35x faster                                           |
| pickle_pure_python   | 280 us                                                          | 231 us: 1.21x faster                                            |
| unpickle_pure_python | 189 us                                                          | 160 us: 1.18x faster                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.6 ms: 1.13x faster                                           |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                            |
| tomli_loads          | 1.91 sec                                                        | 1.71 sec: 1.11x faster                                          |
| xml_etree_process    | 48.1 ms                                                         | 44.2 ms: 1.09x faster                                           |
| json_loads           | 22.4 us                                                         | 21.6 us: 1.03x faster                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                    |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                           |
| python_startup         | 22.9 ms                                                         | 28.3 ms: 1.23x slower                                           |
| Geometric mean         | (ref)                                                           | 1.16x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.09 ms: 1.28x faster                                           |
| django_template | 36.0 ms                                                         | 29.8 ms: 1.21x faster                                           |
| genshi_text     | 21.0 ms                                                         | 21.5 ms: 1.02x slower                                           |
| genshi_xml      | 46.6 ms                                                         | 50.1 ms: 1.08x slower                                           |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 138 us: 2.88x faster                                            |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 484 ms: 1.91x faster                                            |
| async_tree_io            | 940 ms                                                          | 526 ms: 1.79x faster                                            |
| deltablue                | 4.04 ms                                                         | 2.33 ms: 1.73x faster                                           |
| pylint                   | 384 ms                                                          | 227 ms: 1.69x faster                                            |
| logging_silent           | 97.9 ns                                                         | 60.3 ns: 1.62x faster                                           |
| async_tree_none          | 394 ms                                                          | 245 ms: 1.61x faster                                            |
| async_tree_memoization   | 467 ms                                                          | 297 ms: 1.57x faster                                            |
| raytrace                 | 303 ms                                                          | 201 ms: 1.50x faster                                            |
| scimark_lu               | 89.8 ms                                                         | 60.2 ms: 1.49x faster                                           |
| chaos                    | 74.4 ms                                                         | 50.2 ms: 1.48x faster                                           |
| generators               | 31.6 ms                                                         | 21.8 ms: 1.45x faster                                           |
| crypto_pyaes             | 81.3 ms                                                         | 56.9 ms: 1.43x faster                                           |
| comprehensions           | 17.7 us                                                         | 12.5 us: 1.42x faster                                           |
| hexiom                   | 6.13 ms                                                         | 4.44 ms: 1.38x faster                                           |
| richards_super           | 49.9 ms                                                         | 36.7 ms: 1.36x faster                                           |
| json_dumps               | 9.82 ms                                                         | 7.30 ms: 1.35x faster                                           |
| scimark_sor              | 115 ms                                                          | 85.9 ms: 1.34x faster                                           |
| go                       | 146 ms                                                          | 109 ms: 1.34x faster                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.00 ms: 1.33x faster                                           |
| pyflate                  | 422 ms                                                          | 320 ms: 1.32x faster                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 47.7 ms: 1.30x faster                                           |
| mako                     | 9.10 ms                                                         | 7.09 ms: 1.28x faster                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.24 ms: 1.28x faster                                           |
| float                    | 69.6 ms                                                         | 54.6 ms: 1.27x faster                                           |
| tornado_http             | 118 ms                                                          | 94.1 ms: 1.25x faster                                           |
| richards                 | 40.3 ms                                                         | 32.7 ms: 1.23x faster                                           |
| pickle_pure_python       | 280 us                                                          | 231 us: 1.21x faster                                            |
| django_template          | 36.0 ms                                                         | 29.8 ms: 1.21x faster                                           |
| nqueens                  | 87.1 ms                                                         | 72.1 ms: 1.21x faster                                           |
| dulwich_log              | 58.5 ms                                                         | 48.8 ms: 1.20x faster                                           |
| pycparser                | 1.04 sec                                                        | 872 ms: 1.20x faster                                            |
| unpickle_pure_python     | 189 us                                                          | 160 us: 1.18x faster                                            |
| sqlalchemy_imperative    | 13.2 ms                                                         | 11.2 ms: 1.18x faster                                           |
| sqlite_synth             | 2.29 us                                                         | 1.95 us: 1.17x faster                                           |
| deepcopy_memo            | 29.6 us                                                         | 25.4 us: 1.16x faster                                           |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.16x faster                                            |
| spectral_norm            | 80.2 ms                                                         | 69.4 ms: 1.16x faster                                           |
| regex_compile            | 117 ms                                                          | 101 ms: 1.15x faster                                            |
| regex_dna                | 131 ms                                                          | 114 ms: 1.15x faster                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.84 ms: 1.14x faster                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.6 ms: 1.13x faster                                           |
| mdp                      | 1.83 sec                                                        | 1.62 sec: 1.12x faster                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.12x faster                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                            |
| json                     | 4.76 ms                                                         | 4.27 ms: 1.11x faster                                           |
| tomli_loads              | 1.91 sec                                                        | 1.71 sec: 1.11x faster                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.0 ms: 1.11x faster                                           |
| coroutines               | 17.9 ms                                                         | 16.2 ms: 1.10x faster                                           |
| sqlalchemy_declarative   | 104 ms                                                          | 94.9 ms: 1.10x faster                                           |
| docutils                 | 1.95 sec                                                        | 1.78 sec: 1.10x faster                                          |
| html5lib                 | 52.1 ms                                                         | 47.5 ms: 1.10x faster                                           |
| xml_etree_process        | 48.1 ms                                                         | 44.2 ms: 1.09x faster                                           |
| sympy_str                | 229 ms                                                          | 212 ms: 1.08x faster                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 41.4 ms: 1.08x faster                                           |
| meteor_contest           | 80.0 ms                                                         | 74.6 ms: 1.07x faster                                           |
| sqlglot_normalize        | 230 ms                                                          | 216 ms: 1.06x faster                                            |
| fannkuch                 | 317 ms                                                          | 299 ms: 1.06x faster                                            |
| 2to3                     | 265 ms                                                          | 250 ms: 1.06x faster                                            |
| scimark_fft              | 216 ms                                                          | 205 ms: 1.06x faster                                            |
| chameleon                | 6.42 ms                                                         | 6.08 ms: 1.06x faster                                           |
| sympy_expand             | 391 ms                                                          | 373 ms: 1.05x faster                                            |
| json_loads               | 22.4 us                                                         | 21.6 us: 1.03x faster                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                          |
| pprint_safe_repr         | 658 ms                                                          | 648 ms: 1.02x faster                                            |
| nbody                    | 79.1 ms                                                         | 80.0 ms: 1.01x slower                                           |
| deepcopy                 | 310 us                                                          | 314 us: 1.01x slower                                            |
| pathlib                  | 81.2 ms                                                         | 82.9 ms: 1.02x slower                                           |
| genshi_text              | 21.0 ms                                                         | 21.5 ms: 1.02x slower                                           |
| genshi_xml               | 46.6 ms                                                         | 50.1 ms: 1.08x slower                                           |
| regex_effbot             | 1.66 ms                                                         | 1.80 ms: 1.08x slower                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.92 us: 1.09x slower                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                           |
| logging_simple           | 7.29 us                                                         | 7.99 us: 1.10x slower                                           |
| logging_format           | 7.91 us                                                         | 8.72 us: 1.10x slower                                           |
| async_generators         | 241 ms                                                          | 270 ms: 1.12x slower                                            |
| python_startup           | 22.9 ms                                                         | 28.3 ms: 1.23x slower                                           |
| bench_mp_pool            | 66.4 ms                                                         | 90.6 ms: 1.37x slower                                           |
| gc_traversal             | 1.28 ms                                                         | 1.75 ms: 1.37x slower                                           |
| telco                    | 4.83 ms                                                         | 6.96 ms: 1.44x slower                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.53x slower                                           |
| coverage                 | 46.6 ms                                                         | 324 ms: 6.96x slower                                            |
| thrift                   | 902 us                                                          | 9.98 ms: 11.06x slower                                          |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                    |

Benchmark hidden because not significant (2): xml_etree_generate, regex_v8
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown