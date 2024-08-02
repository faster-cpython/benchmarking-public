# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-x86_64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 292 ms: 1.20x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.42 ms: 1.27x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.00 sec: 1.14x faster                                                       |
| html5lib       | 94.6 ms                                                      | 73.6 ms: 1.29x faster                                                        |
| tornado_http   | 157 ms                                                       | 118 ms: 1.33x faster                                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 372 ms: 1.86x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 882 ms: 1.81x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 467 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 615 ms: 1.52x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.73x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.2 ms: 1.50x faster                                                        |
| float          | 111 ms                                                       | 81.0 ms: 1.37x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 144 ms: 1.32x faster                                                         |
| regex_dna      | 261 ms                                                       | 248 ms: 1.05x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 211 us: 1.48x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 311 us: 1.47x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.4 ms: 1.26x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.3 us: 1.25x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.38 sec: 1.22x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 86.8 ms: 1.06x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.79 us: 1.03x slower                                                        |
| pickle               | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 30.8 us: 1.05x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.41 us: 1.07x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.8 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                        |
| django_template | 50.2 ms                                                      | 38.1 ms: 1.32x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 25.9 ms: 1.21x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 56.3 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.08x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.37 ms: 2.22x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 375 ms: 2.08x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                       |
| async_tree_none          | 692 ms                                                       | 372 ms: 1.86x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 882 ms: 1.81x faster                                                         |
| chaos                    | 109 ms                                                       | 60.7 ms: 1.79x faster                                                        |
| raytrace                 | 489 ms                                                       | 277 ms: 1.77x faster                                                         |
| generators               | 57.3 ms                                                      | 32.7 ms: 1.75x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 467 ms: 1.75x faster                                                         |
| logging_silent           | 167 ns                                                       | 96.8 ns: 1.73x faster                                                        |
| scimark_lu               | 167 ms                                                       | 98.4 ms: 1.70x faster                                                        |
| pylint                   | 566 ms                                                       | 340 ms: 1.66x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 64.9 ms: 1.66x faster                                                        |
| go                       | 262 ms                                                       | 160 ms: 1.64x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 73.4 ms: 1.62x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.60x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                                        |
| pyflate                  | 733 ms                                                       | 478 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 615 ms: 1.52x faster                                                         |
| scimark_sor              | 180 ms                                                       | 119 ms: 1.52x faster                                                         |
| richards_super           | 90.6 ms                                                      | 59.8 ms: 1.51x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.51x faster                                                        |
| nbody                    | 134 ms                                                       | 89.2 ms: 1.50x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 211 us: 1.48x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 311 us: 1.47x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 6.44 ms: 1.46x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                        |
| richards                 | 75.1 ms                                                      | 53.1 ms: 1.41x faster                                                        |
| spectral_norm            | 139 ms                                                       | 98.6 ms: 1.41x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.31 us: 1.41x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.99 us: 1.38x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.38x faster                                                        |
| float                    | 111 ms                                                       | 81.0 ms: 1.37x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                         |
| tornado_http             | 157 ms                                                       | 118 ms: 1.33x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 37.6 us: 1.32x faster                                                        |
| regex_compile            | 190 ms                                                       | 144 ms: 1.32x faster                                                         |
| django_template          | 50.2 ms                                                      | 38.1 ms: 1.32x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.86 ms: 1.31x faster                                                        |
| thrift                   | 1.18 ms                                                      | 897 us: 1.31x faster                                                         |
| nqueens                  | 115 ms                                                       | 88.9 ms: 1.29x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 73.6 ms: 1.29x faster                                                        |
| chameleon                | 9.44 ms                                                      | 7.42 ms: 1.27x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 825 ms: 1.27x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 898 us: 1.27x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 60.4 ms: 1.26x faster                                                        |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.3 us: 1.25x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                                        |
| deepcopy                 | 468 us                                                       | 382 us: 1.23x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.38 sec: 1.22x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.46 sec: 1.22x faster                                                       |
| sympy_str                | 360 ms                                                       | 296 ms: 1.22x faster                                                         |
| mypy2                    | 933 ms                                                       | 767 ms: 1.22x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 25.9 ms: 1.21x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 67.0 ms: 1.21x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                         |
| dask                     | 472 ms                                                       | 392 ms: 1.20x faster                                                         |
| 2to3                     | 350 ms                                                       | 292 ms: 1.20x faster                                                         |
| sympy_expand             | 600 ms                                                       | 504 ms: 1.19x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.27 ms: 1.19x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.7 ms: 1.17x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.42 us: 1.17x faster                                                        |
| async_generators         | 421 ms                                                       | 363 ms: 1.16x faster                                                         |
| scimark_fft              | 361 ms                                                       | 313 ms: 1.16x faster                                                         |
| docutils                 | 3.41 sec                                                     | 3.00 sec: 1.14x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 56.3 ms: 1.12x faster                                                        |
| gunicorn                 | 1.16 ms                                                      | 1.04 ms: 1.12x faster                                                        |
| aiohttp                  | 1.19 ms                                                      | 1.07 ms: 1.11x faster                                                        |
| json                     | 5.86 ms                                                      | 5.29 ms: 1.11x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                         |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                                         |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 86.8 ms: 1.06x faster                                                        |
| regex_dna                | 261 ms                                                       | 248 ms: 1.05x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.85 us: 1.05x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.79 us: 1.03x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 30.8 us: 1.05x slower                                                        |
| flaskblogging            | 4.39 ms                                                      | 4.68 ms: 1.07x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.41 us: 1.07x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                        |
| python_startup           | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.41 ms: 1.16x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.8 us: 1.17x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.67 ms: 1.19x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.20x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.51 ms: 1.32x slower                                                        |
| coverage                 | 63.3 ms                                                      | 85.3 ms: 1.35x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.12x