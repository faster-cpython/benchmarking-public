# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 292 ms: 1.20x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.28 ms: 1.30x faster                                            |
| docutils       | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                           |
| html5lib       | 94.6 ms                                                      | 76.2 ms: 1.24x faster                                            |
| tornado_http   | 157 ms                                                       | 123 ms: 1.28x faster                                             |
| Geometric mean | (ref)                                                        | 1.24x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 433 ms: 1.60x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 543 ms: 1.51x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 1.07 sec: 1.49x faster                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 697 ms: 1.34x faster                                             |
| Geometric mean          | (ref)                                                        | 1.48x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 91.5 ms: 1.47x faster                                            |
| float          | 111 ms                                                       | 78.8 ms: 1.41x faster                                            |
| pidigits       | 271 ms                                                       | 262 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                        | 1.29x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                             |
| regex_dna      | 261 ms                                                       | 237 ms: 1.10x faster                                             |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                            |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                            |
| Geometric mean | (ref)                                                        | 1.07x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 305 us: 1.49x faster                                             |
| unpickle_pure_python | 312 us                                                       | 211 us: 1.48x faster                                             |
| json_dumps           | 14.5 ms                                                      | 10.3 ms: 1.41x faster                                            |
| tomli_loads          | 2.92 sec                                                     | 2.29 sec: 1.27x faster                                           |
| xml_etree_process    | 75.9 ms                                                      | 60.2 ms: 1.26x faster                                            |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.11x faster                                             |
| xml_etree_generate   | 92.3 ms                                                      | 87.7 ms: 1.05x faster                                            |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                             |
| unpickle_list        | 4.65 us                                                      | 4.56 us: 1.02x faster                                            |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                            |
| pickle_dict          | 29.5 us                                                      | 31.0 us: 1.05x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.51 us: 1.09x slower                                            |
| unpickle             | 13.5 us                                                      | 15.3 us: 1.13x slower                                            |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.7 ms: 1.10x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 11.1 ms: 1.51x slower                                            |
| Geometric mean         | (ref)                                                        | 1.29x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                            |
| django_template | 50.2 ms                                                      | 37.7 ms: 1.33x faster                                            |
| genshi_text     | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                            |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 116 us: 4.63x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.56 ms: 2.10x faster                                            |
| asyncio_tcp              | 779 ms                                                       | 377 ms: 2.07x faster                                             |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                           |
| raytrace                 | 489 ms                                                       | 253 ms: 1.93x faster                                             |
| chaos                    | 109 ms                                                       | 61.1 ms: 1.78x faster                                            |
| scimark_lu               | 167 ms                                                       | 94.6 ms: 1.76x faster                                            |
| logging_silent           | 167 ns                                                       | 95.3 ns: 1.76x faster                                            |
| generators               | 57.3 ms                                                      | 33.1 ms: 1.73x faster                                            |
| pylint                   | 566 ms                                                       | 344 ms: 1.65x faster                                             |
| crypto_pyaes             | 119 ms                                                       | 72.5 ms: 1.64x faster                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                            |
| comprehensions           | 26.7 us                                                      | 16.7 us: 1.60x faster                                            |
| async_tree_none          | 692 ms                                                       | 433 ms: 1.60x faster                                             |
| richards_super           | 90.6 ms                                                      | 57.5 ms: 1.58x faster                                            |
| go                       | 262 ms                                                       | 167 ms: 1.57x faster                                             |
| scimark_monte_carlo      | 107 ms                                                       | 70.6 ms: 1.52x faster                                            |
| async_tree_memoization   | 819 ms                                                       | 543 ms: 1.51x faster                                             |
| spectral_norm            | 139 ms                                                       | 92.4 ms: 1.51x faster                                            |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                            |
| hexiom                   | 9.42 ms                                                      | 6.32 ms: 1.49x faster                                            |
| pickle_pure_python       | 455 us                                                       | 305 us: 1.49x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 1.07 sec: 1.49x faster                                           |
| unpickle_pure_python     | 312 us                                                       | 211 us: 1.48x faster                                             |
| richards                 | 75.1 ms                                                      | 51.2 ms: 1.47x faster                                            |
| nbody                    | 134 ms                                                       | 91.5 ms: 1.47x faster                                            |
| mako                     | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                            |
| pyflate                  | 733 ms                                                       | 509 ms: 1.44x faster                                             |
| bench_mp_pool            | 6.37 ms                                                      | 4.49 ms: 1.42x faster                                            |
| float                    | 111 ms                                                       | 78.8 ms: 1.41x faster                                            |
| json_dumps               | 14.5 ms                                                      | 10.3 ms: 1.41x faster                                            |
| logging_simple           | 8.88 us                                                      | 6.44 us: 1.38x faster                                            |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.36x faster                                            |
| logging_format           | 9.64 us                                                      | 7.11 us: 1.36x faster                                            |
| thrift                   | 1.18 ms                                                      | 870 us: 1.35x faster                                             |
| deepcopy_memo            | 49.8 us                                                      | 37.0 us: 1.34x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 697 ms: 1.34x faster                                             |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                             |
| django_template          | 50.2 ms                                                      | 37.7 ms: 1.33x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 800 ms: 1.31x faster                                             |
| chameleon                | 9.44 ms                                                      | 7.28 ms: 1.30x faster                                            |
| nqueens                  | 115 ms                                                       | 88.7 ms: 1.30x faster                                            |
| tornado_http             | 157 ms                                                       | 123 ms: 1.28x faster                                             |
| pycparser                | 1.67 sec                                                     | 1.31 sec: 1.28x faster                                           |
| tomli_loads              | 2.92 sec                                                     | 2.29 sec: 1.27x faster                                           |
| scimark_sor              | 180 ms                                                       | 143 ms: 1.26x faster                                             |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.26x faster                                             |
| xml_etree_process        | 75.9 ms                                                      | 60.2 ms: 1.26x faster                                            |
| deepcopy                 | 468 us                                                       | 373 us: 1.25x faster                                             |
| html5lib                 | 94.6 ms                                                      | 76.2 ms: 1.24x faster                                            |
| json_loads               | 30.3 us                                                      | 24.5 us: 1.24x faster                                            |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                             |
| sympy_str                | 360 ms                                                       | 293 ms: 1.23x faster                                             |
| genshi_text              | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.29 us: 1.22x faster                                            |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.20 ms: 1.21x faster                                            |
| docutils                 | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                           |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                           |
| 2to3                     | 350 ms                                                       | 292 ms: 1.20x faster                                             |
| sympy_expand             | 600 ms                                                       | 504 ms: 1.19x faster                                             |
| fannkuch                 | 483 ms                                                       | 406 ms: 1.19x faster                                             |
| dask                     | 472 ms                                                       | 397 ms: 1.19x faster                                             |
| sqlglot_optimize         | 70.1 ms                                                      | 59.1 ms: 1.19x faster                                            |
| dulwich_log              | 81.1 ms                                                      | 68.8 ms: 1.18x faster                                            |
| scimark_fft              | 361 ms                                                       | 307 ms: 1.18x faster                                             |
| bench_thread_pool        | 1.14 ms                                                      | 979 us: 1.17x faster                                             |
| genshi_xml               | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                            |
| async_generators         | 421 ms                                                       | 366 ms: 1.15x faster                                             |
| pathlib                  | 21.4 ms                                                      | 18.9 ms: 1.13x faster                                            |
| gunicorn                 | 1.16 ms                                                      | 1.04 ms: 1.11x faster                                            |
| sqlite_synth             | 2.99 us                                                      | 2.69 us: 1.11x faster                                            |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.11x faster                                             |
| regex_dna                | 261 ms                                                       | 237 ms: 1.10x faster                                             |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                            |
| create_gc_cycles         | 1.76 ms                                                      | 1.61 ms: 1.10x faster                                            |
| aiohttp                  | 1.19 ms                                                      | 1.09 ms: 1.09x faster                                            |
| mypy2                    | 933 ms                                                       | 864 ms: 1.08x faster                                             |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                             |
| xml_etree_generate       | 92.3 ms                                                      | 87.7 ms: 1.05x faster                                            |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                            |
| pidigits                 | 271 ms                                                       | 262 ms: 1.04x faster                                             |
| unpickle_list            | 4.65 us                                                      | 4.56 us: 1.02x faster                                            |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                             |
| pickle                   | 9.89 us                                                      | 10.2 us: 1.03x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 3.55 ms: 1.04x slower                                            |
| pickle_dict              | 29.5 us                                                      | 31.0 us: 1.05x slower                                            |
| flaskblogging            | 4.39 ms                                                      | 4.66 ms: 1.06x slower                                            |
| pickle_list              | 4.12 us                                                      | 4.51 us: 1.09x slower                                            |
| python_startup           | 11.5 ms                                                      | 12.7 ms: 1.10x slower                                            |
| telco                    | 7.23 ms                                                      | 8.09 ms: 1.12x slower                                            |
| unpickle                 | 13.5 us                                                      | 15.3 us: 1.13x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                            |
| coverage                 | 63.3 ms                                                      | 78.5 ms: 1.24x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 11.1 ms: 1.51x slower                                            |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                     |
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.08x