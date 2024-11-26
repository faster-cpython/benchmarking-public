# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b4
- machine: linux-x86_64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.304x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 290 ms: 1.21x faster                                             |
| chameleon      | 9.44 ms                                                      | 7.20 ms: 1.31x faster                                            |
| docutils       | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                           |
| html5lib       | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                            |
| tornado_http   | 157 ms                                                       | 119 ms: 1.32x faster                                             |
| Geometric mean | (ref)                                                        | 1.25x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 367 ms: 1.88x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 875 ms: 1.83x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 464 ms: 1.77x faster                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 614 ms: 1.52x faster                                             |
| Geometric mean          | (ref)                                                        | 1.74x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.7 ms: 1.51x faster                                            |
| float          | 111 ms                                                       | 80.0 ms: 1.39x faster                                            |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                             |
| Geometric mean | (ref)                                                        | 1.31x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                             |
| regex_v8       | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                            |
| regex_dna      | 261 ms                                                       | 251 ms: 1.04x faster                                             |
| regex_effbot   | 3.09 ms                                                      | 3.54 ms: 1.15x slower                                            |
| Geometric mean | (ref)                                                        | 1.07x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 214 us: 1.46x faster                                             |
| pickle_pure_python   | 455 us                                                       | 315 us: 1.45x faster                                             |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                            |
| xml_etree_process    | 75.9 ms                                                      | 61.5 ms: 1.23x faster                                            |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.22x faster                                            |
| tomli_loads          | 2.92 sec                                                     | 2.44 sec: 1.20x faster                                           |
| xml_etree_parse      | 160 ms                                                       | 149 ms: 1.08x faster                                             |
| xml_etree_generate   | 92.3 ms                                                      | 86.9 ms: 1.06x faster                                            |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                             |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                            |
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                            |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                            |
| django_template | 50.2 ms                                                      | 39.1 ms: 1.28x faster                                            |
| genshi_text     | 31.4 ms                                                      | 26.2 ms: 1.20x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 56.8 ms: 1.11x faster                                            |
| Geometric mean  | (ref)                                                        | 1.25x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.12x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                            |
| asyncio_tcp              | 779 ms                                                       | 375 ms: 2.08x faster                                             |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                           |
| async_tree_none          | 692 ms                                                       | 367 ms: 1.88x faster                                             |
| raytrace                 | 489 ms                                                       | 263 ms: 1.86x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 875 ms: 1.83x faster                                             |
| chaos                    | 109 ms                                                       | 60.9 ms: 1.78x faster                                            |
| async_tree_memoization   | 819 ms                                                       | 464 ms: 1.77x faster                                             |
| logging_silent           | 167 ns                                                       | 95.9 ns: 1.75x faster                                            |
| scimark_lu               | 167 ms                                                       | 96.2 ms: 1.74x faster                                            |
| generators               | 57.3 ms                                                      | 33.4 ms: 1.71x faster                                            |
| pylint                   | 566 ms                                                       | 340 ms: 1.66x faster                                             |
| scimark_monte_carlo      | 107 ms                                                       | 66.1 ms: 1.63x faster                                            |
| go                       | 262 ms                                                       | 163 ms: 1.60x faster                                             |
| crypto_pyaes             | 119 ms                                                       | 74.6 ms: 1.60x faster                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.60x faster                                            |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                            |
| scimark_sor              | 180 ms                                                       | 116 ms: 1.55x faster                                             |
| richards_super           | 90.6 ms                                                      | 59.0 ms: 1.54x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 614 ms: 1.52x faster                                             |
| nbody                    | 134 ms                                                       | 88.7 ms: 1.51x faster                                            |
| sqlglot_transpile        | 2.68 ms                                                      | 1.77 ms: 1.51x faster                                            |
| pyflate                  | 733 ms                                                       | 492 ms: 1.49x faster                                             |
| hexiom                   | 9.42 ms                                                      | 6.38 ms: 1.48x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 214 us: 1.46x faster                                             |
| pickle_pure_python       | 455 us                                                       | 315 us: 1.45x faster                                             |
| spectral_norm            | 139 ms                                                       | 97.6 ms: 1.43x faster                                            |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.42x faster                                            |
| richards                 | 75.1 ms                                                      | 53.0 ms: 1.42x faster                                            |
| float                    | 111 ms                                                       | 80.0 ms: 1.39x faster                                            |
| logging_format           | 9.64 us                                                      | 7.01 us: 1.38x faster                                            |
| bench_mp_pool            | 6.37 ms                                                      | 4.64 ms: 1.37x faster                                            |
| logging_simple           | 8.88 us                                                      | 6.47 us: 1.37x faster                                            |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.37x faster                                            |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                           |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                            |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                             |
| deepcopy_memo            | 49.8 us                                                      | 37.5 us: 1.33x faster                                            |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                             |
| tornado_http             | 157 ms                                                       | 119 ms: 1.32x faster                                             |
| chameleon                | 9.44 ms                                                      | 7.20 ms: 1.31x faster                                            |
| thrift                   | 1.18 ms                                                      | 903 us: 1.30x faster                                             |
| nqueens                  | 115 ms                                                       | 88.6 ms: 1.30x faster                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 814 ms: 1.29x faster                                             |
| django_template          | 50.2 ms                                                      | 39.1 ms: 1.28x faster                                            |
| html5lib                 | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 901 us: 1.27x faster                                             |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                             |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                            |
| deepcopy                 | 468 us                                                       | 377 us: 1.24x faster                                             |
| xml_etree_process        | 75.9 ms                                                      | 61.5 ms: 1.23x faster                                            |
| dulwich_log              | 81.1 ms                                                      | 66.3 ms: 1.22x faster                                            |
| sympy_str                | 360 ms                                                       | 295 ms: 1.22x faster                                             |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.16 ms: 1.22x faster                                            |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.22x faster                                            |
| mypy2                    | 933 ms                                                       | 768 ms: 1.21x faster                                             |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                             |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                            |
| 2to3                     | 350 ms                                                       | 290 ms: 1.21x faster                                             |
| genshi_text              | 31.4 ms                                                      | 26.2 ms: 1.20x faster                                            |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                             |
| dask                     | 472 ms                                                       | 394 ms: 1.20x faster                                             |
| tomli_loads              | 2.92 sec                                                     | 2.44 sec: 1.20x faster                                           |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                             |
| sqlglot_optimize         | 70.1 ms                                                      | 58.9 ms: 1.19x faster                                            |
| mdp                      | 3.01 sec                                                     | 2.54 sec: 1.18x faster                                           |
| deepcopy_reduce          | 4.01 us                                                      | 3.44 us: 1.17x faster                                            |
| async_generators         | 421 ms                                                       | 362 ms: 1.16x faster                                             |
| docutils                 | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                           |
| genshi_xml               | 63.3 ms                                                      | 56.8 ms: 1.11x faster                                            |
| json                     | 5.86 ms                                                      | 5.31 ms: 1.10x faster                                            |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.09x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                            |
| xml_etree_parse          | 160 ms                                                       | 149 ms: 1.08x faster                                             |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                             |
| xml_etree_generate       | 92.3 ms                                                      | 86.9 ms: 1.06x faster                                            |
| regex_dna                | 261 ms                                                       | 251 ms: 1.04x faster                                             |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.04x faster                                             |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                             |
| telco                    | 7.23 ms                                                      | 8.29 ms: 1.15x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.54 ms: 1.15x slower                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.02 ms: 1.15x slower                                            |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                            |
| coverage                 | 63.3 ms                                                      | 79.6 ms: 1.26x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 4.60 ms: 1.35x slower                                            |
| Geometric mean           | (ref)                                                        | 1.32x faster                                                     |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-pythonperf2-x86_64-python-v3.13.0b4-3.13.0b4-567c38b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.304x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x