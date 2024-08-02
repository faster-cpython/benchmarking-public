# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-x86
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 235 ms: 1.13x faster                                                           |
| chameleon      | 6.42 ms                                                         | 5.69 ms: 1.13x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                                         |
| html5lib       | 52.1 ms                                                         | 44.7 ms: 1.17x faster                                                          |
| tornado_http   | 118 ms                                                          | 94.0 ms: 1.25x faster                                                          |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 496 ms: 1.86x faster                                                           |
| async_tree_io           | 940 ms                                                          | 533 ms: 1.77x faster                                                           |
| async_tree_none         | 394 ms                                                          | 228 ms: 1.72x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 277 ms: 1.68x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.76x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| float          | 69.6 ms                                                         | 53.5 ms: 1.30x faster                                                          |
| Geometric mean | (ref)                                                           | 1.49x faster                                                                   |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 97.6 ms: 1.19x faster                                                          |
| regex_dna      | 131 ms                                                          | 117 ms: 1.12x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.04 ms: 1.39x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 150 us: 1.26x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 223 us: 1.26x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 103 ms: 1.17x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.64 sec: 1.17x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 42.5 ms: 1.13x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.5 ms: 1.12x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 60.0 ms: 1.03x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 3.03 us: 1.02x slower                                                          |
| pickle               | 7.83 us                                                         | 7.97 us: 1.02x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.04x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.51 us: 1.09x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.7 us: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.6 ms: 1.01x faster                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.12 ms: 1.28x faster                                                          |
| django_template | 36.0 ms                                                         | 29.4 ms: 1.23x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 19.3 ms: 1.09x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 44.4 ms: 1.05x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 133 us: 2.98x faster                                                           |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 496 ms: 1.86x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.22 ms: 1.81x faster                                                          |
| async_tree_io            | 940 ms                                                          | 533 ms: 1.77x faster                                                           |
| pylint                   | 384 ms                                                          | 218 ms: 1.76x faster                                                           |
| async_tree_none          | 394 ms                                                          | 228 ms: 1.72x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 57.8 ns: 1.69x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 277 ms: 1.68x faster                                                           |
| raytrace                 | 303 ms                                                          | 183 ms: 1.65x faster                                                           |
| chaos                    | 74.4 ms                                                         | 46.6 ms: 1.60x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.8 us: 1.51x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 54.6 ms: 1.49x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 61.0 ms: 1.47x faster                                                          |
| generators               | 31.6 ms                                                         | 21.7 ms: 1.46x faster                                                          |
| go                       | 146 ms                                                          | 102 ms: 1.42x faster                                                           |
| richards_super           | 49.9 ms                                                         | 35.4 ms: 1.41x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.38 ms: 1.40x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.04 ms: 1.39x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 954 us: 1.39x faster                                                           |
| pyflate                  | 422 ms                                                          | 310 ms: 1.36x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.19 ms: 1.33x faster                                                          |
| pycparser                | 1.04 sec                                                        | 795 ms: 1.31x faster                                                           |
| float                    | 69.6 ms                                                         | 53.5 ms: 1.30x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 48.3 ms: 1.28x faster                                                          |
| richards                 | 40.3 ms                                                         | 31.5 ms: 1.28x faster                                                          |
| mako                     | 9.10 ms                                                         | 7.12 ms: 1.28x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 68.5 ms: 1.27x faster                                                          |
| thrift                   | 902 us                                                          | 709 us: 1.27x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 150 us: 1.26x faster                                                           |
| scimark_sor              | 115 ms                                                          | 91.4 ms: 1.26x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 223 us: 1.26x faster                                                           |
| tornado_http             | 118 ms                                                          | 94.0 ms: 1.25x faster                                                          |
| django_template          | 36.0 ms                                                         | 29.4 ms: 1.23x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 24.6 us: 1.20x faster                                                          |
| regex_compile            | 117 ms                                                          | 97.6 ms: 1.19x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                          |
| sympy_sum                | 122 ms                                                          | 104 ms: 1.18x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 68.4 ms: 1.17x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 103 ms: 1.17x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.64 sec: 1.17x faster                                                         |
| html5lib                 | 52.1 ms                                                         | 44.7 ms: 1.17x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 969 us: 1.16x faster                                                           |
| json                     | 4.76 ms                                                         | 4.16 ms: 1.14x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 651 ms: 1.14x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 14.6 ms: 1.14x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.61 sec: 1.13x faster                                                         |
| xml_etree_process        | 48.1 ms                                                         | 42.5 ms: 1.13x faster                                                          |
| 2to3                     | 265 ms                                                          | 235 ms: 1.13x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 39.6 ms: 1.13x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 204 ms: 1.13x faster                                                           |
| chameleon                | 6.42 ms                                                         | 5.69 ms: 1.13x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.22 sec: 1.12x faster                                                         |
| sympy_str                | 229 ms                                                          | 205 ms: 1.12x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.5 ms: 1.12x faster                                                          |
| regex_dna                | 131 ms                                                          | 117 ms: 1.12x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.1 ms: 1.11x faster                                                          |
| fannkuch                 | 317 ms                                                          | 288 ms: 1.10x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 599 ms: 1.10x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.95 ms: 1.10x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                                          |
| genshi_text              | 21.0 ms                                                         | 19.3 ms: 1.09x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                                         |
| sympy_expand             | 391 ms                                                          | 365 ms: 1.07x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 75.3 ms: 1.06x faster                                                          |
| deepcopy                 | 310 us                                                          | 292 us: 1.06x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 44.4 ms: 1.05x faster                                                          |
| scimark_fft              | 216 ms                                                          | 207 ms: 1.05x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 60.0 ms: 1.03x faster                                                          |
| python_startup           | 22.9 ms                                                         | 22.6 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.66 us: 1.01x faster                                                          |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                         |
| unpickle_list            | 2.98 us                                                         | 3.03 us: 1.02x slower                                                          |
| pickle                   | 7.83 us                                                         | 7.97 us: 1.02x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.66 us: 1.05x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.31 us: 1.05x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.0 ms: 1.05x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 732 us: 1.06x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 85.8 ms: 1.06x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 71.9 ms: 1.08x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.51 us: 1.09x slower                                                          |
| coverage                 | 46.6 ms                                                         | 50.9 ms: 1.09x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.7 us: 1.13x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                          |
| async_generators         | 241 ms                                                          | 276 ms: 1.14x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.28 ms: 1.30x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (2): nbody, regex_v8
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown