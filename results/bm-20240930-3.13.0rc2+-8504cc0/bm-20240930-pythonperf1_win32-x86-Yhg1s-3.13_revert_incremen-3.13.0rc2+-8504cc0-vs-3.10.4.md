# Results vs. 3.10.4

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: windows-x86
- commit hash: 8504cc0
- commit date: 2024-09-30
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 243 ms: 1.09x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.73 ms: 1.12x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                          |
| html5lib       | 52.1 ms                                                         | 45.7 ms: 1.14x faster                                                           |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                            |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 480 ms: 1.92x faster                                                            |
| async_tree_io           | 940 ms                                                          | 515 ms: 1.83x faster                                                            |
| async_tree_none         | 394 ms                                                          | 238 ms: 1.65x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 290 ms: 1.61x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.75x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.57x faster                                                            |
| float          | 69.6 ms                                                         | 54.8 ms: 1.27x faster                                                           |
| nbody          | 79.1 ms                                                         | 75.5 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.51x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 100 ms: 1.17x faster                                                            |
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.06 ms: 1.39x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 150 us: 1.26x faster                                                            |
| pickle_pure_python   | 280 us                                                          | 225 us: 1.24x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.0 ms: 1.14x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 106 ms: 1.13x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 43.9 ms: 1.10x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 60.1 ms: 1.03x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.94 us: 1.01x faster                                                           |
| pickle               | 7.83 us                                                         | 7.98 us: 1.02x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.39 us: 1.06x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.3 us: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                           |
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.90 ms: 1.32x faster                                                           |
| django_template | 36.0 ms                                                         | 30.1 ms: 1.20x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 44.4 ms: 1.05x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 20.3 ms: 1.04x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.14x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 138 us: 2.86x faster                                                            |
| pidigits                 | 502 ms                                                          | 196 ms: 2.57x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 480 ms: 1.92x faster                                                            |
| async_tree_io            | 940 ms                                                          | 515 ms: 1.83x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.23 ms: 1.81x faster                                                           |
| pylint                   | 384 ms                                                          | 221 ms: 1.74x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 58.4 ns: 1.68x faster                                                           |
| async_tree_none          | 394 ms                                                          | 238 ms: 1.65x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 290 ms: 1.61x faster                                                            |
| raytrace                 | 303 ms                                                          | 189 ms: 1.60x faster                                                            |
| chaos                    | 74.4 ms                                                         | 47.3 ms: 1.57x faster                                                           |
| generators               | 31.6 ms                                                         | 21.4 ms: 1.48x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 61.0 ms: 1.47x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 55.8 ms: 1.46x faster                                                           |
| comprehensions           | 17.7 us                                                         | 12.2 us: 1.46x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.38 ms: 1.40x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.06 ms: 1.39x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 962 us: 1.38x faster                                                            |
| go                       | 146 ms                                                          | 106 ms: 1.37x faster                                                            |
| richards_super           | 49.9 ms                                                         | 36.5 ms: 1.37x faster                                                           |
| scimark_sor              | 115 ms                                                          | 84.6 ms: 1.36x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 46.6 ms: 1.33x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.19 ms: 1.33x faster                                                           |
| mako                     | 9.10 ms                                                         | 6.90 ms: 1.32x faster                                                           |
| pyflate                  | 422 ms                                                          | 326 ms: 1.30x faster                                                            |
| float                    | 69.6 ms                                                         | 54.8 ms: 1.27x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 69.0 ms: 1.26x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 150 us: 1.26x faster                                                            |
| pycparser                | 1.04 sec                                                        | 834 ms: 1.25x faster                                                            |
| richards                 | 40.3 ms                                                         | 32.3 ms: 1.25x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 225 us: 1.24x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 24.7 us: 1.20x faster                                                           |
| django_template          | 36.0 ms                                                         | 30.1 ms: 1.20x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.1 ms: 1.19x faster                                                           |
| regex_compile            | 117 ms                                                          | 100 ms: 1.17x faster                                                            |
| spectral_norm            | 80.2 ms                                                         | 68.8 ms: 1.17x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.97 us: 1.16x faster                                                           |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.16x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.82 ms: 1.15x faster                                                           |
| fannkuch                 | 317 ms                                                          | 277 ms: 1.14x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.7 ms: 1.14x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.0 ms: 1.14x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 45.7 ms: 1.14x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 983 us: 1.14x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 106 ms: 1.13x faster                                                            |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.21 sec: 1.13x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                          |
| json                     | 4.76 ms                                                         | 4.23 ms: 1.13x faster                                                           |
| chameleon                | 6.42 ms                                                         | 5.73 ms: 1.12x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 14.9 ms: 1.12x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.63 sec: 1.12x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 591 ms: 1.11x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 209 ms: 1.10x faster                                                            |
| xml_etree_process        | 48.1 ms                                                         | 43.9 ms: 1.10x faster                                                           |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 41.0 ms: 1.09x faster                                                           |
| 2to3                     | 265 ms                                                          | 243 ms: 1.09x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.79 sec: 1.09x faster                                                          |
| deepcopy                 | 310 us                                                          | 287 us: 1.08x faster                                                            |
| sympy_str                | 229 ms                                                          | 212 ms: 1.08x faster                                                            |
| scimark_fft              | 216 ms                                                          | 200 ms: 1.08x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 74.8 ms: 1.07x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 44.4 ms: 1.05x faster                                                           |
| nbody                    | 79.1 ms                                                         | 75.5 ms: 1.05x faster                                                           |
| sympy_expand             | 391 ms                                                          | 374 ms: 1.04x faster                                                            |
| genshi_text              | 21.0 ms                                                         | 20.3 ms: 1.04x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 60.1 ms: 1.03x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.94 us: 1.01x faster                                                           |
| flaskblogging            | 2.03 sec                                                        | 2.04 sec: 1.00x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                          |
| pickle                   | 7.83 us                                                         | 7.98 us: 1.02x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.58 us: 1.04x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.26 us: 1.04x slower                                                           |
| python_startup           | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.39 us: 1.06x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 88.6 ms: 1.09x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.3 us: 1.11x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 74.1 ms: 1.12x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                           |
| async_generators         | 241 ms                                                          | 274 ms: 1.14x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 49.4 ns: 1.23x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.55 ms: 1.36x slower                                                           |
| coverage                 | 46.6 ms                                                         | 320 ms: 6.88x slower                                                            |
| thrift                   | 902 us                                                          | 10.1 ms: 11.16x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.12x faster                                                                    |

Benchmark hidden because not significant (4): deepcopy_reduce, create_gc_cycles, regex_v8, asyncio_tcp
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240930-3.13.0rc2+-8504cc0/bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown