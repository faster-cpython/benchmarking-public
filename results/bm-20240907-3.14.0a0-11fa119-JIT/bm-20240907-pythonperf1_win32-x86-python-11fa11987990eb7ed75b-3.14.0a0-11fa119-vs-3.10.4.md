# Results vs. 3.10.4

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-x86
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 264 ms: 1.01x faster                                                           |
| docutils       | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                                         |
| html5lib       | 52.1 ms                                                         | 46.3 ms: 1.12x faster                                                          |
| tornado_http   | 118 ms                                                          | 110 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 470 ms: 1.96x faster                                                           |
| async_tree_none         | 394 ms                                                          | 220 ms: 1.79x faster                                                           |
| async_tree_io           | 940 ms                                                          | 544 ms: 1.73x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| nbody          | 79.1 ms                                                         | 50.1 ms: 1.58x faster                                                          |
| float          | 69.6 ms                                                         | 44.5 ms: 1.57x faster                                                          |
| Geometric mean | (ref)                                                           | 1.85x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 101 ms: 1.16x faster                                                           |
| regex_dna      | 131 ms                                                          | 129 ms: 1.01x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 2.00 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.92 ms: 1.42x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.48 sec: 1.29x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 40.1 ms: 1.20x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 161 us: 1.17x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 241 us: 1.16x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 53.3 ms: 1.16x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.14x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.4 ms: 1.14x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.79 us: 1.07x faster                                                          |
| pickle_list          | 3.22 us                                                         | 3.43 us: 1.07x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.6 us: 1.08x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.2 us: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 25.0 ms: 1.09x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.9 ms: 1.16x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.57 ms: 1.63x faster                                                          |
| django_template | 36.0 ms                                                         | 33.5 ms: 1.07x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 23.7 ms: 1.13x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 55.6 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 145 us: 2.73x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 100 ms: 2.30x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.04 ms: 1.98x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 470 ms: 1.96x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 15.7 us: 1.89x faster                                                          |
| async_tree_none          | 394 ms                                                          | 220 ms: 1.79x faster                                                           |
| async_tree_io            | 940 ms                                                          | 544 ms: 1.73x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| scimark_sor              | 115 ms                                                          | 68.1 ms: 1.69x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.4 ms: 1.68x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.57 ms: 1.63x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 49.2 ms: 1.63x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 61.5 ns: 1.59x faster                                                          |
| nbody                    | 79.1 ms                                                         | 50.1 ms: 1.58x faster                                                          |
| float                    | 69.6 ms                                                         | 44.5 ms: 1.57x faster                                                          |
| pyflate                  | 422 ms                                                          | 275 ms: 1.53x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 60.3 ms: 1.49x faster                                                          |
| comprehensions           | 17.7 us                                                         | 12.0 us: 1.48x faster                                                          |
| go                       | 146 ms                                                          | 98.9 ms: 1.47x faster                                                          |
| pylint                   | 384 ms                                                          | 270 ms: 1.42x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.92 ms: 1.42x faster                                                          |
| richards_super           | 49.9 ms                                                         | 36.2 ms: 1.38x faster                                                          |
| chaos                    | 74.4 ms                                                         | 55.0 ms: 1.35x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.40 ms: 1.35x faster                                                          |
| fannkuch                 | 317 ms                                                          | 237 ms: 1.34x faster                                                           |
| generators               | 31.6 ms                                                         | 23.6 ms: 1.34x faster                                                          |
| deepcopy                 | 310 us                                                          | 232 us: 1.33x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.48 sec: 1.29x faster                                                         |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.28x faster                                                          |
| pycparser                | 1.04 sec                                                        | 821 ms: 1.27x faster                                                           |
| scimark_fft              | 216 ms                                                          | 172 ms: 1.26x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.6 ms: 1.25x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.96 ms: 1.24x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.86 us: 1.23x faster                                                          |
| richards                 | 40.3 ms                                                         | 32.9 ms: 1.23x faster                                                          |
| raytrace                 | 303 ms                                                          | 248 ms: 1.22x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 40.1 ms: 1.20x faster                                                          |
| thrift                   | 902 us                                                          | 756 us: 1.19x faster                                                           |
| json                     | 4.76 ms                                                         | 4.03 ms: 1.18x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 49.8 ms: 1.18x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.35 ms: 1.17x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 161 us: 1.17x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 241 us: 1.16x faster                                                           |
| regex_compile            | 117 ms                                                          | 101 ms: 1.16x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 53.3 ms: 1.16x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 574 ms: 1.15x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.14x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.20 sec: 1.14x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.4 ms: 1.14x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.3 ms: 1.12x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 996 us: 1.12x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 79.3 ms: 1.10x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 678 ms: 1.10x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.68 sec: 1.09x faster                                                         |
| django_template          | 36.0 ms                                                         | 33.5 ms: 1.07x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 74.5 ms: 1.07x faster                                                          |
| tornado_http             | 118 ms                                                          | 110 ms: 1.07x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.79 us: 1.07x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.52 us: 1.06x faster                                                          |
| sympy_sum                | 122 ms                                                          | 115 ms: 1.06x faster                                                           |
| sympy_str                | 229 ms                                                          | 224 ms: 1.02x faster                                                           |
| regex_dna                | 131 ms                                                          | 129 ms: 1.01x faster                                                           |
| 2to3                     | 265 ms                                                          | 264 ms: 1.01x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                         |
| sympy_integrate          | 16.6 ms                                                         | 16.8 ms: 1.01x slower                                                          |
| sympy_expand             | 391 ms                                                          | 402 ms: 1.03x slower                                                           |
| coroutines               | 17.9 ms                                                         | 18.5 ms: 1.03x slower                                                          |
| docutils                 | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 46.8 ms: 1.05x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.75 us: 1.06x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.43 us: 1.07x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.46 us: 1.07x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 87.4 ms: 1.08x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.6 us: 1.08x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 752 us: 1.08x slower                                                           |
| python_startup           | 22.9 ms                                                         | 25.0 ms: 1.09x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 44.2 ns: 1.10x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.2 us: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 23.7 ms: 1.13x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.9 ms: 1.16x slower                                                          |
| coverage                 | 46.6 ms                                                         | 54.7 ms: 1.17x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 55.6 ms: 1.19x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 2.00 ms: 1.20x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 80.2 ms: 1.21x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.93 ms: 1.23x slower                                                          |
| async_generators         | 241 ms                                                          | 322 ms: 1.34x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown