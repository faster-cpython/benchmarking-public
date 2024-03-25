# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: linux-x86_64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 291 ms: 1.20x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.36 ms: 1.28x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.96 sec: 1.16x faster                                                       |
| html5lib       | 94.6 ms                                                      | 75.5 ms: 1.25x faster                                                        |
| tornado_http   | 157 ms                                                       | 121 ms: 1.30x faster                                                         |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 851 ms: 1.88x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 438 ms: 1.87x faster                                                         |
| async_tree_none         | 692 ms                                                       | 379 ms: 1.82x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 601 ms: 1.56x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.78x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 86.8 ms: 1.55x faster                                                        |
| float          | 111 ms                                                       | 78.2 ms: 1.42x faster                                                        |
| pidigits       | 271 ms                                                       | 262 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 144 ms: 1.32x faster                                                         |
| regex_dna      | 261 ms                                                       | 233 ms: 1.12x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 307 us: 1.48x faster                                                         |
| unpickle_pure_python | 312 us                                                       | 223 us: 1.40x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 10.5 ms: 1.38x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.21 sec: 1.32x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 57.8 ms: 1.31x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 82.0 ms: 1.12x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 150 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                         |
| unpickle_list        | 4.65 us                                                      | 4.47 us: 1.04x faster                                                        |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 30.9 us: 1.05x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.37 us: 1.06x slower                                                        |
| unpickle             | 13.5 us                                                      | 14.6 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.7 ms: 1.11x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 11.0 ms: 1.50x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.29x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 25.2 ms: 1.24x faster                                                        |
| django_template | 50.2 ms                                                      | 40.9 ms: 1.23x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 54.0 ms: 1.17x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 113 us: 4.76x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.52 ms: 2.13x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 851 ms: 1.88x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 438 ms: 1.87x faster                                                         |
| raytrace                 | 489 ms                                                       | 265 ms: 1.84x faster                                                         |
| async_tree_none          | 692 ms                                                       | 379 ms: 1.82x faster                                                         |
| chaos                    | 109 ms                                                       | 60.9 ms: 1.78x faster                                                        |
| scimark_lu               | 167 ms                                                       | 94.4 ms: 1.77x faster                                                        |
| logging_silent           | 167 ns                                                       | 96.2 ns: 1.74x faster                                                        |
| generators               | 57.3 ms                                                      | 33.5 ms: 1.71x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 71.2 ms: 1.67x faster                                                        |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 66.0 ms: 1.63x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.38 ms: 1.62x faster                                                        |
| comprehensions           | 26.7 us                                                      | 16.7 us: 1.60x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 601 ms: 1.56x faster                                                         |
| nbody                    | 134 ms                                                       | 86.8 ms: 1.55x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.76 ms: 1.52x faster                                                        |
| go                       | 262 ms                                                       | 173 ms: 1.51x faster                                                         |
| spectral_norm            | 139 ms                                                       | 92.2 ms: 1.51x faster                                                        |
| richards_super           | 90.6 ms                                                      | 60.4 ms: 1.50x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 307 us: 1.48x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 6.35 ms: 1.48x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| float                    | 111 ms                                                       | 78.2 ms: 1.42x faster                                                        |
| pyflate                  | 733 ms                                                       | 525 ms: 1.40x faster                                                         |
| unpickle_pure_python     | 312 us                                                       | 223 us: 1.40x faster                                                         |
| richards                 | 75.1 ms                                                      | 54.4 ms: 1.38x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.5 ms: 1.38x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 36.3 us: 1.37x faster                                                        |
| thrift                   | 1.18 ms                                                      | 868 us: 1.35x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.58 us: 1.35x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.74 ms: 1.34x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.7 ms: 1.34x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.33x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 789 ms: 1.33x faster                                                         |
| regex_compile            | 190 ms                                                       | 144 ms: 1.32x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.21 sec: 1.32x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 57.8 ms: 1.31x faster                                                        |
| nqueens                  | 115 ms                                                       | 87.5 ms: 1.31x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.35 us: 1.31x faster                                                        |
| tornado_http             | 157 ms                                                       | 121 ms: 1.30x faster                                                         |
| scimark_sor              | 180 ms                                                       | 140 ms: 1.29x faster                                                         |
| chameleon                | 9.44 ms                                                      | 7.36 ms: 1.28x faster                                                        |
| deepcopy                 | 468 us                                                       | 368 us: 1.27x faster                                                         |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 902 us: 1.27x faster                                                         |
| fannkuch                 | 483 ms                                                       | 385 ms: 1.25x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 75.5 ms: 1.25x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 25.2 ms: 1.24x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 48.2 ns: 1.24x faster                                                        |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                         |
| django_template          | 50.2 ms                                                      | 40.9 ms: 1.23x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                                        |
| scimark_fft              | 361 ms                                                       | 296 ms: 1.22x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.30 us: 1.21x faster                                                        |
| sympy_expand             | 600 ms                                                       | 496 ms: 1.21x faster                                                         |
| mypy2                    | 933 ms                                                       | 771 ms: 1.21x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| 2to3                     | 350 ms                                                       | 291 ms: 1.20x faster                                                         |
| dask                     | 472 ms                                                       | 392 ms: 1.20x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 68.0 ms: 1.19x faster                                                        |
| async_generators         | 421 ms                                                       | 354 ms: 1.19x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 59.2 ms: 1.19x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.32 ms: 1.18x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 54.0 ms: 1.17x faster                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.52 ms: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.96 sec: 1.16x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 82.0 ms: 1.12x faster                                                        |
| regex_dna                | 261 ms                                                       | 233 ms: 1.12x faster                                                         |
| gunicorn                 | 1.16 ms                                                      | 1.04 ms: 1.12x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 19.1 ms: 1.12x faster                                                        |
| aiohttp                  | 1.19 ms                                                      | 1.07 ms: 1.11x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.74 us: 1.09x faster                                                        |
| json                     | 5.86 ms                                                      | 5.40 ms: 1.09x faster                                                        |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 150 ms: 1.07x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                                         |
| unpickle_list            | 4.65 us                                                      | 4.47 us: 1.04x faster                                                        |
| pidigits                 | 271 ms                                                       | 262 ms: 1.03x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                         |
| pickle                   | 9.89 us                                                      | 10.2 us: 1.03x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 30.9 us: 1.05x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.37 us: 1.06x slower                                                        |
| unpickle                 | 13.5 us                                                      | 14.6 us: 1.08x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.91 ms: 1.09x slower                                                        |
| python_startup           | 11.5 ms                                                      | 12.7 ms: 1.11x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.30 ms: 1.26x slower                                                        |
| coverage                 | 63.3 ms                                                      | 79.9 ms: 1.26x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 11.0 ms: 1.50x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                                 |
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x


# Memory

- memory change: 1.09x