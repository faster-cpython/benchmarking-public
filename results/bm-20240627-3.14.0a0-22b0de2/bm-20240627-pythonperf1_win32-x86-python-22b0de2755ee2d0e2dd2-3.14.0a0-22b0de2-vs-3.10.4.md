# Results vs. 3.10.4

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: windows-x86
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.07x faster
- HPT reliability: 96.49%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 264 ms: 1.01x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.96 sec: 1.01x slower                                                         |
| html5lib       | 52.1 ms                                                         | 49.9 ms: 1.04x faster                                                          |
| tornado_http   | 118 ms                                                          | 97.6 ms: 1.20x faster                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 491 ms: 1.88x faster                                                           |
| async_tree_none         | 394 ms                                                          | 241 ms: 1.63x faster                                                           |
| async_tree_io           | 940 ms                                                          | 579 ms: 1.62x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 295 ms: 1.58x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.68x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.52x faster                                                           |
| float          | 69.6 ms                                                         | 64.8 ms: 1.07x faster                                                          |
| nbody          | 79.1 ms                                                         | 103 ms: 1.30x slower                                                           |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                           |
| regex_compile  | 117 ms                                                          | 115 ms: 1.01x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|---------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps          | 9.82 ms                                                         | 7.82 ms: 1.26x faster                                                          |
| xml_etree_parse     | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| json_loads          | 22.4 us                                                         | 21.1 us: 1.06x faster                                                          |
| xml_etree_iterparse | 70.8 ms                                                         | 69.7 ms: 1.02x faster                                                          |
| pickle_pure_python  | 280 us                                                          | 278 us: 1.01x faster                                                           |
| tomli_loads         | 1.91 sec                                                        | 2.01 sec: 1.05x slower                                                         |
| xml_etree_process   | 48.1 ms                                                         | 51.6 ms: 1.07x slower                                                          |
| xml_etree_generate  | 61.6 ms                                                         | 70.2 ms: 1.14x slower                                                          |
| Geometric mean      | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 34.4 ms: 1.05x faster                                                          |
| mako            | 9.10 ms                                                         | 8.76 ms: 1.04x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 54.6 ms: 1.17x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 24.9 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 155 us: 2.55x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.52x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 491 ms: 1.88x faster                                                           |
| pylint                   | 384 ms                                                          | 234 ms: 1.64x faster                                                           |
| async_tree_none          | 394 ms                                                          | 241 ms: 1.63x faster                                                           |
| async_tree_io            | 940 ms                                                          | 579 ms: 1.62x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 295 ms: 1.58x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.88 ms: 1.40x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 63.7 ms: 1.28x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 77.7 ns: 1.26x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.82 ms: 1.26x faster                                                          |
| chaos                    | 74.4 ms                                                         | 60.7 ms: 1.23x faster                                                          |
| raytrace                 | 303 ms                                                          | 247 ms: 1.22x faster                                                           |
| tornado_http             | 118 ms                                                          | 97.6 ms: 1.20x faster                                                          |
| comprehensions           | 17.7 us                                                         | 14.8 us: 1.20x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 75.5 ms: 1.19x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 25.1 us: 1.18x faster                                                          |
| pycparser                | 1.04 sec                                                        | 892 ms: 1.17x faster                                                           |
| go                       | 146 ms                                                          | 127 ms: 1.15x faster                                                           |
| deepcopy                 | 310 us                                                          | 271 us: 1.14x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.43 ms: 1.13x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 992 us: 1.13x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 77.5 ms: 1.12x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| pyflate                  | 422 ms                                                          | 378 ms: 1.12x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 668 ms: 1.11x faster                                                           |
| thrift                   | 902 us                                                          | 810 us: 1.11x faster                                                           |
| generators               | 31.6 ms                                                         | 28.5 ms: 1.11x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.21 ms: 1.10x faster                                                          |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                           |
| richards_super           | 49.9 ms                                                         | 45.8 ms: 1.09x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.45 ms: 1.09x faster                                                          |
| json                     | 4.76 ms                                                         | 4.40 ms: 1.08x faster                                                          |
| scimark_sor              | 115 ms                                                          | 106 ms: 1.08x faster                                                           |
| float                    | 69.6 ms                                                         | 64.8 ms: 1.07x faster                                                          |
| json_loads               | 22.4 us                                                         | 21.1 us: 1.06x faster                                                          |
| sympy_sum                | 122 ms                                                          | 116 ms: 1.06x faster                                                           |
| django_template          | 36.0 ms                                                         | 34.4 ms: 1.05x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 49.9 ms: 1.04x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.75 sec: 1.04x faster                                                         |
| mako                     | 9.10 ms                                                         | 8.76 ms: 1.04x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 16.2 ms: 1.03x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 60.9 ms: 1.02x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 69.7 ms: 1.02x faster                                                          |
| regex_compile            | 117 ms                                                          | 115 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                         |
| pickle_pure_python       | 280 us                                                          | 278 us: 1.01x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 79.6 ms: 1.01x faster                                                          |
| 2to3                     | 265 ms                                                          | 264 ms: 1.01x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.96 sec: 1.01x slower                                                         |
| coroutines               | 17.9 ms                                                         | 18.1 ms: 1.01x slower                                                          |
| sympy_str                | 229 ms                                                          | 233 ms: 1.02x slower                                                           |
| richards                 | 40.3 ms                                                         | 41.2 ms: 1.02x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.76 us: 1.03x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 82.4 ms: 1.03x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 84.0 ms: 1.03x slower                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.42 sec: 1.04x slower                                                         |
| python_startup_no_site   | 18.1 ms                                                         | 18.9 ms: 1.05x slower                                                          |
| tomli_loads              | 1.91 sec                                                        | 2.01 sec: 1.05x slower                                                         |
| pprint_safe_repr         | 658 ms                                                          | 694 ms: 1.05x slower                                                           |
| sympy_expand             | 391 ms                                                          | 413 ms: 1.06x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 47.3 ms: 1.06x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 739 us: 1.06x slower                                                           |
| sqlglot_normalize        | 230 ms                                                          | 246 ms: 1.07x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 71.0 ms: 1.07x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 51.6 ms: 1.07x slower                                                          |
| fannkuch                 | 317 ms                                                          | 347 ms: 1.10x slower                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.61 ms: 1.11x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.1 ms: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 70.2 ms: 1.14x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.16x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 54.6 ms: 1.17x slower                                                          |
| logging_format           | 7.91 us                                                         | 9.33 us: 1.18x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.62 us: 1.18x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 24.9 ms: 1.19x slower                                                          |
| scimark_fft              | 216 ms                                                          | 257 ms: 1.19x slower                                                           |
| nbody                    | 79.1 ms                                                         | 103 ms: 1.30x slower                                                           |
| async_generators         | 241 ms                                                          | 314 ms: 1.30x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.79 ms: 1.41x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.07x faster                                                                   |

Benchmark hidden because not significant (2): python_startup, unpickle_pure_python
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240627-3.14.0a0-22b0de2/bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 96.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown