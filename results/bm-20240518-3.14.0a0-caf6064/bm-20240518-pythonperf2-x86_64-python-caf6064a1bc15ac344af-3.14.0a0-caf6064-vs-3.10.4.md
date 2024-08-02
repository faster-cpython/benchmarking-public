# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.25x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 289 ms: 1.21x faster                                                        |
| chameleon      | 9.44 ms                                                      | 7.29 ms: 1.29x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                                      |
| html5lib       | 94.6 ms                                                      | 74.3 ms: 1.27x faster                                                       |
| tornado_http   | 157 ms                                                       | 119 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 366 ms: 1.89x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 865 ms: 1.85x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 465 ms: 1.76x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 615 ms: 1.52x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.75x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 87.9 ms: 1.53x faster                                                       |
| float          | 111 ms                                                       | 80.0 ms: 1.39x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                       |
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 313 us: 1.45x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 222 us: 1.41x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.8 ms: 1.27x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.35 sec: 1.24x faster                                                      |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.6 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.77 us: 1.03x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 30.7 us: 1.04x slower                                                       |
| pickle               | 9.89 us                                                      | 10.5 us: 1.06x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.44 us: 1.08x slower                                                       |
| unpickle             | 13.5 us                                                      | 14.7 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.8 ms: 1.11x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                       |
| django_template | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.4 ms: 1.24x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 55.9 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 177 us: 3.04x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.41 ms: 2.20x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| async_tree_none          | 692 ms                                                       | 366 ms: 1.89x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 865 ms: 1.85x faster                                                        |
| chaos                    | 109 ms                                                       | 59.8 ms: 1.81x faster                                                       |
| raytrace                 | 489 ms                                                       | 276 ms: 1.77x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 465 ms: 1.76x faster                                                        |
| logging_silent           | 167 ns                                                       | 97.6 ns: 1.72x faster                                                       |
| generators               | 57.3 ms                                                      | 33.7 ms: 1.70x faster                                                       |
| scimark_lu               | 167 ms                                                       | 99.2 ms: 1.68x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 64.2 ms: 1.67x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 72.1 ms: 1.65x faster                                                       |
| pylint                   | 566 ms                                                       | 343 ms: 1.65x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                       |
| go                       | 262 ms                                                       | 170 ms: 1.54x faster                                                        |
| richards_super           | 90.6 ms                                                      | 59.2 ms: 1.53x faster                                                       |
| nbody                    | 134 ms                                                       | 87.9 ms: 1.53x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 615 ms: 1.52x faster                                                        |
| pyflate                  | 733 ms                                                       | 483 ms: 1.52x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.33 ms: 1.49x faster                                                       |
| richards                 | 75.1 ms                                                      | 51.6 ms: 1.46x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 313 us: 1.45x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.4 ms: 1.44x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 222 us: 1.41x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.53 ms: 1.41x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.37 us: 1.39x faster                                                       |
| float                    | 111 ms                                                       | 80.0 ms: 1.39x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.97 us: 1.38x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                        |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                      |
| tornado_http             | 157 ms                                                       | 119 ms: 1.32x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                       |
| scimark_sor              | 180 ms                                                       | 138 ms: 1.31x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 38.2 us: 1.30x faster                                                       |
| thrift                   | 1.18 ms                                                      | 904 us: 1.30x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 810 ms: 1.30x faster                                                        |
| chameleon                | 9.44 ms                                                      | 7.29 ms: 1.29x faster                                                       |
| django_template          | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 74.3 ms: 1.27x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 59.8 ms: 1.27x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 902 us: 1.26x faster                                                        |
| nqueens                  | 115 ms                                                       | 92.2 ms: 1.25x faster                                                       |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.35 sec: 1.24x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 25.4 ms: 1.24x faster                                                       |
| json_loads               | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.12 ms: 1.23x faster                                                       |
| scimark_fft              | 361 ms                                                       | 295 ms: 1.23x faster                                                        |
| deepcopy                 | 468 us                                                       | 384 us: 1.22x faster                                                        |
| 2to3                     | 350 ms                                                       | 289 ms: 1.21x faster                                                        |
| sympy_str                | 360 ms                                                       | 298 ms: 1.21x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                      |
| sympy_integrate          | 28.2 ms                                                      | 23.5 ms: 1.20x faster                                                       |
| dask                     | 472 ms                                                       | 395 ms: 1.20x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 67.9 ms: 1.19x faster                                                       |
| sympy_expand             | 600 ms                                                       | 507 ms: 1.18x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 123 ms: 1.17x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 60.1 ms: 1.17x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.44 us: 1.16x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 55.9 ms: 1.13x faster                                                       |
| async_generators         | 421 ms                                                       | 373 ms: 1.13x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.6 ms: 1.09x faster                                                       |
| json                     | 5.86 ms                                                      | 5.42 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                       |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                       |
| unpickle_list            | 4.65 us                                                      | 4.77 us: 1.03x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 30.7 us: 1.04x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.06x slower                                                       |
| flaskblogging            | 4.39 ms                                                      | 4.73 ms: 1.08x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.44 us: 1.08x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.7 us: 1.09x slower                                                       |
| python_startup           | 11.5 ms                                                      | 12.8 ms: 1.11x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.03 ms: 1.15x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                       |
| coverage                 | 63.3 ms                                                      | 77.7 ms: 1.23x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.40 ms: 1.29x slower                                                       |
| telco                    | 7.23 ms                                                      | 170 ms: 23.49x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.12x