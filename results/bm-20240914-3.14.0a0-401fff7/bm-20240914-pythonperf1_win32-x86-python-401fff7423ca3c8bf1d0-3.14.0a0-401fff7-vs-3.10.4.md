# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-x86
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.128x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.07x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.85 sec: 1.06x faster                                                         |
| html5lib       | 52.1 ms                                                         | 47.3 ms: 1.10x faster                                                          |
| tornado_http   | 118 ms                                                          | 95.2 ms: 1.24x faster                                                          |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 466 ms: 1.98x faster                                                           |
| async_tree_none         | 394 ms                                                          | 221 ms: 1.78x faster                                                           |
| async_tree_io           | 940 ms                                                          | 542 ms: 1.73x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.53x faster                                                           |
| float          | 69.6 ms                                                         | 61.6 ms: 1.13x faster                                                          |
| nbody          | 79.1 ms                                                         | 94.2 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                           |
| regex_compile  | 117 ms                                                          | 109 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.43 ms: 1.32x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 179 us: 1.06x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.8 ms: 1.04x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 269 us: 1.04x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                                         |
| pickle               | 7.83 us                                                         | 7.99 us: 1.02x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 50.1 ms: 1.04x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.44 us: 1.07x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 67.8 ms: 1.10x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.4 us: 1.12x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.9 ms: 1.04x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.00 ms: 1.14x faster                                                          |
| django_template | 36.0 ms                                                         | 34.7 ms: 1.04x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.7 ms: 1.03x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 48.9 ms: 1.05x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 148 us: 2.68x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.53x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 466 ms: 1.98x faster                                                           |
| async_tree_none          | 394 ms                                                          | 221 ms: 1.78x faster                                                           |
| async_tree_io            | 940 ms                                                          | 542 ms: 1.73x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| pylint                   | 384 ms                                                          | 229 ms: 1.68x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.79 ms: 1.44x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 58.3 ms: 1.39x faster                                                          |
| chaos                    | 74.4 ms                                                         | 54.7 ms: 1.36x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 21.8 us: 1.36x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.43 ms: 1.32x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 75.0 ns: 1.30x faster                                                          |
| go                       | 146 ms                                                          | 112 ms: 1.30x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 69.0 ms: 1.30x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.9 us: 1.28x faster                                                          |
| raytrace                 | 303 ms                                                          | 238 ms: 1.27x faster                                                           |
| deepcopy                 | 310 us                                                          | 244 us: 1.27x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.26x faster                                                          |
| tornado_http             | 118 ms                                                          | 95.2 ms: 1.24x faster                                                          |
| generators               | 31.6 ms                                                         | 25.9 ms: 1.22x faster                                                          |
| thrift                   | 902 us                                                          | 748 us: 1.21x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.32 ms: 1.20x faster                                                          |
| pyflate                  | 422 ms                                                          | 353 ms: 1.20x faster                                                           |
| pycparser                | 1.04 sec                                                        | 876 ms: 1.19x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 74.4 ms: 1.17x faster                                                          |
| scimark_sor              | 115 ms                                                          | 98.3 ms: 1.17x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.97 us: 1.16x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.27 ms: 1.16x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 50.9 ms: 1.15x faster                                                          |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.00 ms: 1.14x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 655 ms: 1.14x faster                                                           |
| float                    | 69.6 ms                                                         | 61.6 ms: 1.13x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.12x faster                                                          |
| json                     | 4.76 ms                                                         | 4.29 ms: 1.11x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 47.3 ms: 1.10x faster                                                          |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.9 ms: 1.09x faster                                                          |
| richards_super           | 49.9 ms                                                         | 46.0 ms: 1.08x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                          |
| 2to3                     | 265 ms                                                          | 249 ms: 1.07x faster                                                           |
| regex_compile            | 117 ms                                                          | 109 ms: 1.07x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 75.6 ms: 1.06x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.53 us: 1.06x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 179 us: 1.06x faster                                                           |
| sympy_str                | 229 ms                                                          | 217 ms: 1.06x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.85 sec: 1.06x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.8 ms: 1.04x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 269 us: 1.04x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.12 ms: 1.04x faster                                                          |
| django_template          | 36.0 ms                                                         | 34.7 ms: 1.04x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.87 sec: 1.02x faster                                                         |
| sympy_expand             | 391 ms                                                          | 385 ms: 1.01x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.80 sec: 1.01x faster                                                         |
| richards                 | 40.3 ms                                                         | 40.0 ms: 1.01x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 44.4 ms: 1.01x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 81.0 ms: 1.01x slower                                                          |
| fannkuch                 | 317 ms                                                          | 322 ms: 1.01x slower                                                           |
| pprint_safe_repr         | 658 ms                                                          | 670 ms: 1.02x slower                                                           |
| pickle                   | 7.83 us                                                         | 7.99 us: 1.02x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 82.9 ms: 1.02x slower                                                          |
| coroutines               | 17.9 ms                                                         | 18.5 ms: 1.03x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 21.7 ms: 1.03x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 50.1 ms: 1.04x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.9 ms: 1.04x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 48.9 ms: 1.05x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 735 us: 1.06x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.44 us: 1.07x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 71.5 ms: 1.08x slower                                                          |
| scimark_fft              | 216 ms                                                          | 236 ms: 1.09x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 67.8 ms: 1.10x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.41 ms: 1.10x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.81 us: 1.11x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.15 us: 1.12x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.4 us: 1.12x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 45.5 ns: 1.14x slower                                                          |
| coverage                 | 46.6 ms                                                         | 53.2 ms: 1.14x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                          |
| nbody                    | 79.1 ms                                                         | 94.2 ms: 1.19x slower                                                          |
| async_generators         | 241 ms                                                          | 291 ms: 1.21x slower                                                           |
| telco                    | 4.83 ms                                                         | 7.04 ms: 1.46x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (4): unpickle_list, sqlglot_normalize, pprint_pformat, asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.128x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown