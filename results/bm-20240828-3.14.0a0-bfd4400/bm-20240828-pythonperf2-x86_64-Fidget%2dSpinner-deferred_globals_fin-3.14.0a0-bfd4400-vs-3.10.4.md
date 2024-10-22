# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                                  |
| docutils       | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                                |
| html5lib       | 94.6 ms                                                      | 73.8 ms: 1.28x faster                                                                 |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 332 ms: 2.08x faster                                                                  |
| async_tree_memoization  | 819 ms                                                       | 401 ms: 2.04x faster                                                                  |
| async_tree_io           | 1.60 sec                                                     | 804 ms: 1.99x faster                                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 574 ms: 1.63x faster                                                                  |
| Geometric mean          | (ref)                                                        | 1.93x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 86.9 ms: 1.54x faster                                                                 |
| float          | 111 ms                                                       | 82.4 ms: 1.35x faster                                                                 |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                                  |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                                  |
| regex_v8       | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                                                 |
| regex_effbot   | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 211 us: 1.48x faster                                                                  |
| pickle_pure_python   | 455 us                                                       | 311 us: 1.46x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                                 |
| xml_etree_process    | 75.9 ms                                                      | 59.1 ms: 1.29x faster                                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.30 sec: 1.27x faster                                                                |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                                 |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 84.6 ms: 1.09x faster                                                                 |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                                 |
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                                 |
| django_template | 50.2 ms                                                      | 39.3 ms: 1.28x faster                                                                 |
| genshi_text     | 31.4 ms                                                      | 25.3 ms: 1.24x faster                                                                 |
| genshi_xml      | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.08x faster                                                                  |
| deltablue                | 7.50 ms                                                      | 3.43 ms: 2.19x faster                                                                 |
| async_tree_none          | 692 ms                                                       | 332 ms: 2.08x faster                                                                  |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                                  |
| async_tree_memoization   | 819 ms                                                       | 401 ms: 2.04x faster                                                                  |
| async_tree_io            | 1.60 sec                                                     | 804 ms: 1.99x faster                                                                  |
| generators               | 57.3 ms                                                      | 28.9 ms: 1.99x faster                                                                 |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                                |
| raytrace                 | 489 ms                                                       | 265 ms: 1.84x faster                                                                  |
| scimark_lu               | 167 ms                                                       | 94.8 ms: 1.76x faster                                                                 |
| chaos                    | 109 ms                                                       | 62.0 ms: 1.75x faster                                                                 |
| logging_silent           | 167 ns                                                       | 97.2 ns: 1.72x faster                                                                 |
| deepcopy_memo            | 49.8 us                                                      | 29.4 us: 1.69x faster                                                                 |
| scimark_sor              | 180 ms                                                       | 107 ms: 1.68x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 71.5 ms: 1.67x faster                                                                 |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                                                  |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 574 ms: 1.63x faster                                                                  |
| go                       | 262 ms                                                       | 162 ms: 1.62x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 56.2 ms: 1.61x faster                                                                 |
| deepcopy                 | 468 us                                                       | 292 us: 1.60x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 67.1 ms: 1.60x faster                                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.57x faster                                                                 |
| nbody                    | 134 ms                                                       | 86.9 ms: 1.54x faster                                                                 |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                                 |
| pyflate                  | 733 ms                                                       | 478 ms: 1.53x faster                                                                  |
| richards                 | 75.1 ms                                                      | 50.2 ms: 1.50x faster                                                                 |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                                 |
| hexiom                   | 9.42 ms                                                      | 6.34 ms: 1.48x faster                                                                 |
| unpickle_pure_python     | 312 us                                                       | 211 us: 1.48x faster                                                                  |
| pickle_pure_python       | 455 us                                                       | 311 us: 1.46x faster                                                                  |
| spectral_norm            | 139 ms                                                       | 95.7 ms: 1.45x faster                                                                 |
| logging_simple           | 8.88 us                                                      | 6.19 us: 1.43x faster                                                                 |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                                 |
| logging_format           | 9.64 us                                                      | 6.81 us: 1.42x faster                                                                 |
| coroutines               | 30.3 ms                                                      | 21.7 ms: 1.39x faster                                                                 |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 4.67 ms: 1.37x faster                                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                                                 |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                                  |
| float                    | 111 ms                                                       | 82.4 ms: 1.35x faster                                                                 |
| thrift                   | 1.18 ms                                                      | 872 us: 1.35x faster                                                                  |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                                 |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.33x faster                                                                 |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                                |
| bench_thread_pool        | 1.14 ms                                                      | 869 us: 1.31x faster                                                                  |
| xml_etree_process        | 75.9 ms                                                      | 59.1 ms: 1.29x faster                                                                 |
| nqueens                  | 115 ms                                                       | 89.7 ms: 1.28x faster                                                                 |
| html5lib                 | 94.6 ms                                                      | 73.8 ms: 1.28x faster                                                                 |
| django_template          | 50.2 ms                                                      | 39.3 ms: 1.28x faster                                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 827 ms: 1.27x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.30 sec: 1.27x faster                                                                |
| pprint_pformat           | 2.15 sec                                                     | 1.70 sec: 1.27x faster                                                                |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                                                  |
| genshi_text              | 31.4 ms                                                      | 25.3 ms: 1.24x faster                                                                 |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                                  |
| sympy_str                | 360 ms                                                       | 296 ms: 1.22x faster                                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.18 ms: 1.22x faster                                                                 |
| mdp                      | 3.01 sec                                                     | 2.48 sec: 1.21x faster                                                                |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 23.5 ms: 1.20x faster                                                                 |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                                                  |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                                 |
| sympy_expand             | 600 ms                                                       | 503 ms: 1.19x faster                                                                  |
| sqlglot_optimize         | 70.1 ms                                                      | 58.9 ms: 1.19x faster                                                                 |
| async_generators         | 421 ms                                                       | 356 ms: 1.18x faster                                                                  |
| genshi_xml               | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                                                 |
| docutils                 | 3.41 sec                                                     | 2.97 sec: 1.15x faster                                                                |
| regex_dna                | 261 ms                                                       | 234 ms: 1.12x faster                                                                  |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.37 ms: 1.09x faster                                                                 |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 84.6 ms: 1.09x faster                                                                 |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                                                 |
| telco                    | 7.23 ms                                                      | 7.98 ms: 1.10x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                                 |
| gc_traversal             | 3.42 ms                                                      | 4.45 ms: 1.30x slower                                                                 |
| coverage                 | 63.3 ms                                                      | 83.6 ms: 1.32x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x