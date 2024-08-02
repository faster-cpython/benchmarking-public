# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 291 ms: 1.20x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.40 ms: 1.28x faster                                            |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                           |
| html5lib       | 94.6 ms                                                      | 74.7 ms: 1.27x faster                                            |
| tornado_http   | 157 ms                                                       | 119 ms: 1.31x faster                                             |
| Geometric mean | (ref)                                                        | 1.24x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 365 ms: 1.89x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 873 ms: 1.83x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 460 ms: 1.78x faster                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 604 ms: 1.55x faster                                             |
| Geometric mean          | (ref)                                                        | 1.76x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 87.8 ms: 1.53x faster                                            |
| float          | 111 ms                                                       | 80.2 ms: 1.39x faster                                            |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                             |
| Geometric mean | (ref)                                                        | 1.31x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 144 ms: 1.32x faster                                             |
| regex_dna      | 261 ms                                                       | 249 ms: 1.05x faster                                             |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                            |
| regex_effbot   | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                            |
| Geometric mean | (ref)                                                        | 1.07x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 307 us: 1.48x faster                                             |
| unpickle_pure_python | 312 us                                                       | 224 us: 1.39x faster                                             |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                            |
| xml_etree_process    | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                            |
| tomli_loads          | 2.92 sec                                                     | 2.40 sec: 1.21x faster                                           |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.08x faster                                             |
| xml_etree_generate   | 92.3 ms                                                      | 85.7 ms: 1.08x faster                                            |
| unpickle_list        | 4.65 us                                                      | 4.70 us: 1.01x slower                                            |
| pickle               | 9.89 us                                                      | 10.6 us: 1.07x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.44 us: 1.08x slower                                            |
| pickle_dict          | 29.5 us                                                      | 32.8 us: 1.11x slower                                            |
| unpickle             | 13.5 us                                                      | 15.7 us: 1.16x slower                                            |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 8.85 ms: 1.21x slower                                            |
| Geometric mean         | (ref)                                                        | 1.18x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                            |
| django_template | 50.2 ms                                                      | 39.0 ms: 1.29x faster                                            |
| genshi_text     | 31.4 ms                                                      | 25.9 ms: 1.21x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 58.1 ms: 1.09x faster                                            |
| Geometric mean  | (ref)                                                        | 1.25x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.15x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.37 ms: 2.22x faster                                            |
| asyncio_tcp              | 779 ms                                                       | 378 ms: 2.06x faster                                             |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                           |
| async_tree_none          | 692 ms                                                       | 365 ms: 1.89x faster                                             |
| raytrace                 | 489 ms                                                       | 260 ms: 1.88x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 873 ms: 1.83x faster                                             |
| chaos                    | 109 ms                                                       | 59.6 ms: 1.82x faster                                            |
| async_tree_memoization   | 819 ms                                                       | 460 ms: 1.78x faster                                             |
| logging_silent           | 167 ns                                                       | 96.3 ns: 1.74x faster                                            |
| scimark_lu               | 167 ms                                                       | 97.5 ms: 1.71x faster                                            |
| generators               | 57.3 ms                                                      | 33.5 ms: 1.71x faster                                            |
| pylint                   | 566 ms                                                       | 339 ms: 1.67x faster                                             |
| scimark_monte_carlo      | 107 ms                                                       | 65.5 ms: 1.64x faster                                            |
| crypto_pyaes             | 119 ms                                                       | 73.6 ms: 1.62x faster                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                            |
| go                       | 262 ms                                                       | 165 ms: 1.59x faster                                             |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 604 ms: 1.55x faster                                             |
| nbody                    | 134 ms                                                       | 87.8 ms: 1.53x faster                                            |
| pyflate                  | 733 ms                                                       | 482 ms: 1.52x faster                                             |
| sqlglot_transpile        | 2.68 ms                                                      | 1.76 ms: 1.52x faster                                            |
| scimark_sor              | 180 ms                                                       | 119 ms: 1.52x faster                                             |
| hexiom                   | 9.42 ms                                                      | 6.35 ms: 1.48x faster                                            |
| richards_super           | 90.6 ms                                                      | 61.2 ms: 1.48x faster                                            |
| pickle_pure_python       | 455 us                                                       | 307 us: 1.48x faster                                             |
| spectral_norm            | 139 ms                                                       | 97.3 ms: 1.43x faster                                            |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                            |
| richards                 | 75.1 ms                                                      | 53.4 ms: 1.41x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 224 us: 1.39x faster                                             |
| logging_simple           | 8.88 us                                                      | 6.40 us: 1.39x faster                                            |
| float                    | 111 ms                                                       | 80.2 ms: 1.39x faster                                            |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.38x faster                                            |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                           |
| fannkuch                 | 483 ms                                                       | 353 ms: 1.37x faster                                             |
| logging_format           | 9.64 us                                                      | 7.11 us: 1.36x faster                                            |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                            |
| thrift                   | 1.18 ms                                                      | 880 us: 1.34x faster                                             |
| deepcopy_memo            | 49.8 us                                                      | 37.3 us: 1.34x faster                                            |
| regex_compile            | 190 ms                                                       | 144 ms: 1.32x faster                                             |
| tornado_http             | 157 ms                                                       | 119 ms: 1.31x faster                                             |
| nqueens                  | 115 ms                                                       | 88.4 ms: 1.30x faster                                            |
| bench_mp_pool            | 6.37 ms                                                      | 4.91 ms: 1.30x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                           |
| django_template          | 50.2 ms                                                      | 39.0 ms: 1.29x faster                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 818 ms: 1.28x faster                                             |
| chameleon                | 9.44 ms                                                      | 7.40 ms: 1.28x faster                                            |
| xml_etree_process        | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                            |
| html5lib                 | 94.6 ms                                                      | 74.7 ms: 1.27x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 908 us: 1.26x faster                                             |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                            |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                             |
| deepcopy                 | 468 us                                                       | 377 us: 1.24x faster                                             |
| sympy_str                | 360 ms                                                       | 295 ms: 1.22x faster                                             |
| mdp                      | 3.01 sec                                                     | 2.46 sec: 1.22x faster                                           |
| mypy2                    | 933 ms                                                       | 764 ms: 1.22x faster                                             |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.22x faster                                            |
| genshi_text              | 31.4 ms                                                      | 25.9 ms: 1.21x faster                                            |
| tomli_loads              | 2.92 sec                                                     | 2.40 sec: 1.21x faster                                           |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                            |
| dask                     | 472 ms                                                       | 391 ms: 1.21x faster                                             |
| dulwich_log              | 81.1 ms                                                      | 67.3 ms: 1.21x faster                                            |
| 2to3                     | 350 ms                                                       | 291 ms: 1.20x faster                                             |
| sympy_expand             | 600 ms                                                       | 501 ms: 1.20x faster                                             |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                             |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.28 ms: 1.19x faster                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.39 us: 1.18x faster                                            |
| sqlglot_optimize         | 70.1 ms                                                      | 59.5 ms: 1.18x faster                                            |
| async_generators         | 421 ms                                                       | 363 ms: 1.16x faster                                             |
| scimark_fft              | 361 ms                                                       | 312 ms: 1.16x faster                                             |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                           |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                             |
| gunicorn                 | 1.16 ms                                                      | 1.04 ms: 1.11x faster                                            |
| aiohttp                  | 1.19 ms                                                      | 1.07 ms: 1.11x faster                                            |
| json                     | 5.86 ms                                                      | 5.35 ms: 1.10x faster                                            |
| genshi_xml               | 63.3 ms                                                      | 58.1 ms: 1.09x faster                                            |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                             |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.08x faster                                             |
| xml_etree_generate       | 92.3 ms                                                      | 85.7 ms: 1.08x faster                                            |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                            |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                             |
| regex_dna                | 261 ms                                                       | 249 ms: 1.05x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                            |
| unpickle_list            | 4.65 us                                                      | 4.70 us: 1.01x slower                                            |
| asyncio_websockets       | 390 ms                                                       | 395 ms: 1.01x slower                                             |
| flaskblogging            | 4.39 ms                                                      | 4.68 ms: 1.07x slower                                            |
| pickle                   | 9.89 us                                                      | 10.6 us: 1.07x slower                                            |
| pickle_list              | 4.12 us                                                      | 4.44 us: 1.08x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                            |
| pickle_dict              | 29.5 us                                                      | 32.8 us: 1.11x slower                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.00 ms: 1.14x slower                                            |
| python_startup           | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                            |
| telco                    | 7.23 ms                                                      | 8.40 ms: 1.16x slower                                            |
| unpickle                 | 13.5 us                                                      | 15.7 us: 1.16x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 8.85 ms: 1.21x slower                                            |
| coverage                 | 63.3 ms                                                      | 83.5 ms: 1.32x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 4.69 ms: 1.37x slower                                            |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                     |
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x