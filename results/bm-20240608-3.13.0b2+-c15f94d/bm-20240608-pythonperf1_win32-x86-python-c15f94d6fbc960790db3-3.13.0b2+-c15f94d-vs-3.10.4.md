# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-x86
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 235 ms: 1.13x faster                                                            |
| chameleon      | 6.42 ms                                                         | 5.74 ms: 1.12x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                          |
| html5lib       | 52.1 ms                                                         | 45.9 ms: 1.13x faster                                                           |
| tornado_http   | 118 ms                                                          | 94.0 ms: 1.25x faster                                                           |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 474 ms: 1.94x faster                                                            |
| async_tree_io           | 940 ms                                                          | 531 ms: 1.77x faster                                                            |
| async_tree_none         | 394 ms                                                          | 230 ms: 1.71x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                            |
| float          | 69.6 ms                                                         | 52.7 ms: 1.32x faster                                                           |
| nbody          | 79.1 ms                                                         | 74.7 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                           | 1.53x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 98.6 ms: 1.18x faster                                                           |
| regex_dna      | 131 ms                                                          | 118 ms: 1.10x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.94 ms: 1.42x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 215 us: 1.30x faster                                                            |
| unpickle_pure_python | 189 us                                                          | 146 us: 1.30x faster                                                            |
| tomli_loads          | 1.91 sec                                                        | 1.61 sec: 1.18x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 103 ms: 1.16x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 42.2 ms: 1.14x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.6 ms: 1.11x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.87 us: 1.04x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 59.5 ms: 1.04x faster                                                           |
| pickle               | 7.83 us                                                         | 8.09 us: 1.03x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 20.5 us: 1.12x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.71 us: 1.15x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 22.6 ms: 1.02x faster                                                           |
| python_startup_no_site | 18.1 ms                                                         | 18.3 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.86 ms: 1.33x faster                                                           |
| django_template | 36.0 ms                                                         | 30.2 ms: 1.19x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 19.5 ms: 1.07x faster                                                           |
| genshi_xml      | 46.6 ms                                                         | 44.5 ms: 1.05x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 136 us: 2.92x faster                                                            |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 474 ms: 1.94x faster                                                            |
| deltablue                | 4.04 ms                                                         | 2.23 ms: 1.81x faster                                                           |
| pylint                   | 384 ms                                                          | 217 ms: 1.77x faster                                                            |
| async_tree_io            | 940 ms                                                          | 531 ms: 1.77x faster                                                            |
| async_tree_none          | 394 ms                                                          | 230 ms: 1.71x faster                                                            |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                            |
| logging_silent           | 97.9 ns                                                         | 58.2 ns: 1.68x faster                                                           |
| raytrace                 | 303 ms                                                          | 190 ms: 1.60x faster                                                            |
| chaos                    | 74.4 ms                                                         | 47.6 ms: 1.56x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.7 us: 1.52x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 60.3 ms: 1.49x faster                                                           |
| generators               | 31.6 ms                                                         | 21.4 ms: 1.47x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 55.3 ms: 1.47x faster                                                           |
| richards_super           | 49.9 ms                                                         | 34.6 ms: 1.44x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.27 ms: 1.44x faster                                                           |
| go                       | 146 ms                                                          | 102 ms: 1.43x faster                                                            |
| sqlglot_parse            | 1.33 ms                                                         | 932 us: 1.43x faster                                                            |
| json_dumps               | 9.82 ms                                                         | 6.94 ms: 1.42x faster                                                           |
| scimark_sor              | 115 ms                                                          | 81.6 ms: 1.41x faster                                                           |
| pyflate                  | 422 ms                                                          | 307 ms: 1.37x faster                                                            |
| sqlglot_transpile        | 1.58 ms                                                         | 1.16 ms: 1.36x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 46.4 ms: 1.33x faster                                                           |
| mako                     | 9.10 ms                                                         | 6.86 ms: 1.33x faster                                                           |
| richards                 | 40.3 ms                                                         | 30.4 ms: 1.32x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 65.9 ms: 1.32x faster                                                           |
| float                    | 69.6 ms                                                         | 52.7 ms: 1.32x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 215 us: 1.30x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 146 us: 1.30x faster                                                            |
| pycparser                | 1.04 sec                                                        | 802 ms: 1.30x faster                                                            |
| tornado_http             | 118 ms                                                          | 94.0 ms: 1.25x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 23.9 us: 1.23x faster                                                           |
| django_template          | 36.0 ms                                                         | 30.2 ms: 1.19x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.61 sec: 1.18x faster                                                          |
| regex_compile            | 117 ms                                                          | 98.6 ms: 1.18x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 68.1 ms: 1.18x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.95 us: 1.18x faster                                                           |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.17x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 103 ms: 1.16x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.79 ms: 1.16x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 966 us: 1.16x faster                                                            |
| coroutines               | 17.9 ms                                                         | 15.5 ms: 1.15x faster                                                           |
| fannkuch                 | 317 ms                                                          | 277 ms: 1.15x faster                                                            |
| sqlglot_optimize         | 44.7 ms                                                         | 39.2 ms: 1.14x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 42.2 ms: 1.14x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 202 ms: 1.14x faster                                                            |
| sympy_integrate          | 16.6 ms                                                         | 14.6 ms: 1.14x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 45.9 ms: 1.13x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 658 ms: 1.13x faster                                                            |
| json                     | 4.76 ms                                                         | 4.22 ms: 1.13x faster                                                           |
| 2to3                     | 265 ms                                                          | 235 ms: 1.13x faster                                                            |
| chameleon                | 6.42 ms                                                         | 5.74 ms: 1.12x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.6 ms: 1.11x faster                                                           |
| sympy_str                | 229 ms                                                          | 207 ms: 1.11x faster                                                            |
| meteor_contest           | 80.0 ms                                                         | 72.5 ms: 1.10x faster                                                           |
| regex_dna                | 131 ms                                                          | 118 ms: 1.10x faster                                                            |
| mdp                      | 1.83 sec                                                        | 1.66 sec: 1.10x faster                                                          |
| deepcopy                 | 310 us                                                          | 283 us: 1.10x faster                                                            |
| scimark_fft              | 216 ms                                                          | 198 ms: 1.09x faster                                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.27 sec: 1.08x faster                                                          |
| sympy_expand             | 391 ms                                                          | 362 ms: 1.08x faster                                                            |
| docutils                 | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                          |
| genshi_text              | 21.0 ms                                                         | 19.5 ms: 1.07x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 617 ms: 1.07x faster                                                            |
| nbody                    | 79.1 ms                                                         | 74.7 ms: 1.06x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 44.5 ms: 1.05x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.87 us: 1.04x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 59.5 ms: 1.04x faster                                                           |
| python_startup           | 22.9 ms                                                         | 22.6 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                          |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 18.3 ms: 1.01x slower                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.72 us: 1.01x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.02x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 83.6 ms: 1.03x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.15 us: 1.03x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.09 us: 1.03x slower                                                           |
| logging_simple           | 7.29 us                                                         | 7.54 us: 1.03x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 69.9 ms: 1.05x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 747 us: 1.08x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                           |
| async_generators         | 241 ms                                                          | 270 ms: 1.12x slower                                                            |
| pickle_dict              | 18.2 us                                                         | 20.5 us: 1.12x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.71 us: 1.15x slower                                                           |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.16x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.07 ms: 1.26x slower                                                           |
| coverage                 | 46.6 ms                                                         | 305 ms: 6.54x slower                                                            |
| thrift                   | 902 us                                                          | 9.72 ms: 10.77x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                    |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown