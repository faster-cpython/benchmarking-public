# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c32dc47
- commit date: 2024-04-02
- overall geometric mean: 1.31x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240402-pythonperf2-x86_64-python-main-3.13.0a5+-c32dc47 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 288 ms: 1.21x faster                                         |
| chameleon      | 9.44 ms                                                      | 7.15 ms: 1.32x faster                                        |
| docutils       | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                       |
| html5lib       | 94.6 ms                                                      | 73.2 ms: 1.29x faster                                        |
| tornado_http   | 157 ms                                                       | 120 ms: 1.31x faster                                         |
| Geometric mean | (ref)                                                        | 1.25x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240402-pythonperf2-x86_64-python-main-3.13.0a5+-c32dc47 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 363 ms: 1.90x faster                                         |
| async_tree_io           | 1.60 sec                                                     | 883 ms: 1.81x faster                                         |
| async_tree_memoization  | 819 ms                                                       | 457 ms: 1.79x faster                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 607 ms: 1.54x faster                                         |
| Geometric mean          | (ref)                                                        | 1.76x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240402-pythonperf2-x86_64-python-main-3.13.0a5+-c32dc47 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.3 ms: 1.57x faster                                        |
| float          | 111 ms                                                       | 75.3 ms: 1.48x faster                                        |
| pidigits       | 271 ms                                                       | 263 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240402-pythonperf2-x86_64-python-main-3.13.0a5+-c32dc47 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                         |
| regex_dna      | 261 ms                                                       | 230 ms: 1.13x faster                                         |
| regex_v8       | 27.2 ms                                                      | 25.7 ms: 1.05x faster                                        |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240402-pythonperf2-x86_64-python-main-3.13.0a5+-c32dc47 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 305 us: 1.49x faster                                         |
| unpickle_pure_python | 312 us                                                       | 210 us: 1.48x faster                                         |
| json_dumps           | 14.5 ms                                                      | 10.5 ms: 1.39x faster                                        |
| tomli_loads          | 2.92 sec                                                     | 2.19 sec: 1.33x faster                                       |
| xml_etree_process    | 75.9 ms                                                      | 57.5 ms: 1.32x faster                                        |
| json_loads           | 30.3 us                                                      | 25.6 us: 1.18x faster                                        |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                         |
| xml_etree_generate   | 92.3 ms                                                      | 82.4 ms: 1.12x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.07x faster                                         |
| pickle               | 9.89 us                                                      | 10.5 us: 1.07x slower                                        |
| pickle_list          | 4.12 us                                                      | 4.53 us: 1.10x slower                                        |
| unpickle             | 13.5 us                                                      | 14.9 us: 1.10x slower                                        |
| pickle_dict          | 29.5 us                                                      | 33.1 us: 1.12x slower                                        |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240402-pythonperf2-x86_64-python-main-3.13.0a5+-c32dc47 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.9 ms: 1.12x slower                                        |
| python_startup_no_site | 7.33 ms                                                      | 11.1 ms: 1.52x slower                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240402-pythonperf2-x86_64-python-main-3.13.0a5+-c32dc47 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako           | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                        |
| genshi_text    | 31.4 ms                                                      | 25.1 ms: 1.25x faster                                        |
| genshi_xml     | 63.3 ms                                                      | 53.1 ms: 1.19x faster                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240402-pythonperf2-x86_64-python-main-3.13.0a5+-c32dc47 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 114 us: 4.70x faster                                         |
| deltablue                | 7.50 ms                                                      | 3.39 ms: 2.21x faster                                        |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                       |
| raytrace                 | 489 ms                                                       | 251 ms: 1.95x faster                                         |
| async_tree_none          | 692 ms                                                       | 363 ms: 1.90x faster                                         |
| chaos                    | 109 ms                                                       | 58.6 ms: 1.85x faster                                        |
| async_tree_io            | 1.60 sec                                                     | 883 ms: 1.81x faster                                         |
| async_tree_memoization   | 819 ms                                                       | 457 ms: 1.79x faster                                         |
| pylint                   | 566 ms                                                       | 317 ms: 1.79x faster                                         |
| logging_silent           | 167 ns                                                       | 93.8 ns: 1.78x faster                                        |
| scimark_lu               | 167 ms                                                       | 93.7 ms: 1.78x faster                                        |
| generators               | 57.3 ms                                                      | 33.1 ms: 1.73x faster                                        |
| scimark_monte_carlo      | 107 ms                                                       | 64.4 ms: 1.67x faster                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.36 ms: 1.65x faster                                        |
| crypto_pyaes             | 119 ms                                                       | 72.4 ms: 1.65x faster                                        |
| richards_super           | 90.6 ms                                                      | 57.0 ms: 1.59x faster                                        |
| comprehensions           | 26.7 us                                                      | 16.8 us: 1.59x faster                                        |
| nbody                    | 134 ms                                                       | 85.3 ms: 1.57x faster                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 607 ms: 1.54x faster                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.74 ms: 1.54x faster                                        |
| go                       | 262 ms                                                       | 170 ms: 1.54x faster                                         |
| spectral_norm            | 139 ms                                                       | 92.3 ms: 1.51x faster                                        |
| richards                 | 75.1 ms                                                      | 50.1 ms: 1.50x faster                                        |
| pickle_pure_python       | 455 us                                                       | 305 us: 1.49x faster                                         |
| unpickle_pure_python     | 312 us                                                       | 210 us: 1.48x faster                                         |
| hexiom                   | 9.42 ms                                                      | 6.38 ms: 1.48x faster                                        |
| float                    | 111 ms                                                       | 75.3 ms: 1.48x faster                                        |
| pyflate                  | 733 ms                                                       | 500 ms: 1.47x faster                                         |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.47 ms: 1.42x faster                                        |
| json_dumps               | 14.5 ms                                                      | 10.5 ms: 1.39x faster                                        |
| deepcopy_memo            | 49.8 us                                                      | 36.3 us: 1.37x faster                                        |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                       |
| thrift                   | 1.18 ms                                                      | 859 us: 1.37x faster                                         |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 780 ms: 1.35x faster                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.60 sec: 1.34x faster                                       |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                        |
| logging_simple           | 8.88 us                                                      | 6.62 us: 1.34x faster                                        |
| tomli_loads              | 2.92 sec                                                     | 2.19 sec: 1.33x faster                                       |
| xml_etree_process        | 75.9 ms                                                      | 57.5 ms: 1.32x faster                                        |
| chameleon                | 9.44 ms                                                      | 7.15 ms: 1.32x faster                                        |
| nqueens                  | 115 ms                                                       | 88.0 ms: 1.31x faster                                        |
| tornado_http             | 157 ms                                                       | 120 ms: 1.31x faster                                         |
| unpack_sequence          | 59.9 ns                                                      | 45.9 ns: 1.31x faster                                        |
| logging_format           | 9.64 us                                                      | 7.41 us: 1.30x faster                                        |
| fannkuch                 | 483 ms                                                       | 371 ms: 1.30x faster                                         |
| bench_thread_pool        | 1.14 ms                                                      | 880 us: 1.30x faster                                         |
| html5lib                 | 94.6 ms                                                      | 73.2 ms: 1.29x faster                                        |
| deepcopy                 | 468 us                                                       | 367 us: 1.27x faster                                         |
| scimark_sor              | 180 ms                                                       | 142 ms: 1.27x faster                                         |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                         |
| genshi_text              | 31.4 ms                                                      | 25.1 ms: 1.25x faster                                        |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                         |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                         |
| sympy_expand             | 600 ms                                                       | 491 ms: 1.22x faster                                         |
| 2to3                     | 350 ms                                                       | 288 ms: 1.21x faster                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                        |
| mypy2                    | 933 ms                                                       | 771 ms: 1.21x faster                                         |
| dask                     | 472 ms                                                       | 391 ms: 1.21x faster                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.21 ms: 1.21x faster                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 58.2 ms: 1.20x faster                                        |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                         |
| mdp                      | 3.01 sec                                                     | 2.51 sec: 1.20x faster                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.35 us: 1.20x faster                                        |
| genshi_xml               | 63.3 ms                                                      | 53.1 ms: 1.19x faster                                        |
| json_loads               | 30.3 us                                                      | 25.6 us: 1.18x faster                                        |
| async_generators         | 421 ms                                                       | 356 ms: 1.18x faster                                         |
| dulwich_log              | 81.1 ms                                                      | 69.0 ms: 1.18x faster                                        |
| docutils                 | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                       |
| regex_dna                | 261 ms                                                       | 230 ms: 1.13x faster                                         |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                         |
| xml_etree_generate       | 92.3 ms                                                      | 82.4 ms: 1.12x faster                                        |
| gunicorn                 | 1.16 ms                                                      | 1.04 ms: 1.12x faster                                        |
| pathlib                  | 21.4 ms                                                      | 19.2 ms: 1.11x faster                                        |
| sqlite_synth             | 2.99 us                                                      | 2.68 us: 1.11x faster                                        |
| aiohttp                  | 1.19 ms                                                      | 1.07 ms: 1.11x faster                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                         |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.07x faster                                         |
| regex_v8                 | 27.2 ms                                                      | 25.7 ms: 1.05x faster                                        |
| json                     | 5.86 ms                                                      | 5.58 ms: 1.05x faster                                        |
| pidigits                 | 271 ms                                                       | 263 ms: 1.03x faster                                         |
| asyncio_websockets       | 390 ms                                                       | 395 ms: 1.01x slower                                         |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.07x slower                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                        |
| pickle_list              | 4.12 us                                                      | 4.53 us: 1.10x slower                                        |
| unpickle                 | 13.5 us                                                      | 14.9 us: 1.10x slower                                        |
| telco                    | 7.23 ms                                                      | 8.04 ms: 1.11x slower                                        |
| pickle_dict              | 29.5 us                                                      | 33.1 us: 1.12x slower                                        |
| python_startup           | 11.5 ms                                                      | 12.9 ms: 1.12x slower                                        |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                        |
| coverage                 | 63.3 ms                                                      | 81.9 ms: 1.29x slower                                        |
| gc_traversal             | 3.42 ms                                                      | 4.64 ms: 1.36x slower                                        |
| python_startup_no_site   | 7.33 ms                                                      | 11.1 ms: 1.52x slower                                        |
| Geometric mean           | (ref)                                                        | 1.31x faster                                                 |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: django_template, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240402-3.13.0a5+-c32dc47/bm-20240402-pythonperf2-x86_64-python-main-3.13.0a5+-c32dc47.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.10x