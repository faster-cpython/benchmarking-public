# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 292 ms: 1.20x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.47 ms: 1.26x faster                                            |
| docutils       | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                           |
| html5lib       | 94.6 ms                                                      | 73.7 ms: 1.28x faster                                            |
| tornado_http   | 157 ms                                                       | 119 ms: 1.32x faster                                             |
| Geometric mean | (ref)                                                        | 1.25x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 429 ms: 1.61x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 542 ms: 1.51x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 1.07 sec: 1.50x faster                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 690 ms: 1.36x faster                                             |
| Geometric mean          | (ref)                                                        | 1.49x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.9 ms: 1.60x faster                                            |
| float          | 111 ms                                                       | 80.9 ms: 1.37x faster                                            |
| pidigits       | 271 ms                                                       | 265 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                        | 1.31x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                             |
| regex_dna      | 261 ms                                                       | 241 ms: 1.08x faster                                             |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                            |
| regex_effbot   | 3.09 ms                                                      | 3.63 ms: 1.17x slower                                            |
| Geometric mean | (ref)                                                        | 1.07x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 308 us: 1.48x faster                                             |
| unpickle_pure_python | 312 us                                                       | 225 us: 1.39x faster                                             |
| json_dumps           | 14.5 ms                                                      | 10.5 ms: 1.38x faster                                            |
| tomli_loads          | 2.92 sec                                                     | 2.16 sec: 1.35x faster                                           |
| xml_etree_process    | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                            |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                            |
| xml_etree_generate   | 92.3 ms                                                      | 84.0 ms: 1.10x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 151 ms: 1.06x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 108 ms: 1.03x faster                                             |
| pickle               | 9.89 us                                                      | 10.0 us: 1.01x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.34 us: 1.05x slower                                            |
| pickle_dict          | 29.5 us                                                      | 32.6 us: 1.11x slower                                            |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                            |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                     |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 12.9 ms: 1.12x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 11.3 ms: 1.54x slower                                            |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                            |
| django_template | 50.2 ms                                                      | 38.8 ms: 1.29x faster                                            |
| genshi_text     | 31.4 ms                                                      | 25.6 ms: 1.23x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                            |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 126 us: 4.27x faster                                             |
| asyncio_tcp              | 779 ms                                                       | 368 ms: 2.12x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.61 ms: 2.08x faster                                            |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                           |
| raytrace                 | 489 ms                                                       | 271 ms: 1.80x faster                                             |
| chaos                    | 109 ms                                                       | 61.9 ms: 1.75x faster                                            |
| logging_silent           | 167 ns                                                       | 96.5 ns: 1.73x faster                                            |
| scimark_lu               | 167 ms                                                       | 98.6 ms: 1.69x faster                                            |
| generators               | 57.3 ms                                                      | 34.2 ms: 1.67x faster                                            |
| crypto_pyaes             | 119 ms                                                       | 71.7 ms: 1.66x faster                                            |
| pylint                   | 566 ms                                                       | 346 ms: 1.64x faster                                             |
| async_tree_none          | 692 ms                                                       | 429 ms: 1.61x faster                                             |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.60x faster                                            |
| comprehensions           | 26.7 us                                                      | 16.6 us: 1.60x faster                                            |
| nbody                    | 134 ms                                                       | 83.9 ms: 1.60x faster                                            |
| scimark_monte_carlo      | 107 ms                                                       | 67.9 ms: 1.58x faster                                            |
| richards_super           | 90.6 ms                                                      | 58.3 ms: 1.56x faster                                            |
| go                       | 262 ms                                                       | 173 ms: 1.51x faster                                             |
| async_tree_memoization   | 819 ms                                                       | 542 ms: 1.51x faster                                             |
| spectral_norm            | 139 ms                                                       | 92.3 ms: 1.51x faster                                            |
| async_tree_io            | 1.60 sec                                                     | 1.07 sec: 1.50x faster                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                            |
| hexiom                   | 9.42 ms                                                      | 6.35 ms: 1.48x faster                                            |
| pickle_pure_python       | 455 us                                                       | 308 us: 1.48x faster                                             |
| mako                     | 14.7 ms                                                      | 10.1 ms: 1.46x faster                                            |
| richards                 | 75.1 ms                                                      | 52.1 ms: 1.44x faster                                            |
| pyflate                  | 733 ms                                                       | 513 ms: 1.43x faster                                             |
| bench_mp_pool            | 6.37 ms                                                      | 4.54 ms: 1.40x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 225 us: 1.39x faster                                             |
| json_dumps               | 14.5 ms                                                      | 10.5 ms: 1.38x faster                                            |
| logging_simple           | 8.88 us                                                      | 6.44 us: 1.38x faster                                            |
| float                    | 111 ms                                                       | 80.9 ms: 1.37x faster                                            |
| thrift                   | 1.18 ms                                                      | 858 us: 1.37x faster                                             |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.36x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 690 ms: 1.36x faster                                             |
| tomli_loads              | 2.92 sec                                                     | 2.16 sec: 1.35x faster                                           |
| logging_format           | 9.64 us                                                      | 7.20 us: 1.34x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                           |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                             |
| pprint_safe_repr         | 1.05 sec                                                     | 792 ms: 1.33x faster                                             |
| deepcopy_memo            | 49.8 us                                                      | 37.6 us: 1.32x faster                                            |
| tornado_http             | 157 ms                                                       | 119 ms: 1.32x faster                                             |
| xml_etree_process        | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                            |
| deepcopy                 | 468 us                                                       | 362 us: 1.29x faster                                             |
| django_template          | 50.2 ms                                                      | 38.8 ms: 1.29x faster                                            |
| fannkuch                 | 483 ms                                                       | 374 ms: 1.29x faster                                             |
| nqueens                  | 115 ms                                                       | 89.5 ms: 1.28x faster                                            |
| html5lib                 | 94.6 ms                                                      | 73.7 ms: 1.28x faster                                            |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                             |
| pycparser                | 1.67 sec                                                     | 1.31 sec: 1.28x faster                                           |
| chameleon                | 9.44 ms                                                      | 7.47 ms: 1.26x faster                                            |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                             |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.25x faster                                             |
| sympy_expand             | 600 ms                                                       | 488 ms: 1.23x faster                                             |
| scimark_sor              | 180 ms                                                       | 146 ms: 1.23x faster                                             |
| genshi_text              | 31.4 ms                                                      | 25.6 ms: 1.23x faster                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.27 us: 1.23x faster                                            |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.22x faster                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.19 ms: 1.21x faster                                            |
| dulwich_log              | 81.1 ms                                                      | 66.9 ms: 1.21x faster                                            |
| docutils                 | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                           |
| sqlglot_optimize         | 70.1 ms                                                      | 58.1 ms: 1.21x faster                                            |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                             |
| bench_thread_pool        | 1.14 ms                                                      | 951 us: 1.20x faster                                             |
| 2to3                     | 350 ms                                                       | 292 ms: 1.20x faster                                             |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                            |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                           |
| genshi_xml               | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                            |
| create_gc_cycles         | 1.76 ms                                                      | 1.55 ms: 1.14x faster                                            |
| async_generators         | 421 ms                                                       | 370 ms: 1.14x faster                                             |
| json                     | 5.86 ms                                                      | 5.20 ms: 1.13x faster                                            |
| pathlib                  | 21.4 ms                                                      | 19.1 ms: 1.12x faster                                            |
| aiohttp                  | 1.19 ms                                                      | 1.06 ms: 1.12x faster                                            |
| gunicorn                 | 1.16 ms                                                      | 1.05 ms: 1.11x faster                                            |
| xml_etree_generate       | 92.3 ms                                                      | 84.0 ms: 1.10x faster                                            |
| sqlite_synth             | 2.99 us                                                      | 2.74 us: 1.09x faster                                            |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                             |
| regex_dna                | 261 ms                                                       | 241 ms: 1.08x faster                                             |
| mypy2                    | 933 ms                                                       | 862 ms: 1.08x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                            |
| xml_etree_parse          | 160 ms                                                       | 151 ms: 1.06x faster                                             |
| xml_etree_iterparse      | 110 ms                                                       | 108 ms: 1.03x faster                                             |
| pidigits                 | 271 ms                                                       | 265 ms: 1.02x faster                                             |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                             |
| pickle                   | 9.89 us                                                      | 10.0 us: 1.01x slower                                            |
| pickle_list              | 4.12 us                                                      | 4.34 us: 1.05x slower                                            |
| flaskblogging            | 4.39 ms                                                      | 4.63 ms: 1.06x slower                                            |
| pickle_dict              | 29.5 us                                                      | 32.6 us: 1.11x slower                                            |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                            |
| python_startup           | 11.5 ms                                                      | 12.9 ms: 1.12x slower                                            |
| telco                    | 7.23 ms                                                      | 8.17 ms: 1.13x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 3.94 ms: 1.15x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.63 ms: 1.17x slower                                            |
| coverage                 | 63.3 ms                                                      | 79.1 ms: 1.25x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 11.3 ms: 1.54x slower                                            |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                     |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.06x