# Results vs. 3.13.0b2

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.28x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 350 ms: 1.20x slower                                         |
| chameleon      | 7.40 ms                                                          | 9.44 ms: 1.28x slower                                        |
| docutils       | 2.98 sec                                                         | 3.41 sec: 1.14x slower                                       |
| html5lib       | 74.7 ms                                                          | 94.6 ms: 1.27x slower                                        |
| tornado_http   | 119 ms                                                           | 157 ms: 1.31x slower                                         |
| Geometric mean | (ref)                                                            | 1.24x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 604 ms                                                           | 936 ms: 1.55x slower                                         |
| async_tree_memoization  | 460 ms                                                           | 819 ms: 1.78x slower                                         |
| async_tree_io           | 873 ms                                                           | 1.60 sec: 1.83x slower                                       |
| async_tree_none         | 365 ms                                                           | 692 ms: 1.89x slower                                         |
| Geometric mean          | (ref)                                                            | 1.76x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 271 ms: 1.07x slower                                         |
| float          | 80.2 ms                                                          | 111 ms: 1.39x slower                                         |
| nbody          | 87.8 ms                                                          | 134 ms: 1.53x slower                                         |
| Geometric mean | (ref)                                                            | 1.31x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.40 ms                                                          | 3.09 ms: 1.10x faster                                        |
| regex_v8       | 26.0 ms                                                          | 27.2 ms: 1.04x slower                                        |
| regex_dna      | 249 ms                                                           | 261 ms: 1.05x slower                                         |
| regex_compile  | 144 ms                                                           | 190 ms: 1.32x slower                                         |
| Geometric mean | (ref)                                                            | 1.07x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle             | 15.7 us                                                          | 13.5 us: 1.16x faster                                        |
| pickle_dict          | 32.8 us                                                          | 29.5 us: 1.11x faster                                        |
| pickle_list          | 4.44 us                                                          | 4.12 us: 1.08x faster                                        |
| pickle               | 10.6 us                                                          | 9.89 us: 1.07x faster                                        |
| unpickle_list        | 4.70 us                                                          | 4.65 us: 1.01x faster                                        |
| xml_etree_generate   | 85.7 ms                                                          | 92.3 ms: 1.08x slower                                        |
| xml_etree_iterparse  | 103 ms                                                           | 110 ms: 1.08x slower                                         |
| xml_etree_parse      | 144 ms                                                           | 160 ms: 1.11x slower                                         |
| json_loads           | 25.0 us                                                          | 30.3 us: 1.21x slower                                        |
| tomli_loads          | 2.40 sec                                                         | 2.92 sec: 1.21x slower                                       |
| xml_etree_process    | 59.7 ms                                                          | 75.9 ms: 1.27x slower                                        |
| json_dumps           | 10.8 ms                                                          | 14.5 ms: 1.35x slower                                        |
| unpickle_pure_python | 224 us                                                           | 312 us: 1.39x slower                                         |
| pickle_pure_python   | 307 us                                                           | 455 us: 1.48x slower                                         |
| Geometric mean       | (ref)                                                            | 1.11x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 7.33 ms: 1.21x faster                                        |
| python_startup         | 13.2 ms                                                          | 11.5 ms: 1.15x faster                                        |
| Geometric mean         | (ref)                                                            | 1.18x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 63.3 ms: 1.09x slower                                        |
| genshi_text     | 25.9 ms                                                          | 31.4 ms: 1.21x slower                                        |
| django_template | 39.0 ms                                                          | 50.2 ms: 1.29x slower                                        |
| mako            | 10.4 ms                                                          | 14.7 ms: 1.42x slower                                        |
| Geometric mean  | (ref)                                                            | 1.25x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| gc_traversal             | 4.69 ms                                                          | 3.42 ms: 1.37x faster                                        |
| coverage                 | 83.5 ms                                                          | 63.3 ms: 1.32x faster                                        |
| python_startup_no_site   | 8.85 ms                                                          | 7.33 ms: 1.21x faster                                        |
| unpickle                 | 15.7 us                                                          | 13.5 us: 1.16x faster                                        |
| telco                    | 8.40 ms                                                          | 7.23 ms: 1.16x faster                                        |
| python_startup           | 13.2 ms                                                          | 11.5 ms: 1.15x faster                                        |
| create_gc_cycles         | 2.00 ms                                                          | 1.76 ms: 1.14x faster                                        |
| pickle_dict              | 32.8 us                                                          | 29.5 us: 1.11x faster                                        |
| regex_effbot             | 3.40 ms                                                          | 3.09 ms: 1.10x faster                                        |
| pickle_list              | 4.44 us                                                          | 4.12 us: 1.08x faster                                        |
| pickle                   | 10.6 us                                                          | 9.89 us: 1.07x faster                                        |
| flaskblogging            | 4.68 ms                                                          | 4.39 ms: 1.07x faster                                        |
| asyncio_websockets       | 395 ms                                                           | 390 ms: 1.01x faster                                         |
| unpickle_list            | 4.70 us                                                          | 4.65 us: 1.01x faster                                        |
| regex_v8                 | 26.0 ms                                                          | 27.2 ms: 1.04x slower                                        |
| regex_dna                | 249 ms                                                           | 261 ms: 1.05x slower                                         |
| pidigits                 | 254 ms                                                           | 271 ms: 1.07x slower                                         |
| sqlite_synth             | 2.80 us                                                          | 2.99 us: 1.07x slower                                        |
| xml_etree_generate       | 85.7 ms                                                          | 92.3 ms: 1.08x slower                                        |
| xml_etree_iterparse      | 103 ms                                                           | 110 ms: 1.08x slower                                         |
| meteor_contest           | 128 ms                                                           | 138 ms: 1.08x slower                                         |
| genshi_xml               | 58.1 ms                                                          | 63.3 ms: 1.09x slower                                        |
| json                     | 5.35 ms                                                          | 5.86 ms: 1.10x slower                                        |
| aiohttp                  | 1.07 ms                                                          | 1.19 ms: 1.11x slower                                        |
| gunicorn                 | 1.04 ms                                                          | 1.16 ms: 1.11x slower                                        |
| xml_etree_parse          | 144 ms                                                           | 160 ms: 1.11x slower                                         |
| docutils                 | 2.98 sec                                                         | 3.41 sec: 1.14x slower                                       |
| scimark_fft              | 312 ms                                                           | 361 ms: 1.16x slower                                         |
| async_generators         | 363 ms                                                           | 421 ms: 1.16x slower                                         |
| sqlglot_optimize         | 59.5 ms                                                          | 70.1 ms: 1.18x slower                                        |
| deepcopy_reduce          | 3.39 us                                                          | 4.01 us: 1.18x slower                                        |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 5.08 ms: 1.19x slower                                        |
| sqlglot_normalize        | 120 ms                                                           | 144 ms: 1.20x slower                                         |
| sympy_expand             | 501 ms                                                           | 600 ms: 1.20x slower                                         |
| 2to3                     | 291 ms                                                           | 350 ms: 1.20x slower                                         |
| dulwich_log              | 67.3 ms                                                          | 81.1 ms: 1.21x slower                                        |
| dask                     | 391 ms                                                           | 472 ms: 1.21x slower                                         |
| json_loads               | 25.0 us                                                          | 30.3 us: 1.21x slower                                        |
| tomli_loads              | 2.40 sec                                                         | 2.92 sec: 1.21x slower                                       |
| genshi_text              | 25.9 ms                                                          | 31.4 ms: 1.21x slower                                        |
| sympy_integrate          | 23.2 ms                                                          | 28.2 ms: 1.22x slower                                        |
| mypy2                    | 764 ms                                                           | 933 ms: 1.22x slower                                         |
| mdp                      | 2.46 sec                                                         | 3.01 sec: 1.22x slower                                       |
| sympy_str                | 295 ms                                                           | 360 ms: 1.22x slower                                         |
| deepcopy                 | 377 us                                                           | 468 us: 1.24x slower                                         |
| sympy_sum                | 155 ms                                                           | 193 ms: 1.24x slower                                         |
| pathlib                  | 17.1 ms                                                          | 21.4 ms: 1.25x slower                                        |
| bench_thread_pool        | 908 us                                                           | 1.14 ms: 1.26x slower                                        |
| html5lib                 | 74.7 ms                                                          | 94.6 ms: 1.27x slower                                        |
| xml_etree_process        | 59.7 ms                                                          | 75.9 ms: 1.27x slower                                        |
| chameleon                | 7.40 ms                                                          | 9.44 ms: 1.28x slower                                        |
| pprint_safe_repr         | 818 ms                                                           | 1.05 sec: 1.28x slower                                       |
| django_template          | 39.0 ms                                                          | 50.2 ms: 1.29x slower                                        |
| pprint_pformat           | 1.66 sec                                                         | 2.15 sec: 1.30x slower                                       |
| bench_mp_pool            | 4.91 ms                                                          | 6.37 ms: 1.30x slower                                        |
| nqueens                  | 88.4 ms                                                          | 115 ms: 1.30x slower                                         |
| tornado_http             | 119 ms                                                           | 157 ms: 1.31x slower                                         |
| regex_compile            | 144 ms                                                           | 190 ms: 1.32x slower                                         |
| deepcopy_memo            | 37.3 us                                                          | 49.8 us: 1.34x slower                                        |
| thrift                   | 880 us                                                           | 1.18 ms: 1.34x slower                                        |
| json_dumps               | 10.8 ms                                                          | 14.5 ms: 1.35x slower                                        |
| logging_format           | 7.11 us                                                          | 9.64 us: 1.36x slower                                        |
| fannkuch                 | 353 ms                                                           | 483 ms: 1.37x slower                                         |
| pycparser                | 1.22 sec                                                         | 1.67 sec: 1.37x slower                                       |
| coroutines               | 22.0 ms                                                          | 30.3 ms: 1.38x slower                                        |
| float                    | 80.2 ms                                                          | 111 ms: 1.39x slower                                         |
| logging_simple           | 6.40 us                                                          | 8.88 us: 1.39x slower                                        |
| unpickle_pure_python     | 224 us                                                           | 312 us: 1.39x slower                                         |
| richards                 | 53.4 ms                                                          | 75.1 ms: 1.41x slower                                        |
| mako                     | 10.4 ms                                                          | 14.7 ms: 1.42x slower                                        |
| spectral_norm            | 97.3 ms                                                          | 139 ms: 1.43x slower                                         |
| pickle_pure_python       | 307 us                                                           | 455 us: 1.48x slower                                         |
| richards_super           | 61.2 ms                                                          | 90.6 ms: 1.48x slower                                        |
| hexiom                   | 6.35 ms                                                          | 9.42 ms: 1.48x slower                                        |
| scimark_sor              | 119 ms                                                           | 180 ms: 1.52x slower                                         |
| sqlglot_transpile        | 1.76 ms                                                          | 2.68 ms: 1.52x slower                                        |
| pyflate                  | 482 ms                                                           | 733 ms: 1.52x slower                                         |
| nbody                    | 87.8 ms                                                          | 134 ms: 1.53x slower                                         |
| async_tree_cpu_io_mixed  | 604 ms                                                           | 936 ms: 1.55x slower                                         |
| comprehensions           | 17.0 us                                                          | 26.7 us: 1.57x slower                                        |
| go                       | 165 ms                                                           | 262 ms: 1.59x slower                                         |
| sqlglot_parse            | 1.39 ms                                                          | 2.24 ms: 1.61x slower                                        |
| crypto_pyaes             | 73.6 ms                                                          | 119 ms: 1.62x slower                                         |
| scimark_monte_carlo      | 65.5 ms                                                          | 107 ms: 1.64x slower                                         |
| pylint                   | 339 ms                                                           | 566 ms: 1.67x slower                                         |
| generators               | 33.5 ms                                                          | 57.3 ms: 1.71x slower                                        |
| scimark_lu               | 97.5 ms                                                          | 167 ms: 1.71x slower                                         |
| logging_silent           | 96.3 ns                                                          | 167 ns: 1.74x slower                                         |
| async_tree_memoization   | 460 ms                                                           | 819 ms: 1.78x slower                                         |
| chaos                    | 59.6 ms                                                          | 109 ms: 1.82x slower                                         |
| async_tree_io            | 873 ms                                                           | 1.60 sec: 1.83x slower                                       |
| raytrace                 | 260 ms                                                           | 489 ms: 1.88x slower                                         |
| async_tree_none          | 365 ms                                                           | 692 ms: 1.89x slower                                         |
| asyncio_tcp_ssl          | 1.58 sec                                                         | 3.10 sec: 1.96x slower                                       |
| asyncio_tcp              | 378 ms                                                           | 779 ms: 2.06x slower                                         |
| deltablue                | 3.37 ms                                                          | 7.50 ms: 2.22x slower                                        |
| typing_runtime_protocols | 171 us                                                           | 537 us: 3.15x slower                                         |
| Geometric mean           | (ref)                                                            | 1.28x slower                                                 |
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.24x
- 95% likely to have a slowdown of 1.23x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 0.90x