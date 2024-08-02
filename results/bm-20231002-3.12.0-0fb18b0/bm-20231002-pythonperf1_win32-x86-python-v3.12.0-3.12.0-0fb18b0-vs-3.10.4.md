
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0
- machine: windows-x86
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.01x slower
- HPT reliability: 97.16%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 280 ms: 1.05x slower                                            |
| chameleon      | 6.42 ms                                                         | 7.75 ms: 1.21x slower                                           |
| docutils       | 1.95 sec                                                        | 1.98 sec: 1.02x slower                                          |
| tornado_http   | 118 ms                                                          | 105 ms: 1.12x faster                                            |
| Geometric mean | (ref)                                                           | 1.04x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 564 ms: 1.64x faster                                            |
| async_tree_io           | 940 ms                                                          | 693 ms: 1.36x faster                                            |
| async_tree_none         | 394 ms                                                          | 298 ms: 1.32x faster                                            |
| async_tree_memoization  | 467 ms                                                          | 364 ms: 1.28x faster                                            |
| Geometric mean          | (ref)                                                           | 1.39x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.52x faster                                            |
| float          | 69.6 ms                                                         | 76.7 ms: 1.10x slower                                           |
| nbody          | 79.1 ms                                                         | 127 ms: 1.60x slower                                            |
| Geometric mean | (ref)                                                           | 1.13x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 15.0 ms: 1.05x faster                                           |
| regex_dna      | 131 ms                                                          | 127 ms: 1.03x faster                                            |
| regex_compile  | 117 ms                                                          | 129 ms: 1.11x slower                                            |
| regex_effbot   | 1.66 ms                                                         | 2.04 ms: 1.22x slower                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.40 ms: 1.33x faster                                           |
| json_loads           | 22.4 us                                                         | 20.4 us: 1.10x faster                                           |
| xml_etree_parse      | 120 ms                                                          | 113 ms: 1.06x faster                                            |
| unpickle_list        | 2.98 us                                                         | 2.95 us: 1.01x faster                                           |
| unpickle             | 9.82 us                                                         | 9.71 us: 1.01x faster                                           |
| pickle_pure_python   | 280 us                                                          | 286 us: 1.02x slower                                            |
| pickle_list          | 3.22 us                                                         | 3.37 us: 1.05x slower                                           |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 77.6 ms: 1.10x slower                                           |
| xml_etree_process    | 48.1 ms                                                         | 53.2 ms: 1.11x slower                                           |
| unpickle_pure_python | 189 us                                                          | 210 us: 1.11x slower                                            |
| tomli_loads          | 1.91 sec                                                        | 2.20 sec: 1.15x slower                                          |
| xml_etree_generate   | 61.6 ms                                                         | 72.1 ms: 1.17x slower                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                    |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.4 ms: 1.03x faster                                           |
| python_startup_no_site | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                           |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 36.0 ms                                                         | 36.9 ms: 1.02x slower                                           |
| mako            | 9.10 ms                                                         | 9.96 ms: 1.09x slower                                           |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 126 us: 3.13x faster                                            |
| pidigits                 | 502 ms                                                          | 199 ms: 2.52x faster                                            |
| sqlglot_normalize        | 230 ms                                                          | 100 ms: 2.30x faster                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 564 ms: 1.64x faster                                            |
| async_tree_io            | 940 ms                                                          | 693 ms: 1.36x faster                                            |
| json_dumps               | 9.82 ms                                                         | 7.40 ms: 1.33x faster                                           |
| async_tree_none          | 394 ms                                                          | 298 ms: 1.32x faster                                            |
| async_tree_memoization   | 467 ms                                                          | 364 ms: 1.28x faster                                            |
| crypto_pyaes             | 81.3 ms                                                         | 69.2 ms: 1.17x faster                                           |
| json                     | 4.76 ms                                                         | 4.15 ms: 1.15x faster                                           |
| deltablue                | 4.04 ms                                                         | 3.58 ms: 1.13x faster                                           |
| asyncio_tcp              | 744 ms                                                          | 662 ms: 1.12x faster                                            |
| tornado_http             | 118 ms                                                          | 105 ms: 1.12x faster                                            |
| sqlite_synth             | 2.29 us                                                         | 2.07 us: 1.11x faster                                           |
| json_loads               | 22.4 us                                                         | 20.4 us: 1.10x faster                                           |
| aiohttp                  | 1.13 ms                                                         | 1.06 ms: 1.08x faster                                           |
| richards_super           | 49.9 ms                                                         | 46.5 ms: 1.07x faster                                           |
| chaos                    | 74.4 ms                                                         | 69.4 ms: 1.07x faster                                           |
| sqlalchemy_imperative    | 13.2 ms                                                         | 12.3 ms: 1.07x faster                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.25 ms: 1.07x faster                                           |
| pycparser                | 1.04 sec                                                        | 978 ms: 1.07x faster                                            |
| create_gc_cycles         | 694 us                                                          | 652 us: 1.06x faster                                            |
| xml_etree_parse          | 120 ms                                                          | 113 ms: 1.06x faster                                            |
| go                       | 146 ms                                                          | 137 ms: 1.06x faster                                            |
| dask                     | 341 ms                                                          | 323 ms: 1.06x faster                                            |
| regex_v8                 | 15.8 ms                                                         | 15.0 ms: 1.05x faster                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.53 ms: 1.03x faster                                           |
| regex_dna                | 131 ms                                                          | 127 ms: 1.03x faster                                            |
| python_startup           | 22.9 ms                                                         | 22.4 ms: 1.03x faster                                           |
| sqlalchemy_declarative   | 104 ms                                                          | 103 ms: 1.01x faster                                            |
| unpickle_list            | 2.98 us                                                         | 2.95 us: 1.01x faster                                           |
| unpickle                 | 9.82 us                                                         | 9.71 us: 1.01x faster                                           |
| raytrace                 | 303 ms                                                          | 308 ms: 1.02x slower                                            |
| docutils                 | 1.95 sec                                                        | 1.98 sec: 1.02x slower                                          |
| sympy_expand             | 391 ms                                                          | 398 ms: 1.02x slower                                            |
| pickle_pure_python       | 280 us                                                          | 286 us: 1.02x slower                                            |
| django_template          | 36.0 ms                                                         | 36.9 ms: 1.02x slower                                           |
| richards                 | 40.3 ms                                                         | 41.3 ms: 1.03x slower                                           |
| logging_silent           | 97.9 ns                                                         | 101 ns: 1.03x slower                                            |
| scimark_lu               | 89.8 ms                                                         | 93.2 ms: 1.04x slower                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.7 sec: 1.04x slower                                          |
| coverage                 | 46.6 ms                                                         | 48.4 ms: 1.04x slower                                           |
| sympy_str                | 229 ms                                                          | 240 ms: 1.05x slower                                            |
| mdp                      | 1.83 sec                                                        | 1.91 sec: 1.05x slower                                          |
| pickle_list              | 3.22 us                                                         | 3.37 us: 1.05x slower                                           |
| sympy_integrate          | 16.6 ms                                                         | 17.5 ms: 1.05x slower                                           |
| 2to3                     | 265 ms                                                          | 280 ms: 1.05x slower                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 66.4 ms: 1.07x slower                                           |
| nqueens                  | 87.1 ms                                                         | 93.7 ms: 1.08x slower                                           |
| comprehensions           | 17.7 us                                                         | 19.2 us: 1.08x slower                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 48.5 ms: 1.08x slower                                           |
| meteor_contest           | 80.0 ms                                                         | 86.9 ms: 1.09x slower                                           |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                           |
| mako                     | 9.10 ms                                                         | 9.96 ms: 1.09x slower                                           |
| pprint_safe_repr         | 658 ms                                                          | 721 ms: 1.09x slower                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.50 sec: 1.10x slower                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 77.6 ms: 1.10x slower                                           |
| float                    | 69.6 ms                                                         | 76.7 ms: 1.10x slower                                           |
| xml_etree_process        | 48.1 ms                                                         | 53.2 ms: 1.11x slower                                           |
| regex_compile            | 117 ms                                                          | 129 ms: 1.11x slower                                            |
| unpickle_pure_python     | 189 us                                                          | 210 us: 1.11x slower                                            |
| hexiom                   | 6.13 ms                                                         | 6.82 ms: 1.11x slower                                           |
| fannkuch                 | 317 ms                                                          | 354 ms: 1.11x slower                                            |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                           |
| pathlib                  | 81.2 ms                                                         | 91.4 ms: 1.13x slower                                           |
| scimark_sor              | 115 ms                                                          | 130 ms: 1.13x slower                                            |
| bench_mp_pool            | 66.4 ms                                                         | 75.4 ms: 1.14x slower                                           |
| telco                    | 4.83 ms                                                         | 5.51 ms: 1.14x slower                                           |
| tomli_loads              | 1.91 sec                                                        | 2.20 sec: 1.15x slower                                          |
| deepcopy                 | 310 us                                                          | 360 us: 1.16x slower                                            |
| coroutines               | 17.9 ms                                                         | 20.9 ms: 1.16x slower                                           |
| xml_etree_generate       | 61.6 ms                                                         | 72.1 ms: 1.17x slower                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.86 ms: 1.19x slower                                           |
| deepcopy_reduce          | 2.68 us                                                         | 3.23 us: 1.20x slower                                           |
| chameleon                | 6.42 ms                                                         | 7.75 ms: 1.21x slower                                           |
| generators               | 31.6 ms                                                         | 38.5 ms: 1.22x slower                                           |
| regex_effbot             | 1.66 ms                                                         | 2.04 ms: 1.22x slower                                           |
| scimark_fft              | 216 ms                                                          | 271 ms: 1.25x slower                                            |
| spectral_norm            | 80.2 ms                                                         | 104 ms: 1.29x slower                                            |
| deepcopy_memo            | 29.6 us                                                         | 38.4 us: 1.30x slower                                           |
| async_generators         | 241 ms                                                          | 313 ms: 1.30x slower                                            |
| logging_format           | 7.91 us                                                         | 10.4 us: 1.32x slower                                           |
| logging_simple           | 7.29 us                                                         | 9.75 us: 1.34x slower                                           |
| unpack_sequence          | 40.0 ns                                                         | 62.5 ns: 1.56x slower                                           |
| nbody                    | 79.1 ms                                                         | 127 ms: 1.60x slower                                            |
| Geometric mean           | (ref)                                                           | 1.01x slower                                                    |

Benchmark hidden because not significant (6): bench_thread_pool, mypy2, pickle, dulwich_log, sympy_sum, pyflate
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 97.16% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: unknown