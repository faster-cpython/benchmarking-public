# Results vs. 3.10.4

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-x86_64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                           |
| docutils       | 3.41 sec                                                     | 2.96 sec: 1.16x faster                                                         |
| html5lib       | 94.6 ms                                                      | 74.0 ms: 1.28x faster                                                          |
| tornado_http   | 157 ms                                                       | 117 ms: 1.34x faster                                                           |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 320 ms: 2.16x faster                                                           |
| async_tree_memoization  | 819 ms                                                       | 397 ms: 2.06x faster                                                           |
| async_tree_io           | 1.60 sec                                                     | 803 ms: 1.99x faster                                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 571 ms: 1.64x faster                                                           |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 92.6 ms: 1.45x faster                                                          |
| float          | 111 ms                                                       | 80.3 ms: 1.38x faster                                                          |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                           |
| regex_dna      | 261 ms                                                       | 255 ms: 1.03x faster                                                           |
| regex_v8       | 27.2 ms                                                      | 27.1 ms: 1.00x faster                                                          |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 313 us: 1.45x faster                                                           |
| unpickle_pure_python | 312 us                                                       | 218 us: 1.43x faster                                                           |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                          |
| xml_etree_process    | 75.9 ms                                                      | 60.2 ms: 1.26x faster                                                          |
| json_loads           | 30.3 us                                                      | 24.9 us: 1.22x faster                                                          |
| tomli_loads          | 2.92 sec                                                     | 2.51 sec: 1.16x faster                                                         |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                                           |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                           |
| xml_etree_generate   | 92.3 ms                                                      | 85.8 ms: 1.08x faster                                                          |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                          |
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                          |
| genshi_text     | 31.4 ms                                                      | 24.1 ms: 1.30x faster                                                          |
| django_template | 50.2 ms                                                      | 40.5 ms: 1.24x faster                                                          |
| genshi_xml      | 63.3 ms                                                      | 52.2 ms: 1.21x faster                                                          |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.07x faster                                                           |
| deltablue                | 7.50 ms                                                      | 3.37 ms: 2.23x faster                                                          |
| async_tree_none          | 692 ms                                                       | 320 ms: 2.16x faster                                                           |
| asyncio_tcp              | 779 ms                                                       | 368 ms: 2.12x faster                                                           |
| async_tree_memoization   | 819 ms                                                       | 397 ms: 2.06x faster                                                           |
| async_tree_io            | 1.60 sec                                                     | 803 ms: 1.99x faster                                                           |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                         |
| generators               | 57.3 ms                                                      | 29.3 ms: 1.96x faster                                                          |
| raytrace                 | 489 ms                                                       | 270 ms: 1.81x faster                                                           |
| chaos                    | 109 ms                                                       | 61.2 ms: 1.77x faster                                                          |
| scimark_lu               | 167 ms                                                       | 96.5 ms: 1.73x faster                                                          |
| logging_silent           | 167 ns                                                       | 98.9 ns: 1.69x faster                                                          |
| deepcopy_memo            | 49.8 us                                                      | 30.2 us: 1.65x faster                                                          |
| crypto_pyaes             | 119 ms                                                       | 72.4 ms: 1.65x faster                                                          |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 571 ms: 1.64x faster                                                           |
| richards_super           | 90.6 ms                                                      | 55.7 ms: 1.63x faster                                                          |
| pylint                   | 566 ms                                                       | 348 ms: 1.63x faster                                                           |
| deepcopy                 | 468 us                                                       | 290 us: 1.61x faster                                                           |
| scimark_monte_carlo      | 107 ms                                                       | 67.2 ms: 1.60x faster                                                          |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                          |
| pyflate                  | 733 ms                                                       | 472 ms: 1.55x faster                                                           |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                          |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.52x faster                                                           |
| hexiom                   | 9.42 ms                                                      | 6.22 ms: 1.51x faster                                                          |
| richards                 | 75.1 ms                                                      | 49.6 ms: 1.51x faster                                                          |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                          |
| go                       | 262 ms                                                       | 177 ms: 1.48x faster                                                           |
| spectral_norm            | 139 ms                                                       | 95.3 ms: 1.46x faster                                                          |
| pickle_pure_python       | 455 us                                                       | 313 us: 1.45x faster                                                           |
| nbody                    | 134 ms                                                       | 92.6 ms: 1.45x faster                                                          |
| unpickle_pure_python     | 312 us                                                       | 218 us: 1.43x faster                                                           |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                                          |
| logging_simple           | 8.88 us                                                      | 6.24 us: 1.42x faster                                                          |
| bench_mp_pool            | 6.37 ms                                                      | 4.48 ms: 1.42x faster                                                          |
| coroutines               | 30.3 ms                                                      | 21.4 ms: 1.42x faster                                                          |
| logging_format           | 9.64 us                                                      | 6.92 us: 1.39x faster                                                          |
| float                    | 111 ms                                                       | 80.3 ms: 1.38x faster                                                          |
| thrift                   | 1.18 ms                                                      | 853 us: 1.38x faster                                                           |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                          |
| deepcopy_reduce          | 4.01 us                                                      | 2.92 us: 1.37x faster                                                          |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                          |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                         |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                           |
| tornado_http             | 157 ms                                                       | 117 ms: 1.34x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 862 us: 1.32x faster                                                           |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                                           |
| genshi_text              | 31.4 ms                                                      | 24.1 ms: 1.30x faster                                                          |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                         |
| nqueens                  | 115 ms                                                       | 88.9 ms: 1.29x faster                                                          |
| pprint_safe_repr         | 1.05 sec                                                     | 813 ms: 1.29x faster                                                           |
| html5lib                 | 94.6 ms                                                      | 74.0 ms: 1.28x faster                                                          |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                           |
| xml_etree_process        | 75.9 ms                                                      | 60.2 ms: 1.26x faster                                                          |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                           |
| django_template          | 50.2 ms                                                      | 40.5 ms: 1.24x faster                                                          |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.12 ms: 1.23x faster                                                          |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                           |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.23x faster                                                          |
| json_loads               | 30.3 us                                                      | 24.9 us: 1.22x faster                                                          |
| scimark_fft              | 361 ms                                                       | 298 ms: 1.21x faster                                                           |
| genshi_xml               | 63.3 ms                                                      | 52.2 ms: 1.21x faster                                                          |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                           |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.20x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 58.8 ms: 1.19x faster                                                          |
| sympy_expand             | 600 ms                                                       | 505 ms: 1.19x faster                                                           |
| async_generators         | 421 ms                                                       | 362 ms: 1.16x faster                                                           |
| tomli_loads              | 2.92 sec                                                     | 2.51 sec: 1.16x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.96 sec: 1.16x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                                           |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                           |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                          |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                           |
| xml_etree_generate       | 92.3 ms                                                      | 85.8 ms: 1.08x faster                                                          |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                           |
| regex_dna                | 261 ms                                                       | 255 ms: 1.03x faster                                                           |
| regex_v8                 | 27.2 ms                                                      | 27.1 ms: 1.00x faster                                                          |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                          |
| telco                    | 7.23 ms                                                      | 8.19 ms: 1.13x slower                                                          |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                          |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                          |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                          |
| coverage                 | 63.3 ms                                                      | 79.7 ms: 1.26x slower                                                          |
| gc_traversal             | 3.42 ms                                                      | 4.46 ms: 1.31x slower                                                          |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240824-3.14.0a0-bf9cfa8/bm-20240824-pythonperf2-x86_64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x