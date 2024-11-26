# Results vs. 3.10.4

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-x86
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.175x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 263 ms: 1.01x faster                                                            |
| docutils       | 1.95 sec                                                        | 2.06 sec: 1.06x slower                                                          |
| html5lib       | 52.1 ms                                                         | 46.4 ms: 1.12x faster                                                           |
| tornado_http   | 118 ms                                                          | 110 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 467 ms: 1.97x faster                                                            |
| async_tree_io           | 940 ms                                                          | 523 ms: 1.80x faster                                                            |
| async_tree_none         | 394 ms                                                          | 220 ms: 1.79x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 280 ms: 1.67x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 205 ms: 2.45x faster                                                            |
| float          | 69.6 ms                                                         | 46.7 ms: 1.49x faster                                                           |
| nbody          | 79.1 ms                                                         | 65.9 ms: 1.20x faster                                                           |
| Geometric mean | (ref)                                                           | 1.64x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 104 ms: 1.12x faster                                                            |
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.49 sec: 1.28x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 8.14 ms: 1.21x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 159 us: 1.19x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 239 us: 1.17x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 41.4 ms: 1.16x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 55.6 ms: 1.11x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.2 ms: 1.09x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 111 ms: 1.08x faster                                                            |
| json_loads           | 22.4 us                                                         | 21.3 us: 1.05x faster                                                           |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                           |
| python_startup         | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.68 ms: 1.60x faster                                                           |
| django_template | 36.0 ms                                                         | 33.4 ms: 1.08x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 23.1 ms: 1.10x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 52.7 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 147 us: 2.70x faster                                                            |
| pidigits                 | 502 ms                                                          | 205 ms: 2.45x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 467 ms: 1.97x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 16.2 us: 1.83x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 53.8 ns: 1.82x faster                                                           |
| async_tree_io            | 940 ms                                                          | 523 ms: 1.80x faster                                                            |
| async_tree_none          | 394 ms                                                          | 220 ms: 1.79x faster                                                            |
| scimark_sor              | 115 ms                                                          | 66.5 ms: 1.73x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 280 ms: 1.67x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 49.6 ms: 1.64x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.68 ms: 1.60x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.0 ms: 1.59x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.55 ms: 1.58x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 59.5 ms: 1.51x faster                                                           |
| go                       | 146 ms                                                          | 96.7 ms: 1.51x faster                                                           |
| float                    | 69.6 ms                                                         | 46.7 ms: 1.49x faster                                                           |
| chaos                    | 74.4 ms                                                         | 52.8 ms: 1.41x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 58.3 ms: 1.38x faster                                                           |
| pylint                   | 384 ms                                                          | 283 ms: 1.35x faster                                                            |
| comprehensions           | 17.7 us                                                         | 13.2 us: 1.35x faster                                                           |
| deepcopy                 | 310 us                                                          | 231 us: 1.34x faster                                                            |
| pyflate                  | 422 ms                                                          | 319 ms: 1.32x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.50 ms: 1.30x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.49 sec: 1.28x faster                                                          |
| fannkuch                 | 317 ms                                                          | 248 ms: 1.28x faster                                                            |
| generators               | 31.6 ms                                                         | 24.7 ms: 1.28x faster                                                           |
| pycparser                | 1.04 sec                                                        | 824 ms: 1.27x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.25x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.14 ms: 1.21x faster                                                           |
| nbody                    | 79.1 ms                                                         | 65.9 ms: 1.20x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.14 sec: 1.20x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 159 us: 1.19x faster                                                            |
| dulwich_log              | 58.5 ms                                                         | 49.3 ms: 1.19x faster                                                           |
| scimark_fft              | 216 ms                                                          | 182 ms: 1.19x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 73.9 ms: 1.18x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 560 ms: 1.18x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 239 us: 1.17x faster                                                            |
| thrift                   | 902 us                                                          | 770 us: 1.17x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.27 ms: 1.16x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 41.4 ms: 1.16x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.37 ms: 1.16x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 991 us: 1.13x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 46.4 ms: 1.12x faster                                                           |
| richards_super           | 49.9 ms                                                         | 44.5 ms: 1.12x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.40 us: 1.12x faster                                                           |
| regex_compile            | 117 ms                                                          | 104 ms: 1.12x faster                                                            |
| raytrace                 | 303 ms                                                          | 271 ms: 1.12x faster                                                            |
| xml_etree_generate       | 61.6 ms                                                         | 55.6 ms: 1.11x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 73.1 ms: 1.09x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.2 ms: 1.09x faster                                                           |
| django_template          | 36.0 ms                                                         | 33.4 ms: 1.08x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 111 ms: 1.08x faster                                                            |
| tornado_http             | 118 ms                                                          | 110 ms: 1.07x faster                                                            |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                            |
| json_loads               | 22.4 us                                                         | 21.3 us: 1.05x faster                                                           |
| sympy_sum                | 122 ms                                                          | 117 ms: 1.04x faster                                                            |
| richards                 | 40.3 ms                                                         | 39.3 ms: 1.02x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.7 ms: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                           |
| 2to3                     | 265 ms                                                          | 263 ms: 1.01x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.84 sec: 1.01x slower                                                          |
| sympy_expand             | 391 ms                                                          | 400 ms: 1.02x slower                                                            |
| sympy_integrate          | 16.6 ms                                                         | 17.3 ms: 1.04x slower                                                           |
| sqlglot_normalize        | 230 ms                                                          | 240 ms: 1.04x slower                                                            |
| logging_simple           | 7.29 us                                                         | 7.63 us: 1.05x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.28 us: 1.05x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.06 sec: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 88.1 ms: 1.08x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 23.1 ms: 1.10x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 49.8 ms: 1.11x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 52.7 ms: 1.13x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                           |
| coverage                 | 46.6 ms                                                         | 54.1 ms: 1.16x slower                                                           |
| python_startup           | 22.9 ms                                                         | 27.0 ms: 1.18x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.06 ms: 1.26x slower                                                           |
| async_generators         | 241 ms                                                          | 315 ms: 1.31x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 94.1 ms: 1.42x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.82 ms: 1.42x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.20 ms: 1.73x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (2): sympy_str, json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.175x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown