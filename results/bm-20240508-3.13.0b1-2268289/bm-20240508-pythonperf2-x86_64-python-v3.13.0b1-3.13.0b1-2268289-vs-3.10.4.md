# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b1
- machine: linux-x86_64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 290 ms: 1.21x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.66 ms: 1.23x faster                                            |
| docutils       | 3.41 sec                                                     | 3.03 sec: 1.13x faster                                           |
| html5lib       | 94.6 ms                                                      | 75.9 ms: 1.25x faster                                            |
| tornado_http   | 157 ms                                                       | 120 ms: 1.31x faster                                             |
| Geometric mean | (ref)                                                        | 1.22x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 371 ms: 1.86x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 870 ms: 1.84x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 467 ms: 1.76x faster                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 619 ms: 1.51x faster                                             |
| Geometric mean          | (ref)                                                        | 1.74x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 90.1 ms: 1.49x faster                                            |
| float          | 111 ms                                                       | 81.1 ms: 1.37x faster                                            |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                        | 1.30x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.29x faster                                             |
| regex_dna      | 261 ms                                                       | 243 ms: 1.08x faster                                             |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                            |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                            |
| Geometric mean | (ref)                                                        | 1.06x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 318 us: 1.43x faster                                             |
| unpickle_pure_python | 312 us                                                       | 222 us: 1.40x faster                                             |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                            |
| xml_etree_process    | 75.9 ms                                                      | 60.6 ms: 1.25x faster                                            |
| json_loads           | 30.3 us                                                      | 24.4 us: 1.24x faster                                            |
| tomli_loads          | 2.92 sec                                                     | 2.58 sec: 1.13x faster                                           |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                             |
| xml_etree_generate   | 92.3 ms                                                      | 88.9 ms: 1.04x faster                                            |
| unpickle_list        | 4.65 us                                                      | 4.75 us: 1.02x slower                                            |
| pickle               | 9.89 us                                                      | 10.4 us: 1.05x slower                                            |
| pickle_dict          | 29.5 us                                                      | 31.2 us: 1.06x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.49 us: 1.09x slower                                            |
| unpickle             | 13.5 us                                                      | 15.5 us: 1.15x slower                                            |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.9 ms: 1.13x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                            |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                            |
| django_template | 50.2 ms                                                      | 39.5 ms: 1.27x faster                                            |
| genshi_text     | 31.4 ms                                                      | 26.2 ms: 1.20x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 57.8 ms: 1.10x faster                                            |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.08x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.39 ms: 2.21x faster                                            |
| asyncio_tcp              | 779 ms                                                       | 380 ms: 2.05x faster                                             |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                           |
| async_tree_none          | 692 ms                                                       | 371 ms: 1.86x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 870 ms: 1.84x faster                                             |
| chaos                    | 109 ms                                                       | 59.4 ms: 1.83x faster                                            |
| raytrace                 | 489 ms                                                       | 268 ms: 1.82x faster                                             |
| async_tree_memoization   | 819 ms                                                       | 467 ms: 1.76x faster                                             |
| logging_silent           | 167 ns                                                       | 96.6 ns: 1.73x faster                                            |
| generators               | 57.3 ms                                                      | 33.3 ms: 1.72x faster                                            |
| scimark_lu               | 167 ms                                                       | 101 ms: 1.65x faster                                             |
| crypto_pyaes             | 119 ms                                                       | 72.9 ms: 1.64x faster                                            |
| pylint                   | 566 ms                                                       | 346 ms: 1.63x faster                                             |
| go                       | 262 ms                                                       | 160 ms: 1.63x faster                                             |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.44 ms: 1.55x faster                                            |
| scimark_monte_carlo      | 107 ms                                                       | 69.5 ms: 1.55x faster                                            |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                             |
| pyflate                  | 733 ms                                                       | 480 ms: 1.53x faster                                             |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 619 ms: 1.51x faster                                             |
| nbody                    | 134 ms                                                       | 90.1 ms: 1.49x faster                                            |
| richards_super           | 90.6 ms                                                      | 61.0 ms: 1.49x faster                                            |
| hexiom                   | 9.42 ms                                                      | 6.37 ms: 1.48x faster                                            |
| sqlglot_transpile        | 2.68 ms                                                      | 1.83 ms: 1.46x faster                                            |
| pickle_pure_python       | 455 us                                                       | 318 us: 1.43x faster                                             |
| spectral_norm            | 139 ms                                                       | 97.5 ms: 1.43x faster                                            |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 222 us: 1.40x faster                                             |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                            |
| richards                 | 75.1 ms                                                      | 54.0 ms: 1.39x faster                                            |
| float                    | 111 ms                                                       | 81.1 ms: 1.37x faster                                            |
| logging_simple           | 8.88 us                                                      | 6.50 us: 1.37x faster                                            |
| logging_format           | 9.64 us                                                      | 7.09 us: 1.36x faster                                            |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                            |
| bench_mp_pool            | 6.37 ms                                                      | 4.78 ms: 1.33x faster                                            |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                             |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                           |
| tornado_http             | 157 ms                                                       | 120 ms: 1.31x faster                                             |
| thrift                   | 1.18 ms                                                      | 908 us: 1.29x faster                                             |
| regex_compile            | 190 ms                                                       | 147 ms: 1.29x faster                                             |
| bench_thread_pool        | 1.14 ms                                                      | 895 us: 1.27x faster                                             |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.27x faster                                           |
| django_template          | 50.2 ms                                                      | 39.5 ms: 1.27x faster                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 830 ms: 1.26x faster                                             |
| deepcopy_memo            | 49.8 us                                                      | 39.4 us: 1.26x faster                                            |
| nqueens                  | 115 ms                                                       | 91.1 ms: 1.26x faster                                            |
| xml_etree_process        | 75.9 ms                                                      | 60.6 ms: 1.25x faster                                            |
| html5lib                 | 94.6 ms                                                      | 75.9 ms: 1.25x faster                                            |
| json_loads               | 30.3 us                                                      | 24.4 us: 1.24x faster                                            |
| chameleon                | 9.44 ms                                                      | 7.66 ms: 1.23x faster                                            |
| pathlib                  | 21.4 ms                                                      | 17.3 ms: 1.23x faster                                            |
| sympy_sum                | 193 ms                                                       | 157 ms: 1.23x faster                                             |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.19 ms: 1.21x faster                                            |
| 2to3                     | 350 ms                                                       | 290 ms: 1.21x faster                                             |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                           |
| dulwich_log              | 81.1 ms                                                      | 67.6 ms: 1.20x faster                                            |
| genshi_text              | 31.4 ms                                                      | 26.2 ms: 1.20x faster                                            |
| mypy2                    | 933 ms                                                       | 780 ms: 1.20x faster                                             |
| sympy_str                | 360 ms                                                       | 302 ms: 1.19x faster                                             |
| dask                     | 472 ms                                                       | 396 ms: 1.19x faster                                             |
| sympy_integrate          | 28.2 ms                                                      | 23.8 ms: 1.19x faster                                            |
| sqlglot_normalize        | 144 ms                                                       | 121 ms: 1.18x faster                                             |
| deepcopy                 | 468 us                                                       | 395 us: 1.18x faster                                             |
| sympy_expand             | 600 ms                                                       | 514 ms: 1.17x faster                                             |
| sqlglot_optimize         | 70.1 ms                                                      | 60.1 ms: 1.17x faster                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.48 us: 1.15x faster                                            |
| async_generators         | 421 ms                                                       | 367 ms: 1.15x faster                                             |
| tomli_loads              | 2.92 sec                                                     | 2.58 sec: 1.13x faster                                           |
| docutils                 | 3.41 sec                                                     | 3.03 sec: 1.13x faster                                           |
| gunicorn                 | 1.16 ms                                                      | 1.04 ms: 1.11x faster                                            |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                             |
| scimark_fft              | 361 ms                                                       | 328 ms: 1.10x faster                                             |
| aiohttp                  | 1.19 ms                                                      | 1.08 ms: 1.10x faster                                            |
| genshi_xml               | 63.3 ms                                                      | 57.8 ms: 1.10x faster                                            |
| json                     | 5.86 ms                                                      | 5.36 ms: 1.09x faster                                            |
| regex_dna                | 261 ms                                                       | 243 ms: 1.08x faster                                             |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                             |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                            |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                            |
| meteor_contest           | 138 ms                                                       | 132 ms: 1.05x faster                                             |
| xml_etree_generate       | 92.3 ms                                                      | 88.9 ms: 1.04x faster                                            |
| unpickle_list            | 4.65 us                                                      | 4.75 us: 1.02x slower                                            |
| pickle                   | 9.89 us                                                      | 10.4 us: 1.05x slower                                            |
| pickle_dict              | 29.5 us                                                      | 31.2 us: 1.06x slower                                            |
| flaskblogging            | 4.39 ms                                                      | 4.75 ms: 1.08x slower                                            |
| pickle_list              | 4.12 us                                                      | 4.49 us: 1.09x slower                                            |
| python_startup           | 11.5 ms                                                      | 12.9 ms: 1.13x slower                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                            |
| unpickle                 | 13.5 us                                                      | 15.5 us: 1.15x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                            |
| coverage                 | 63.3 ms                                                      | 83.7 ms: 1.32x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 4.66 ms: 1.37x slower                                            |
| telco                    | 7.23 ms                                                      | 175 ms: 24.16x slower                                            |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.12x