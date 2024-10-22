# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-x86
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 258 ms: 1.03x faster                                                           |
| docutils       | 1.95 sec                                                        | 2.02 sec: 1.04x slower                                                         |
| html5lib       | 52.1 ms                                                         | 47.9 ms: 1.09x faster                                                          |
| tornado_http   | 118 ms                                                          | 106 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 477 ms: 1.93x faster                                                           |
| async_tree_none         | 394 ms                                                          | 226 ms: 1.74x faster                                                           |
| async_tree_io           | 940 ms                                                          | 548 ms: 1.72x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 277 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.77x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.57x faster                                                           |
| float          | 69.6 ms                                                         | 43.0 ms: 1.62x faster                                                          |
| nbody          | 79.1 ms                                                         | 52.3 ms: 1.51x faster                                                          |
| Geometric mean | (ref)                                                           | 1.85x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 95.2 ms: 1.22x faster                                                          |
| regex_dna      | 131 ms                                                          | 128 ms: 1.02x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 2.08 ms: 1.25x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.09 ms: 1.39x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 213 us: 1.32x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 146 us: 1.30x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.55 sec: 1.23x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.0 ms: 1.12x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 43.7 ms: 1.10x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 57.7 ms: 1.07x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.19x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.49 ms: 1.66x faster                                                          |
| django_template | 36.0 ms                                                         | 33.9 ms: 1.06x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 24.0 ms: 1.14x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 53.3 ms: 1.14x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits                 | 502 ms                                                          | 196 ms: 2.57x faster                                                           |
| typing_runtime_protocols | 396 us                                                          | 161 us: 2.45x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 477 ms: 1.93x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 15.8 us: 1.87x faster                                                          |
| async_tree_none          | 394 ms                                                          | 226 ms: 1.74x faster                                                           |
| async_tree_io            | 940 ms                                                          | 548 ms: 1.72x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 57.7 ns: 1.70x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 277 ms: 1.69x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 48.3 ms: 1.68x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 47.7 ms: 1.68x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.49 ms: 1.66x faster                                                          |
| float                    | 69.6 ms                                                         | 43.0 ms: 1.62x faster                                                          |
| pyflate                  | 422 ms                                                          | 261 ms: 1.61x faster                                                           |
| pylint                   | 384 ms                                                          | 251 ms: 1.53x faster                                                           |
| nbody                    | 79.1 ms                                                         | 52.3 ms: 1.51x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.8 us: 1.51x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.6 ms: 1.49x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.75 ms: 1.47x faster                                                          |
| chaos                    | 74.4 ms                                                         | 52.8 ms: 1.41x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.31 ms: 1.40x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.09 ms: 1.39x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 965 us: 1.38x faster                                                           |
| fannkuch                 | 317 ms                                                          | 233 ms: 1.36x faster                                                           |
| raytrace                 | 303 ms                                                          | 228 ms: 1.33x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 213 us: 1.32x faster                                                           |
| go                       | 146 ms                                                          | 111 ms: 1.31x faster                                                           |
| scimark_fft              | 216 ms                                                          | 165 ms: 1.31x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.73 ms: 1.30x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 146 us: 1.30x faster                                                           |
| pycparser                | 1.04 sec                                                        | 806 ms: 1.29x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.23 ms: 1.29x faster                                                          |
| richards_super           | 49.9 ms                                                         | 39.1 ms: 1.28x faster                                                          |
| deepcopy                 | 310 us                                                          | 249 us: 1.24x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.55 sec: 1.23x faster                                                         |
| regex_compile            | 117 ms                                                          | 95.2 ms: 1.22x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 73.9 ms: 1.21x faster                                                          |
| richards                 | 40.3 ms                                                         | 33.3 ms: 1.21x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 73.0 ms: 1.19x faster                                                          |
| scimark_sor              | 115 ms                                                          | 96.9 ms: 1.19x faster                                                          |
| thrift                   | 902 us                                                          | 766 us: 1.18x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 50.2 ms: 1.17x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 70.1 ms: 1.14x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.0 ms: 1.12x faster                                                          |
| json                     | 4.76 ms                                                         | 4.25 ms: 1.12x faster                                                          |
| generators               | 31.6 ms                                                         | 28.5 ms: 1.11x faster                                                          |
| tornado_http             | 118 ms                                                          | 106 ms: 1.11x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.24 sec: 1.10x faster                                                         |
| xml_etree_process        | 48.1 ms                                                         | 43.7 ms: 1.10x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 599 ms: 1.10x faster                                                           |
| sympy_sum                | 122 ms                                                          | 112 ms: 1.10x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 47.9 ms: 1.09x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 695 ms: 1.07x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 57.7 ms: 1.07x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.52 us: 1.07x faster                                                          |
| django_template          | 36.0 ms                                                         | 33.9 ms: 1.06x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                         |
| sympy_str                | 229 ms                                                          | 223 ms: 1.03x faster                                                           |
| 2to3                     | 265 ms                                                          | 258 ms: 1.03x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.3 ms: 1.02x faster                                                          |
| regex_dna                | 131 ms                                                          | 128 ms: 1.02x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| coroutines               | 17.9 ms                                                         | 18.0 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.3 sec: 1.02x slower                                                         |
| sympy_expand             | 391 ms                                                          | 401 ms: 1.03x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.02 sec: 1.04x slower                                                         |
| sqlglot_normalize        | 230 ms                                                          | 239 ms: 1.04x slower                                                           |
| python_startup           | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.06 us: 1.11x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.76 us: 1.11x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 90.7 ms: 1.12x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 775 us: 1.12x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.13x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 24.0 ms: 1.14x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 53.3 ms: 1.14x slower                                                          |
| coverage                 | 46.6 ms                                                         | 53.6 ms: 1.15x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 77.4 ms: 1.17x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.87 ms: 1.22x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 2.08 ms: 1.25x slower                                                          |
| async_generators         | 241 ms                                                          | 320 ms: 1.33x slower                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 3.09 ms: 2.76x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.18x faster                                                                   |

Benchmark hidden because not significant (1): sqlglot_optimize
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown