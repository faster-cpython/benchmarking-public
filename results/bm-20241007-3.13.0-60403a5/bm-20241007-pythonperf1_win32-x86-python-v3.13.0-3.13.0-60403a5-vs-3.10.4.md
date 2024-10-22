# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: windows-x86
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 253 ms: 1.05x faster                                            |
| chameleon      | 6.42 ms                                                         | 6.14 ms: 1.05x faster                                           |
| docutils       | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                          |
| html5lib       | 52.1 ms                                                         | 48.3 ms: 1.08x faster                                           |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                            |
| Geometric mean | (ref)                                                           | 1.07x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 494 ms: 1.87x faster                                            |
| async_tree_io           | 940 ms                                                          | 537 ms: 1.75x faster                                            |
| async_tree_none         | 394 ms                                                          | 246 ms: 1.60x faster                                            |
| async_tree_memoization  | 467 ms                                                          | 302 ms: 1.54x faster                                            |
| Geometric mean          | (ref)                                                           | 1.69x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 202 ms: 2.49x faster                                            |
| float          | 69.6 ms                                                         | 57.8 ms: 1.20x faster                                           |
| nbody          | 79.1 ms                                                         | 81.9 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                           | 1.43x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 103 ms: 1.13x faster                                            |
| regex_dna      | 131 ms                                                          | 117 ms: 1.12x faster                                            |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                           |
| regex_effbot   | 1.66 ms                                                         | 1.81 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.40 ms: 1.33x faster                                           |
| pickle_pure_python   | 280 us                                                          | 238 us: 1.18x faster                                            |
| unpickle_pure_python | 189 us                                                          | 162 us: 1.17x faster                                            |
| tomli_loads          | 1.91 sec                                                        | 1.73 sec: 1.10x faster                                          |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.1 ms: 1.09x faster                                           |
| xml_etree_process    | 48.1 ms                                                         | 45.0 ms: 1.07x faster                                           |
| json_loads           | 22.4 us                                                         | 21.0 us: 1.07x faster                                           |
| xml_etree_generate   | 61.6 ms                                                         | 62.6 ms: 1.02x slower                                           |
| unpickle_list        | 2.98 us                                                         | 3.09 us: 1.04x slower                                           |
| pickle_list          | 3.22 us                                                         | 3.40 us: 1.06x slower                                           |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                           |
| pickle               | 7.83 us                                                         | 8.42 us: 1.08x slower                                           |
| pickle_dict          | 18.2 us                                                         | 21.7 us: 1.19x slower                                           |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.3 ms: 1.06x slower                                           |
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                           |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.31 ms: 1.25x faster                                           |
| django_template | 36.0 ms                                                         | 32.7 ms: 1.10x faster                                           |
| genshi_xml      | 46.6 ms                                                         | 49.5 ms: 1.06x slower                                           |
| genshi_text     | 21.0 ms                                                         | 22.4 ms: 1.07x slower                                           |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 136 us: 2.90x faster                                            |
| pidigits                 | 502 ms                                                          | 202 ms: 2.49x faster                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 494 ms: 1.87x faster                                            |
| async_tree_io            | 940 ms                                                          | 537 ms: 1.75x faster                                            |
| pylint                   | 384 ms                                                          | 225 ms: 1.71x faster                                            |
| deltablue                | 4.04 ms                                                         | 2.41 ms: 1.68x faster                                           |
| async_tree_none          | 394 ms                                                          | 246 ms: 1.60x faster                                            |
| logging_silent           | 97.9 ns                                                         | 61.6 ns: 1.59x faster                                           |
| async_tree_memoization   | 467 ms                                                          | 302 ms: 1.54x faster                                            |
| raytrace                 | 303 ms                                                          | 205 ms: 1.47x faster                                            |
| chaos                    | 74.4 ms                                                         | 51.2 ms: 1.45x faster                                           |
| generators               | 31.6 ms                                                         | 22.1 ms: 1.43x faster                                           |
| scimark_lu               | 89.8 ms                                                         | 63.5 ms: 1.41x faster                                           |
| crypto_pyaes             | 81.3 ms                                                         | 58.2 ms: 1.40x faster                                           |
| comprehensions           | 17.7 us                                                         | 12.7 us: 1.39x faster                                           |
| json_dumps               | 9.82 ms                                                         | 7.40 ms: 1.33x faster                                           |
| hexiom                   | 6.13 ms                                                         | 4.64 ms: 1.32x faster                                           |
| richards_super           | 49.9 ms                                                         | 38.0 ms: 1.31x faster                                           |
| go                       | 146 ms                                                          | 111 ms: 1.31x faster                                            |
| pyflate                  | 422 ms                                                          | 326 ms: 1.29x faster                                            |
| sqlglot_parse            | 1.33 ms                                                         | 1.05 ms: 1.27x faster                                           |
| scimark_sor              | 115 ms                                                          | 91.8 ms: 1.25x faster                                           |
| mako                     | 9.10 ms                                                         | 7.31 ms: 1.25x faster                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.3 ms: 1.23x faster                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.29 ms: 1.23x faster                                           |
| float                    | 69.6 ms                                                         | 57.8 ms: 1.20x faster                                           |
| pycparser                | 1.04 sec                                                        | 869 ms: 1.20x faster                                            |
| richards                 | 40.3 ms                                                         | 33.8 ms: 1.19x faster                                           |
| dulwich_log              | 58.5 ms                                                         | 49.7 ms: 1.18x faster                                           |
| pickle_pure_python       | 280 us                                                          | 238 us: 1.18x faster                                            |
| unpickle_pure_python     | 189 us                                                          | 162 us: 1.17x faster                                            |
| sqlite_synth             | 2.29 us                                                         | 1.97 us: 1.17x faster                                           |
| nqueens                  | 87.1 ms                                                         | 75.1 ms: 1.16x faster                                           |
| coroutines               | 17.9 ms                                                         | 15.7 ms: 1.14x faster                                           |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                            |
| deepcopy_memo            | 29.6 us                                                         | 26.2 us: 1.13x faster                                           |
| regex_compile            | 117 ms                                                          | 103 ms: 1.13x faster                                            |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                            |
| spectral_norm            | 80.2 ms                                                         | 71.3 ms: 1.12x faster                                           |
| regex_dna                | 131 ms                                                          | 117 ms: 1.12x faster                                            |
| json                     | 4.76 ms                                                         | 4.27 ms: 1.12x faster                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.90 ms: 1.12x faster                                           |
| tomli_loads              | 1.91 sec                                                        | 1.73 sec: 1.10x faster                                          |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                            |
| django_template          | 36.0 ms                                                         | 32.7 ms: 1.10x faster                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.2 ms: 1.10x faster                                           |
| mdp                      | 1.83 sec                                                        | 1.67 sec: 1.09x faster                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.1 ms: 1.09x faster                                           |
| fannkuch                 | 317 ms                                                          | 293 ms: 1.08x faster                                            |
| html5lib                 | 52.1 ms                                                         | 48.3 ms: 1.08x faster                                           |
| docutils                 | 1.95 sec                                                        | 1.82 sec: 1.07x faster                                          |
| xml_etree_process        | 48.1 ms                                                         | 45.0 ms: 1.07x faster                                           |
| json_loads               | 22.4 us                                                         | 21.0 us: 1.07x faster                                           |
| sympy_str                | 229 ms                                                          | 215 ms: 1.07x faster                                            |
| pprint_pformat           | 1.37 sec                                                        | 1.30 sec: 1.06x faster                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 42.5 ms: 1.05x faster                                           |
| 2to3                     | 265 ms                                                          | 253 ms: 1.05x faster                                            |
| sqlglot_normalize        | 230 ms                                                          | 220 ms: 1.05x faster                                            |
| scimark_fft              | 216 ms                                                          | 206 ms: 1.05x faster                                            |
| chameleon                | 6.42 ms                                                         | 6.14 ms: 1.05x faster                                           |
| sympy_expand             | 391 ms                                                          | 375 ms: 1.04x faster                                            |
| meteor_contest           | 80.0 ms                                                         | 77.0 ms: 1.04x faster                                           |
| pprint_safe_repr         | 658 ms                                                          | 644 ms: 1.02x faster                                            |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                           |
| deepcopy                 | 310 us                                                          | 307 us: 1.01x faster                                            |
| flaskblogging            | 2.03 sec                                                        | 2.04 sec: 1.00x slower                                          |
| xml_etree_generate       | 61.6 ms                                                         | 62.6 ms: 1.02x slower                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.4 sec: 1.02x slower                                          |
| create_gc_cycles         | 694 us                                                          | 713 us: 1.03x slower                                            |
| nbody                    | 79.1 ms                                                         | 81.9 ms: 1.03x slower                                           |
| unpickle_list            | 2.98 us                                                         | 3.09 us: 1.04x slower                                           |
| pickle_list              | 3.22 us                                                         | 3.40 us: 1.06x slower                                           |
| python_startup           | 22.9 ms                                                         | 24.3 ms: 1.06x slower                                           |
| genshi_xml               | 46.6 ms                                                         | 49.5 ms: 1.06x slower                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.85 us: 1.06x slower                                           |
| genshi_text              | 21.0 ms                                                         | 22.4 ms: 1.07x slower                                           |
| unpack_sequence          | 40.0 ns                                                         | 42.9 ns: 1.07x slower                                           |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                           |
| pickle                   | 7.83 us                                                         | 8.42 us: 1.08x slower                                           |
| logging_simple           | 7.29 us                                                         | 7.87 us: 1.08x slower                                           |
| logging_format           | 7.91 us                                                         | 8.57 us: 1.08x slower                                           |
| regex_effbot             | 1.66 ms                                                         | 1.81 ms: 1.09x slower                                           |
| pathlib                  | 81.2 ms                                                         | 89.4 ms: 1.10x slower                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                           |
| bench_mp_pool            | 66.4 ms                                                         | 74.3 ms: 1.12x slower                                           |
| asyncio_tcp              | 744 ms                                                          | 842 ms: 1.13x slower                                            |
| gc_traversal             | 1.28 ms                                                         | 1.45 ms: 1.13x slower                                           |
| async_generators         | 241 ms                                                          | 274 ms: 1.14x slower                                            |
| pickle_dict              | 18.2 us                                                         | 21.7 us: 1.19x slower                                           |
| telco                    | 4.83 ms                                                         | 6.67 ms: 1.38x slower                                           |
| coverage                 | 46.6 ms                                                         | 333 ms: 7.15x slower                                            |
| thrift                   | 902 us                                                          | 10.1 ms: 11.25x slower                                          |
| Geometric mean           | (ref)                                                           | 1.09x faster                                                    |
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown