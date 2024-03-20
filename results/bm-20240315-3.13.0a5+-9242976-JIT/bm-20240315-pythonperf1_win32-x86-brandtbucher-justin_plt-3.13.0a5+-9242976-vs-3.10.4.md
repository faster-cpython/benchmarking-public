# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_plt
- machine: windows-x86
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.04x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 262 ms: 1.01x faster                                                        |
| chameleon      | 6.42 ms                                                         | 5.91 ms: 1.09x faster                                                       |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                      |
| html5lib       | 52.1 ms                                                         | 46.4 ms: 1.12x faster                                                       |
| tornado_http   | 118 ms                                                          | 98.4 ms: 1.20x faster                                                       |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 510 ms: 1.81x faster                                                        |
| async_tree_none         | 394 ms                                                          | 261 ms: 1.51x faster                                                        |
| async_tree_io           | 940 ms                                                          | 623 ms: 1.51x faster                                                        |
| async_tree_memoization  | 467 ms                                                          | 320 ms: 1.46x faster                                                        |
| Geometric mean          | (ref)                                                           | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                        |
| float          | 69.6 ms                                                         | 54.7 ms: 1.27x faster                                                       |
| nbody          | 79.1 ms                                                         | 98.8 ms: 1.25x slower                                                       |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 122 ms: 1.07x faster                                                        |
| regex_compile  | 117 ms                                                          | 112 ms: 1.04x faster                                                        |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                       |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.98 ms: 1.41x faster                                                       |
| pickle_pure_python   | 280 us                                                          | 224 us: 1.25x faster                                                        |
| tomli_loads          | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                      |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                        |
| json_loads           | 22.4 us                                                         | 20.1 us: 1.11x faster                                                       |
| unpickle_pure_python | 189 us                                                          | 174 us: 1.09x faster                                                        |
| xml_etree_process    | 48.1 ms                                                         | 45.2 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                       |
| unpickle_list        | 2.98 us                                                         | 2.88 us: 1.04x faster                                                       |
| pickle_list          | 3.22 us                                                         | 3.19 us: 1.01x faster                                                       |
| pickle               | 7.83 us                                                         | 8.02 us: 1.02x slower                                                       |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.04x slower                                                       |
| xml_etree_generate   | 61.6 ms                                                         | 64.0 ms: 1.04x slower                                                       |
| pickle_dict          | 18.2 us                                                         | 20.0 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                       |
| python_startup_no_site | 18.1 ms                                                         | 23.6 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.21x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.88 ms: 1.32x faster                                                       |
| django_template | 36.0 ms                                                         | 31.7 ms: 1.14x faster                                                       |
| genshi_xml      | 46.6 ms                                                         | 50.9 ms: 1.09x slower                                                       |
| genshi_text     | 21.0 ms                                                         | 23.4 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 99.4 us: 3.98x faster                                                       |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                        |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 510 ms: 1.81x faster                                                        |
| pylint                   | 384 ms                                                          | 235 ms: 1.63x faster                                                        |
| async_tree_none          | 394 ms                                                          | 261 ms: 1.51x faster                                                        |
| async_tree_io            | 940 ms                                                          | 623 ms: 1.51x faster                                                        |
| deltablue                | 4.04 ms                                                         | 2.69 ms: 1.50x faster                                                       |
| async_tree_memoization   | 467 ms                                                          | 320 ms: 1.46x faster                                                        |
| logging_silent           | 97.9 ns                                                         | 67.8 ns: 1.44x faster                                                       |
| json_dumps               | 9.82 ms                                                         | 6.98 ms: 1.41x faster                                                       |
| crypto_pyaes             | 81.3 ms                                                         | 60.2 ms: 1.35x faster                                                       |
| mako                     | 9.10 ms                                                         | 6.88 ms: 1.32x faster                                                       |
| sqlglot_parse            | 1.33 ms                                                         | 1.01 ms: 1.32x faster                                                       |
| generators               | 31.6 ms                                                         | 24.3 ms: 1.30x faster                                                       |
| float                    | 69.6 ms                                                         | 54.7 ms: 1.27x faster                                                       |
| chaos                    | 74.4 ms                                                         | 59.1 ms: 1.26x faster                                                       |
| pickle_pure_python       | 280 us                                                          | 224 us: 1.25x faster                                                        |
| sqlglot_transpile        | 1.58 ms                                                         | 1.27 ms: 1.25x faster                                                       |
| richards_super           | 49.9 ms                                                         | 40.8 ms: 1.22x faster                                                       |
| sqlite_synth             | 2.29 us                                                         | 1.89 us: 1.21x faster                                                       |
| tornado_http             | 118 ms                                                          | 98.4 ms: 1.20x faster                                                       |
| coroutines               | 17.9 ms                                                         | 15.0 ms: 1.19x faster                                                       |
| comprehensions           | 17.7 us                                                         | 14.9 us: 1.19x faster                                                       |
| pycparser                | 1.04 sec                                                        | 878 ms: 1.19x faster                                                        |
| go                       | 146 ms                                                          | 125 ms: 1.16x faster                                                        |
| asyncio_tcp              | 744 ms                                                          | 641 ms: 1.16x faster                                                        |
| django_template          | 36.0 ms                                                         | 31.7 ms: 1.14x faster                                                       |
| json                     | 4.76 ms                                                         | 4.21 ms: 1.13x faster                                                       |
| raytrace                 | 303 ms                                                          | 269 ms: 1.13x faster                                                        |
| html5lib                 | 52.1 ms                                                         | 46.4 ms: 1.12x faster                                                       |
| pyflate                  | 422 ms                                                          | 377 ms: 1.12x faster                                                        |
| tomli_loads              | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                      |
| richards                 | 40.3 ms                                                         | 36.0 ms: 1.12x faster                                                       |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                        |
| json_loads               | 22.4 us                                                         | 20.1 us: 1.11x faster                                                       |
| spectral_norm            | 80.2 ms                                                         | 73.2 ms: 1.10x faster                                                       |
| deepcopy_memo            | 29.6 us                                                         | 27.1 us: 1.09x faster                                                       |
| unpickle_pure_python     | 189 us                                                          | 174 us: 1.09x faster                                                        |
| sympy_sum                | 122 ms                                                          | 112 ms: 1.09x faster                                                        |
| scimark_sor              | 115 ms                                                          | 106 ms: 1.09x faster                                                        |
| chameleon                | 6.42 ms                                                         | 5.91 ms: 1.09x faster                                                       |
| bench_thread_pool        | 1.12 ms                                                         | 1.04 ms: 1.08x faster                                                       |
| regex_dna                | 131 ms                                                          | 122 ms: 1.07x faster                                                        |
| deepcopy                 | 310 us                                                          | 291 us: 1.07x faster                                                        |
| xml_etree_process        | 48.1 ms                                                         | 45.2 ms: 1.07x faster                                                       |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.0 ms: 1.06x faster                                                       |
| create_gc_cycles         | 694 us                                                          | 661 us: 1.05x faster                                                        |
| regex_compile            | 117 ms                                                          | 112 ms: 1.04x faster                                                        |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                      |
| sympy_integrate          | 16.6 ms                                                         | 16.0 ms: 1.04x faster                                                       |
| sympy_str                | 229 ms                                                          | 220 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.11 ms: 1.04x faster                                                       |
| unpickle_list            | 2.98 us                                                         | 2.88 us: 1.04x faster                                                       |
| mdp                      | 1.83 sec                                                        | 1.76 sec: 1.04x faster                                                      |
| deepcopy_reduce          | 2.68 us                                                         | 2.60 us: 1.03x faster                                                       |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.7 sec: 1.01x faster                                                      |
| 2to3                     | 265 ms                                                          | 262 ms: 1.01x faster                                                        |
| scimark_lu               | 89.8 ms                                                         | 88.9 ms: 1.01x faster                                                       |
| pickle_list              | 3.22 us                                                         | 3.19 us: 1.01x faster                                                       |
| sympy_expand             | 391 ms                                                          | 388 ms: 1.01x faster                                                        |
| pickle                   | 7.83 us                                                         | 8.02 us: 1.02x slower                                                       |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                       |
| scimark_monte_carlo      | 61.9 ms                                                         | 64.0 ms: 1.03x slower                                                       |
| meteor_contest           | 80.0 ms                                                         | 82.9 ms: 1.04x slower                                                       |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                                       |
| xml_etree_generate       | 61.6 ms                                                         | 64.0 ms: 1.04x slower                                                       |
| sqlglot_normalize        | 230 ms                                                          | 241 ms: 1.05x slower                                                        |
| pathlib                  | 81.2 ms                                                         | 86.1 ms: 1.06x slower                                                       |
| fannkuch                 | 317 ms                                                          | 338 ms: 1.06x slower                                                        |
| sqlglot_optimize         | 44.7 ms                                                         | 48.0 ms: 1.07x slower                                                       |
| nqueens                  | 87.1 ms                                                         | 95.0 ms: 1.09x slower                                                       |
| genshi_xml               | 46.6 ms                                                         | 50.9 ms: 1.09x slower                                                       |
| pickle_dict              | 18.2 us                                                         | 20.0 us: 1.09x slower                                                       |
| scimark_fft              | 216 ms                                                          | 237 ms: 1.10x slower                                                        |
| unpack_sequence          | 40.0 ns                                                         | 44.0 ns: 1.10x slower                                                       |
| gc_traversal             | 1.28 ms                                                         | 1.42 ms: 1.11x slower                                                       |
| pprint_pformat           | 1.37 sec                                                        | 1.52 sec: 1.11x slower                                                      |
| genshi_text              | 21.0 ms                                                         | 23.4 ms: 1.12x slower                                                       |
| python_startup           | 22.9 ms                                                         | 25.8 ms: 1.13x slower                                                       |
| bench_mp_pool            | 66.4 ms                                                         | 74.7 ms: 1.13x slower                                                       |
| logging_format           | 7.91 us                                                         | 8.96 us: 1.13x slower                                                       |
| pprint_safe_repr         | 658 ms                                                          | 746 ms: 1.13x slower                                                        |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.13x slower                                                       |
| logging_simple           | 7.29 us                                                         | 8.31 us: 1.14x slower                                                       |
| async_generators         | 241 ms                                                          | 292 ms: 1.21x slower                                                        |
| nbody                    | 79.1 ms                                                         | 98.8 ms: 1.25x slower                                                       |
| python_startup_no_site   | 18.1 ms                                                         | 23.6 ms: 1.31x slower                                                       |
| telco                    | 4.83 ms                                                         | 6.62 ms: 1.37x slower                                                       |
| coverage                 | 46.6 ms                                                         | 489 ms: 10.50x slower                                                       |
| thrift                   | 902 us                                                          | 10.9 ms: 12.08x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.04x faster                                                                |

Benchmark hidden because not significant (1): hexiom
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240315-3.13.0a5+-9242976-JIT/bm-20240315-pythonperf1_win32-x86-brandtbucher-justin_plt-3.13.0a5+-9242976.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: unknown