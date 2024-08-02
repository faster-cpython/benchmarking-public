# Results vs. 3.10.4

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-x86_64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 288 ms: 1.22x faster                                                             |
| chameleon      | 9.44 ms                                                      | 7.86 ms: 1.20x faster                                                            |
| docutils       | 3.41 sec                                                     | 3.02 sec: 1.13x faster                                                           |
| html5lib       | 94.6 ms                                                      | 74.9 ms: 1.26x faster                                                            |
| tornado_http   | 157 ms                                                       | 120 ms: 1.31x faster                                                             |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 371 ms: 1.86x faster                                                             |
| async_tree_io           | 1.60 sec                                                     | 868 ms: 1.84x faster                                                             |
| async_tree_memoization  | 819 ms                                                       | 465 ms: 1.76x faster                                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 618 ms: 1.52x faster                                                             |
| Geometric mean          | (ref)                                                        | 1.74x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.9 ms: 1.49x faster                                                            |
| float          | 111 ms                                                       | 80.6 ms: 1.38x faster                                                            |
| pidigits       | 271 ms                                                       | 257 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 148 ms: 1.29x faster                                                             |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                                             |
| regex_v8       | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                                            |
| regex_effbot   | 3.09 ms                                                      | 3.42 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 215 us: 1.45x faster                                                             |
| pickle_pure_python   | 455 us                                                       | 317 us: 1.43x faster                                                             |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                            |
| xml_etree_process    | 75.9 ms                                                      | 60.3 ms: 1.26x faster                                                            |
| json_loads           | 30.3 us                                                      | 24.8 us: 1.22x faster                                                            |
| tomli_loads          | 2.92 sec                                                     | 2.57 sec: 1.13x faster                                                           |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                             |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                             |
| xml_etree_generate   | 92.3 ms                                                      | 88.6 ms: 1.04x faster                                                            |
| unpickle_list        | 4.65 us                                                      | 4.82 us: 1.04x slower                                                            |
| pickle               | 9.89 us                                                      | 10.3 us: 1.04x slower                                                            |
| pickle_dict          | 29.5 us                                                      | 30.9 us: 1.05x slower                                                            |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                            |
| pickle_list          | 4.12 us                                                      | 4.52 us: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.8 ms: 1.12x slower                                                            |
| python_startup_no_site | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                            |
| django_template | 50.2 ms                                                      | 39.3 ms: 1.28x faster                                                            |
| genshi_text     | 31.4 ms                                                      | 26.0 ms: 1.21x faster                                                            |
| genshi_xml      | 63.3 ms                                                      | 56.7 ms: 1.12x faster                                                            |
| Geometric mean  | (ref)                                                        | 1.25x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 179 us: 2.99x faster                                                             |
| deltablue                | 7.50 ms                                                      | 3.35 ms: 2.24x faster                                                            |
| asyncio_tcp              | 779 ms                                                       | 375 ms: 2.08x faster                                                             |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                           |
| raytrace                 | 489 ms                                                       | 262 ms: 1.87x faster                                                             |
| async_tree_none          | 692 ms                                                       | 371 ms: 1.86x faster                                                             |
| chaos                    | 109 ms                                                       | 58.8 ms: 1.85x faster                                                            |
| async_tree_io            | 1.60 sec                                                     | 868 ms: 1.84x faster                                                             |
| async_tree_memoization   | 819 ms                                                       | 465 ms: 1.76x faster                                                             |
| logging_silent           | 167 ns                                                       | 97.1 ns: 1.72x faster                                                            |
| scimark_lu               | 167 ms                                                       | 97.1 ms: 1.72x faster                                                            |
| generators               | 57.3 ms                                                      | 34.1 ms: 1.68x faster                                                            |
| scimark_monte_carlo      | 107 ms                                                       | 65.4 ms: 1.64x faster                                                            |
| pylint                   | 566 ms                                                       | 348 ms: 1.63x faster                                                             |
| go                       | 262 ms                                                       | 163 ms: 1.60x faster                                                             |
| scimark_sor              | 180 ms                                                       | 113 ms: 1.59x faster                                                             |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                            |
| crypto_pyaes             | 119 ms                                                       | 75.1 ms: 1.59x faster                                                            |
| pyflate                  | 733 ms                                                       | 470 ms: 1.56x faster                                                             |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.55x faster                                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 618 ms: 1.52x faster                                                             |
| hexiom                   | 9.42 ms                                                      | 6.29 ms: 1.50x faster                                                            |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.49x faster                                                            |
| nbody                    | 134 ms                                                       | 89.9 ms: 1.49x faster                                                            |
| richards_super           | 90.6 ms                                                      | 61.4 ms: 1.48x faster                                                            |
| spectral_norm            | 139 ms                                                       | 94.7 ms: 1.47x faster                                                            |
| unpickle_pure_python     | 312 us                                                       | 215 us: 1.45x faster                                                             |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.43x faster                                                             |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                            |
| bench_mp_pool            | 6.37 ms                                                      | 4.57 ms: 1.39x faster                                                            |
| richards                 | 75.1 ms                                                      | 54.4 ms: 1.38x faster                                                            |
| float                    | 111 ms                                                       | 80.6 ms: 1.38x faster                                                            |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.38x faster                                                            |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                           |
| fannkuch                 | 483 ms                                                       | 357 ms: 1.35x faster                                                             |
| logging_simple           | 8.88 us                                                      | 6.59 us: 1.35x faster                                                            |
| logging_format           | 9.64 us                                                      | 7.21 us: 1.34x faster                                                            |
| thrift                   | 1.18 ms                                                      | 886 us: 1.33x faster                                                             |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                            |
| tornado_http             | 157 ms                                                       | 120 ms: 1.31x faster                                                             |
| deepcopy_memo            | 49.8 us                                                      | 38.3 us: 1.30x faster                                                            |
| nqueens                  | 115 ms                                                       | 88.6 ms: 1.30x faster                                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 813 ms: 1.29x faster                                                             |
| regex_compile            | 190 ms                                                       | 148 ms: 1.29x faster                                                             |
| django_template          | 50.2 ms                                                      | 39.3 ms: 1.28x faster                                                            |
| html5lib                 | 94.6 ms                                                      | 74.9 ms: 1.26x faster                                                            |
| xml_etree_process        | 75.9 ms                                                      | 60.3 ms: 1.26x faster                                                            |
| bench_thread_pool        | 1.14 ms                                                      | 912 us: 1.25x faster                                                             |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                            |
| sympy_sum                | 193 ms                                                       | 157 ms: 1.23x faster                                                             |
| json_loads               | 30.3 us                                                      | 24.8 us: 1.22x faster                                                            |
| deepcopy                 | 468 us                                                       | 384 us: 1.22x faster                                                             |
| dulwich_log              | 81.1 ms                                                      | 66.5 ms: 1.22x faster                                                            |
| scimark_fft              | 361 ms                                                       | 297 ms: 1.22x faster                                                             |
| 2to3                     | 350 ms                                                       | 288 ms: 1.22x faster                                                             |
| genshi_text              | 31.4 ms                                                      | 26.0 ms: 1.21x faster                                                            |
| mypy2                    | 933 ms                                                       | 774 ms: 1.21x faster                                                             |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.20x faster                                                           |
| chameleon                | 9.44 ms                                                      | 7.86 ms: 1.20x faster                                                            |
| sympy_str                | 360 ms                                                       | 301 ms: 1.20x faster                                                             |
| dask                     | 472 ms                                                       | 395 ms: 1.20x faster                                                             |
| sympy_integrate          | 28.2 ms                                                      | 23.6 ms: 1.20x faster                                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.30 ms: 1.18x faster                                                            |
| sqlglot_normalize        | 144 ms                                                       | 122 ms: 1.18x faster                                                             |
| sqlglot_optimize         | 70.1 ms                                                      | 59.7 ms: 1.18x faster                                                            |
| async_generators         | 421 ms                                                       | 360 ms: 1.17x faster                                                             |
| sympy_expand             | 600 ms                                                       | 513 ms: 1.17x faster                                                             |
| deepcopy_reduce          | 4.01 us                                                      | 3.44 us: 1.17x faster                                                            |
| tomli_loads              | 2.92 sec                                                     | 2.57 sec: 1.13x faster                                                           |
| docutils                 | 3.41 sec                                                     | 3.02 sec: 1.13x faster                                                           |
| genshi_xml               | 63.3 ms                                                      | 56.7 ms: 1.12x faster                                                            |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                             |
| regex_dna                | 261 ms                                                       | 235 ms: 1.11x faster                                                             |
| gunicorn                 | 1.16 ms                                                      | 1.05 ms: 1.10x faster                                                            |
| aiohttp                  | 1.19 ms                                                      | 1.10 ms: 1.08x faster                                                            |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                                             |
| sqlite_synth             | 2.99 us                                                      | 2.79 us: 1.07x faster                                                            |
| json                     | 5.86 ms                                                      | 5.51 ms: 1.06x faster                                                            |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                                             |
| pidigits                 | 271 ms                                                       | 257 ms: 1.06x faster                                                             |
| xml_etree_generate       | 92.3 ms                                                      | 88.6 ms: 1.04x faster                                                            |
| regex_v8                 | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                                            |
| unpickle_list            | 4.65 us                                                      | 4.82 us: 1.04x slower                                                            |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.04x slower                                                            |
| pickle_dict              | 29.5 us                                                      | 30.9 us: 1.05x slower                                                            |
| flaskblogging            | 4.39 ms                                                      | 4.64 ms: 1.06x slower                                                            |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                            |
| pickle_list              | 4.12 us                                                      | 4.52 us: 1.10x slower                                                            |
| regex_effbot             | 3.09 ms                                                      | 3.42 ms: 1.11x slower                                                            |
| python_startup           | 11.5 ms                                                      | 12.8 ms: 1.12x slower                                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                                            |
| telco                    | 7.23 ms                                                      | 8.30 ms: 1.15x slower                                                            |
| python_startup_no_site   | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                            |
| coverage                 | 63.3 ms                                                      | 83.2 ms: 1.32x slower                                                            |
| gc_traversal             | 3.42 ms                                                      | 4.67 ms: 1.37x slower                                                            |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240504-3.13.0a6+-4c1049b/bm-20240504-pythonperf2-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.12x