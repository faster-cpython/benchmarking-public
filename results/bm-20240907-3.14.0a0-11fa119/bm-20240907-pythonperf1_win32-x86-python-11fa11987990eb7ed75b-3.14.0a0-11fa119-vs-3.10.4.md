# Results vs. 3.10.4

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-x86
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.128x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 252 ms: 1.05x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| html5lib       | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| tornado_http   | 118 ms                                                          | 106 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 480 ms: 1.92x faster                                                           |
| async_tree_none         | 394 ms                                                          | 222 ms: 1.78x faster                                                           |
| async_tree_io           | 940 ms                                                          | 540 ms: 1.74x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                           |
| float          | 69.6 ms                                                         | 62.0 ms: 1.12x faster                                                          |
| nbody          | 79.1 ms                                                         | 94.3 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 109 ms: 1.07x faster                                                           |
| regex_dna      | 131 ms                                                          | 124 ms: 1.05x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.62 ms: 1.29x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.13x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 255 us: 1.10x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 179 us: 1.06x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.0 ms: 1.04x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                         |
| unpickle_list        | 2.98 us                                                         | 3.02 us: 1.01x slower                                                          |
| pickle               | 7.83 us                                                         | 7.97 us: 1.02x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 49.5 ms: 1.03x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.35 us: 1.04x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.6 us: 1.08x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 66.7 ms: 1.08x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.4 us: 1.12x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.2 ms: 1.06x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.5 ms: 1.14x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                          |
| mako            | 9.10 ms                                                         | 8.27 ms: 1.10x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 47.0 ms: 1.01x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 22.4 ms: 1.07x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 152 us: 2.60x faster                                                           |
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 480 ms: 1.92x faster                                                           |
| async_tree_none          | 394 ms                                                          | 222 ms: 1.78x faster                                                           |
| async_tree_io            | 940 ms                                                          | 540 ms: 1.74x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| pylint                   | 384 ms                                                          | 233 ms: 1.64x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.68 ms: 1.50x faster                                                          |
| go                       | 146 ms                                                          | 103 ms: 1.41x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 58.7 ms: 1.39x faster                                                          |
| chaos                    | 74.4 ms                                                         | 54.1 ms: 1.38x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 21.9 us: 1.35x faster                                                          |
| raytrace                 | 303 ms                                                          | 229 ms: 1.32x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 75.2 ns: 1.30x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.7 us: 1.29x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.62 ms: 1.29x faster                                                          |
| deepcopy                 | 310 us                                                          | 242 us: 1.28x faster                                                           |
| thrift                   | 902 us                                                          | 719 us: 1.25x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 72.3 ms: 1.24x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.08 ms: 1.24x faster                                                          |
| pycparser                | 1.04 sec                                                        | 866 ms: 1.20x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.33 ms: 1.19x faster                                                          |
| pyflate                  | 422 ms                                                          | 355 ms: 1.19x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.25 ms: 1.17x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 50.4 ms: 1.16x faster                                                          |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                           |
| richards_super           | 49.9 ms                                                         | 43.7 ms: 1.14x faster                                                          |
| generators               | 31.6 ms                                                         | 27.6 ms: 1.14x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 76.5 ms: 1.14x faster                                                          |
| json                     | 4.76 ms                                                         | 4.22 ms: 1.13x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.13x faster                                                           |
| float                    | 69.6 ms                                                         | 62.0 ms: 1.12x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.5 ms: 1.12x faster                                                          |
| django_template          | 36.0 ms                                                         | 32.4 ms: 1.11x faster                                                          |
| tornado_http             | 118 ms                                                          | 106 ms: 1.11x faster                                                           |
| scimark_sor              | 115 ms                                                          | 103 ms: 1.11x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.27 ms: 1.10x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 255 us: 1.10x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.8 ms: 1.09x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.47 us: 1.09x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                          |
| regex_compile            | 117 ms                                                          | 109 ms: 1.07x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 179 us: 1.06x faster                                                           |
| sympy_str                | 229 ms                                                          | 217 ms: 1.06x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 76.0 ms: 1.06x faster                                                          |
| 2to3                     | 265 ms                                                          | 252 ms: 1.05x faster                                                           |
| regex_dna                | 131 ms                                                          | 124 ms: 1.05x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| mdp                      | 1.83 sec                                                        | 1.75 sec: 1.04x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.0 ms: 1.04x faster                                                          |
| richards                 | 40.3 ms                                                         | 38.8 ms: 1.04x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.32 sec: 1.04x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 642 ms: 1.02x faster                                                           |
| sympy_expand             | 391 ms                                                          | 381 ms: 1.02x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 43.9 ms: 1.02x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.19 ms: 1.02x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                         |
| sqlglot_normalize        | 230 ms                                                          | 232 ms: 1.00x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 47.0 ms: 1.01x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.02 us: 1.01x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.01x slower                                                         |
| meteor_contest           | 80.0 ms                                                         | 81.4 ms: 1.02x slower                                                          |
| pickle                   | 7.83 us                                                         | 7.97 us: 1.02x slower                                                          |
| coroutines               | 17.9 ms                                                         | 18.4 ms: 1.03x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 49.5 ms: 1.03x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.35 us: 1.04x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.2 ms: 1.06x slower                                                          |
| fannkuch                 | 317 ms                                                          | 336 ms: 1.06x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 739 us: 1.06x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.4 ms: 1.07x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 86.9 ms: 1.07x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.6 us: 1.08x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 66.7 ms: 1.08x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 72.1 ms: 1.09x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.61 us: 1.09x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.94 us: 1.09x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.4 us: 1.12x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.1 ms: 1.12x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.5 ms: 1.14x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.46 ms: 1.14x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 46.5 ns: 1.16x slower                                                          |
| scimark_fft              | 216 ms                                                          | 253 ms: 1.17x slower                                                           |
| nbody                    | 79.1 ms                                                         | 94.3 ms: 1.19x slower                                                          |
| async_generators         | 241 ms                                                          | 298 ms: 1.24x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.90 ms: 1.43x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_tcp
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.128x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown