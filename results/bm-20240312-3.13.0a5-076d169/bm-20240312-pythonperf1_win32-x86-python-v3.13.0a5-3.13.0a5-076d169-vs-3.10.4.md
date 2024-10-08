# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a5
- machine: windows-x86
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 237 ms: 1.12x faster                                                |
| chameleon      | 6.42 ms                                                         | 5.53 ms: 1.16x faster                                               |
| docutils       | 1.95 sec                                                        | 1.70 sec: 1.15x faster                                              |
| html5lib       | 52.1 ms                                                         | 42.0 ms: 1.24x faster                                               |
| tornado_http   | 118 ms                                                          | 93.5 ms: 1.26x faster                                               |
| Geometric mean | (ref)                                                           | 1.18x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 484 ms: 1.91x faster                                                |
| async_tree_none         | 394 ms                                                          | 241 ms: 1.63x faster                                                |
| async_tree_io           | 940 ms                                                          | 591 ms: 1.59x faster                                                |
| async_tree_memoization  | 467 ms                                                          | 301 ms: 1.55x faster                                                |
| Geometric mean          | (ref)                                                           | 1.66x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                |
| float          | 69.6 ms                                                         | 53.8 ms: 1.29x faster                                               |
| nbody          | 79.1 ms                                                         | 74.7 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                           | 1.52x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 94.7 ms: 1.23x faster                                               |
| regex_dna      | 131 ms                                                          | 119 ms: 1.10x faster                                                |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                               |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                               |
| Geometric mean | (ref)                                                           | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.67 ms: 1.47x faster                                               |
| unpickle_pure_python | 189 us                                                          | 139 us: 1.37x faster                                                |
| pickle_pure_python   | 280 us                                                          | 206 us: 1.36x faster                                                |
| tomli_loads          | 1.91 sec                                                        | 1.58 sec: 1.21x faster                                              |
| xml_etree_process    | 48.1 ms                                                         | 40.5 ms: 1.19x faster                                               |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                |
| json_loads           | 22.4 us                                                         | 20.1 us: 1.11x faster                                               |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.4 ms: 1.08x faster                                               |
| xml_etree_generate   | 61.6 ms                                                         | 57.9 ms: 1.06x faster                                               |
| unpickle_list        | 2.98 us                                                         | 2.82 us: 1.06x faster                                               |
| pickle               | 7.83 us                                                         | 7.74 us: 1.01x faster                                               |
| unpickle             | 9.82 us                                                         | 9.87 us: 1.00x slower                                               |
| pickle_dict          | 18.2 us                                                         | 20.0 us: 1.10x slower                                               |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                        |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.8 ms: 1.01x faster                                               |
| python_startup_no_site | 18.1 ms                                                         | 20.6 ms: 1.14x slower                                               |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.75 ms: 1.35x faster                                               |
| django_template | 36.0 ms                                                         | 28.6 ms: 1.26x faster                                               |
| genshi_text     | 21.0 ms                                                         | 18.3 ms: 1.15x faster                                               |
| genshi_xml      | 46.6 ms                                                         | 41.0 ms: 1.14x faster                                               |
| Geometric mean  | (ref)                                                           | 1.22x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 90.2 us: 4.39x faster                                               |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 484 ms: 1.91x faster                                                |
| deltablue                | 4.04 ms                                                         | 2.13 ms: 1.89x faster                                               |
| pylint                   | 384 ms                                                          | 217 ms: 1.77x faster                                                |
| logging_silent           | 97.9 ns                                                         | 57.3 ns: 1.71x faster                                               |
| async_tree_none          | 394 ms                                                          | 241 ms: 1.63x faster                                                |
| comprehensions           | 17.7 us                                                         | 11.0 us: 1.61x faster                                               |
| async_tree_io            | 940 ms                                                          | 591 ms: 1.59x faster                                                |
| raytrace                 | 303 ms                                                          | 192 ms: 1.58x faster                                                |
| richards_super           | 49.9 ms                                                         | 31.8 ms: 1.57x faster                                               |
| chaos                    | 74.4 ms                                                         | 47.5 ms: 1.57x faster                                               |
| sqlglot_parse            | 1.33 ms                                                         | 856 us: 1.55x faster                                                |
| crypto_pyaes             | 81.3 ms                                                         | 52.3 ms: 1.55x faster                                               |
| async_tree_memoization   | 467 ms                                                          | 301 ms: 1.55x faster                                                |
| go                       | 146 ms                                                          | 94.3 ms: 1.54x faster                                               |
| scimark_lu               | 89.8 ms                                                         | 58.7 ms: 1.53x faster                                               |
| hexiom                   | 6.13 ms                                                         | 4.16 ms: 1.48x faster                                               |
| json_dumps               | 9.82 ms                                                         | 6.67 ms: 1.47x faster                                               |
| sqlglot_transpile        | 1.58 ms                                                         | 1.08 ms: 1.46x faster                                               |
| scimark_sor              | 115 ms                                                          | 79.3 ms: 1.45x faster                                               |
| generators               | 31.6 ms                                                         | 21.9 ms: 1.44x faster                                               |
| richards                 | 40.3 ms                                                         | 28.2 ms: 1.43x faster                                               |
| scimark_monte_carlo      | 61.9 ms                                                         | 44.5 ms: 1.39x faster                                               |
| pyflate                  | 422 ms                                                          | 309 ms: 1.37x faster                                                |
| unpickle_pure_python     | 189 us                                                          | 139 us: 1.37x faster                                                |
| pickle_pure_python       | 280 us                                                          | 206 us: 1.36x faster                                                |
| mako                     | 9.10 ms                                                         | 6.75 ms: 1.35x faster                                               |
| pycparser                | 1.04 sec                                                        | 777 ms: 1.34x faster                                                |
| deepcopy_memo            | 29.6 us                                                         | 22.4 us: 1.32x faster                                               |
| float                    | 69.6 ms                                                         | 53.8 ms: 1.29x faster                                               |
| nqueens                  | 87.1 ms                                                         | 67.6 ms: 1.29x faster                                               |
| coroutines               | 17.9 ms                                                         | 14.1 ms: 1.27x faster                                               |
| django_template          | 36.0 ms                                                         | 28.6 ms: 1.26x faster                                               |
| tornado_http             | 118 ms                                                          | 93.5 ms: 1.26x faster                                               |
| sympy_sum                | 122 ms                                                          | 98.5 ms: 1.24x faster                                               |
| html5lib                 | 52.1 ms                                                         | 42.0 ms: 1.24x faster                                               |
| regex_compile            | 117 ms                                                          | 94.7 ms: 1.23x faster                                               |
| spectral_norm            | 80.2 ms                                                         | 65.6 ms: 1.22x faster                                               |
| tomli_loads              | 1.91 sec                                                        | 1.58 sec: 1.21x faster                                              |
| sqlite_synth             | 2.29 us                                                         | 1.91 us: 1.20x faster                                               |
| asyncio_tcp              | 744 ms                                                          | 622 ms: 1.20x faster                                                |
| sqlglot_normalize        | 230 ms                                                          | 193 ms: 1.19x faster                                                |
| sqlglot_optimize         | 44.7 ms                                                         | 37.6 ms: 1.19x faster                                               |
| xml_etree_process        | 48.1 ms                                                         | 40.5 ms: 1.19x faster                                               |
| deepcopy                 | 310 us                                                          | 261 us: 1.19x faster                                                |
| fannkuch                 | 317 ms                                                          | 268 ms: 1.18x faster                                                |
| sympy_integrate          | 16.6 ms                                                         | 14.1 ms: 1.18x faster                                               |
| pprint_pformat           | 1.37 sec                                                        | 1.16 sec: 1.18x faster                                              |
| sympy_str                | 229 ms                                                          | 195 ms: 1.18x faster                                                |
| pprint_safe_repr         | 658 ms                                                          | 565 ms: 1.16x faster                                                |
| json                     | 4.76 ms                                                         | 4.10 ms: 1.16x faster                                               |
| chameleon                | 6.42 ms                                                         | 5.53 ms: 1.16x faster                                               |
| mdp                      | 1.83 sec                                                        | 1.58 sec: 1.16x faster                                              |
| deepcopy_reduce          | 2.68 us                                                         | 2.32 us: 1.16x faster                                               |
| docutils                 | 1.95 sec                                                        | 1.70 sec: 1.15x faster                                              |
| genshi_text              | 21.0 ms                                                         | 18.3 ms: 1.15x faster                                               |
| sympy_expand             | 391 ms                                                          | 341 ms: 1.15x faster                                                |
| genshi_xml               | 46.6 ms                                                         | 41.0 ms: 1.14x faster                                               |
| bench_thread_pool        | 1.12 ms                                                         | 986 us: 1.14x faster                                                |
| 2to3                     | 265 ms                                                          | 237 ms: 1.12x faster                                                |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.91 ms: 1.11x faster                                               |
| json_loads               | 22.4 us                                                         | 20.1 us: 1.11x faster                                               |
| regex_dna                | 131 ms                                                          | 119 ms: 1.10x faster                                                |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.4 ms: 1.08x faster                                               |
| scimark_fft              | 216 ms                                                          | 201 ms: 1.08x faster                                                |
| meteor_contest           | 80.0 ms                                                         | 74.9 ms: 1.07x faster                                               |
| xml_etree_generate       | 61.6 ms                                                         | 57.9 ms: 1.06x faster                                               |
| unpickle_list            | 2.98 us                                                         | 2.82 us: 1.06x faster                                               |
| nbody                    | 79.1 ms                                                         | 74.7 ms: 1.06x faster                                               |
| create_gc_cycles         | 694 us                                                          | 657 us: 1.06x faster                                                |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.7 sec: 1.01x faster                                              |
| pickle                   | 7.83 us                                                         | 7.74 us: 1.01x faster                                               |
| python_startup           | 22.9 ms                                                         | 22.8 ms: 1.01x faster                                               |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                              |
| unpickle                 | 9.82 us                                                         | 9.87 us: 1.00x slower                                               |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                               |
| logging_format           | 7.91 us                                                         | 8.10 us: 1.02x slower                                               |
| logging_simple           | 7.29 us                                                         | 7.53 us: 1.03x slower                                               |
| async_generators         | 241 ms                                                          | 261 ms: 1.08x slower                                                |
| gc_traversal             | 1.28 ms                                                         | 1.40 ms: 1.09x slower                                               |
| pickle_dict              | 18.2 us                                                         | 20.0 us: 1.10x slower                                               |
| pathlib                  | 81.2 ms                                                         | 89.2 ms: 1.10x slower                                               |
| bench_mp_pool            | 66.4 ms                                                         | 74.1 ms: 1.12x slower                                               |
| python_startup_no_site   | 18.1 ms                                                         | 20.6 ms: 1.14x slower                                               |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                               |
| telco                    | 4.83 ms                                                         | 5.99 ms: 1.24x slower                                               |
| coverage                 | 46.6 ms                                                         | 497 ms: 10.67x slower                                               |
| thrift                   | 902 us                                                          | 10.1 ms: 11.19x slower                                              |
| Geometric mean           | (ref)                                                           | 1.18x faster                                                        |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown