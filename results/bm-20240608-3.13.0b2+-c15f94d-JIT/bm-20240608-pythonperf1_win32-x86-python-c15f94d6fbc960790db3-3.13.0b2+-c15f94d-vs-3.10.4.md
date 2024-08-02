# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-x86
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 246 ms: 1.08x faster                                                            |
| chameleon      | 6.42 ms                                                         | 6.01 ms: 1.07x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                          |
| html5lib       | 52.1 ms                                                         | 46.1 ms: 1.13x faster                                                           |
| tornado_http   | 118 ms                                                          | 97.1 ms: 1.21x faster                                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 469 ms: 1.97x faster                                                            |
| async_tree_io           | 940 ms                                                          | 531 ms: 1.77x faster                                                            |
| async_tree_none         | 394 ms                                                          | 227 ms: 1.74x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 287 ms: 1.62x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.77x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                            |
| float          | 69.6 ms                                                         | 41.9 ms: 1.66x faster                                                           |
| nbody          | 79.1 ms                                                         | 53.4 ms: 1.48x faster                                                           |
| Geometric mean | (ref)                                                           | 1.85x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 92.1 ms: 1.27x faster                                                           |
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.54 ms: 1.50x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 198 us: 1.42x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 134 us: 1.41x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.40 sec: 1.36x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 40.9 ms: 1.18x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 60.4 ms: 1.17x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 103 ms: 1.17x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 55.6 ms: 1.11x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.80 us: 1.07x faster                                                           |
| pickle               | 7.83 us                                                         | 8.32 us: 1.06x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.06x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.58 us: 1.11x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.8 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 20.9 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.34 ms: 1.70x faster                                                           |
| django_template | 36.0 ms                                                         | 30.8 ms: 1.17x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 50.0 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 141 us: 2.81x faster                                                            |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 469 ms: 1.97x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 54.2 ns: 1.81x faster                                                           |
| async_tree_io            | 940 ms                                                          | 531 ms: 1.77x faster                                                            |
| async_tree_none          | 394 ms                                                          | 227 ms: 1.74x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 47.1 ms: 1.72x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.34 ms: 1.70x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 47.5 ms: 1.69x faster                                                           |
| float                    | 69.6 ms                                                         | 41.9 ms: 1.66x faster                                                           |
| comprehensions           | 17.7 us                                                         | 10.8 us: 1.64x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 287 ms: 1.62x faster                                                            |
| pylint                   | 384 ms                                                          | 237 ms: 1.62x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.51 ms: 1.61x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.6 ms: 1.56x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.54 ms: 1.50x faster                                                           |
| chaos                    | 74.4 ms                                                         | 50.1 ms: 1.49x faster                                                           |
| raytrace                 | 303 ms                                                          | 204 ms: 1.48x faster                                                            |
| nbody                    | 79.1 ms                                                         | 53.4 ms: 1.48x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 20.1 us: 1.47x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 904 us: 1.47x faster                                                            |
| fannkuch                 | 317 ms                                                          | 216 ms: 1.47x faster                                                            |
| richards_super           | 49.9 ms                                                         | 34.8 ms: 1.43x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 198 us: 1.42x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 134 us: 1.41x faster                                                            |
| pyflate                  | 422 ms                                                          | 303 ms: 1.39x faster                                                            |
| go                       | 146 ms                                                          | 106 ms: 1.38x faster                                                            |
| hexiom                   | 6.13 ms                                                         | 4.49 ms: 1.37x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.40 sec: 1.36x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.39 ms: 1.36x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.17 ms: 1.36x faster                                                           |
| pycparser                | 1.04 sec                                                        | 781 ms: 1.33x faster                                                            |
| generators               | 31.6 ms                                                         | 23.9 ms: 1.32x faster                                                           |
| scimark_fft              | 216 ms                                                          | 165 ms: 1.31x faster                                                            |
| richards                 | 40.3 ms                                                         | 30.9 ms: 1.30x faster                                                           |
| scimark_sor              | 115 ms                                                          | 88.6 ms: 1.30x faster                                                           |
| regex_compile            | 117 ms                                                          | 92.1 ms: 1.27x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 68.9 ms: 1.26x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 72.4 ms: 1.24x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.87 us: 1.23x faster                                                           |
| tornado_http             | 118 ms                                                          | 97.1 ms: 1.21x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 625 ms: 1.19x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 40.9 ms: 1.18x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.17 sec: 1.17x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 60.4 ms: 1.17x faster                                                           |
| django_template          | 36.0 ms                                                         | 30.8 ms: 1.17x faster                                                           |
| json                     | 4.76 ms                                                         | 4.07 ms: 1.17x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 103 ms: 1.17x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 566 ms: 1.16x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.6 ms: 1.15x faster                                                           |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.14x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 989 us: 1.13x faster                                                            |
| html5lib                 | 52.1 ms                                                         | 46.1 ms: 1.13x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.62 sec: 1.13x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 55.6 ms: 1.11x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 73.0 ms: 1.10x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                                           |
| sympy_str                | 229 ms                                                          | 210 ms: 1.09x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 41.4 ms: 1.08x faster                                                           |
| 2to3                     | 265 ms                                                          | 246 ms: 1.08x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.07x faster                                                           |
| chameleon                | 6.42 ms                                                         | 6.01 ms: 1.07x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.80 us: 1.07x faster                                                           |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 218 ms: 1.06x faster                                                            |
| deepcopy                 | 310 us                                                          | 294 us: 1.05x faster                                                            |
| sympy_expand             | 391 ms                                                          | 375 ms: 1.04x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                          |
| flaskblogging            | 2.03 sec                                                        | 2.04 sec: 1.00x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.70 us: 1.01x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 84.0 ms: 1.03x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.32 us: 1.06x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.06x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 50.0 ms: 1.07x slower                                                           |
| python_startup           | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 751 us: 1.08x slower                                                            |
| pickle_list              | 3.22 us                                                         | 3.58 us: 1.11x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.8 us: 1.14x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 76.7 ms: 1.16x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.9 ms: 1.16x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.63 ms: 1.17x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                           |
| async_generators         | 241 ms                                                          | 295 ms: 1.22x slower                                                            |
| coverage                 | 46.6 ms                                                         | 331 ms: 7.10x slower                                                            |
| thrift                   | 902 us                                                          | 10.2 ms: 11.30x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (3): genshi_text, logging_format, logging_simple
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown