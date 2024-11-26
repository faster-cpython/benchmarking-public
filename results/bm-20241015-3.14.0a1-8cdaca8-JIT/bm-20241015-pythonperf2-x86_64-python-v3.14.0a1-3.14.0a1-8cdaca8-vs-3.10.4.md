# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.286x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 314 ms: 1.12x faster                                             |
| docutils       | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                           |
| html5lib       | 94.6 ms                                                      | 69.2 ms: 1.37x faster                                            |
| tornado_http   | 157 ms                                                       | 123 ms: 1.27x faster                                             |
| Geometric mean | (ref)                                                        | 1.20x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 333 ms: 2.08x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 408 ms: 2.01x faster                                             |
| async_tree_io           | 1.60 sec                                                     | 846 ms: 1.89x faster                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 574 ms: 1.63x faster                                             |
| Geometric mean          | (ref)                                                        | 1.89x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.7 ms: 1.60x faster                                            |
| float          | 111 ms                                                       | 79.3 ms: 1.40x faster                                            |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                        | 1.34x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 150 ms: 1.26x faster                                             |
| regex_dna      | 261 ms                                                       | 233 ms: 1.12x faster                                             |
| regex_v8       | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                            |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.15x slower                                            |
| Geometric mean | (ref)                                                        | 1.07x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 221 us: 1.41x faster                                             |
| tomli_loads          | 2.92 sec                                                     | 2.12 sec: 1.38x faster                                           |
| pickle_pure_python   | 455 us                                                       | 333 us: 1.37x faster                                             |
| xml_etree_process    | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                            |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                            |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                            |
| xml_etree_generate   | 92.3 ms                                                      | 80.6 ms: 1.15x faster                                            |
| xml_etree_iterparse  | 110 ms                                                       | 99.5 ms: 1.11x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.11x faster                                             |
| pickle               | 9.89 us                                                      | 10.7 us: 1.08x slower                                            |
| unpickle             | 13.5 us                                                      | 14.9 us: 1.10x slower                                            |
| pickle_dict          | 29.5 us                                                      | 32.9 us: 1.12x slower                                            |
| pickle_list          | 4.12 us                                                      | 4.66 us: 1.13x slower                                            |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                     |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                            |
| python_startup         | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                            |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.52 ms: 1.54x faster                                            |
| django_template | 50.2 ms                                                      | 42.9 ms: 1.17x faster                                            |
| genshi_text     | 31.4 ms                                                      | 28.0 ms: 1.12x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 62.1 ms: 1.02x faster                                            |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 180 us: 2.99x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.30 ms: 2.27x faster                                            |
| async_tree_none          | 692 ms                                                       | 333 ms: 2.08x faster                                             |
| asyncio_tcp              | 779 ms                                                       | 377 ms: 2.07x faster                                             |
| async_tree_memoization   | 819 ms                                                       | 408 ms: 2.01x faster                                             |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                           |
| async_tree_io            | 1.60 sec                                                     | 846 ms: 1.89x faster                                             |
| logging_silent           | 167 ns                                                       | 93.9 ns: 1.78x faster                                            |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.75x faster                                             |
| scimark_lu               | 167 ms                                                       | 95.5 ms: 1.75x faster                                            |
| go                       | 262 ms                                                       | 152 ms: 1.72x faster                                             |
| richards_super           | 90.6 ms                                                      | 53.6 ms: 1.69x faster                                            |
| deepcopy_memo            | 49.8 us                                                      | 29.9 us: 1.67x faster                                            |
| crypto_pyaes             | 119 ms                                                       | 72.2 ms: 1.65x faster                                            |
| chaos                    | 109 ms                                                       | 66.5 ms: 1.63x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 574 ms: 1.63x faster                                             |
| richards                 | 75.1 ms                                                      | 46.6 ms: 1.61x faster                                            |
| nbody                    | 134 ms                                                       | 83.7 ms: 1.60x faster                                            |
| scimark_monte_carlo      | 107 ms                                                       | 68.4 ms: 1.57x faster                                            |
| raytrace                 | 489 ms                                                       | 315 ms: 1.55x faster                                             |
| pyflate                  | 733 ms                                                       | 473 ms: 1.55x faster                                             |
| mako                     | 14.7 ms                                                      | 9.52 ms: 1.54x faster                                            |
| deepcopy                 | 468 us                                                       | 309 us: 1.51x faster                                             |
| spectral_norm            | 139 ms                                                       | 93.0 ms: 1.50x faster                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.50 ms: 1.49x faster                                            |
| generators               | 57.3 ms                                                      | 39.4 ms: 1.46x faster                                            |
| comprehensions           | 26.7 us                                                      | 18.8 us: 1.42x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 221 us: 1.41x faster                                             |
| float                    | 111 ms                                                       | 79.3 ms: 1.40x faster                                            |
| coroutines               | 30.3 ms                                                      | 21.6 ms: 1.40x faster                                            |
| tomli_loads              | 2.92 sec                                                     | 2.12 sec: 1.38x faster                                           |
| html5lib                 | 94.6 ms                                                      | 69.2 ms: 1.37x faster                                            |
| pickle_pure_python       | 455 us                                                       | 333 us: 1.37x faster                                             |
| sqlglot_transpile        | 2.68 ms                                                      | 1.98 ms: 1.35x faster                                            |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                            |
| logging_simple           | 8.88 us                                                      | 6.62 us: 1.34x faster                                            |
| fannkuch                 | 483 ms                                                       | 361 ms: 1.34x faster                                             |
| pylint                   | 566 ms                                                       | 423 ms: 1.34x faster                                             |
| logging_format           | 9.64 us                                                      | 7.21 us: 1.34x faster                                            |
| hexiom                   | 9.42 ms                                                      | 7.11 ms: 1.32x faster                                            |
| xml_etree_process        | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 798 ms: 1.32x faster                                             |
| thrift                   | 1.18 ms                                                      | 894 us: 1.31x faster                                             |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                           |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                            |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                           |
| deepcopy_reduce          | 4.01 us                                                      | 3.10 us: 1.29x faster                                            |
| tornado_http             | 157 ms                                                       | 123 ms: 1.27x faster                                             |
| regex_compile            | 190 ms                                                       | 150 ms: 1.26x faster                                             |
| dulwich_log              | 81.1 ms                                                      | 64.5 ms: 1.26x faster                                            |
| scimark_fft              | 361 ms                                                       | 290 ms: 1.25x faster                                             |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.23x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 950 us: 1.20x faster                                             |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.26 ms: 1.19x faster                                            |
| django_template          | 50.2 ms                                                      | 42.9 ms: 1.17x faster                                            |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                           |
| json                     | 5.86 ms                                                      | 5.08 ms: 1.15x faster                                            |
| xml_etree_generate       | 92.3 ms                                                      | 80.6 ms: 1.15x faster                                            |
| sympy_expand             | 600 ms                                                       | 530 ms: 1.13x faster                                             |
| sympy_str                | 360 ms                                                       | 319 ms: 1.13x faster                                             |
| regex_dna                | 261 ms                                                       | 233 ms: 1.12x faster                                             |
| genshi_text              | 31.4 ms                                                      | 28.0 ms: 1.12x faster                                            |
| 2to3                     | 350 ms                                                       | 314 ms: 1.12x faster                                             |
| sympy_sum                | 193 ms                                                       | 173 ms: 1.11x faster                                             |
| async_generators         | 421 ms                                                       | 379 ms: 1.11x faster                                             |
| xml_etree_iterparse      | 110 ms                                                       | 99.5 ms: 1.11x faster                                            |
| nqueens                  | 115 ms                                                       | 104 ms: 1.11x faster                                             |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.11x faster                                             |
| sqlite_synth             | 2.99 us                                                      | 2.73 us: 1.10x faster                                            |
| regex_v8                 | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                            |
| sqlglot_normalize        | 144 ms                                                       | 132 ms: 1.09x faster                                             |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                             |
| docutils                 | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                           |
| meteor_contest           | 138 ms                                                       | 133 ms: 1.04x faster                                             |
| sympy_integrate          | 28.2 ms                                                      | 27.3 ms: 1.03x faster                                            |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.02x faster                                             |
| genshi_xml               | 63.3 ms                                                      | 62.1 ms: 1.02x faster                                            |
| sqlglot_optimize         | 70.1 ms                                                      | 69.7 ms: 1.01x faster                                            |
| telco                    | 7.23 ms                                                      | 7.80 ms: 1.08x slower                                            |
| pickle                   | 9.89 us                                                      | 10.7 us: 1.08x slower                                            |
| unpickle                 | 13.5 us                                                      | 14.9 us: 1.10x slower                                            |
| pickle_dict              | 29.5 us                                                      | 32.9 us: 1.12x slower                                            |
| pickle_list              | 4.12 us                                                      | 4.66 us: 1.13x slower                                            |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.15x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                            |
| coverage                 | 63.3 ms                                                      | 79.2 ms: 1.25x slower                                            |
| python_startup           | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                            |
| unpack_sequence          | 59.9 ns                                                      | 89.6 ns: 1.50x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 5.21 ms: 1.53x slower                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.65x slower                                            |
| bench_mp_pool            | 6.37 ms                                                      | 2.28 sec: 358.41x slower                                         |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                     |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf2-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.286x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.34x