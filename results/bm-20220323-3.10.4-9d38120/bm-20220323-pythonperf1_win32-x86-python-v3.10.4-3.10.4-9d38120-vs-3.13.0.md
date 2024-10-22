# Results vs. 3.13.0

- fork: python
- ref: v3.10.4
- machine: windows-x86
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 265 ms: 1.05x slower                                            |
| chameleon      | 6.14 ms                                                         | 6.42 ms: 1.05x slower                                           |
| docutils       | 1.82 sec                                                        | 1.95 sec: 1.07x slower                                          |
| html5lib       | 48.3 ms                                                         | 52.1 ms: 1.08x slower                                           |
| tornado_http   | 104 ms                                                          | 118 ms: 1.13x slower                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_generators        | 274 ms                                                          | 241 ms: 1.14x faster                                            |
| asyncio_tcp             | 842 ms                                                          | 744 ms: 1.13x faster                                            |
| asyncio_tcp_ssl         | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                          |
| coroutines              | 15.7 ms                                                         | 17.9 ms: 1.14x slower                                           |
| async_tree_memoization  | 302 ms                                                          | 467 ms: 1.54x slower                                            |
| async_tree_none         | 246 ms                                                          | 394 ms: 1.60x slower                                            |
| async_tree_io           | 537 ms                                                          | 940 ms: 1.75x slower                                            |
| async_tree_cpu_io_mixed | 494 ms                                                          | 922 ms: 1.87x slower                                            |
| Geometric mean          | (ref)                                                           | 1.28x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 79.1 ms: 1.03x faster                                           |
| float          | 57.8 ms                                                         | 69.6 ms: 1.20x slower                                           |
| pidigits       | 202 ms                                                          | 502 ms: 2.49x slower                                            |
| Geometric mean | (ref)                                                           | 1.43x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.81 ms                                                         | 1.66 ms: 1.09x faster                                           |
| regex_v8       | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                           |
| regex_dna      | 117 ms                                                          | 131 ms: 1.12x slower                                            |
| regex_compile  | 103 ms                                                          | 117 ms: 1.13x slower                                            |
| Geometric mean | (ref)                                                           | 1.04x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_dict          | 21.7 us                                                         | 18.2 us: 1.19x faster                                           |
| pickle               | 8.42 us                                                         | 7.83 us: 1.08x faster                                           |
| unpickle             | 10.5 us                                                         | 9.82 us: 1.07x faster                                           |
| pickle_list          | 3.40 us                                                         | 3.22 us: 1.06x faster                                           |
| unpickle_list        | 3.09 us                                                         | 2.98 us: 1.04x faster                                           |
| xml_etree_generate   | 62.6 ms                                                         | 61.6 ms: 1.02x faster                                           |
| json_loads           | 21.0 us                                                         | 22.4 us: 1.07x slower                                           |
| xml_etree_process    | 45.0 ms                                                         | 48.1 ms: 1.07x slower                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 70.8 ms: 1.09x slower                                           |
| xml_etree_parse      | 109 ms                                                          | 120 ms: 1.10x slower                                            |
| tomli_loads          | 1.73 sec                                                        | 1.91 sec: 1.10x slower                                          |
| unpickle_pure_python | 162 us                                                          | 189 us: 1.17x slower                                            |
| pickle_pure_python   | 238 us                                                          | 280 us: 1.18x slower                                            |
| json_dumps           | 7.40 ms                                                         | 9.82 ms: 1.33x slower                                           |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 18.1 ms: 1.10x faster                                           |
| python_startup         | 24.3 ms                                                         | 22.9 ms: 1.06x faster                                           |
| Geometric mean         | (ref)                                                           | 1.08x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                         | 21.0 ms: 1.07x faster                                           |
| genshi_xml      | 49.5 ms                                                         | 46.6 ms: 1.06x faster                                           |
| django_template | 32.7 ms                                                         | 36.0 ms: 1.10x slower                                           |
| mako            | 7.31 ms                                                         | 9.10 ms: 1.25x slower                                           |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                    |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| thrift                   | 10.1 ms                                                         | 902 us: 11.25x faster                                           |
| coverage                 | 333 ms                                                          | 46.6 ms: 7.15x faster                                           |
| telco                    | 6.67 ms                                                         | 4.83 ms: 1.38x faster                                           |
| pickle_dict              | 21.7 us                                                         | 18.2 us: 1.19x faster                                           |
| async_generators         | 274 ms                                                          | 241 ms: 1.14x faster                                            |
| gc_traversal             | 1.45 ms                                                         | 1.28 ms: 1.13x faster                                           |
| asyncio_tcp              | 842 ms                                                          | 744 ms: 1.13x faster                                            |
| bench_mp_pool            | 74.3 ms                                                         | 66.4 ms: 1.12x faster                                           |
| python_startup_no_site   | 19.9 ms                                                         | 18.1 ms: 1.10x faster                                           |
| pathlib                  | 89.4 ms                                                         | 81.2 ms: 1.10x faster                                           |
| regex_effbot             | 1.81 ms                                                         | 1.66 ms: 1.09x faster                                           |
| logging_format           | 8.57 us                                                         | 7.91 us: 1.08x faster                                           |
| logging_simple           | 7.87 us                                                         | 7.29 us: 1.08x faster                                           |
| pickle                   | 8.42 us                                                         | 7.83 us: 1.08x faster                                           |
| unpickle                 | 10.5 us                                                         | 9.82 us: 1.07x faster                                           |
| unpack_sequence          | 42.9 ns                                                         | 40.0 ns: 1.07x faster                                           |
| genshi_text              | 22.4 ms                                                         | 21.0 ms: 1.07x faster                                           |
| deepcopy_reduce          | 2.85 us                                                         | 2.68 us: 1.06x faster                                           |
| genshi_xml               | 49.5 ms                                                         | 46.6 ms: 1.06x faster                                           |
| python_startup           | 24.3 ms                                                         | 22.9 ms: 1.06x faster                                           |
| pickle_list              | 3.40 us                                                         | 3.22 us: 1.06x faster                                           |
| unpickle_list            | 3.09 us                                                         | 2.98 us: 1.04x faster                                           |
| nbody                    | 81.9 ms                                                         | 79.1 ms: 1.03x faster                                           |
| create_gc_cycles         | 713 us                                                          | 694 us: 1.03x faster                                            |
| asyncio_tcp_ssl          | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                          |
| xml_etree_generate       | 62.6 ms                                                         | 61.6 ms: 1.02x faster                                           |
| flaskblogging            | 2.04 sec                                                        | 2.03 sec: 1.00x faster                                          |
| deepcopy                 | 307 us                                                          | 310 us: 1.01x slower                                            |
| regex_v8                 | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                           |
| pprint_safe_repr         | 644 ms                                                          | 658 ms: 1.02x slower                                            |
| meteor_contest           | 77.0 ms                                                         | 80.0 ms: 1.04x slower                                           |
| sympy_expand             | 375 ms                                                          | 391 ms: 1.04x slower                                            |
| chameleon                | 6.14 ms                                                         | 6.42 ms: 1.05x slower                                           |
| scimark_fft              | 206 ms                                                          | 216 ms: 1.05x slower                                            |
| sqlglot_normalize        | 220 ms                                                          | 230 ms: 1.05x slower                                            |
| 2to3                     | 253 ms                                                          | 265 ms: 1.05x slower                                            |
| sqlglot_optimize         | 42.5 ms                                                         | 44.7 ms: 1.05x slower                                           |
| pprint_pformat           | 1.30 sec                                                        | 1.37 sec: 1.06x slower                                          |
| sympy_str                | 215 ms                                                          | 229 ms: 1.07x slower                                            |
| json_loads               | 21.0 us                                                         | 22.4 us: 1.07x slower                                           |
| xml_etree_process        | 45.0 ms                                                         | 48.1 ms: 1.07x slower                                           |
| docutils                 | 1.82 sec                                                        | 1.95 sec: 1.07x slower                                          |
| html5lib                 | 48.3 ms                                                         | 52.1 ms: 1.08x slower                                           |
| fannkuch                 | 293 ms                                                          | 317 ms: 1.08x slower                                            |
| xml_etree_iterparse      | 65.1 ms                                                         | 70.8 ms: 1.09x slower                                           |
| mdp                      | 1.67 sec                                                        | 1.83 sec: 1.09x slower                                          |
| sympy_integrate          | 15.2 ms                                                         | 16.6 ms: 1.10x slower                                           |
| bench_thread_pool        | 1.02 ms                                                         | 1.12 ms: 1.10x slower                                           |
| django_template          | 32.7 ms                                                         | 36.0 ms: 1.10x slower                                           |
| xml_etree_parse          | 109 ms                                                          | 120 ms: 1.10x slower                                            |
| tomli_loads              | 1.73 sec                                                        | 1.91 sec: 1.10x slower                                          |
| scimark_sparse_mat_mult  | 2.90 ms                                                         | 3.24 ms: 1.12x slower                                           |
| json                     | 4.27 ms                                                         | 4.76 ms: 1.12x slower                                           |
| regex_dna                | 117 ms                                                          | 131 ms: 1.12x slower                                            |
| spectral_norm            | 71.3 ms                                                         | 80.2 ms: 1.12x slower                                           |
| tornado_http             | 104 ms                                                          | 118 ms: 1.13x slower                                            |
| regex_compile            | 103 ms                                                          | 117 ms: 1.13x slower                                            |
| deepcopy_memo            | 26.2 us                                                         | 29.6 us: 1.13x slower                                           |
| sympy_sum                | 108 ms                                                          | 122 ms: 1.13x slower                                            |
| coroutines               | 15.7 ms                                                         | 17.9 ms: 1.14x slower                                           |
| nqueens                  | 75.1 ms                                                         | 87.1 ms: 1.16x slower                                           |
| sqlite_synth             | 1.97 us                                                         | 2.29 us: 1.17x slower                                           |
| unpickle_pure_python     | 162 us                                                          | 189 us: 1.17x slower                                            |
| pickle_pure_python       | 238 us                                                          | 280 us: 1.18x slower                                            |
| dulwich_log              | 49.7 ms                                                         | 58.5 ms: 1.18x slower                                           |
| richards                 | 33.8 ms                                                         | 40.3 ms: 1.19x slower                                           |
| pycparser                | 869 ms                                                          | 1.04 sec: 1.20x slower                                          |
| float                    | 57.8 ms                                                         | 69.6 ms: 1.20x slower                                           |
| sqlglot_transpile        | 1.29 ms                                                         | 1.58 ms: 1.23x slower                                           |
| scimark_monte_carlo      | 50.3 ms                                                         | 61.9 ms: 1.23x slower                                           |
| mako                     | 7.31 ms                                                         | 9.10 ms: 1.25x slower                                           |
| scimark_sor              | 91.8 ms                                                         | 115 ms: 1.25x slower                                            |
| sqlglot_parse            | 1.05 ms                                                         | 1.33 ms: 1.27x slower                                           |
| pyflate                  | 326 ms                                                          | 422 ms: 1.29x slower                                            |
| go                       | 111 ms                                                          | 146 ms: 1.31x slower                                            |
| richards_super           | 38.0 ms                                                         | 49.9 ms: 1.31x slower                                           |
| hexiom                   | 4.64 ms                                                         | 6.13 ms: 1.32x slower                                           |
| json_dumps               | 7.40 ms                                                         | 9.82 ms: 1.33x slower                                           |
| comprehensions           | 12.7 us                                                         | 17.7 us: 1.39x slower                                           |
| crypto_pyaes             | 58.2 ms                                                         | 81.3 ms: 1.40x slower                                           |
| scimark_lu               | 63.5 ms                                                         | 89.8 ms: 1.41x slower                                           |
| generators               | 22.1 ms                                                         | 31.6 ms: 1.43x slower                                           |
| chaos                    | 51.2 ms                                                         | 74.4 ms: 1.45x slower                                           |
| raytrace                 | 205 ms                                                          | 303 ms: 1.47x slower                                            |
| async_tree_memoization   | 302 ms                                                          | 467 ms: 1.54x slower                                            |
| logging_silent           | 61.6 ns                                                         | 97.9 ns: 1.59x slower                                           |
| async_tree_none          | 246 ms                                                          | 394 ms: 1.60x slower                                            |
| deltablue                | 2.41 ms                                                         | 4.04 ms: 1.68x slower                                           |
| pylint                   | 225 ms                                                          | 384 ms: 1.71x slower                                            |
| async_tree_io            | 537 ms                                                          | 940 ms: 1.75x slower                                            |
| async_tree_cpu_io_mixed  | 494 ms                                                          | 922 ms: 1.87x slower                                            |
| pidigits                 | 202 ms                                                          | 502 ms: 2.49x slower                                            |
| typing_runtime_protocols | 136 us                                                          | 396 us: 2.90x slower                                            |
| Geometric mean           | (ref)                                                           | 1.09x slower                                                    |
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown