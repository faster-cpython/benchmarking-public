# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 291 ms: 1.20x faster                                        |
| docutils       | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                      |
| html5lib       | 94.6 ms                                                      | 73.5 ms: 1.29x faster                                       |
| tornado_http   | 157 ms                                                       | 117 ms: 1.34x faster                                        |
| Geometric mean | (ref)                                                        | 1.24x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 339 ms: 2.04x faster                                        |
| async_tree_memoization  | 819 ms                                                       | 411 ms: 2.00x faster                                        |
| async_tree_io           | 1.60 sec                                                     | 822 ms: 1.94x faster                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 573 ms: 1.63x faster                                        |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.9 ms: 1.51x faster                                       |
| float          | 111 ms                                                       | 79.8 ms: 1.39x faster                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.34x faster                                        |
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                        |
| regex_v8       | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                       |
| regex_effbot   | 3.09 ms                                                      | 3.41 ms: 1.10x slower                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 321 us: 1.42x faster                                        |
| unpickle_pure_python | 312 us                                                       | 222 us: 1.40x faster                                        |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                       |
| xml_etree_process    | 75.9 ms                                                      | 60.5 ms: 1.26x faster                                       |
| tomli_loads          | 2.92 sec                                                     | 2.40 sec: 1.22x faster                                      |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                       |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                        |
| xml_etree_generate   | 92.3 ms                                                      | 86.1 ms: 1.07x faster                                       |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                       |
| django_template | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                       |
| genshi_text     | 31.4 ms                                                      | 25.8 ms: 1.22x faster                                       |
| genshi_xml      | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                       |
| Geometric mean  | (ref)                                                        | 1.25x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.05x faster                                        |
| deltablue                | 7.50 ms                                                      | 3.43 ms: 2.19x faster                                       |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                        |
| async_tree_none          | 692 ms                                                       | 339 ms: 2.04x faster                                        |
| async_tree_memoization   | 819 ms                                                       | 411 ms: 2.00x faster                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                      |
| async_tree_io            | 1.60 sec                                                     | 822 ms: 1.94x faster                                        |
| raytrace                 | 489 ms                                                       | 268 ms: 1.83x faster                                        |
| chaos                    | 109 ms                                                       | 62.0 ms: 1.75x faster                                       |
| scimark_lu               | 167 ms                                                       | 97.1 ms: 1.72x faster                                       |
| generators               | 57.3 ms                                                      | 33.9 ms: 1.69x faster                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.69x faster                                       |
| logging_silent           | 167 ns                                                       | 99.4 ns: 1.68x faster                                       |
| crypto_pyaes             | 119 ms                                                       | 71.3 ms: 1.67x faster                                       |
| pylint                   | 566 ms                                                       | 342 ms: 1.66x faster                                        |
| go                       | 262 ms                                                       | 160 ms: 1.63x faster                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 573 ms: 1.63x faster                                        |
| deepcopy                 | 468 us                                                       | 290 us: 1.61x faster                                        |
| scimark_monte_carlo      | 107 ms                                                       | 67.2 ms: 1.60x faster                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                       |
| scimark_sor              | 180 ms                                                       | 115 ms: 1.57x faster                                        |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                       |
| richards_super           | 90.6 ms                                                      | 58.8 ms: 1.54x faster                                       |
| nbody                    | 134 ms                                                       | 88.9 ms: 1.51x faster                                       |
| pyflate                  | 733 ms                                                       | 488 ms: 1.50x faster                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.49x faster                                       |
| hexiom                   | 9.42 ms                                                      | 6.39 ms: 1.47x faster                                       |
| richards                 | 75.1 ms                                                      | 51.5 ms: 1.46x faster                                       |
| spectral_norm            | 139 ms                                                       | 96.2 ms: 1.45x faster                                       |
| pickle_pure_python       | 455 us                                                       | 321 us: 1.42x faster                                        |
| unpickle_pure_python     | 312 us                                                       | 222 us: 1.40x faster                                        |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                       |
| float                    | 111 ms                                                       | 79.8 ms: 1.39x faster                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.93 us: 1.37x faster                                       |
| logging_simple           | 8.88 us                                                      | 6.49 us: 1.37x faster                                       |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.37x faster                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.69 ms: 1.36x faster                                       |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                      |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                       |
| logging_format           | 9.64 us                                                      | 7.14 us: 1.35x faster                                       |
| regex_compile            | 190 ms                                                       | 141 ms: 1.34x faster                                        |
| tornado_http             | 157 ms                                                       | 117 ms: 1.34x faster                                        |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                       |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                        |
| thrift                   | 1.18 ms                                                      | 892 us: 1.32x faster                                        |
| bench_thread_pool        | 1.14 ms                                                      | 879 us: 1.30x faster                                        |
| html5lib                 | 94.6 ms                                                      | 73.5 ms: 1.29x faster                                       |
| nqueens                  | 115 ms                                                       | 89.6 ms: 1.28x faster                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 828 ms: 1.27x faster                                        |
| xml_etree_process        | 75.9 ms                                                      | 60.5 ms: 1.26x faster                                       |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                        |
| django_template          | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                       |
| dask                     | 472 ms                                                       | 384 ms: 1.23x faster                                        |
| sympy_str                | 360 ms                                                       | 295 ms: 1.22x faster                                        |
| genshi_text              | 31.4 ms                                                      | 25.8 ms: 1.22x faster                                       |
| dulwich_log              | 81.1 ms                                                      | 66.6 ms: 1.22x faster                                       |
| tomli_loads              | 2.92 sec                                                     | 2.40 sec: 1.22x faster                                      |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                       |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.20x faster                                        |
| 2to3                     | 350 ms                                                       | 291 ms: 1.20x faster                                        |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.20x faster                                      |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                        |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                       |
| sympy_expand             | 600 ms                                                       | 505 ms: 1.19x faster                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.3 ms: 1.18x faster                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.32 ms: 1.18x faster                                       |
| docutils                 | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                      |
| async_generators         | 421 ms                                                       | 366 ms: 1.15x faster                                        |
| genshi_xml               | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                       |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                        |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                        |
| json                     | 5.86 ms                                                      | 5.44 ms: 1.08x faster                                       |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                        |
| xml_etree_generate       | 92.3 ms                                                      | 86.1 ms: 1.07x faster                                       |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                        |
| regex_v8                 | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                       |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                        |
| regex_effbot             | 3.09 ms                                                      | 3.41 ms: 1.10x slower                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                       |
| python_startup           | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                       |
| telco                    | 7.23 ms                                                      | 8.33 ms: 1.15x slower                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                       |
| gc_traversal             | 3.42 ms                                                      | 4.44 ms: 1.30x slower                                       |
| coverage                 | 63.3 ms                                                      | 83.8 ms: 1.32x slower                                       |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240703-3.14.0a0-7c66906/bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.12x