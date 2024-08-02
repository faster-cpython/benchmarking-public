# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 292 ms: 1.20x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.42 ms: 1.27x faster                                            |
| docutils       | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                           |
| html5lib       | 94.6 ms                                                      | 76.0 ms: 1.24x faster                                            |
| tornado_http   | 157 ms                                                       | 122 ms: 1.28x faster                                             |
| Geometric mean | (ref)                                                        | 1.24x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 434 ms: 1.59x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 546 ms: 1.50x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 1.08 sec: 1.48x faster                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 699 ms: 1.34x faster                                             |
| Geometric mean          | (ref)                                                        | 1.48x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.8 ms: 1.58x faster                                            |
| float          | 111 ms                                                       | 78.8 ms: 1.41x faster                                            |
| pidigits       | 271 ms                                                       | 262 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                        | 1.32x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 142 ms: 1.34x faster                                             |
| regex_dna      | 261 ms                                                       | 241 ms: 1.08x faster                                             |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                            |
| regex_effbot   | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                            |
| Geometric mean | (ref)                                                        | 1.08x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 316 us: 1.44x faster                                             |
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                             |
| json_dumps           | 14.5 ms                                                      | 10.5 ms: 1.39x faster                                            |
| xml_etree_process    | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                            |
| tomli_loads          | 2.92 sec                                                     | 2.38 sec: 1.22x faster                                           |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                            |
| xml_etree_generate   | 92.3 ms                                                      | 85.1 ms: 1.08x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 148 ms: 1.08x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                             |
| unpickle_list        | 4.65 us                                                      | 4.68 us: 1.01x slower                                            |
| pickle_dict          | 29.5 us                                                      | 30.3 us: 1.03x slower                                            |
| pickle               | 9.89 us                                                      | 10.3 us: 1.04x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.33 us: 1.05x slower                                            |
| unpickle             | 13.5 us                                                      | 15.3 us: 1.13x slower                                            |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.6 ms: 1.10x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 11.0 ms: 1.51x slower                                            |
| Geometric mean         | (ref)                                                        | 1.29x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                            |
| django_template | 50.2 ms                                                      | 38.4 ms: 1.31x faster                                            |
| genshi_text     | 31.4 ms                                                      | 25.9 ms: 1.22x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 55.8 ms: 1.13x faster                                            |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 117 us: 4.59x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.59 ms: 2.09x faster                                            |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                             |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                           |
| raytrace                 | 489 ms                                                       | 262 ms: 1.87x faster                                             |
| logging_silent           | 167 ns                                                       | 93.6 ns: 1.79x faster                                            |
| chaos                    | 109 ms                                                       | 61.0 ms: 1.78x faster                                            |
| scimark_lu               | 167 ms                                                       | 94.4 ms: 1.77x faster                                            |
| generators               | 57.3 ms                                                      | 34.1 ms: 1.68x faster                                            |
| crypto_pyaes             | 119 ms                                                       | 71.3 ms: 1.67x faster                                            |
| pylint                   | 566 ms                                                       | 345 ms: 1.64x faster                                             |
| comprehensions           | 26.7 us                                                      | 16.5 us: 1.62x faster                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                            |
| scimark_monte_carlo      | 107 ms                                                       | 67.0 ms: 1.60x faster                                            |
| async_tree_none          | 692 ms                                                       | 434 ms: 1.59x faster                                             |
| nbody                    | 134 ms                                                       | 84.8 ms: 1.58x faster                                            |
| go                       | 262 ms                                                       | 170 ms: 1.54x faster                                             |
| spectral_norm            | 139 ms                                                       | 92.5 ms: 1.50x faster                                            |
| async_tree_memoization   | 819 ms                                                       | 546 ms: 1.50x faster                                             |
| richards_super           | 90.6 ms                                                      | 60.8 ms: 1.49x faster                                            |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                            |
| async_tree_io            | 1.60 sec                                                     | 1.08 sec: 1.48x faster                                           |
| hexiom                   | 9.42 ms                                                      | 6.44 ms: 1.46x faster                                            |
| pyflate                  | 733 ms                                                       | 506 ms: 1.45x faster                                             |
| pickle_pure_python       | 455 us                                                       | 316 us: 1.44x faster                                             |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                             |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                            |
| float                    | 111 ms                                                       | 78.8 ms: 1.41x faster                                            |
| bench_mp_pool            | 6.37 ms                                                      | 4.58 ms: 1.39x faster                                            |
| json_dumps               | 14.5 ms                                                      | 10.5 ms: 1.39x faster                                            |
| richards                 | 75.1 ms                                                      | 54.4 ms: 1.38x faster                                            |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.37x faster                                            |
| thrift                   | 1.18 ms                                                      | 873 us: 1.35x faster                                             |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 699 ms: 1.34x faster                                             |
| logging_simple           | 8.88 us                                                      | 6.63 us: 1.34x faster                                            |
| deepcopy_memo            | 49.8 us                                                      | 37.2 us: 1.34x faster                                            |
| regex_compile            | 190 ms                                                       | 142 ms: 1.34x faster                                             |
| logging_format           | 9.64 us                                                      | 7.21 us: 1.34x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 791 ms: 1.33x faster                                             |
| xml_etree_process        | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                            |
| django_template          | 50.2 ms                                                      | 38.4 ms: 1.31x faster                                            |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                           |
| nqueens                  | 115 ms                                                       | 88.8 ms: 1.29x faster                                            |
| tornado_http             | 157 ms                                                       | 122 ms: 1.28x faster                                             |
| chameleon                | 9.44 ms                                                      | 7.42 ms: 1.27x faster                                            |
| deepcopy                 | 468 us                                                       | 369 us: 1.27x faster                                             |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                             |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.25x faster                                             |
| html5lib                 | 94.6 ms                                                      | 76.0 ms: 1.24x faster                                            |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                             |
| scimark_sor              | 180 ms                                                       | 146 ms: 1.23x faster                                             |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.12 ms: 1.23x faster                                            |
| fannkuch                 | 483 ms                                                       | 393 ms: 1.23x faster                                             |
| tomli_loads              | 2.92 sec                                                     | 2.38 sec: 1.22x faster                                           |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.22x faster                                            |
| genshi_text              | 31.4 ms                                                      | 25.9 ms: 1.22x faster                                            |
| sympy_expand             | 600 ms                                                       | 496 ms: 1.21x faster                                             |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                           |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                             |
| docutils                 | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                           |
| 2to3                     | 350 ms                                                       | 292 ms: 1.20x faster                                             |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                            |
| sqlglot_optimize         | 70.1 ms                                                      | 58.6 ms: 1.20x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 958 us: 1.19x faster                                             |
| dulwich_log              | 81.1 ms                                                      | 69.0 ms: 1.18x faster                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.41 us: 1.18x faster                                            |
| async_generators         | 421 ms                                                       | 359 ms: 1.17x faster                                             |
| genshi_xml               | 63.3 ms                                                      | 55.8 ms: 1.13x faster                                            |
| pathlib                  | 21.4 ms                                                      | 19.0 ms: 1.12x faster                                            |
| aiohttp                  | 1.19 ms                                                      | 1.06 ms: 1.12x faster                                            |
| gunicorn                 | 1.16 ms                                                      | 1.04 ms: 1.11x faster                                            |
| json                     | 5.86 ms                                                      | 5.30 ms: 1.11x faster                                            |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                             |
| create_gc_cycles         | 1.76 ms                                                      | 1.61 ms: 1.10x faster                                            |
| sqlite_synth             | 2.99 us                                                      | 2.73 us: 1.09x faster                                            |
| xml_etree_generate       | 92.3 ms                                                      | 85.1 ms: 1.08x faster                                            |
| regex_dna                | 261 ms                                                       | 241 ms: 1.08x faster                                             |
| xml_etree_parse          | 160 ms                                                       | 148 ms: 1.08x faster                                             |
| mypy2                    | 933 ms                                                       | 867 ms: 1.08x faster                                             |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                            |
| pidigits                 | 271 ms                                                       | 262 ms: 1.03x faster                                             |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                             |
| unpickle_list            | 4.65 us                                                      | 4.68 us: 1.01x slower                                            |
| pickle_dict              | 29.5 us                                                      | 30.3 us: 1.03x slower                                            |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.04x slower                                            |
| flaskblogging            | 4.39 ms                                                      | 4.58 ms: 1.04x slower                                            |
| pickle_list              | 4.12 us                                                      | 4.33 us: 1.05x slower                                            |
| python_startup           | 11.5 ms                                                      | 12.6 ms: 1.10x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 3.76 ms: 1.10x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                            |
| telco                    | 7.23 ms                                                      | 8.16 ms: 1.13x slower                                            |
| unpickle                 | 13.5 us                                                      | 15.3 us: 1.13x slower                                            |
| coverage                 | 63.3 ms                                                      | 82.9 ms: 1.31x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 11.0 ms: 1.51x slower                                            |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                     |
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.07x