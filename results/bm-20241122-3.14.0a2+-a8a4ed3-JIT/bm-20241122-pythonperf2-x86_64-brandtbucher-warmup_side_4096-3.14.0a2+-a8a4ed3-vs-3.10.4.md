# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.284x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 292 ms: 1.20x faster                                                           |
| docutils       | 3.41 sec                                                     | 3.04 sec: 1.12x faster                                                         |
| html5lib       | 94.6 ms                                                      | 72.1 ms: 1.31x faster                                                          |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 333 ms: 2.08x faster                                                           |
| async_tree_memoization  | 819 ms                                                       | 408 ms: 2.01x faster                                                           |
| async_tree_io           | 1.60 sec                                                     | 838 ms: 1.91x faster                                                           |
| async_tree_cpu_io_mixed | 936 ms                                                       | 576 ms: 1.62x faster                                                           |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.9 ms: 1.56x faster                                                          |
| float          | 111 ms                                                       | 79.9 ms: 1.39x faster                                                          |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                                           |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                          |
| regex_dna      | 261 ms                                                       | 253 ms: 1.03x faster                                                           |
| regex_effbot   | 3.09 ms                                                      | 3.34 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 201 us: 1.55x faster                                                           |
| xml_etree_process    | 75.9 ms                                                      | 57.4 ms: 1.32x faster                                                          |
| pickle_pure_python   | 455 us                                                       | 345 us: 1.32x faster                                                           |
| tomli_loads          | 2.92 sec                                                     | 2.21 sec: 1.32x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                          |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                          |
| xml_etree_generate   | 92.3 ms                                                      | 81.5 ms: 1.13x faster                                                          |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                           |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.09x faster                                                           |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                          |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.42 ms: 1.56x faster                                                          |
| django_template | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                                          |
| genshi_text     | 31.4 ms                                                      | 29.4 ms: 1.07x faster                                                          |
| Geometric mean  | (ref)                                                        | 1.19x faster                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 186 us: 2.88x faster                                                           |
| deltablue                | 7.50 ms                                                      | 3.26 ms: 2.30x faster                                                          |
| async_tree_none          | 692 ms                                                       | 333 ms: 2.08x faster                                                           |
| async_tree_memoization   | 819 ms                                                       | 408 ms: 2.01x faster                                                           |
| async_tree_io            | 1.60 sec                                                     | 838 ms: 1.91x faster                                                           |
| richards_super           | 90.6 ms                                                      | 50.1 ms: 1.81x faster                                                          |
| logging_silent           | 167 ns                                                       | 93.6 ns: 1.79x faster                                                          |
| scimark_lu               | 167 ms                                                       | 94.5 ms: 1.76x faster                                                          |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.76x faster                                                           |
| pylint                   | 566 ms                                                       | 323 ms: 1.75x faster                                                           |
| richards                 | 75.1 ms                                                      | 43.8 ms: 1.71x faster                                                          |
| deepcopy_memo            | 49.8 us                                                      | 29.1 us: 1.71x faster                                                          |
| go                       | 262 ms                                                       | 157 ms: 1.67x faster                                                           |
| chaos                    | 109 ms                                                       | 66.3 ms: 1.64x faster                                                          |
| crypto_pyaes             | 119 ms                                                       | 72.9 ms: 1.63x faster                                                          |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 576 ms: 1.62x faster                                                           |
| scimark_monte_carlo      | 107 ms                                                       | 67.4 ms: 1.59x faster                                                          |
| nbody                    | 134 ms                                                       | 85.9 ms: 1.56x faster                                                          |
| mako                     | 14.7 ms                                                      | 9.42 ms: 1.56x faster                                                          |
| unpickle_pure_python     | 312 us                                                       | 201 us: 1.55x faster                                                           |
| pyflate                  | 733 ms                                                       | 477 ms: 1.54x faster                                                           |
| raytrace                 | 489 ms                                                       | 322 ms: 1.52x faster                                                           |
| deepcopy                 | 468 us                                                       | 310 us: 1.51x faster                                                           |
| sqlglot_parse            | 2.24 ms                                                      | 1.48 ms: 1.51x faster                                                          |
| spectral_norm            | 139 ms                                                       | 96.9 ms: 1.44x faster                                                          |
| sqlglot_transpile        | 2.68 ms                                                      | 1.87 ms: 1.43x faster                                                          |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                          |
| float                    | 111 ms                                                       | 79.9 ms: 1.39x faster                                                          |
| comprehensions           | 26.7 us                                                      | 19.6 us: 1.36x faster                                                          |
| generators               | 57.3 ms                                                      | 42.9 ms: 1.34x faster                                                          |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                                           |
| deepcopy_reduce          | 4.01 us                                                      | 3.03 us: 1.32x faster                                                          |
| xml_etree_process        | 75.9 ms                                                      | 57.4 ms: 1.32x faster                                                          |
| hexiom                   | 9.42 ms                                                      | 7.12 ms: 1.32x faster                                                          |
| pickle_pure_python       | 455 us                                                       | 345 us: 1.32x faster                                                           |
| tomli_loads              | 2.92 sec                                                     | 2.21 sec: 1.32x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 798 ms: 1.31x faster                                                           |
| html5lib                 | 94.6 ms                                                      | 72.1 ms: 1.31x faster                                                          |
| thrift                   | 1.18 ms                                                      | 896 us: 1.31x faster                                                           |
| logging_simple           | 8.88 us                                                      | 6.77 us: 1.31x faster                                                          |
| logging_format           | 9.64 us                                                      | 7.36 us: 1.31x faster                                                          |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                           |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 16.5 ms: 1.29x faster                                                          |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                          |
| fannkuch                 | 483 ms                                                       | 384 ms: 1.26x faster                                                           |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.5 ms: 1.23x faster                                                          |
| django_template          | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                                          |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                          |
| 2to3                     | 350 ms                                                       | 292 ms: 1.20x faster                                                           |
| dulwich_log              | 81.1 ms                                                      | 67.8 ms: 1.20x faster                                                          |
| sympy_sum                | 193 ms                                                       | 161 ms: 1.20x faster                                                           |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 967 us: 1.18x faster                                                           |
| sympy_str                | 360 ms                                                       | 311 ms: 1.16x faster                                                           |
| sympy_integrate          | 28.2 ms                                                      | 24.4 ms: 1.15x faster                                                          |
| mdp                      | 3.01 sec                                                     | 2.62 sec: 1.15x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 126 ms: 1.14x faster                                                           |
| json                     | 5.86 ms                                                      | 5.16 ms: 1.14x faster                                                          |
| xml_etree_generate       | 92.3 ms                                                      | 81.5 ms: 1.13x faster                                                          |
| nqueens                  | 115 ms                                                       | 102 ms: 1.13x faster                                                           |
| sympy_expand             | 600 ms                                                       | 531 ms: 1.13x faster                                                           |
| docutils                 | 3.41 sec                                                     | 3.04 sec: 1.12x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 63.0 ms: 1.11x faster                                                          |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                           |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.09x faster                                                           |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                           |
| genshi_text              | 31.4 ms                                                      | 29.4 ms: 1.07x faster                                                          |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                          |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                          |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.87 ms: 1.04x faster                                                          |
| regex_dna                | 261 ms                                                       | 253 ms: 1.03x faster                                                           |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                           |
| telco                    | 7.23 ms                                                      | 7.64 ms: 1.06x slower                                                          |
| regex_effbot             | 3.09 ms                                                      | 3.34 ms: 1.08x slower                                                          |
| async_generators         | 421 ms                                                       | 475 ms: 1.13x slower                                                           |
| python_startup_no_site   | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                          |
| coverage                 | 63.3 ms                                                      | 79.6 ms: 1.26x slower                                                          |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                          |
| create_gc_cycles         | 1.76 ms                                                      | 2.84 ms: 1.61x slower                                                          |
| gc_traversal             | 3.42 ms                                                      | 5.82 ms: 1.70x slower                                                          |
| bench_mp_pool            | 6.37 ms                                                      | 1.37 sec: 215.70x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.20x faster                                                                   |

Benchmark hidden because not significant (1): genshi_xml
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.284x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.29x