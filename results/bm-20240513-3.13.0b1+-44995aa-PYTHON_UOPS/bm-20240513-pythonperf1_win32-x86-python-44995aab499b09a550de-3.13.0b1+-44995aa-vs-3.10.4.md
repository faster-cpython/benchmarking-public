# Results vs. 3.10.4

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-x86
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 257 ms: 1.03x faster                                                            |
| docutils       | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                                          |
| html5lib       | 52.1 ms                                                         | 50.8 ms: 1.02x faster                                                           |
| tornado_http   | 118 ms                                                          | 99.6 ms: 1.18x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 487 ms: 1.89x faster                                                            |
| async_tree_io           | 940 ms                                                          | 534 ms: 1.76x faster                                                            |
| async_tree_none         | 394 ms                                                          | 233 ms: 1.69x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 282 ms: 1.66x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.75x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| float          | 69.6 ms                                                         | 57.2 ms: 1.22x faster                                                           |
| Geometric mean | (ref)                                                           | 1.44x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                           |
| regex_compile  | 117 ms                                                          | 126 ms: 1.08x slower                                                            |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.98 ms: 1.41x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 255 us: 1.10x faster                                                            |
| unpickle_list        | 2.98 us                                                         | 2.73 us: 1.09x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 44.5 ms: 1.08x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.5 ms: 1.07x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 181 us: 1.05x faster                                                            |
| xml_etree_generate   | 61.6 ms                                                         | 62.0 ms: 1.01x slower                                                           |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| pickle               | 7.83 us                                                         | 8.24 us: 1.05x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.64 us: 1.13x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.7 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.3 ms: 1.03x faster                                                           |
| python_startup_no_site | 18.1 ms                                                         | 18.4 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.78 ms: 1.17x faster                                                           |
| django_template | 36.0 ms                                                         | 31.9 ms: 1.13x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 20.6 ms: 1.02x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 48.4 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 146 us: 2.71x faster                                                            |
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 487 ms: 1.89x faster                                                            |
| async_tree_io            | 940 ms                                                          | 534 ms: 1.76x faster                                                            |
| async_tree_none          | 394 ms                                                          | 233 ms: 1.69x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 282 ms: 1.66x faster                                                            |
| pylint                   | 384 ms                                                          | 244 ms: 1.57x faster                                                            |
| raytrace                 | 303 ms                                                          | 214 ms: 1.41x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.98 ms: 1.41x faster                                                           |
| chaos                    | 74.4 ms                                                         | 53.3 ms: 1.40x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.90 ms: 1.39x faster                                                           |
| generators               | 31.6 ms                                                         | 23.4 ms: 1.35x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 60.2 ms: 1.35x faster                                                           |
| richards_super           | 49.9 ms                                                         | 37.1 ms: 1.34x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.03 ms: 1.29x faster                                                           |
| go                       | 146 ms                                                          | 118 ms: 1.24x faster                                                            |
| richards                 | 40.3 ms                                                         | 32.6 ms: 1.23x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.29 ms: 1.23x faster                                                           |
| pycparser                | 1.04 sec                                                        | 853 ms: 1.22x faster                                                            |
| float                    | 69.6 ms                                                         | 57.2 ms: 1.22x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.7 us: 1.21x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 81.3 ns: 1.20x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                                           |
| scimark_sor              | 115 ms                                                          | 97.1 ms: 1.19x faster                                                           |
| tornado_http             | 118 ms                                                          | 99.6 ms: 1.18x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.78 ms: 1.17x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                            |
| tomli_loads              | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 76.8 ms: 1.13x faster                                                           |
| django_template          | 36.0 ms                                                         | 31.9 ms: 1.13x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.1 ms: 1.12x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.0 ms: 1.12x faster                                                           |
| json                     | 4.76 ms                                                         | 4.25 ms: 1.12x faster                                                           |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                            |
| pickle_pure_python       | 280 us                                                          | 255 us: 1.10x faster                                                            |
| unpickle_list            | 2.98 us                                                         | 2.73 us: 1.09x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.68 sec: 1.09x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 44.5 ms: 1.08x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.04 ms: 1.08x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.5 ms: 1.07x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 84.5 ms: 1.06x faster                                                           |
| pyflate                  | 422 ms                                                          | 397 ms: 1.06x faster                                                            |
| fannkuch                 | 317 ms                                                          | 299 ms: 1.06x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 181 us: 1.05x faster                                                            |
| sympy_sum                | 122 ms                                                          | 118 ms: 1.03x faster                                                            |
| asyncio_tcp              | 744 ms                                                          | 719 ms: 1.03x faster                                                            |
| 2to3                     | 265 ms                                                          | 257 ms: 1.03x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                          |
| python_startup           | 22.9 ms                                                         | 22.3 ms: 1.03x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 50.8 ms: 1.02x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 20.6 ms: 1.02x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 78.6 ms: 1.02x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 648 ms: 1.02x faster                                                            |
| sqlglot_normalize        | 230 ms                                                          | 227 ms: 1.02x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 44.2 ms: 1.01x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 79.7 ms: 1.00x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 6.16 ms: 1.00x slower                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 62.0 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.29 ms: 1.02x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 18.4 ms: 1.02x slower                                                           |
| scimark_fft              | 216 ms                                                          | 220 ms: 1.02x slower                                                            |
| deepcopy_memo            | 29.6 us                                                         | 30.3 us: 1.02x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.03x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                           |
| sympy_str                | 229 ms                                                          | 237 ms: 1.03x slower                                                            |
| deepcopy                 | 310 us                                                          | 321 us: 1.04x slower                                                            |
| genshi_xml               | 46.6 ms                                                         | 48.4 ms: 1.04x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.81 us: 1.05x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.24 us: 1.05x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.40 us: 1.06x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.82 us: 1.07x slower                                                           |
| sympy_expand             | 391 ms                                                          | 421 ms: 1.08x slower                                                            |
| regex_compile            | 117 ms                                                          | 126 ms: 1.08x slower                                                            |
| pathlib                  | 81.2 ms                                                         | 88.3 ms: 1.09x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 761 us: 1.10x slower                                                            |
| bench_mp_pool            | 66.4 ms                                                         | 72.8 ms: 1.10x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.64 us: 1.13x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.7 us: 1.14x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.46 ms: 1.14x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                           |
| async_generators         | 241 ms                                                          | 290 ms: 1.20x slower                                                            |
| telco                    | 4.83 ms                                                         | 6.89 ms: 1.43x slower                                                           |
| coverage                 | 46.6 ms                                                         | 331 ms: 7.11x slower                                                            |
| thrift                   | 902 us                                                          | 11.8 ms: 13.04x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (5): chameleon, asyncio_tcp_ssl, flaskblogging, sympy_integrate, nbody
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown