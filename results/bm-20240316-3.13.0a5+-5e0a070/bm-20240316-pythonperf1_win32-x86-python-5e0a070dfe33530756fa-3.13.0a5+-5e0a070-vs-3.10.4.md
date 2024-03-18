# Results vs. 3.10.4

- fork: python
- ref: 5e0a070dfe33530756fa
- machine: windows-x86
- commit hash: 5e0a070
- commit date: 2024-03-16
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 230 ms: 1.15x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.50 ms: 1.17x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.70 sec: 1.15x faster                                                          |
| html5lib       | 52.1 ms                                                         | 42.1 ms: 1.24x faster                                                           |
| tornado_http   | 118 ms                                                          | 93.8 ms: 1.25x faster                                                           |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 497 ms: 1.86x faster                                                            |
| async_tree_none         | 394 ms                                                          | 241 ms: 1.63x faster                                                            |
| async_tree_io           | 940 ms                                                          | 585 ms: 1.61x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 303 ms: 1.54x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.66x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                            |
| float          | 69.6 ms                                                         | 52.9 ms: 1.32x faster                                                           |
| nbody          | 79.1 ms                                                         | 75.2 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.52x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 94.8 ms: 1.23x faster                                                           |
| regex_dna      | 131 ms                                                          | 117 ms: 1.12x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.60 ms: 1.49x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 199 us: 1.41x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 140 us: 1.36x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.59 sec: 1.20x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 41.0 ms: 1.17x faster                                                           |
| json_loads           | 22.4 us                                                         | 19.8 us: 1.13x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.2 ms: 1.09x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.80 us: 1.06x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 58.0 ms: 1.06x faster                                                           |
| pickle_list          | 3.22 us                                                         | 3.20 us: 1.01x faster                                                           |
| pickle               | 7.83 us                                                         | 7.98 us: 1.02x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 19.9 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.2 ms: 1.03x faster                                                           |
| python_startup_no_site | 18.1 ms                                                         | 19.8 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.82 ms: 1.34x faster                                                           |
| django_template | 36.0 ms                                                         | 27.9 ms: 1.29x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 17.7 ms: 1.19x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 41.2 ms: 1.13x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.23x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 87.8 us: 4.51x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.15 ms: 1.88x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 497 ms: 1.86x faster                                                            |
| pylint                   | 384 ms                                                          | 214 ms: 1.79x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 57.2 ns: 1.71x faster                                                           |
| async_tree_none          | 394 ms                                                          | 241 ms: 1.63x faster                                                            |
| async_tree_io            | 940 ms                                                          | 585 ms: 1.61x faster                                                            |
| comprehensions           | 17.7 us                                                         | 11.0 us: 1.61x faster                                                           |
| raytrace                 | 303 ms                                                          | 191 ms: 1.58x faster                                                            |
| richards_super           | 49.9 ms                                                         | 31.7 ms: 1.57x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 857 us: 1.55x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 303 ms: 1.54x faster                                                            |
| crypto_pyaes             | 81.3 ms                                                         | 53.0 ms: 1.53x faster                                                           |
| go                       | 146 ms                                                          | 95.2 ms: 1.53x faster                                                           |
| chaos                    | 74.4 ms                                                         | 48.7 ms: 1.53x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 58.9 ms: 1.52x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.60 ms: 1.49x faster                                                           |
| scimark_sor              | 115 ms                                                          | 77.9 ms: 1.48x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.09 ms: 1.45x faster                                                           |
| generators               | 31.6 ms                                                         | 21.9 ms: 1.44x faster                                                           |
| richards                 | 40.3 ms                                                         | 28.1 ms: 1.43x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.32 ms: 1.42x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 199 us: 1.41x faster                                                            |
| scimark_monte_carlo      | 61.9 ms                                                         | 44.1 ms: 1.40x faster                                                           |
| pyflate                  | 422 ms                                                          | 309 ms: 1.36x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 140 us: 1.36x faster                                                            |
| mako                     | 9.10 ms                                                         | 6.82 ms: 1.34x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 22.4 us: 1.32x faster                                                           |
| float                    | 69.6 ms                                                         | 52.9 ms: 1.32x faster                                                           |
| pycparser                | 1.04 sec                                                        | 802 ms: 1.30x faster                                                            |
| django_template          | 36.0 ms                                                         | 27.9 ms: 1.29x faster                                                           |
| coroutines               | 17.9 ms                                                         | 14.1 ms: 1.27x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 69.2 ms: 1.26x faster                                                           |
| sympy_sum                | 122 ms                                                          | 97.6 ms: 1.26x faster                                                           |
| tornado_http             | 118 ms                                                          | 93.8 ms: 1.25x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 42.1 ms: 1.24x faster                                                           |
| regex_compile            | 117 ms                                                          | 94.8 ms: 1.23x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.13 sec: 1.21x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 66.4 ms: 1.21x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                                           |
| deepcopy                 | 310 us                                                          | 258 us: 1.20x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 13.9 ms: 1.20x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.59 sec: 1.20x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 192 ms: 1.20x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 623 ms: 1.19x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 37.6 ms: 1.19x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 17.7 ms: 1.19x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 556 ms: 1.18x faster                                                            |
| sympy_str                | 229 ms                                                          | 194 ms: 1.18x faster                                                            |
| deepcopy_reduce          | 2.68 us                                                         | 2.27 us: 1.18x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 41.0 ms: 1.17x faster                                                           |
| chameleon                | 6.42 ms                                                         | 5.50 ms: 1.17x faster                                                           |
| fannkuch                 | 317 ms                                                          | 274 ms: 1.16x faster                                                            |
| sympy_expand             | 391 ms                                                          | 337 ms: 1.16x faster                                                            |
| bench_thread_pool        | 1.12 ms                                                         | 968 us: 1.16x faster                                                            |
| 2to3                     | 265 ms                                                          | 230 ms: 1.15x faster                                                            |
| json                     | 4.76 ms                                                         | 4.15 ms: 1.15x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.70 sec: 1.15x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.60 sec: 1.14x faster                                                          |
| genshi_xml               | 46.6 ms                                                         | 41.2 ms: 1.13x faster                                                           |
| json_loads               | 22.4 us                                                         | 19.8 us: 1.13x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                            |
| regex_dna                | 131 ms                                                          | 117 ms: 1.12x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.91 ms: 1.11x faster                                                           |
| create_gc_cycles         | 694 us                                                          | 638 us: 1.09x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.2 ms: 1.09x faster                                                           |
| scimark_fft              | 216 ms                                                          | 202 ms: 1.07x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.80 us: 1.06x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 58.0 ms: 1.06x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 75.7 ms: 1.06x faster                                                           |
| nbody                    | 79.1 ms                                                         | 75.2 ms: 1.05x faster                                                           |
| python_startup           | 22.9 ms                                                         | 22.2 ms: 1.03x faster                                                           |
| unpack_sequence          | 40.0 ns                                                         | 39.2 ns: 1.02x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.7 sec: 1.02x faster                                                          |
| pickle_list              | 3.22 us                                                         | 3.20 us: 1.01x faster                                                           |
| logging_format           | 7.91 us                                                         | 8.00 us: 1.01x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.41 us: 1.02x slower                                                           |
| pickle                   | 7.83 us                                                         | 7.98 us: 1.02x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 68.0 ms: 1.02x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 85.7 ms: 1.06x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.39 ms: 1.08x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 19.9 us: 1.09x slower                                                           |
| async_generators         | 241 ms                                                          | 264 ms: 1.10x slower                                                            |
| python_startup_no_site   | 18.1 ms                                                         | 19.8 ms: 1.10x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                           |
| telco                    | 4.83 ms                                                         | 5.75 ms: 1.19x slower                                                           |
| coverage                 | 46.6 ms                                                         | 453 ms: 9.73x slower                                                            |
| thrift                   | 902 us                                                          | 9.64 ms: 10.69x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.18x faster                                                                    |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240316-3.13.0a5+-5e0a070/bm-20240316-pythonperf1_win32-x86-python-5e0a070dfe33530756fa-3.13.0a5+-5e0a070.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x


# Memory

- memory change: unknown