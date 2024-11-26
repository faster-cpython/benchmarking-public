# Results vs. 3.10.4

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-x86
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.130x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 251 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| html5lib       | 52.1 ms                                                         | 45.5 ms: 1.14x faster                                                          |
| tornado_http   | 118 ms                                                          | 95.6 ms: 1.23x faster                                                          |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 487 ms: 1.89x faster                                                           |
| async_tree_none         | 394 ms                                                          | 218 ms: 1.80x faster                                                           |
| async_tree_io           | 940 ms                                                          | 538 ms: 1.75x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 270 ms: 1.73x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| float          | 69.6 ms                                                         | 62.7 ms: 1.11x faster                                                          |
| nbody          | 79.1 ms                                                         | 93.0 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                           |
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.70 ms: 1.28x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 260 us: 1.08x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 177 us: 1.07x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.6 ms: 1.05x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                         |
| unpickle_list        | 2.98 us                                                         | 3.01 us: 1.01x slower                                                          |
| pickle               | 7.83 us                                                         | 7.91 us: 1.01x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 49.9 ms: 1.04x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.40 us: 1.06x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.06x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.8 us: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.7 ms: 1.04x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.09 ms: 1.13x faster                                                          |
| django_template | 36.0 ms                                                         | 33.2 ms: 1.09x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 47.7 ms: 1.02x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 144 us: 2.74x faster                                                           |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 487 ms: 1.89x faster                                                           |
| async_tree_none          | 394 ms                                                          | 218 ms: 1.80x faster                                                           |
| async_tree_io            | 940 ms                                                          | 538 ms: 1.75x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 270 ms: 1.73x faster                                                           |
| pylint                   | 384 ms                                                          | 235 ms: 1.63x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.76 ms: 1.46x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 57.1 ms: 1.42x faster                                                          |
| go                       | 146 ms                                                          | 106 ms: 1.37x faster                                                           |
| chaos                    | 74.4 ms                                                         | 54.7 ms: 1.36x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 73.5 ns: 1.33x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 22.5 us: 1.31x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.7 us: 1.29x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 69.6 ms: 1.29x faster                                                          |
| raytrace                 | 303 ms                                                          | 237 ms: 1.28x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.70 ms: 1.28x faster                                                          |
| deepcopy                 | 310 us                                                          | 245 us: 1.27x faster                                                           |
| tornado_http             | 118 ms                                                          | 95.6 ms: 1.23x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.09 ms: 1.22x faster                                                          |
| generators               | 31.6 ms                                                         | 25.8 ms: 1.22x faster                                                          |
| pycparser                | 1.04 sec                                                        | 862 ms: 1.21x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.13 ms: 1.20x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.34 ms: 1.18x faster                                                          |
| pyflate                  | 422 ms                                                          | 358 ms: 1.18x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 74.6 ms: 1.17x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.98 us: 1.16x faster                                                          |
| thrift                   | 902 us                                                          | 779 us: 1.16x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 50.6 ms: 1.16x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 650 ms: 1.14x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 45.5 ms: 1.14x faster                                                          |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.14x faster                                                           |
| scimark_sor              | 115 ms                                                          | 101 ms: 1.14x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.09 ms: 1.13x faster                                                          |
| json                     | 4.76 ms                                                         | 4.24 ms: 1.12x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| richards_super           | 49.9 ms                                                         | 44.8 ms: 1.11x faster                                                          |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                           |
| float                    | 69.6 ms                                                         | 62.7 ms: 1.11x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.03 ms: 1.09x faster                                                          |
| django_template          | 36.0 ms                                                         | 33.2 ms: 1.09x faster                                                          |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 260 us: 1.08x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 177 us: 1.07x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 57.7 ms: 1.07x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.07x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 75.5 ms: 1.06x faster                                                          |
| 2to3                     | 265 ms                                                          | 251 ms: 1.06x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.73 sec: 1.06x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.6 ms: 1.05x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.09 ms: 1.05x faster                                                          |
| sympy_str                | 229 ms                                                          | 219 ms: 1.05x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.85 sec: 1.03x faster                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.60 us: 1.03x faster                                                          |
| sympy_expand             | 391 ms                                                          | 387 ms: 1.01x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 44.4 ms: 1.01x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 231 ms: 1.00x slower                                                           |
| richards                 | 40.3 ms                                                         | 40.5 ms: 1.01x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 80.6 ms: 1.01x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.01 us: 1.01x slower                                                          |
| pickle                   | 7.83 us                                                         | 7.91 us: 1.01x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| coroutines               | 17.9 ms                                                         | 18.3 ms: 1.02x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 47.7 ms: 1.02x slower                                                          |
| pprint_safe_repr         | 658 ms                                                          | 676 ms: 1.03x slower                                                           |
| fannkuch                 | 317 ms                                                          | 326 ms: 1.03x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 83.9 ms: 1.03x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.7 ms: 1.04x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 49.9 ms: 1.04x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 728 us: 1.05x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.40 us: 1.06x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.06x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 71.4 ms: 1.08x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.91 us: 1.08x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.62 us: 1.09x slower                                                          |
| scimark_fft              | 216 ms                                                          | 236 ms: 1.09x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.41 ms: 1.10x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 45.3 ns: 1.13x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.7 ms: 1.13x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.8 us: 1.14x slower                                                          |
| nbody                    | 79.1 ms                                                         | 93.0 ms: 1.18x slower                                                          |
| async_generators         | 241 ms                                                          | 303 ms: 1.26x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.79 ms: 1.41x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (2): pprint_pformat, asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.130x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown