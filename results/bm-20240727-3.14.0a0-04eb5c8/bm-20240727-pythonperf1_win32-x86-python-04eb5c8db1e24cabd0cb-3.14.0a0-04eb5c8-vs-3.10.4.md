# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-x86
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.07x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.89 sec: 1.03x faster                                                         |
| html5lib       | 52.1 ms                                                         | 48.5 ms: 1.07x faster                                                          |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 481 ms: 1.92x faster                                                           |
| async_tree_none         | 394 ms                                                          | 223 ms: 1.76x faster                                                           |
| async_tree_io           | 940 ms                                                          | 541 ms: 1.74x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 274 ms: 1.71x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.56x faster                                                           |
| float          | 69.6 ms                                                         | 58.2 ms: 1.20x faster                                                          |
| nbody          | 79.1 ms                                                         | 90.9 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.39x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 104 ms: 1.12x faster                                                           |
| regex_dna      | 131 ms                                                          | 122 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.46 ms: 1.32x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 239 us: 1.17x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 106 ms: 1.13x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 170 us: 1.11x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.2 us: 1.11x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                         |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.5 ms: 1.05x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 46.9 ms: 1.03x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 65.5 ms: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.06 ms: 1.13x faster                                                          |
| django_template | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 47.3 ms: 1.02x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 21.5 ms: 1.03x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 148 us: 2.67x faster                                                           |
| pidigits                 | 502 ms                                                          | 197 ms: 2.56x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 481 ms: 1.92x faster                                                           |
| async_tree_none          | 394 ms                                                          | 223 ms: 1.76x faster                                                           |
| async_tree_io            | 940 ms                                                          | 541 ms: 1.74x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 274 ms: 1.71x faster                                                           |
| pylint                   | 384 ms                                                          | 233 ms: 1.65x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.58 ms: 1.56x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 56.8 ms: 1.43x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 20.9 us: 1.42x faster                                                          |
| chaos                    | 74.4 ms                                                         | 53.6 ms: 1.39x faster                                                          |
| raytrace                 | 303 ms                                                          | 222 ms: 1.36x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 72.6 ns: 1.35x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.3 us: 1.33x faster                                                          |
| go                       | 146 ms                                                          | 110 ms: 1.32x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.46 ms: 1.32x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 68.4 ms: 1.31x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.02 ms: 1.30x faster                                                          |
| deepcopy                 | 310 us                                                          | 242 us: 1.28x faster                                                           |
| richards_super           | 49.9 ms                                                         | 39.9 ms: 1.25x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.28 ms: 1.24x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.95 ms: 1.24x faster                                                          |
| pyflate                  | 422 ms                                                          | 341 ms: 1.24x faster                                                           |
| generators               | 31.6 ms                                                         | 25.7 ms: 1.23x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.6 ms: 1.22x faster                                                          |
| pycparser                | 1.04 sec                                                        | 858 ms: 1.21x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 71.9 ms: 1.21x faster                                                          |
| float                    | 69.6 ms                                                         | 58.2 ms: 1.20x faster                                                          |
| thrift                   | 902 us                                                          | 770 us: 1.17x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 239 us: 1.17x faster                                                           |
| scimark_sor              | 115 ms                                                          | 98.4 ms: 1.17x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 50.1 ms: 1.17x faster                                                          |
| json                     | 4.76 ms                                                         | 4.15 ms: 1.15x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 106 ms: 1.13x faster                                                           |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.06 ms: 1.13x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 992 us: 1.13x faster                                                           |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.13x faster                                                           |
| regex_compile            | 117 ms                                                          | 104 ms: 1.12x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 170 us: 1.11x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.2 us: 1.11x faster                                                          |
| richards                 | 40.3 ms                                                         | 36.7 ms: 1.10x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.2 ms: 1.09x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.67 sec: 1.09x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                         |
| django_template          | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 48.5 ms: 1.07x faster                                                          |
| regex_dna                | 131 ms                                                          | 122 ms: 1.07x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.51 us: 1.07x faster                                                          |
| 2to3                     | 265 ms                                                          | 249 ms: 1.07x faster                                                           |
| sympy_str                | 229 ms                                                          | 217 ms: 1.05x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.5 ms: 1.05x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.10 ms: 1.05x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.3 ms: 1.04x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 722 ms: 1.03x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.89 sec: 1.03x faster                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 43.5 ms: 1.03x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 46.9 ms: 1.03x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 78.1 ms: 1.03x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 225 ms: 1.02x faster                                                           |
| fannkuch                 | 317 ms                                                          | 311 ms: 1.02x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 646 ms: 1.02x faster                                                           |
| sympy_expand             | 391 ms                                                          | 385 ms: 1.02x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 47.3 ms: 1.02x slower                                                          |
| scimark_fft              | 216 ms                                                          | 221 ms: 1.02x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 21.5 ms: 1.03x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.8 ms: 1.04x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 65.5 ms: 1.06x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.78 us: 1.07x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.4 ms: 1.07x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 748 us: 1.08x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 88.1 ms: 1.08x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.58 us: 1.09x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 73.4 ms: 1.11x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.0 ms: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                          |
| nbody                    | 79.1 ms                                                         | 90.9 ms: 1.15x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| async_generators         | 241 ms                                                          | 281 ms: 1.16x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.24 ms: 1.29x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                   |

Benchmark hidden because not significant (2): meteor_contest, asyncio_tcp_ssl
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown