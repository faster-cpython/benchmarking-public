# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: lto_fix
- machine: linux-x86_64
- commit hash: 8891cd2
- commit date: 2025-04-07
- overall geometric mean: 1.367x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 274 ms: 1.28x faster                                                      |
| docutils       | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                    |
| html5lib       | 94.6 ms                                                      | 66.1 ms: 1.43x faster                                                     |
| Geometric mean | (ref)                                                        | 1.30x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 629 ms: 2.54x faster                                                      |
| async_tree_memoization  | 819 ms                                                       | 332 ms: 2.47x faster                                                      |
| async_tree_none         | 692 ms                                                       | 285 ms: 2.43x faster                                                      |
| async_tree_cpu_io_mixed | 936 ms                                                       | 504 ms: 1.86x faster                                                      |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 68.1 ms: 1.63x faster                                                     |
| nbody          | 134 ms                                                       | 93.4 ms: 1.44x faster                                                     |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                        | 1.36x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                      |
| regex_v8       | 27.2 ms                                                      | 24.4 ms: 1.11x faster                                                     |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                                      |
| regex_effbot   | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                        | 1.15x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 210 us: 1.48x faster                                                      |
| tomli_loads          | 2.92 sec                                                     | 2.06 sec: 1.42x faster                                                    |
| pickle_pure_python   | 455 us                                                       | 328 us: 1.39x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                     |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                     |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                      |
| json_loads           | 30.3 us                                                      | 26.7 us: 1.14x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                       | 98.4 ms: 1.12x faster                                                     |
| xml_etree_generate   | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                     |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                     |
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                     |
| genshi_text     | 31.4 ms                                                      | 22.9 ms: 1.37x faster                                                     |
| mako            | 14.7 ms                                                      | 11.1 ms: 1.32x faster                                                     |
| genshi_xml      | 63.3 ms                                                      | 53.1 ms: 1.19x faster                                                     |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.16x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 629 ms: 2.54x faster                                                      |
| async_tree_memoization   | 819 ms                                                       | 332 ms: 2.47x faster                                                      |
| async_tree_none          | 692 ms                                                       | 285 ms: 2.43x faster                                                      |
| deltablue                | 7.50 ms                                                      | 3.19 ms: 2.35x faster                                                     |
| mdp                      | 3.01 sec                                                     | 1.30 sec: 2.32x faster                                                    |
| go                       | 262 ms                                                       | 126 ms: 2.07x faster                                                      |
| generators               | 57.3 ms                                                      | 28.9 ms: 1.99x faster                                                     |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 504 ms: 1.86x faster                                                      |
| scimark_monte_carlo      | 107 ms                                                       | 58.3 ms: 1.84x faster                                                     |
| chaos                    | 109 ms                                                       | 59.0 ms: 1.84x faster                                                     |
| raytrace                 | 489 ms                                                       | 268 ms: 1.82x faster                                                      |
| logging_silent           | 167 ns                                                       | 92.0 ns: 1.82x faster                                                     |
| deepcopy_memo            | 49.8 us                                                      | 27.9 us: 1.79x faster                                                     |
| pylint                   | 566 ms                                                       | 317 ms: 1.78x faster                                                      |
| richards_super           | 90.6 ms                                                      | 51.5 ms: 1.76x faster                                                     |
| scimark_lu               | 167 ms                                                       | 94.9 ms: 1.76x faster                                                     |
| pyflate                  | 733 ms                                                       | 421 ms: 1.74x faster                                                      |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.73x faster                                                      |
| deepcopy                 | 468 us                                                       | 274 us: 1.71x faster                                                      |
| richards                 | 75.1 ms                                                      | 45.4 ms: 1.65x faster                                                     |
| float                    | 111 ms                                                       | 68.1 ms: 1.63x faster                                                     |
| spectral_norm            | 139 ms                                                       | 89.5 ms: 1.55x faster                                                     |
| comprehensions           | 26.7 us                                                      | 17.7 us: 1.51x faster                                                     |
| crypto_pyaes             | 119 ms                                                       | 79.4 ms: 1.50x faster                                                     |
| hexiom                   | 9.42 ms                                                      | 6.27 ms: 1.50x faster                                                     |
| unpickle_pure_python     | 312 us                                                       | 210 us: 1.48x faster                                                      |
| nbody                    | 134 ms                                                       | 93.4 ms: 1.44x faster                                                     |
| html5lib                 | 94.6 ms                                                      | 66.1 ms: 1.43x faster                                                     |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.06 sec: 1.42x faster                                                    |
| logging_format           | 9.64 us                                                      | 6.81 us: 1.42x faster                                                     |
| logging_simple           | 8.88 us                                                      | 6.28 us: 1.41x faster                                                     |
| django_template          | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                     |
| coroutines               | 30.3 ms                                                      | 21.6 ms: 1.40x faster                                                     |
| deepcopy_reduce          | 4.01 us                                                      | 2.86 us: 1.40x faster                                                     |
| pickle_pure_python       | 455 us                                                       | 328 us: 1.39x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 22.9 ms: 1.37x faster                                                     |
| pprint_pformat           | 2.15 sec                                                     | 1.58 sec: 1.36x faster                                                    |
| pprint_safe_repr         | 1.05 sec                                                     | 773 ms: 1.36x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                    |
| fannkuch                 | 483 ms                                                       | 363 ms: 1.33x faster                                                      |
| mako                     | 14.7 ms                                                      | 11.1 ms: 1.32x faster                                                     |
| dulwich_log              | 81.1 ms                                                      | 62.0 ms: 1.31x faster                                                     |
| xml_etree_process        | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                     |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                     |
| sqlalchemy_declarative   | 190 ms                                                       | 147 ms: 1.29x faster                                                      |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                      |
| 2to3                     | 350 ms                                                       | 274 ms: 1.28x faster                                                      |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.8 ms: 1.28x faster                                                     |
| sympy_integrate          | 28.2 ms                                                      | 22.1 ms: 1.27x faster                                                     |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.27x faster                                                     |
| sympy_str                | 360 ms                                                       | 286 ms: 1.26x faster                                                      |
| sympy_expand             | 600 ms                                                       | 484 ms: 1.24x faster                                                      |
| nqueens                  | 115 ms                                                       | 94.1 ms: 1.22x faster                                                     |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.20x faster                                                      |
| docutils                 | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                    |
| genshi_xml               | 63.3 ms                                                      | 53.1 ms: 1.19x faster                                                     |
| bench_thread_pool        | 1.14 ms                                                      | 974 us: 1.17x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                      |
| json_loads               | 30.3 us                                                      | 26.7 us: 1.14x faster                                                     |
| xml_etree_iterparse      | 110 ms                                                       | 98.4 ms: 1.12x faster                                                     |
| regex_v8                 | 27.2 ms                                                      | 24.4 ms: 1.11x faster                                                     |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.59 ms: 1.11x faster                                                     |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                     |
| json                     | 5.86 ms                                                      | 5.44 ms: 1.08x faster                                                     |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                      |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                                     |
| async_generators         | 421 ms                                                       | 407 ms: 1.03x faster                                                      |
| regex_effbot             | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                     |
| telco                    | 7.23 ms                                                      | 7.72 ms: 1.07x slower                                                     |
| coverage                 | 63.3 ms                                                      | 81.8 ms: 1.29x slower                                                     |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                     |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                     |
| create_gc_cycles         | 1.76 ms                                                      | 2.80 ms: 1.59x slower                                                     |
| gc_traversal             | 3.42 ms                                                      | 6.58 ms: 1.93x slower                                                     |
| bench_mp_pool            | 6.37 ms                                                      | 1.09 sec: 170.64x slower                                                  |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250407-3.14.0a6+-8891cd2/bm-20250407-pythonperf2-x86_64-Fidget%2dSpinner-lto_fix-3.14.0a6+-8891cd2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.367x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.29x