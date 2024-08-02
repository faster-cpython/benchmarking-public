
# Results vs. 3.12.0

- fork: python
- ref: v3.10.4
- machine: windows-x86
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.01x faster
- HPT reliability: 97.16%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 265 ms: 1.05x faster                                            |
| chameleon      | 7.75 ms                                                         | 6.42 ms: 1.21x faster                                           |
| docutils       | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                          |
| tornado_http   | 105 ms                                                          | 118 ms: 1.12x slower                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization  | 364 ms                                                          | 467 ms: 1.28x slower                                            |
| async_tree_none         | 298 ms                                                          | 394 ms: 1.32x slower                                            |
| async_tree_io           | 693 ms                                                          | 940 ms: 1.36x slower                                            |
| async_tree_cpu_io_mixed | 564 ms                                                          | 922 ms: 1.64x slower                                            |
| Geometric mean          | (ref)                                                           | 1.39x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 79.1 ms: 1.60x faster                                           |
| float          | 76.7 ms                                                         | 69.6 ms: 1.10x faster                                           |
| pidigits       | 199 ms                                                          | 502 ms: 2.52x slower                                            |
| Geometric mean | (ref)                                                           | 1.13x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.66 ms: 1.22x faster                                           |
| regex_compile  | 129 ms                                                          | 117 ms: 1.11x faster                                            |
| regex_dna      | 127 ms                                                          | 131 ms: 1.03x slower                                            |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_generate   | 72.1 ms                                                         | 61.6 ms: 1.17x faster                                           |
| tomli_loads          | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                          |
| unpickle_pure_python | 210 us                                                          | 189 us: 1.11x faster                                            |
| xml_etree_process    | 53.2 ms                                                         | 48.1 ms: 1.11x faster                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 70.8 ms: 1.10x faster                                           |
| pickle_dict          | 19.9 us                                                         | 18.2 us: 1.09x faster                                           |
| pickle_list          | 3.37 us                                                         | 3.22 us: 1.05x faster                                           |
| pickle_pure_python   | 286 us                                                          | 280 us: 1.02x faster                                            |
| unpickle             | 9.71 us                                                         | 9.82 us: 1.01x slower                                           |
| unpickle_list        | 2.95 us                                                         | 2.98 us: 1.01x slower                                           |
| xml_etree_parse      | 113 ms                                                          | 120 ms: 1.06x slower                                            |
| json_loads           | 20.4 us                                                         | 22.4 us: 1.10x slower                                           |
| json_dumps           | 7.40 ms                                                         | 9.82 ms: 1.33x slower                                           |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                    |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.1 ms: 1.06x faster                                           |
| python_startup         | 22.4 ms                                                         | 22.9 ms: 1.03x slower                                           |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 9.10 ms: 1.09x faster                                           |
| django_template | 36.9 ms                                                         | 36.0 ms: 1.02x faster                                           |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody                    | 127 ms                                                          | 79.1 ms: 1.60x faster                                           |
| unpack_sequence          | 62.5 ns                                                         | 40.0 ns: 1.56x faster                                           |
| logging_simple           | 9.75 us                                                         | 7.29 us: 1.34x faster                                           |
| logging_format           | 10.4 us                                                         | 7.91 us: 1.32x faster                                           |
| async_generators         | 313 ms                                                          | 241 ms: 1.30x faster                                            |
| deepcopy_memo            | 38.4 us                                                         | 29.6 us: 1.30x faster                                           |
| spectral_norm            | 104 ms                                                          | 80.2 ms: 1.29x faster                                           |
| scimark_fft              | 271 ms                                                          | 216 ms: 1.25x faster                                            |
| regex_effbot             | 2.04 ms                                                         | 1.66 ms: 1.22x faster                                           |
| generators               | 38.5 ms                                                         | 31.6 ms: 1.22x faster                                           |
| chameleon                | 7.75 ms                                                         | 6.42 ms: 1.21x faster                                           |
| deepcopy_reduce          | 3.23 us                                                         | 2.68 us: 1.20x faster                                           |
| scimark_sparse_mat_mult  | 3.86 ms                                                         | 3.24 ms: 1.19x faster                                           |
| xml_etree_generate       | 72.1 ms                                                         | 61.6 ms: 1.17x faster                                           |
| coroutines               | 20.9 ms                                                         | 17.9 ms: 1.16x faster                                           |
| deepcopy                 | 360 us                                                          | 310 us: 1.16x faster                                            |
| tomli_loads              | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                          |
| telco                    | 5.51 ms                                                         | 4.83 ms: 1.14x faster                                           |
| bench_mp_pool            | 75.4 ms                                                         | 66.4 ms: 1.14x faster                                           |
| scimark_sor              | 130 ms                                                          | 115 ms: 1.13x faster                                            |
| pathlib                  | 91.4 ms                                                         | 81.2 ms: 1.13x faster                                           |
| gc_traversal             | 1.44 ms                                                         | 1.28 ms: 1.13x faster                                           |
| fannkuch                 | 354 ms                                                          | 317 ms: 1.11x faster                                            |
| hexiom                   | 6.82 ms                                                         | 6.13 ms: 1.11x faster                                           |
| unpickle_pure_python     | 210 us                                                          | 189 us: 1.11x faster                                            |
| regex_compile            | 129 ms                                                          | 117 ms: 1.11x faster                                            |
| xml_etree_process        | 53.2 ms                                                         | 48.1 ms: 1.11x faster                                           |
| float                    | 76.7 ms                                                         | 69.6 ms: 1.10x faster                                           |
| xml_etree_iterparse      | 77.6 ms                                                         | 70.8 ms: 1.10x faster                                           |
| pprint_pformat           | 1.50 sec                                                        | 1.37 sec: 1.10x faster                                          |
| pprint_safe_repr         | 721 ms                                                          | 658 ms: 1.09x faster                                            |
| mako                     | 9.96 ms                                                         | 9.10 ms: 1.09x faster                                           |
| pickle_dict              | 19.9 us                                                         | 18.2 us: 1.09x faster                                           |
| meteor_contest           | 86.9 ms                                                         | 80.0 ms: 1.09x faster                                           |
| sqlglot_optimize         | 48.5 ms                                                         | 44.7 ms: 1.08x faster                                           |
| comprehensions           | 19.2 us                                                         | 17.7 us: 1.08x faster                                           |
| nqueens                  | 93.7 ms                                                         | 87.1 ms: 1.08x faster                                           |
| scimark_monte_carlo      | 66.4 ms                                                         | 61.9 ms: 1.07x faster                                           |
| python_startup_no_site   | 19.1 ms                                                         | 18.1 ms: 1.06x faster                                           |
| 2to3                     | 280 ms                                                          | 265 ms: 1.05x faster                                            |
| sympy_integrate          | 17.5 ms                                                         | 16.6 ms: 1.05x faster                                           |
| pickle_list              | 3.37 us                                                         | 3.22 us: 1.05x faster                                           |
| mdp                      | 1.91 sec                                                        | 1.83 sec: 1.05x faster                                          |
| sympy_str                | 240 ms                                                          | 229 ms: 1.05x faster                                            |
| coverage                 | 48.4 ms                                                         | 46.6 ms: 1.04x faster                                           |
| asyncio_tcp_ssl          | 17.7 sec                                                        | 17.0 sec: 1.04x faster                                          |
| scimark_lu               | 93.2 ms                                                         | 89.8 ms: 1.04x faster                                           |
| logging_silent           | 101 ns                                                          | 97.9 ns: 1.03x faster                                           |
| richards                 | 41.3 ms                                                         | 40.3 ms: 1.03x faster                                           |
| django_template          | 36.9 ms                                                         | 36.0 ms: 1.02x faster                                           |
| pickle_pure_python       | 286 us                                                          | 280 us: 1.02x faster                                            |
| sympy_expand             | 398 ms                                                          | 391 ms: 1.02x faster                                            |
| docutils                 | 1.98 sec                                                        | 1.95 sec: 1.02x faster                                          |
| raytrace                 | 308 ms                                                          | 303 ms: 1.02x faster                                            |
| unpickle                 | 9.71 us                                                         | 9.82 us: 1.01x slower                                           |
| unpickle_list            | 2.95 us                                                         | 2.98 us: 1.01x slower                                           |
| sqlalchemy_declarative   | 103 ms                                                          | 104 ms: 1.01x slower                                            |
| python_startup           | 22.4 ms                                                         | 22.9 ms: 1.03x slower                                           |
| regex_dna                | 127 ms                                                          | 131 ms: 1.03x slower                                            |
| sqlglot_transpile        | 1.53 ms                                                         | 1.58 ms: 1.03x slower                                           |
| regex_v8                 | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                           |
| dask                     | 323 ms                                                          | 341 ms: 1.06x slower                                            |
| go                       | 137 ms                                                          | 146 ms: 1.06x slower                                            |
| xml_etree_parse          | 113 ms                                                          | 120 ms: 1.06x slower                                            |
| create_gc_cycles         | 652 us                                                          | 694 us: 1.06x slower                                            |
| pycparser                | 978 ms                                                          | 1.04 sec: 1.07x slower                                          |
| sqlglot_parse            | 1.25 ms                                                         | 1.33 ms: 1.07x slower                                           |
| sqlalchemy_imperative    | 12.3 ms                                                         | 13.2 ms: 1.07x slower                                           |
| chaos                    | 69.4 ms                                                         | 74.4 ms: 1.07x slower                                           |
| richards_super           | 46.5 ms                                                         | 49.9 ms: 1.07x slower                                           |
| aiohttp                  | 1.06 ms                                                         | 1.13 ms: 1.08x slower                                           |
| json_loads               | 20.4 us                                                         | 22.4 us: 1.10x slower                                           |
| sqlite_synth             | 2.07 us                                                         | 2.29 us: 1.11x slower                                           |
| tornado_http             | 105 ms                                                          | 118 ms: 1.12x slower                                            |
| asyncio_tcp              | 662 ms                                                          | 744 ms: 1.12x slower                                            |
| deltablue                | 3.58 ms                                                         | 4.04 ms: 1.13x slower                                           |
| json                     | 4.15 ms                                                         | 4.76 ms: 1.15x slower                                           |
| crypto_pyaes             | 69.2 ms                                                         | 81.3 ms: 1.17x slower                                           |
| async_tree_memoization   | 364 ms                                                          | 467 ms: 1.28x slower                                            |
| async_tree_none          | 298 ms                                                          | 394 ms: 1.32x slower                                            |
| json_dumps               | 7.40 ms                                                         | 9.82 ms: 1.33x slower                                           |
| async_tree_io            | 693 ms                                                          | 940 ms: 1.36x slower                                            |
| async_tree_cpu_io_mixed  | 564 ms                                                          | 922 ms: 1.64x slower                                            |
| sqlglot_normalize        | 100 ms                                                          | 230 ms: 2.30x slower                                            |
| pidigits                 | 199 ms                                                          | 502 ms: 2.52x slower                                            |
| typing_runtime_protocols | 126 us                                                          | 396 us: 3.13x slower                                            |
| Geometric mean           | (ref)                                                           | 1.01x faster                                                    |

Benchmark hidden because not significant (6): pyflate, sympy_sum, dulwich_log, pickle, mypy2, bench_thread_pool
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 97.16% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown