# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: windows-x86
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.11x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.07x faster                                                                     |
| docutils       | 1.95 sec                                                        | 1.84 sec: 1.06x faster                                                                   |
| html5lib       | 52.1 ms                                                         | 44.7 ms: 1.17x faster                                                                    |
| tornado_http   | 118 ms                                                          | 103 ms: 1.14x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 470 ms: 1.96x faster                                                                     |
| async_tree_none         | 394 ms                                                          | 218 ms: 1.81x faster                                                                     |
| async_tree_io           | 940 ms                                                          | 537 ms: 1.75x faster                                                                     |
| async_tree_memoization  | 467 ms                                                          | 271 ms: 1.72x faster                                                                     |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                                     |
| float          | 69.6 ms                                                         | 61.2 ms: 1.14x faster                                                                    |
| nbody          | 79.1 ms                                                         | 89.4 ms: 1.13x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 113 ms: 1.16x faster                                                                     |
| regex_compile  | 117 ms                                                          | 106 ms: 1.10x faster                                                                     |
| regex_v8       | 15.8 ms                                                         | 15.3 ms: 1.03x faster                                                                    |
| regex_effbot   | 1.66 ms                                                         | 1.79 ms: 1.07x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 9.02 ms: 1.09x faster                                                                    |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                                    |
| tomli_loads          | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                                   |
| xml_etree_parse      | 120 ms                                                          | 113 ms: 1.06x faster                                                                     |
| unpickle_pure_python | 189 us                                                          | 180 us: 1.05x faster                                                                     |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                                    |
| pickle_pure_python   | 280 us                                                          | 272 us: 1.03x faster                                                                     |
| xml_etree_process    | 48.1 ms                                                         | 47.4 ms: 1.01x faster                                                                    |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.06x slower                                                                    |
| xml_etree_generate   | 61.6 ms                                                         | 66.6 ms: 1.08x slower                                                                    |
| pickle               | 7.83 us                                                         | 8.48 us: 1.08x slower                                                                    |
| pickle_list          | 3.22 us                                                         | 3.50 us: 1.09x slower                                                                    |
| pickle_dict          | 18.2 us                                                         | 21.7 us: 1.19x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                                             |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.3 ms: 1.06x slower                                                                    |
| python_startup_no_site | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                                    |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.86 ms: 1.16x faster                                                                    |
| django_template | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                                    |
| genshi_xml      | 46.6 ms                                                         | 45.6 ms: 1.02x faster                                                                    |
| genshi_text     | 21.0 ms                                                         | 20.6 ms: 1.02x faster                                                                    |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|--------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 145 us: 2.73x faster                                                                     |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                                     |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 470 ms: 1.96x faster                                                                     |
| async_tree_none          | 394 ms                                                          | 218 ms: 1.81x faster                                                                     |
| async_tree_io            | 940 ms                                                          | 537 ms: 1.75x faster                                                                     |
| async_tree_memoization   | 467 ms                                                          | 271 ms: 1.72x faster                                                                     |
| pylint                   | 384 ms                                                          | 234 ms: 1.64x faster                                                                     |
| deltablue                | 4.04 ms                                                         | 2.72 ms: 1.48x faster                                                                    |
| go                       | 146 ms                                                          | 103 ms: 1.42x faster                                                                     |
| crypto_pyaes             | 81.3 ms                                                         | 59.2 ms: 1.37x faster                                                                    |
| logging_silent           | 97.9 ns                                                         | 73.2 ns: 1.34x faster                                                                    |
| comprehensions           | 17.7 us                                                         | 13.3 us: 1.34x faster                                                                    |
| generators               | 31.6 ms                                                         | 23.6 ms: 1.34x faster                                                                    |
| deepcopy_memo            | 29.6 us                                                         | 22.1 us: 1.34x faster                                                                    |
| chaos                    | 74.4 ms                                                         | 55.9 ms: 1.33x faster                                                                    |
| scimark_lu               | 89.8 ms                                                         | 67.8 ms: 1.32x faster                                                                    |
| deepcopy                 | 310 us                                                          | 241 us: 1.29x faster                                                                     |
| pycparser                | 1.04 sec                                                        | 835 ms: 1.25x faster                                                                     |
| hexiom                   | 6.13 ms                                                         | 4.94 ms: 1.24x faster                                                                    |
| thrift                   | 902 us                                                          | 739 us: 1.22x faster                                                                     |
| sqlglot_parse            | 1.33 ms                                                         | 1.09 ms: 1.22x faster                                                                    |
| raytrace                 | 303 ms                                                          | 249 ms: 1.22x faster                                                                     |
| sqlglot_transpile        | 1.58 ms                                                         | 1.33 ms: 1.19x faster                                                                    |
| nqueens                  | 87.1 ms                                                         | 73.5 ms: 1.18x faster                                                                    |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                                    |
| pyflate                  | 422 ms                                                          | 362 ms: 1.17x faster                                                                     |
| html5lib                 | 52.1 ms                                                         | 44.7 ms: 1.17x faster                                                                    |
| regex_dna                | 131 ms                                                          | 113 ms: 1.16x faster                                                                     |
| mako                     | 9.10 ms                                                         | 7.86 ms: 1.16x faster                                                                    |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.15x faster                                                                     |
| dulwich_log              | 58.5 ms                                                         | 51.2 ms: 1.14x faster                                                                    |
| float                    | 69.6 ms                                                         | 61.2 ms: 1.14x faster                                                                    |
| tornado_http             | 118 ms                                                          | 103 ms: 1.14x faster                                                                     |
| scimark_sor              | 115 ms                                                          | 102 ms: 1.13x faster                                                                     |
| bench_thread_pool        | 1.12 ms                                                         | 997 us: 1.12x faster                                                                     |
| json                     | 4.76 ms                                                         | 4.30 ms: 1.11x faster                                                                    |
| django_template          | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                                    |
| regex_compile            | 117 ms                                                          | 106 ms: 1.10x faster                                                                     |
| scimark_monte_carlo      | 61.9 ms                                                         | 56.7 ms: 1.09x faster                                                                    |
| json_dumps               | 9.82 ms                                                         | 9.02 ms: 1.09x faster                                                                    |
| richards_super           | 49.9 ms                                                         | 46.0 ms: 1.08x faster                                                                    |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                                    |
| tomli_loads              | 1.91 sec                                                        | 1.77 sec: 1.08x faster                                                                   |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                                    |
| 2to3                     | 265 ms                                                          | 249 ms: 1.07x faster                                                                     |
| xml_etree_parse          | 120 ms                                                          | 113 ms: 1.06x faster                                                                     |
| sympy_str                | 229 ms                                                          | 216 ms: 1.06x faster                                                                     |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                                   |
| deepcopy_reduce          | 2.68 us                                                         | 2.53 us: 1.06x faster                                                                    |
| docutils                 | 1.95 sec                                                        | 1.84 sec: 1.06x faster                                                                   |
| spectral_norm            | 80.2 ms                                                         | 75.9 ms: 1.06x faster                                                                    |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.08 ms: 1.05x faster                                                                    |
| unpickle_pure_python     | 189 us                                                          | 180 us: 1.05x faster                                                                     |
| pprint_pformat           | 1.37 sec                                                        | 1.31 sec: 1.05x faster                                                                   |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.1 ms: 1.04x faster                                                                    |
| regex_v8                 | 15.8 ms                                                         | 15.3 ms: 1.03x faster                                                                    |
| pickle_pure_python       | 280 us                                                          | 272 us: 1.03x faster                                                                     |
| sqlglot_normalize        | 230 ms                                                          | 224 ms: 1.03x faster                                                                     |
| sqlglot_optimize         | 44.7 ms                                                         | 43.5 ms: 1.03x faster                                                                    |
| coroutines               | 17.9 ms                                                         | 17.5 ms: 1.02x faster                                                                    |
| genshi_xml               | 46.6 ms                                                         | 45.6 ms: 1.02x faster                                                                    |
| sympy_expand             | 391 ms                                                          | 384 ms: 1.02x faster                                                                     |
| pprint_safe_repr         | 658 ms                                                          | 647 ms: 1.02x faster                                                                     |
| genshi_text              | 21.0 ms                                                         | 20.6 ms: 1.02x faster                                                                    |
| xml_etree_process        | 48.1 ms                                                         | 47.4 ms: 1.01x faster                                                                    |
| fannkuch                 | 317 ms                                                          | 324 ms: 1.02x slower                                                                     |
| richards                 | 40.3 ms                                                         | 41.3 ms: 1.02x slower                                                                    |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.5 sec: 1.03x slower                                                                   |
| scimark_fft              | 216 ms                                                          | 229 ms: 1.06x slower                                                                     |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.06x slower                                                                    |
| python_startup           | 22.9 ms                                                         | 24.3 ms: 1.06x slower                                                                    |
| logging_simple           | 7.29 us                                                         | 7.77 us: 1.07x slower                                                                    |
| regex_effbot             | 1.66 ms                                                         | 1.79 ms: 1.07x slower                                                                    |
| xml_etree_generate       | 61.6 ms                                                         | 66.6 ms: 1.08x slower                                                                    |
| pathlib                  | 81.2 ms                                                         | 87.8 ms: 1.08x slower                                                                    |
| pickle                   | 7.83 us                                                         | 8.48 us: 1.08x slower                                                                    |
| logging_format           | 7.91 us                                                         | 8.58 us: 1.08x slower                                                                    |
| pickle_list              | 3.22 us                                                         | 3.50 us: 1.09x slower                                                                    |
| python_startup_no_site   | 18.1 ms                                                         | 20.0 ms: 1.11x slower                                                                    |
| bench_mp_pool            | 66.4 ms                                                         | 73.6 ms: 1.11x slower                                                                    |
| create_gc_cycles         | 694 us                                                          | 774 us: 1.12x slower                                                                     |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                                    |
| coverage                 | 46.6 ms                                                         | 52.6 ms: 1.13x slower                                                                    |
| nbody                    | 79.1 ms                                                         | 89.4 ms: 1.13x slower                                                                    |
| pickle_dict              | 18.2 us                                                         | 21.7 us: 1.19x slower                                                                    |
| async_generators         | 241 ms                                                          | 303 ms: 1.26x slower                                                                     |
| unpack_sequence          | 40.0 ns                                                         | 52.3 ns: 1.30x slower                                                                    |
| telco                    | 4.83 ms                                                         | 6.86 ms: 1.42x slower                                                                    |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                             |

Benchmark hidden because not significant (3): asyncio_tcp, meteor_contest, unpickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown