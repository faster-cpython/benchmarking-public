# Results vs. 3.10.4

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-x86
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.95 sec                                                        | 2.06 sec: 1.06x slower                                                          |
| html5lib       | 52.1 ms                                                         | 46.2 ms: 1.13x faster                                                           |
| tornado_http   | 118 ms                                                          | 109 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 476 ms: 1.94x faster                                                            |
| async_tree_io           | 940 ms                                                          | 524 ms: 1.80x faster                                                            |
| async_tree_none         | 394 ms                                                          | 222 ms: 1.77x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 204 ms: 2.46x faster                                                            |
| float          | 69.6 ms                                                         | 46.6 ms: 1.49x faster                                                           |
| nbody          | 79.1 ms                                                         | 64.6 ms: 1.22x faster                                                           |
| Geometric mean | (ref)                                                           | 1.65x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 105 ms: 1.11x faster                                                            |
| regex_dna      | 131 ms                                                          | 124 ms: 1.06x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.4 ms: 1.02x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.53 sec: 1.25x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 8.14 ms: 1.21x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 160 us: 1.18x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 42.1 ms: 1.14x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 246 us: 1.14x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 55.1 ms: 1.12x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.1 ms: 1.09x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 112 ms: 1.07x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.7 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.69 ms: 1.60x faster                                                           |
| django_template | 36.0 ms                                                         | 32.7 ms: 1.10x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 23.4 ms: 1.11x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 54.3 ms: 1.16x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 141 us: 2.81x faster                                                            |
| pidigits                 | 502 ms                                                          | 204 ms: 2.46x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 101 ms: 2.28x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 476 ms: 1.94x faster                                                            |
| async_tree_io            | 940 ms                                                          | 524 ms: 1.80x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 16.6 us: 1.78x faster                                                           |
| async_tree_none          | 394 ms                                                          | 222 ms: 1.77x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 55.6 ns: 1.76x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                            |
| scimark_sor              | 115 ms                                                          | 70.2 ms: 1.64x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 49.8 ms: 1.63x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.69 ms: 1.60x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.52 ms: 1.60x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.0 ms: 1.55x faster                                                           |
| go                       | 146 ms                                                          | 96.7 ms: 1.51x faster                                                           |
| float                    | 69.6 ms                                                         | 46.6 ms: 1.49x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 61.8 ms: 1.45x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 57.8 ms: 1.39x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.0 us: 1.37x faster                                                           |
| chaos                    | 74.4 ms                                                         | 54.5 ms: 1.37x faster                                                           |
| pylint                   | 384 ms                                                          | 283 ms: 1.35x faster                                                            |
| pyflate                  | 422 ms                                                          | 312 ms: 1.35x faster                                                            |
| fannkuch                 | 317 ms                                                          | 237 ms: 1.34x faster                                                            |
| generators               | 31.6 ms                                                         | 23.9 ms: 1.32x faster                                                           |
| deepcopy                 | 310 us                                                          | 236 us: 1.32x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.48 ms: 1.31x faster                                                           |
| pycparser                | 1.04 sec                                                        | 809 ms: 1.29x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.05 ms: 1.26x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.53 sec: 1.25x faster                                                          |
| nbody                    | 79.1 ms                                                         | 64.6 ms: 1.22x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.14 ms: 1.21x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.16 sec: 1.18x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 49.5 ms: 1.18x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 160 us: 1.18x faster                                                            |
| scimark_fft              | 216 ms                                                          | 183 ms: 1.18x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.35 ms: 1.17x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 567 ms: 1.16x faster                                                            |
| thrift                   | 902 us                                                          | 780 us: 1.16x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 5.32 ms: 1.15x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 42.1 ms: 1.14x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 76.3 ms: 1.14x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 246 us: 1.14x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 988 us: 1.13x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 46.2 ms: 1.13x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 55.1 ms: 1.12x faster                                                           |
| regex_compile            | 117 ms                                                          | 105 ms: 1.11x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 72.3 ms: 1.11x faster                                                           |
| richards_super           | 49.9 ms                                                         | 45.3 ms: 1.10x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.7 ms: 1.10x faster                                                           |
| raytrace                 | 303 ms                                                          | 275 ms: 1.10x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.44 us: 1.10x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.1 ms: 1.09x faster                                                           |
| tornado_http             | 118 ms                                                          | 109 ms: 1.08x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.07x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 112 ms: 1.07x faster                                                            |
| sympy_sum                | 122 ms                                                          | 116 ms: 1.06x faster                                                            |
| regex_dna                | 131 ms                                                          | 124 ms: 1.06x faster                                                            |
| coroutines               | 17.9 ms                                                         | 17.3 ms: 1.04x faster                                                           |
| richards                 | 40.3 ms                                                         | 39.2 ms: 1.03x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.4 ms: 1.02x faster                                                           |
| sympy_expand             | 391 ms                                                          | 399 ms: 1.02x slower                                                            |
| logging_simple           | 7.29 us                                                         | 7.58 us: 1.04x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.23 us: 1.04x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 17.3 ms: 1.04x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.06 sec: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 88.0 ms: 1.08x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 23.4 ms: 1.11x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 49.9 ms: 1.12x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.5 ms: 1.15x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.7 ms: 1.16x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 54.3 ms: 1.16x slower                                                           |
| async_generators         | 241 ms                                                          | 314 ms: 1.30x slower                                                            |
| telco                    | 4.83 ms                                                         | 6.33 ms: 1.31x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 94.1 ms: 1.42x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.82 ms: 1.42x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.19 ms: 1.71x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.18x faster                                                                    |

Benchmark hidden because not significant (3): 2to3, sympy_str, json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown