# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-x86
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 257 ms: 1.03x faster                                                           |
| docutils       | 1.95 sec                                                        | 2.00 sec: 1.02x slower                                                         |
| html5lib       | 52.1 ms                                                         | 47.2 ms: 1.10x faster                                                          |
| tornado_http   | 118 ms                                                          | 99.7 ms: 1.18x faster                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 485 ms: 1.90x faster                                                           |
| async_tree_none         | 394 ms                                                          | 223 ms: 1.77x faster                                                           |
| async_tree_io           | 940 ms                                                          | 547 ms: 1.72x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 281 ms: 1.66x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.76x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 195 ms: 2.57x faster                                                           |
| float          | 69.6 ms                                                         | 43.8 ms: 1.59x faster                                                          |
| nbody          | 79.1 ms                                                         | 50.6 ms: 1.56x faster                                                          |
| Geometric mean | (ref)                                                           | 1.86x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 103 ms: 1.13x faster                                                           |
| regex_dna      | 131 ms                                                          | 116 ms: 1.12x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.71 ms: 1.46x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.50 sec: 1.27x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 39.5 ms: 1.22x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 52.7 ms: 1.17x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 164 us: 1.16x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.7 ms: 1.15x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 247 us: 1.13x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                          |
| pickle               | 7.83 us                                                         | 7.94 us: 1.01x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.29 us: 1.02x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.7 ms: 1.04x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.47 ms: 1.67x faster                                                          |
| django_template | 36.0 ms                                                         | 35.1 ms: 1.03x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 56.0 ms: 1.20x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 25.8 ms: 1.23x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 151 us: 2.63x faster                                                           |
| pidigits                 | 502 ms                                                          | 195 ms: 2.57x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 100.0 ms: 2.31x faster                                                         |
| deepcopy_memo            | 29.6 us                                                         | 15.2 us: 1.94x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.09 ms: 1.94x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 485 ms: 1.90x faster                                                           |
| async_tree_none          | 394 ms                                                          | 223 ms: 1.77x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 46.0 ms: 1.74x faster                                                          |
| async_tree_io            | 940 ms                                                          | 547 ms: 1.72x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 47.5 ms: 1.71x faster                                                          |
| scimark_sor              | 115 ms                                                          | 68.7 ms: 1.67x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.47 ms: 1.67x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 281 ms: 1.66x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 60.3 ns: 1.62x faster                                                          |
| float                    | 69.6 ms                                                         | 43.8 ms: 1.59x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.3 us: 1.57x faster                                                          |
| nbody                    | 79.1 ms                                                         | 50.6 ms: 1.56x faster                                                          |
| pyflate                  | 422 ms                                                          | 274 ms: 1.54x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 59.9 ms: 1.50x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.71 ms: 1.46x faster                                                          |
| pylint                   | 384 ms                                                          | 265 ms: 1.45x faster                                                           |
| go                       | 146 ms                                                          | 103 ms: 1.41x faster                                                           |
| richards_super           | 49.9 ms                                                         | 36.4 ms: 1.37x faster                                                          |
| chaos                    | 74.4 ms                                                         | 54.6 ms: 1.36x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.39 ms: 1.36x faster                                                          |
| fannkuch                 | 317 ms                                                          | 238 ms: 1.33x faster                                                           |
| deepcopy                 | 310 us                                                          | 233 us: 1.33x faster                                                           |
| generators               | 31.6 ms                                                         | 24.0 ms: 1.32x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.50 sec: 1.27x faster                                                         |
| sqlglot_parse            | 1.33 ms                                                         | 1.05 ms: 1.27x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.91 ms: 1.25x faster                                                          |
| scimark_fft              | 216 ms                                                          | 174 ms: 1.25x faster                                                           |
| pycparser                | 1.04 sec                                                        | 839 ms: 1.24x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.9 ms: 1.24x faster                                                          |
| raytrace                 | 303 ms                                                          | 248 ms: 1.22x faster                                                           |
| richards                 | 40.3 ms                                                         | 33.0 ms: 1.22x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 39.5 ms: 1.22x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 612 ms: 1.21x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 48.3 ms: 1.21x faster                                                          |
| json                     | 4.76 ms                                                         | 4.01 ms: 1.19x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                          |
| tornado_http             | 118 ms                                                          | 99.7 ms: 1.18x faster                                                          |
| thrift                   | 902 us                                                          | 768 us: 1.17x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 52.7 ms: 1.17x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.36 ms: 1.17x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 164 us: 1.16x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.16x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.7 ms: 1.15x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 984 us: 1.14x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 247 us: 1.13x faster                                                           |
| regex_compile            | 117 ms                                                          | 103 ms: 1.13x faster                                                           |
| regex_dna                | 131 ms                                                          | 116 ms: 1.12x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 78.7 ms: 1.11x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 47.2 ms: 1.10x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 72.7 ms: 1.10x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 600 ms: 1.10x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                          |
| sympy_sum                | 122 ms                                                          | 114 ms: 1.08x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.27 sec: 1.08x faster                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.52 us: 1.06x faster                                                          |
| 2to3                     | 265 ms                                                          | 257 ms: 1.03x faster                                                           |
| sympy_str                | 229 ms                                                          | 222 ms: 1.03x faster                                                           |
| django_template          | 36.0 ms                                                         | 35.1 ms: 1.03x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.83 sec: 1.00x slower                                                         |
| sympy_integrate          | 16.6 ms                                                         | 16.8 ms: 1.01x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 82.2 ms: 1.01x slower                                                          |
| pickle                   | 7.83 us                                                         | 7.94 us: 1.01x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.29 us: 1.02x slower                                                          |
| docutils                 | 1.95 sec                                                        | 2.00 sec: 1.02x slower                                                         |
| sympy_expand             | 391 ms                                                          | 402 ms: 1.03x slower                                                           |
| coroutines               | 17.9 ms                                                         | 18.5 ms: 1.03x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.7 ms: 1.04x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 41.5 ns: 1.04x slower                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 46.4 ms: 1.04x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.5 ms: 1.08x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 750 us: 1.08x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.56 us: 1.08x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.93 us: 1.09x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.42 ms: 1.11x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 75.0 ms: 1.13x slower                                                          |
| coverage                 | 46.6 ms                                                         | 53.8 ms: 1.16x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 56.0 ms: 1.20x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 25.8 ms: 1.23x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.20 ms: 1.28x slower                                                          |
| async_generators         | 241 ms                                                          | 320 ms: 1.33x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (2): unpickle_list, asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown