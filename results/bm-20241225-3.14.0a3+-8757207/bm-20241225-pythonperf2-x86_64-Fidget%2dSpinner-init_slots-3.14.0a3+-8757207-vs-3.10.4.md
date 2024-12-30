# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: init_slots
- machine: linux-x86_64
- commit hash: 8757207
- commit date: 2024-12-25
- overall geometric mean: 1.345x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| html5lib       | 94.6 ms                                                      | 67.4 ms: 1.40x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 635 ms: 2.52x faster                                                         |
| async_tree_none         | 692 ms                                                       | 286 ms: 2.42x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 349 ms: 2.35x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 509 ms: 1.84x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.26x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.7 ms: 1.57x faster                                                        |
| nbody          | 134 ms                                                       | 86.5 ms: 1.55x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.39x faster                                                         |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.21 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 205 us: 1.52x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 326 us: 1.40x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 59.5 ms: 1.28x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.0 us: 1.26x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 95.6 ms: 1.16x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 83.7 ms: 1.10x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                        |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 23.8 ms: 1.32x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 53.6 ms: 1.18x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.11x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 635 ms: 2.52x faster                                                         |
| async_tree_none          | 692 ms                                                       | 286 ms: 2.42x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 349 ms: 2.35x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.34 ms: 2.24x faster                                                        |
| go                       | 262 ms                                                       | 125 ms: 2.10x faster                                                         |
| generators               | 57.3 ms                                                      | 28.5 ms: 2.01x faster                                                        |
| raytrace                 | 489 ms                                                       | 264 ms: 1.86x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 509 ms: 1.84x faster                                                         |
| pylint                   | 566 ms                                                       | 322 ms: 1.76x faster                                                         |
| richards_super           | 90.6 ms                                                      | 51.7 ms: 1.75x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.4 ms: 1.75x faster                                                        |
| chaos                    | 109 ms                                                       | 62.5 ms: 1.74x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 62.6 ms: 1.72x faster                                                        |
| logging_silent           | 167 ns                                                       | 98.7 ns: 1.70x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.33 ms: 1.68x faster                                                        |
| deepcopy                 | 468 us                                                       | 284 us: 1.65x faster                                                         |
| richards                 | 75.1 ms                                                      | 45.8 ms: 1.64x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 30.4 us: 1.64x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.8 ms: 1.64x faster                                                        |
| pyflate                  | 733 ms                                                       | 454 ms: 1.61x faster                                                         |
| scimark_sor              | 180 ms                                                       | 113 ms: 1.59x faster                                                         |
| spectral_norm            | 139 ms                                                       | 88.5 ms: 1.57x faster                                                        |
| float                    | 111 ms                                                       | 70.7 ms: 1.57x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.01 ms: 1.57x faster                                                        |
| nbody                    | 134 ms                                                       | 86.5 ms: 1.55x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.74 ms: 1.54x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.52x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 205 us: 1.52x faster                                                         |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.31 us: 1.41x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.86 us: 1.41x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 67.4 ms: 1.40x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.87 us: 1.40x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 326 us: 1.40x faster                                                         |
| regex_compile            | 190 ms                                                       | 137 ms: 1.39x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                                       |
| thrift                   | 1.18 ms                                                      | 859 us: 1.37x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 771 ms: 1.36x faster                                                         |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.33x faster                                                        |
| fannkuch                 | 483 ms                                                       | 364 ms: 1.33x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 23.8 ms: 1.32x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 144 ms: 1.32x faster                                                         |
| nqueens                  | 115 ms                                                       | 88.2 ms: 1.30x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 59.5 ms: 1.28x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.9 ms: 1.27x faster                                                        |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.0 us: 1.26x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.25x faster                                                         |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                         |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 930 us: 1.23x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.22x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.48 sec: 1.21x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 57.8 ms: 1.21x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 67.1 ms: 1.21x faster                                                        |
| sympy_expand             | 600 ms                                                       | 498 ms: 1.20x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 53.6 ms: 1.18x faster                                                        |
| scimark_fft              | 361 ms                                                       | 311 ms: 1.16x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 95.6 ms: 1.16x faster                                                        |
| json                     | 5.86 ms                                                      | 5.17 ms: 1.14x faster                                                        |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 83.7 ms: 1.10x faster                                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                         |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.84 ms: 1.05x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                        |
| async_generators         | 421 ms                                                       | 430 ms: 1.02x slower                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.21 ms: 1.04x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.85 ms: 1.09x slower                                                        |
| mypy2                    | 933 ms                                                       | 1.02 sec: 1.10x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 78.3 ms: 1.24x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.78 ms: 1.58x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.58 ms: 1.93x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.44 sec: 225.33x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241225-3.14.0a3+-8757207/bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.345x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.29x