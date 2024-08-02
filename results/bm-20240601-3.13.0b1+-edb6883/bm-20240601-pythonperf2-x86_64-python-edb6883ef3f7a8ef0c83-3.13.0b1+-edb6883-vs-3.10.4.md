# Results vs. 3.10.4

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: linux-x86_64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 293 ms: 1.19x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.46 ms: 1.27x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                       |
| html5lib       | 94.6 ms                                                      | 73.7 ms: 1.28x faster                                                        |
| tornado_http   | 157 ms                                                       | 119 ms: 1.32x faster                                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 368 ms: 1.88x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 885 ms: 1.81x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 464 ms: 1.77x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 612 ms: 1.53x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.74x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 87.0 ms: 1.54x faster                                                        |
| float          | 111 ms                                                       | 79.2 ms: 1.40x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 144 ms: 1.32x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                                        |
| regex_dna      | 261 ms                                                       | 251 ms: 1.04x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 310 us: 1.47x faster                                                         |
| unpickle_pure_python | 312 us                                                       | 224 us: 1.39x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.5 ms: 1.25x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.8 us: 1.22x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.40 sec: 1.22x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 86.7 ms: 1.06x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.79 us: 1.03x slower                                                        |
| pickle               | 9.89 us                                                      | 10.4 us: 1.05x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 31.1 us: 1.05x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.43 us: 1.08x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.2 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.1 ms: 1.14x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 8.79 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.7 ms: 1.38x faster                                                        |
| django_template | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 25.9 ms: 1.21x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 56.7 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.09x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.36 ms: 2.23x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 378 ms: 2.06x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| async_tree_none          | 692 ms                                                       | 368 ms: 1.88x faster                                                         |
| raytrace                 | 489 ms                                                       | 265 ms: 1.84x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 885 ms: 1.81x faster                                                         |
| chaos                    | 109 ms                                                       | 60.7 ms: 1.79x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 464 ms: 1.77x faster                                                         |
| logging_silent           | 167 ns                                                       | 97.5 ns: 1.72x faster                                                        |
| scimark_lu               | 167 ms                                                       | 97.4 ms: 1.71x faster                                                        |
| generators               | 57.3 ms                                                      | 34.3 ms: 1.67x faster                                                        |
| pylint                   | 566 ms                                                       | 342 ms: 1.65x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 72.7 ms: 1.64x faster                                                        |
| go                       | 262 ms                                                       | 160 ms: 1.63x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 66.2 ms: 1.62x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                        |
| scimark_sor              | 180 ms                                                       | 114 ms: 1.57x faster                                                         |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                                        |
| nbody                    | 134 ms                                                       | 87.0 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 612 ms: 1.53x faster                                                         |
| pyflate                  | 733 ms                                                       | 482 ms: 1.52x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.51x faster                                                        |
| richards_super           | 90.6 ms                                                      | 61.5 ms: 1.47x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 310 us: 1.47x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 6.55 ms: 1.44x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.8 ms: 1.44x faster                                                        |
| float                    | 111 ms                                                       | 79.2 ms: 1.40x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 224 us: 1.39x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.39 us: 1.39x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.97 us: 1.38x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.38x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.38x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| richards                 | 75.1 ms                                                      | 55.3 ms: 1.36x faster                                                        |
| fannkuch                 | 483 ms                                                       | 355 ms: 1.36x faster                                                         |
| thrift                   | 1.18 ms                                                      | 867 us: 1.36x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 37.3 us: 1.33x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.81 ms: 1.33x faster                                                        |
| regex_compile            | 190 ms                                                       | 144 ms: 1.32x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                       |
| tornado_http             | 157 ms                                                       | 119 ms: 1.32x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 73.7 ms: 1.28x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.28x faster                                                       |
| django_template          | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 826 ms: 1.27x faster                                                         |
| chameleon                | 9.44 ms                                                      | 7.46 ms: 1.27x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 903 us: 1.26x faster                                                         |
| nqueens                  | 115 ms                                                       | 91.1 ms: 1.26x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 60.5 ms: 1.25x faster                                                        |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                                        |
| deepcopy                 | 468 us                                                       | 380 us: 1.23x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.8 us: 1.22x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.40 sec: 1.22x faster                                                       |
| sympy_str                | 360 ms                                                       | 297 ms: 1.21x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 25.9 ms: 1.21x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.19 ms: 1.21x faster                                                        |
| mypy2                    | 933 ms                                                       | 770 ms: 1.21x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 67.5 ms: 1.20x faster                                                        |
| dask                     | 472 ms                                                       | 393 ms: 1.20x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.5 ms: 1.20x faster                                                        |
| 2to3                     | 350 ms                                                       | 293 ms: 1.19x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.19x faster                                                       |
| scimark_fft              | 361 ms                                                       | 304 ms: 1.19x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 121 ms: 1.19x faster                                                         |
| sympy_expand             | 600 ms                                                       | 506 ms: 1.18x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 59.4 ms: 1.18x faster                                                        |
| async_generators         | 421 ms                                                       | 359 ms: 1.17x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.42 us: 1.17x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                       |
| json                     | 5.86 ms                                                      | 5.23 ms: 1.12x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 56.7 ms: 1.12x faster                                                        |
| aiohttp                  | 1.19 ms                                                      | 1.07 ms: 1.11x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                         |
| gunicorn                 | 1.16 ms                                                      | 1.05 ms: 1.10x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                         |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 86.7 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| regex_dna                | 261 ms                                                       | 251 ms: 1.04x faster                                                         |
| unpickle_list            | 4.65 us                                                      | 4.79 us: 1.03x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.4 us: 1.05x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 31.1 us: 1.05x slower                                                        |
| flaskblogging            | 4.39 ms                                                      | 4.70 ms: 1.07x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.43 us: 1.08x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.2 us: 1.12x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                        |
| python_startup           | 11.5 ms                                                      | 13.1 ms: 1.14x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.58 ms: 1.19x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.79 ms: 1.20x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                        |
| coverage                 | 63.3 ms                                                      | 86.7 ms: 1.37x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240601-3.13.0b1+-edb6883/bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.12x