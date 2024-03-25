# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: linux-x86_64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.25x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 302 ms: 1.16x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.29 ms: 1.29x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.04 sec: 1.12x faster                                                       |
| html5lib       | 94.6 ms                                                      | 73.4 ms: 1.29x faster                                                        |
| tornado_http   | 157 ms                                                       | 123 ms: 1.27x faster                                                         |
| Geometric mean | (ref)                                                        | 1.23x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 860 ms: 1.86x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 442 ms: 1.85x faster                                                         |
| async_tree_none         | 692 ms                                                       | 385 ms: 1.80x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 608 ms: 1.54x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.76x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 76.2 ms: 1.46x faster                                                        |
| nbody          | 134 ms                                                       | 100 ms: 1.34x faster                                                         |
| pidigits       | 271 ms                                                       | 262 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 145 ms: 1.31x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                        |
| regex_dna      | 261 ms                                                       | 249 ms: 1.05x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.47 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 308 us: 1.48x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                       |
| unpickle_pure_python | 312 us                                                       | 230 us: 1.36x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 58.6 ms: 1.30x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.19x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 147 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| unpickle_list        | 4.65 us                                                      | 4.60 us: 1.01x faster                                                        |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 30.6 us: 1.04x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.49 us: 1.09x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 14.2 ms: 1.24x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 12.5 ms: 1.70x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.45x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                                        |
| django_template | 50.2 ms                                                      | 40.4 ms: 1.24x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 29.2 ms: 1.07x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 62.5 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.19x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 121 us: 4.42x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 378 ms: 2.06x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.70 ms: 2.03x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 860 ms: 1.86x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 442 ms: 1.85x faster                                                         |
| async_tree_none          | 692 ms                                                       | 385 ms: 1.80x faster                                                         |
| logging_silent           | 167 ns                                                       | 96.9 ns: 1.73x faster                                                        |
| generators               | 57.3 ms                                                      | 33.3 ms: 1.72x faster                                                        |
| chaos                    | 109 ms                                                       | 67.6 ms: 1.61x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                        |
| richards_super           | 90.6 ms                                                      | 57.2 ms: 1.58x faster                                                        |
| raytrace                 | 489 ms                                                       | 311 ms: 1.57x faster                                                         |
| pylint                   | 566 ms                                                       | 361 ms: 1.57x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 608 ms: 1.54x faster                                                         |
| go                       | 262 ms                                                       | 172 ms: 1.52x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 78.6 ms: 1.52x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 308 us: 1.48x faster                                                         |
| richards                 | 75.1 ms                                                      | 50.9 ms: 1.48x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.47x faster                                                        |
| spectral_norm            | 139 ms                                                       | 94.9 ms: 1.47x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.0 ms: 1.47x faster                                                        |
| float                    | 111 ms                                                       | 76.2 ms: 1.46x faster                                                        |
| scimark_lu               | 167 ms                                                       | 116 ms: 1.44x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 75.9 ms: 1.42x faster                                                        |
| pyflate                  | 733 ms                                                       | 523 ms: 1.40x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                       |
| comprehensions           | 26.7 us                                                      | 19.6 us: 1.36x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 230 us: 1.36x faster                                                         |
| nbody                    | 134 ms                                                       | 100 ms: 1.34x faster                                                         |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                        |
| thrift                   | 1.18 ms                                                      | 878 us: 1.34x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.64 us: 1.34x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.79 ms: 1.33x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                       |
| regex_compile            | 190 ms                                                       | 145 ms: 1.31x faster                                                         |
| logging_format           | 9.64 us                                                      | 7.35 us: 1.31x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 38.0 us: 1.31x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.6 ms: 1.30x faster                                                        |
| chameleon                | 9.44 ms                                                      | 7.29 ms: 1.29x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 73.4 ms: 1.29x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.34 ms: 1.28x faster                                                        |
| tornado_http             | 157 ms                                                       | 123 ms: 1.27x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.71 sec: 1.26x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 837 ms: 1.25x faster                                                         |
| django_template          | 50.2 ms                                                      | 40.4 ms: 1.24x faster                                                        |
| deepcopy                 | 468 us                                                       | 380 us: 1.23x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.14 ms: 1.23x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 936 us: 1.22x faster                                                         |
| fannkuch                 | 483 ms                                                       | 398 ms: 1.21x faster                                                         |
| sympy_sum                | 193 ms                                                       | 161 ms: 1.20x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 67.9 ms: 1.19x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.36 us: 1.19x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.19x faster                                                        |
| sympy_str                | 360 ms                                                       | 302 ms: 1.19x faster                                                         |
| scimark_sor              | 180 ms                                                       | 152 ms: 1.19x faster                                                         |
| dask                     | 472 ms                                                       | 399 ms: 1.18x faster                                                         |
| create_gc_cycles         | 1.76 ms                                                      | 1.50 ms: 1.17x faster                                                        |
| sympy_expand             | 600 ms                                                       | 512 ms: 1.17x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 123 ms: 1.17x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.58 sec: 1.16x faster                                                       |
| 2to3                     | 350 ms                                                       | 302 ms: 1.16x faster                                                         |
| mypy2                    | 933 ms                                                       | 818 ms: 1.14x faster                                                         |
| scimark_fft              | 361 ms                                                       | 318 ms: 1.14x faster                                                         |
| nqueens                  | 115 ms                                                       | 102 ms: 1.13x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 25.1 ms: 1.12x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.04 sec: 1.12x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 63.0 ms: 1.11x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 19.2 ms: 1.11x faster                                                        |
| async_generators         | 421 ms                                                       | 383 ms: 1.10x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.72 us: 1.10x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 147 ms: 1.09x faster                                                         |
| json                     | 5.86 ms                                                      | 5.39 ms: 1.09x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 29.2 ms: 1.07x faster                                                        |
| aiohttp                  | 1.19 ms                                                      | 1.11 ms: 1.07x faster                                                        |
| gunicorn                 | 1.16 ms                                                      | 1.09 ms: 1.06x faster                                                        |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                        |
| regex_dna                | 261 ms                                                       | 249 ms: 1.05x faster                                                         |
| pidigits                 | 271 ms                                                       | 262 ms: 1.04x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 62.5 ms: 1.01x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.60 us: 1.01x faster                                                        |
| pickle                   | 9.89 us                                                      | 10.2 us: 1.03x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 30.6 us: 1.04x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.49 us: 1.09x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.47 ms: 1.12x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.14 ms: 1.13x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 73.6 ns: 1.23x slower                                                        |
| python_startup           | 11.5 ms                                                      | 14.2 ms: 1.24x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.30 ms: 1.26x slower                                                        |
| coverage                 | 63.3 ms                                                      | 84.1 ms: 1.33x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 12.5 ms: 1.70x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x


# Memory

- memory change: 1.25x