# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-x86
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 247 ms: 1.07x faster                                                           |
| chameleon      | 6.42 ms                                                         | 6.01 ms: 1.07x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                         |
| html5lib       | 52.1 ms                                                         | 45.1 ms: 1.15x faster                                                          |
| tornado_http   | 118 ms                                                          | 95.8 ms: 1.23x faster                                                          |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 482 ms: 1.91x faster                                                           |
| async_tree_io           | 940 ms                                                          | 536 ms: 1.75x faster                                                           |
| async_tree_none         | 394 ms                                                          | 229 ms: 1.72x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 279 ms: 1.68x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.76x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                           |
| float          | 69.6 ms                                                         | 40.6 ms: 1.71x faster                                                          |
| nbody          | 79.1 ms                                                         | 53.3 ms: 1.49x faster                                                          |
| Geometric mean | (ref)                                                           | 1.87x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 90.7 ms: 1.29x faster                                                          |
| regex_dna      | 131 ms                                                          | 121 ms: 1.08x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.67 ms: 1.47x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 199 us: 1.40x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 135 us: 1.40x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.42 sec: 1.35x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 39.9 ms: 1.21x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 60.4 ms: 1.17x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 103 ms: 1.17x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 54.9 ms: 1.12x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.1 us: 1.06x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.88 us: 1.04x faster                                                          |
| pickle               | 7.83 us                                                         | 8.16 us: 1.04x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.04x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.62 us: 1.12x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.9 us: 1.15x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.2 ms: 1.06x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.30 ms: 1.72x faster                                                          |
| django_template | 36.0 ms                                                         | 30.9 ms: 1.17x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.5 ms: 1.03x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 51.8 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.78x faster                                                           |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 482 ms: 1.91x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 53.9 ns: 1.82x faster                                                          |
| async_tree_io            | 940 ms                                                          | 536 ms: 1.75x faster                                                           |
| async_tree_none          | 394 ms                                                          | 229 ms: 1.72x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.30 ms: 1.72x faster                                                          |
| float                    | 69.6 ms                                                         | 40.6 ms: 1.71x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 47.5 ms: 1.69x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 279 ms: 1.68x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 49.2 ms: 1.65x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.51 ms: 1.61x faster                                                          |
| pylint                   | 384 ms                                                          | 240 ms: 1.60x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.2 us: 1.58x faster                                                          |
| raytrace                 | 303 ms                                                          | 198 ms: 1.52x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.5 ms: 1.49x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 895 us: 1.49x faster                                                           |
| nbody                    | 79.1 ms                                                         | 53.3 ms: 1.49x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.67 ms: 1.47x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 20.3 us: 1.46x faster                                                          |
| pyflate                  | 422 ms                                                          | 292 ms: 1.44x faster                                                           |
| richards_super           | 49.9 ms                                                         | 34.9 ms: 1.43x faster                                                          |
| fannkuch                 | 317 ms                                                          | 224 ms: 1.42x faster                                                           |
| chaos                    | 74.4 ms                                                         | 52.8 ms: 1.41x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 199 us: 1.40x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.32 ms: 1.40x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 135 us: 1.40x faster                                                           |
| generators               | 31.6 ms                                                         | 22.6 ms: 1.39x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.43 ms: 1.39x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.15 ms: 1.37x faster                                                          |
| go                       | 146 ms                                                          | 107 ms: 1.36x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.42 sec: 1.35x faster                                                         |
| richards                 | 40.3 ms                                                         | 30.3 ms: 1.33x faster                                                          |
| scimark_fft              | 216 ms                                                          | 167 ms: 1.29x faster                                                           |
| pycparser                | 1.04 sec                                                        | 805 ms: 1.29x faster                                                           |
| regex_compile            | 117 ms                                                          | 90.7 ms: 1.29x faster                                                          |
| thrift                   | 902 us                                                          | 703 us: 1.28x faster                                                           |
| scimark_sor              | 115 ms                                                          | 89.7 ms: 1.28x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 68.8 ms: 1.27x faster                                                          |
| tornado_http             | 118 ms                                                          | 95.8 ms: 1.23x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 73.4 ms: 1.22x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 611 ms: 1.22x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.89 us: 1.21x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 39.9 ms: 1.21x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.16 sec: 1.18x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 60.4 ms: 1.17x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 103 ms: 1.17x faster                                                           |
| django_template          | 36.0 ms                                                         | 30.9 ms: 1.17x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 567 ms: 1.16x faster                                                           |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.15x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 45.1 ms: 1.15x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 986 us: 1.14x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 54.9 ms: 1.12x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.64 sec: 1.12x faster                                                         |
| meteor_contest           | 80.0 ms                                                         | 71.9 ms: 1.11x faster                                                          |
| coroutines               | 17.9 ms                                                         | 16.2 ms: 1.11x faster                                                          |
| sympy_str                | 229 ms                                                          | 207 ms: 1.11x faster                                                           |
| json                     | 4.76 ms                                                         | 4.39 ms: 1.08x faster                                                          |
| regex_dna                | 131 ms                                                          | 121 ms: 1.08x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                          |
| 2to3                     | 265 ms                                                          | 247 ms: 1.07x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 41.8 ms: 1.07x faster                                                          |
| chameleon                | 6.42 ms                                                         | 6.01 ms: 1.07x faster                                                          |
| json_loads               | 22.4 us                                                         | 21.1 us: 1.06x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 218 ms: 1.06x faster                                                           |
| sympy_expand             | 391 ms                                                          | 370 ms: 1.06x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.88 sec: 1.04x faster                                                         |
| unpickle_list            | 2.98 us                                                         | 2.88 us: 1.04x faster                                                          |
| deepcopy                 | 310 us                                                          | 300 us: 1.03x faster                                                           |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| logging_format           | 7.91 us                                                         | 7.98 us: 1.01x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.73 us: 1.02x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 21.5 ms: 1.03x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.16 us: 1.04x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.2 ms: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 85.8 ms: 1.06x slower                                                          |
| coverage                 | 46.6 ms                                                         | 49.6 ms: 1.07x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 754 us: 1.09x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 51.8 ms: 1.11x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 74.4 ms: 1.12x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.62 us: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.47 ms: 1.13x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.9 us: 1.15x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| async_generators         | 241 ms                                                          | 293 ms: 1.22x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, logging_simple
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown