# Results vs. 3.10.4

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-x86
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.158x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 246 ms: 1.08x faster                                                            |
| docutils       | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                                          |
| html5lib       | 52.1 ms                                                         | 43.8 ms: 1.19x faster                                                           |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 428 ms: 2.20x faster                                                            |
| async_tree_cpu_io_mixed | 922 ms                                                          | 432 ms: 2.13x faster                                                            |
| async_tree_none         | 394 ms                                                          | 194 ms: 2.02x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 244 ms: 1.91x faster                                                            |
| Geometric mean          | (ref)                                                           | 2.06x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| float          | 69.6 ms                                                         | 56.5 ms: 1.23x faster                                                           |
| nbody          | 79.1 ms                                                         | 85.5 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.42x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 102 ms: 1.15x faster                                                            |
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.5 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.61 sec: 1.18x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| json_dumps           | 9.82 ms                                                         | 8.78 ms: 1.12x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 171 us: 1.10x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 259 us: 1.08x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.2 ms: 1.07x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 48.7 ms: 1.01x slower                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 66.7 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.3 ms: 1.15x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.69 ms: 1.18x faster                                                           |
| django_template | 36.0 ms                                                         | 31.9 ms: 1.13x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 44.6 ms: 1.04x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 20.6 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 141 us: 2.80x faster                                                            |
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                            |
| async_tree_io            | 940 ms                                                          | 428 ms: 2.20x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 432 ms: 2.13x faster                                                            |
| async_tree_none          | 394 ms                                                          | 194 ms: 2.02x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 244 ms: 1.91x faster                                                            |
| pylint                   | 384 ms                                                          | 212 ms: 1.81x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.59 ms: 1.56x faster                                                           |
| go                       | 146 ms                                                          | 97.2 ms: 1.50x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 70.9 ns: 1.38x faster                                                           |
| chaos                    | 74.4 ms                                                         | 54.4 ms: 1.37x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 68.2 ms: 1.32x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 62.1 ms: 1.31x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.02 ms: 1.30x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.7 us: 1.30x faster                                                           |
| deepcopy                 | 310 us                                                          | 240 us: 1.29x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 23.1 us: 1.28x faster                                                           |
| generators               | 31.6 ms                                                         | 24.7 ms: 1.28x faster                                                           |
| pycparser                | 1.04 sec                                                        | 825 ms: 1.26x faster                                                            |
| pyflate                  | 422 ms                                                          | 336 ms: 1.26x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.26 ms: 1.25x faster                                                           |
| raytrace                 | 303 ms                                                          | 243 ms: 1.25x faster                                                            |
| float                    | 69.6 ms                                                         | 56.5 ms: 1.23x faster                                                           |
| thrift                   | 902 us                                                          | 737 us: 1.22x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.07 ms: 1.21x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                                           |
| richards_super           | 49.9 ms                                                         | 41.9 ms: 1.19x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 43.8 ms: 1.19x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.69 ms: 1.18x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.61 sec: 1.18x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 49.7 ms: 1.18x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 52.7 ms: 1.17x faster                                                           |
| scimark_sor              | 115 ms                                                          | 98.2 ms: 1.17x faster                                                           |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.17x faster                                                            |
| regex_compile            | 117 ms                                                          | 102 ms: 1.15x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 76.1 ms: 1.14x faster                                                           |
| django_template          | 36.0 ms                                                         | 31.9 ms: 1.13x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 71.6 ms: 1.12x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.78 ms: 1.12x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.1 ms: 1.12x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.11x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.92 ms: 1.11x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 171 us: 1.10x faster                                                            |
| json                     | 4.76 ms                                                         | 4.33 ms: 1.10x faster                                                           |
| richards                 | 40.3 ms                                                         | 36.9 ms: 1.09x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 259 us: 1.08x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                           |
| 2to3                     | 265 ms                                                          | 246 ms: 1.08x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 41.5 ms: 1.08x faster                                                           |
| fannkuch                 | 317 ms                                                          | 296 ms: 1.07x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.2 ms: 1.07x faster                                                           |
| sympy_str                | 229 ms                                                          | 214 ms: 1.07x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.28 sec: 1.07x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.71 sec: 1.07x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 216 ms: 1.06x faster                                                            |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.54 us: 1.06x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 627 ms: 1.05x faster                                                            |
| genshi_xml               | 46.6 ms                                                         | 44.6 ms: 1.04x faster                                                           |
| sympy_expand             | 391 ms                                                          | 377 ms: 1.04x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 20.6 ms: 1.02x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.5 ms: 1.02x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 48.7 ms: 1.01x slower                                                           |
| meteor_contest           | 80.0 ms                                                         | 81.1 ms: 1.01x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 83.6 ms: 1.03x slower                                                           |
| scimark_fft              | 216 ms                                                          | 225 ms: 1.04x slower                                                            |
| logging_simple           | 7.29 us                                                         | 7.75 us: 1.06x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.43 us: 1.07x slower                                                           |
| nbody                    | 79.1 ms                                                         | 85.5 ms: 1.08x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 66.7 ms: 1.08x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                           |
| coverage                 | 46.6 ms                                                         | 52.0 ms: 1.12x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.3 ms: 1.15x slower                                                           |
| mypy2                    | 590 ms                                                          | 683 ms: 1.16x slower                                                            |
| async_generators         | 241 ms                                                          | 304 ms: 1.26x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 93.0 ms: 1.40x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.81 ms: 1.41x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.06 ms: 1.52x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1_win32-x86-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.158x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown