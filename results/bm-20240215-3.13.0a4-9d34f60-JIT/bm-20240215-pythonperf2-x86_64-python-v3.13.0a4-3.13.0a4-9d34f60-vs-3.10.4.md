# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 300 ms: 1.17x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.14 ms: 1.32x faster                                            |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                           |
| tornado_http   | 157 ms                                                       | 126 ms: 1.25x faster                                             |
| Geometric mean | (ref)                                                        | 1.23x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 434 ms: 1.59x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 548 ms: 1.50x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 1.08 sec: 1.48x faster                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 701 ms: 1.34x faster                                             |
| Geometric mean          | (ref)                                                        | 1.47x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 111 ms                                                       | 80.7 ms: 1.38x faster                                            |
| nbody          | 134 ms                                                       | 106 ms: 1.27x faster                                             |
| pidigits       | 271 ms                                                       | 262 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                        | 1.22x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 145 ms: 1.31x faster                                             |
| regex_v8       | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                            |
| regex_dna      | 261 ms                                                       | 244 ms: 1.07x faster                                             |
| regex_effbot   | 3.09 ms                                                      | 3.53 ms: 1.14x slower                                            |
| Geometric mean | (ref)                                                        | 1.07x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 304 us: 1.50x faster                                             |
| json_dumps           | 14.5 ms                                                      | 10.5 ms: 1.38x faster                                            |
| unpickle_pure_python | 312 us                                                       | 230 us: 1.36x faster                                             |
| xml_etree_process    | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                            |
| tomli_loads          | 2.92 sec                                                     | 2.31 sec: 1.26x faster                                           |
| json_loads           | 30.3 us                                                      | 25.6 us: 1.19x faster                                            |
| xml_etree_generate   | 92.3 ms                                                      | 83.4 ms: 1.11x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 148 ms: 1.08x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                             |
| pickle               | 9.89 us                                                      | 10.2 us: 1.04x slower                                            |
| pickle_dict          | 29.5 us                                                      | 30.6 us: 1.04x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.50 us: 1.09x slower                                            |
| unpickle             | 13.5 us                                                      | 15.3 us: 1.13x slower                                            |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                     |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.7 ms: 1.11x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 11.1 ms: 1.52x slower                                            |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 14.7 ms                                                      | 11.8 ms: 1.25x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 117 us: 4.58x faster                                             |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.69 ms: 2.03x faster                                            |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                           |
| raytrace                 | 489 ms                                                       | 274 ms: 1.79x faster                                             |
| logging_silent           | 167 ns                                                       | 97.7 ns: 1.71x faster                                            |
| generators               | 57.3 ms                                                      | 34.0 ms: 1.68x faster                                            |
| scimark_lu               | 167 ms                                                       | 99.3 ms: 1.68x faster                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                            |
| async_tree_none          | 692 ms                                                       | 434 ms: 1.59x faster                                             |
| richards_super           | 90.6 ms                                                      | 57.6 ms: 1.57x faster                                            |
| go                       | 262 ms                                                       | 167 ms: 1.56x faster                                             |
| chaos                    | 109 ms                                                       | 69.4 ms: 1.56x faster                                            |
| crypto_pyaes             | 119 ms                                                       | 79.3 ms: 1.50x faster                                            |
| pickle_pure_python       | 455 us                                                       | 304 us: 1.50x faster                                             |
| async_tree_memoization   | 819 ms                                                       | 548 ms: 1.50x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 1.08 sec: 1.48x faster                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.48x faster                                            |
| richards                 | 75.1 ms                                                      | 51.7 ms: 1.45x faster                                            |
| pyflate                  | 733 ms                                                       | 529 ms: 1.39x faster                                             |
| json_dumps               | 14.5 ms                                                      | 10.5 ms: 1.38x faster                                            |
| comprehensions           | 26.7 us                                                      | 19.3 us: 1.38x faster                                            |
| float                    | 111 ms                                                       | 80.7 ms: 1.38x faster                                            |
| scimark_monte_carlo      | 107 ms                                                       | 78.5 ms: 1.37x faster                                            |
| logging_simple           | 8.88 us                                                      | 6.51 us: 1.36x faster                                            |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 230 us: 1.36x faster                                             |
| deepcopy_memo            | 49.8 us                                                      | 36.9 us: 1.35x faster                                            |
| logging_format           | 9.64 us                                                      | 7.20 us: 1.34x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 701 ms: 1.34x faster                                             |
| chameleon                | 9.44 ms                                                      | 7.14 ms: 1.32x faster                                            |
| xml_etree_process        | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                            |
| regex_compile            | 190 ms                                                       | 145 ms: 1.31x faster                                             |
| bench_mp_pool            | 6.37 ms                                                      | 4.90 ms: 1.30x faster                                            |
| unpack_sequence          | 59.9 ns                                                      | 46.9 ns: 1.28x faster                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 826 ms: 1.27x faster                                             |
| nbody                    | 134 ms                                                       | 106 ms: 1.27x faster                                             |
| deepcopy                 | 468 us                                                       | 370 us: 1.26x faster                                             |
| tomli_loads              | 2.92 sec                                                     | 2.31 sec: 1.26x faster                                           |
| pycparser                | 1.67 sec                                                     | 1.33 sec: 1.26x faster                                           |
| scimark_sor              | 180 ms                                                       | 143 ms: 1.26x faster                                             |
| pprint_pformat           | 2.15 sec                                                     | 1.72 sec: 1.25x faster                                           |
| mako                     | 14.7 ms                                                      | 11.8 ms: 1.25x faster                                            |
| tornado_http             | 157 ms                                                       | 126 ms: 1.25x faster                                             |
| hexiom                   | 9.42 ms                                                      | 7.63 ms: 1.23x faster                                            |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                             |
| sympy_sum                | 193 ms                                                       | 158 ms: 1.22x faster                                             |
| spectral_norm            | 139 ms                                                       | 115 ms: 1.21x faster                                             |
| sympy_str                | 360 ms                                                       | 298 ms: 1.21x faster                                             |
| nqueens                  | 115 ms                                                       | 95.4 ms: 1.20x faster                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.33 us: 1.20x faster                                            |
| sympy_expand             | 600 ms                                                       | 502 ms: 1.20x faster                                             |
| mdp                      | 3.01 sec                                                     | 2.53 sec: 1.19x faster                                           |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                           |
| json_loads               | 30.3 us                                                      | 25.6 us: 1.19x faster                                            |
| sympy_integrate          | 28.2 ms                                                      | 23.9 ms: 1.18x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 967 us: 1.18x faster                                             |
| fannkuch                 | 483 ms                                                       | 409 ms: 1.18x faster                                             |
| dulwich_log              | 81.1 ms                                                      | 69.1 ms: 1.17x faster                                            |
| 2to3                     | 350 ms                                                       | 300 ms: 1.17x faster                                             |
| sqlglot_optimize         | 70.1 ms                                                      | 60.4 ms: 1.16x faster                                            |
| create_gc_cycles         | 1.76 ms                                                      | 1.55 ms: 1.14x faster                                            |
| async_generators         | 421 ms                                                       | 371 ms: 1.13x faster                                             |
| pathlib                  | 21.4 ms                                                      | 19.1 ms: 1.12x faster                                            |
| xml_etree_generate       | 92.3 ms                                                      | 83.4 ms: 1.11x faster                                            |
| json                     | 5.86 ms                                                      | 5.35 ms: 1.10x faster                                            |
| regex_v8                 | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                            |
| xml_etree_parse          | 160 ms                                                       | 148 ms: 1.08x faster                                             |
| sqlite_synth             | 2.99 us                                                      | 2.77 us: 1.08x faster                                            |
| regex_dna                | 261 ms                                                       | 244 ms: 1.07x faster                                             |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                             |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                             |
| pidigits                 | 271 ms                                                       | 262 ms: 1.03x faster                                             |
| scimark_fft              | 361 ms                                                       | 357 ms: 1.01x faster                                             |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                             |
| gc_traversal             | 3.42 ms                                                      | 3.47 ms: 1.02x slower                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.23 ms: 1.03x slower                                            |
| pickle                   | 9.89 us                                                      | 10.2 us: 1.04x slower                                            |
| pickle_dict              | 29.5 us                                                      | 30.6 us: 1.04x slower                                            |
| pickle_list              | 4.12 us                                                      | 4.50 us: 1.09x slower                                            |
| python_startup           | 11.5 ms                                                      | 12.7 ms: 1.11x slower                                            |
| telco                    | 7.23 ms                                                      | 8.12 ms: 1.12x slower                                            |
| unpickle                 | 13.5 us                                                      | 15.3 us: 1.13x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.53 ms: 1.14x slower                                            |
| dask                     | 472 ms                                                       | 584 ms: 1.24x slower                                             |
| coverage                 | 63.3 ms                                                      | 84.4 ms: 1.33x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 11.1 ms: 1.52x slower                                            |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                     |

Benchmark hidden because not significant (2): mypy2, unpickle_list
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x


# Memory

- memory change: 1.11x