# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: linux-x86_64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.335x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 280 ms: 1.25x faster                                                                  |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                                |
| html5lib       | 94.6 ms                                                      | 70.1 ms: 1.35x faster                                                                 |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 321 ms: 2.15x faster                                                                  |
| async_tree_memoization  | 819 ms                                                       | 403 ms: 2.03x faster                                                                  |
| async_tree_io           | 1.60 sec                                                     | 803 ms: 1.99x faster                                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 575 ms: 1.63x faster                                                                  |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.8 ms: 1.49x faster                                                                 |
| float          | 111 ms                                                       | 80.6 ms: 1.38x faster                                                                 |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                                  |
| regex_v8       | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                                 |
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                                  |
| regex_effbot   | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 215 us: 1.45x faster                                                                  |
| pickle_pure_python   | 455 us                                                       | 317 us: 1.44x faster                                                                  |
| xml_etree_process    | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                                                 |
| json_loads           | 30.3 us                                                      | 24.9 us: 1.22x faster                                                                 |
| json_dumps           | 14.5 ms                                                      | 12.1 ms: 1.21x faster                                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.50 sec: 1.17x faster                                                                |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                                 |
| unpickle_list        | 4.65 us                                                      | 4.69 us: 1.01x slower                                                                 |
| pickle_dict          | 29.5 us                                                      | 30.4 us: 1.03x slower                                                                 |
| pickle               | 9.89 us                                                      | 10.6 us: 1.07x slower                                                                 |
| pickle_list          | 4.12 us                                                      | 4.57 us: 1.11x slower                                                                 |
| unpickle             | 13.5 us                                                      | 15.7 us: 1.16x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| python_startup_no_site | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                                 |
| genshi_text     | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                                 |
| genshi_xml      | 63.3 ms                                                      | 53.1 ms: 1.19x faster                                                                 |
| django_template | 50.2 ms                                                      | 42.7 ms: 1.18x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.25x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.06x faster                                                                  |
| deltablue                | 7.50 ms                                                      | 3.39 ms: 2.21x faster                                                                 |
| async_tree_none          | 692 ms                                                       | 321 ms: 2.15x faster                                                                  |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                                                  |
| async_tree_memoization   | 819 ms                                                       | 403 ms: 2.03x faster                                                                  |
| async_tree_io            | 1.60 sec                                                     | 803 ms: 1.99x faster                                                                  |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                                |
| generators               | 57.3 ms                                                      | 29.3 ms: 1.96x faster                                                                 |
| go                       | 262 ms                                                       | 137 ms: 1.91x faster                                                                  |
| raytrace                 | 489 ms                                                       | 267 ms: 1.83x faster                                                                  |
| scimark_lu               | 167 ms                                                       | 94.3 ms: 1.77x faster                                                                 |
| chaos                    | 109 ms                                                       | 63.5 ms: 1.71x faster                                                                 |
| logging_silent           | 167 ns                                                       | 98.2 ns: 1.70x faster                                                                 |
| deepcopy_memo            | 49.8 us                                                      | 29.6 us: 1.68x faster                                                                 |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.67x faster                                                                  |
| pylint                   | 566 ms                                                       | 346 ms: 1.64x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 73.1 ms: 1.63x faster                                                                 |
| deepcopy                 | 468 us                                                       | 287 us: 1.63x faster                                                                  |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 575 ms: 1.63x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 66.4 ms: 1.62x faster                                                                 |
| richards_super           | 90.6 ms                                                      | 56.2 ms: 1.61x faster                                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                                 |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                                 |
| richards                 | 75.1 ms                                                      | 49.3 ms: 1.52x faster                                                                 |
| pyflate                  | 733 ms                                                       | 484 ms: 1.52x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.26 ms: 1.50x faster                                                                 |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.50x faster                                                                 |
| nbody                    | 134 ms                                                       | 89.8 ms: 1.49x faster                                                                 |
| unpickle_pure_python     | 312 us                                                       | 215 us: 1.45x faster                                                                  |
| spectral_norm            | 139 ms                                                       | 96.5 ms: 1.44x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.44x faster                                                                  |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                                 |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                                |
| float                    | 111 ms                                                       | 80.6 ms: 1.38x faster                                                                 |
| fannkuch                 | 483 ms                                                       | 353 ms: 1.37x faster                                                                  |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                                 |
| logging_format           | 9.64 us                                                      | 7.08 us: 1.36x faster                                                                 |
| logging_simple           | 8.88 us                                                      | 6.52 us: 1.36x faster                                                                 |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.36x faster                                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                                                 |
| html5lib                 | 94.6 ms                                                      | 70.1 ms: 1.35x faster                                                                 |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                                  |
| thrift                   | 1.18 ms                                                      | 876 us: 1.34x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 784 ms: 1.34x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.33x faster                                                                |
| bench_thread_pool        | 1.14 ms                                                      | 888 us: 1.29x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                                  |
| genshi_text              | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                                 |
| nqueens                  | 115 ms                                                       | 90.0 ms: 1.28x faster                                                                 |
| xml_etree_process        | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                                                 |
| 2to3                     | 350 ms                                                       | 280 ms: 1.25x faster                                                                  |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                                  |
| dulwich_log              | 81.1 ms                                                      | 65.9 ms: 1.23x faster                                                                 |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.13 ms: 1.23x faster                                                                 |
| unpack_sequence          | 59.9 ns                                                      | 49.1 ns: 1.22x faster                                                                 |
| json_loads               | 30.3 us                                                      | 24.9 us: 1.22x faster                                                                 |
| mdp                      | 3.01 sec                                                     | 2.47 sec: 1.22x faster                                                                |
| scimark_fft              | 361 ms                                                       | 298 ms: 1.21x faster                                                                  |
| sympy_expand             | 600 ms                                                       | 495 ms: 1.21x faster                                                                  |
| json_dumps               | 14.5 ms                                                      | 12.1 ms: 1.21x faster                                                                 |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.20x faster                                                                 |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.20x faster                                                                  |
| genshi_xml               | 63.3 ms                                                      | 53.1 ms: 1.19x faster                                                                 |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                                |
| sqlglot_optimize         | 70.1 ms                                                      | 59.5 ms: 1.18x faster                                                                 |
| django_template          | 50.2 ms                                                      | 42.7 ms: 1.18x faster                                                                 |
| tomli_loads              | 2.92 sec                                                     | 2.50 sec: 1.17x faster                                                                |
| async_generators         | 421 ms                                                       | 371 ms: 1.13x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 123 ms: 1.13x faster                                                                  |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                                  |
| sqlite_synth             | 2.99 us                                                      | 2.74 us: 1.09x faster                                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                                 |
| xml_etree_generate       | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                                 |
| json                     | 5.86 ms                                                      | 5.39 ms: 1.09x faster                                                                 |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                                  |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                                                  |
| unpickle_list            | 4.65 us                                                      | 4.69 us: 1.01x slower                                                                 |
| pickle_dict              | 29.5 us                                                      | 30.4 us: 1.03x slower                                                                 |
| pickle                   | 9.89 us                                                      | 10.6 us: 1.07x slower                                                                 |
| telco                    | 7.23 ms                                                      | 7.88 ms: 1.09x slower                                                                 |
| pickle_list              | 4.12 us                                                      | 4.57 us: 1.11x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| unpickle                 | 13.5 us                                                      | 15.7 us: 1.16x slower                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 2.06 ms: 1.17x slower                                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                                                 |
| coverage                 | 63.3 ms                                                      | 78.9 ms: 1.25x slower                                                                 |
| gc_traversal             | 3.42 ms                                                      | 4.74 ms: 1.39x slower                                                                 |
| bench_mp_pool            | 6.37 ms                                                      | 2.45 sec: 385.15x slower                                                              |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-pythonperf2-x86_64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.335x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.12x