# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: c73f8ac
- commit date: 2024-06-04
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 308 ms: 1.14x faster                                                          |
| docutils       | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                        |
| html5lib       | 94.6 ms                                                      | 74.6 ms: 1.27x faster                                                         |
| tornado_http   | 157 ms                                                       | 123 ms: 1.28x faster                                                          |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 373 ms: 1.85x faster                                                          |
| async_tree_io           | 1.60 sec                                                     | 883 ms: 1.81x faster                                                          |
| async_tree_memoization  | 819 ms                                                       | 474 ms: 1.73x faster                                                          |
| async_tree_cpu_io_mixed | 936 ms                                                       | 623 ms: 1.50x faster                                                          |
| Geometric mean          | (ref)                                                        | 1.72x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.3 ms: 1.59x faster                                                         |
| float          | 111 ms                                                       | 75.0 ms: 1.48x faster                                                         |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                          |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                          |
| regex_dna      | 261 ms                                                       | 245 ms: 1.07x faster                                                          |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.43 ms: 1.11x slower                                                         |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 326 us: 1.40x faster                                                          |
| unpickle_pure_python | 312 us                                                       | 224 us: 1.39x faster                                                          |
| tomli_loads          | 2.92 sec                                                     | 2.10 sec: 1.39x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                         |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.19x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 81.5 ms: 1.13x faster                                                         |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.12x faster                                                          |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                          |
| unpickle_list        | 4.65 us                                                      | 4.73 us: 1.02x slower                                                         |
| pickle               | 9.89 us                                                      | 10.5 us: 1.07x slower                                                         |
| pickle_dict          | 29.5 us                                                      | 31.6 us: 1.07x slower                                                         |
| pickle_list          | 4.12 us                                                      | 4.42 us: 1.07x slower                                                         |
| unpickle             | 13.5 us                                                      | 15.7 us: 1.16x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.7 ms: 1.19x slower                                                         |
| python_startup_no_site | 7.33 ms                                                      | 9.41 ms: 1.28x slower                                                         |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.27 ms: 1.59x faster                                                         |
| django_template | 50.2 ms                                                      | 43.0 ms: 1.17x faster                                                         |
| genshi_text     | 31.4 ms                                                      | 28.8 ms: 1.09x faster                                                         |
| genshi_xml      | 63.3 ms                                                      | 67.0 ms: 1.06x slower                                                         |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 185 us: 2.89x faster                                                          |
| asyncio_tcp              | 779 ms                                                       | 381 ms: 2.04x faster                                                          |
| deltablue                | 7.50 ms                                                      | 3.82 ms: 1.96x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                        |
| async_tree_none          | 692 ms                                                       | 373 ms: 1.85x faster                                                          |
| async_tree_io            | 1.60 sec                                                     | 883 ms: 1.81x faster                                                          |
| async_tree_memoization   | 819 ms                                                       | 474 ms: 1.73x faster                                                          |
| raytrace                 | 489 ms                                                       | 285 ms: 1.72x faster                                                          |
| richards_super           | 90.6 ms                                                      | 53.3 ms: 1.70x faster                                                         |
| generators               | 57.3 ms                                                      | 34.3 ms: 1.67x faster                                                         |
| spectral_norm            | 139 ms                                                       | 83.4 ms: 1.67x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 72.4 ms: 1.65x faster                                                         |
| chaos                    | 109 ms                                                       | 66.0 ms: 1.65x faster                                                         |
| richards                 | 75.1 ms                                                      | 45.7 ms: 1.64x faster                                                         |
| pyflate                  | 733 ms                                                       | 454 ms: 1.61x faster                                                          |
| go                       | 262 ms                                                       | 163 ms: 1.60x faster                                                          |
| nbody                    | 134 ms                                                       | 84.3 ms: 1.59x faster                                                         |
| mako                     | 14.7 ms                                                      | 9.27 ms: 1.59x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 69.1 ms: 1.56x faster                                                         |
| logging_silent           | 167 ns                                                       | 109 ns: 1.54x faster                                                          |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 623 ms: 1.50x faster                                                          |
| pylint                   | 566 ms                                                       | 380 ms: 1.49x faster                                                          |
| float                    | 111 ms                                                       | 75.0 ms: 1.48x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.84 ms: 1.46x faster                                                         |
| comprehensions           | 26.7 us                                                      | 18.4 us: 1.45x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 326 us: 1.40x faster                                                          |
| unpickle_pure_python     | 312 us                                                       | 224 us: 1.39x faster                                                          |
| tomli_loads              | 2.92 sec                                                     | 2.10 sec: 1.39x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.38x faster                                                         |
| scimark_lu               | 167 ms                                                       | 122 ms: 1.36x faster                                                          |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                         |
| fannkuch                 | 483 ms                                                       | 355 ms: 1.36x faster                                                          |
| logging_simple           | 8.88 us                                                      | 6.55 us: 1.36x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 6.96 ms: 1.35x faster                                                         |
| logging_format           | 9.64 us                                                      | 7.12 us: 1.35x faster                                                         |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                          |
| scimark_sor              | 180 ms                                                       | 134 ms: 1.35x faster                                                          |
| pprint_safe_repr         | 1.05 sec                                                     | 790 ms: 1.33x faster                                                          |
| deepcopy_memo            | 49.8 us                                                      | 37.6 us: 1.32x faster                                                         |
| bench_mp_pool            | 6.37 ms                                                      | 4.82 ms: 1.32x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.31x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                         |
| thrift                   | 1.18 ms                                                      | 905 us: 1.30x faster                                                          |
| pathlib                  | 21.4 ms                                                      | 16.5 ms: 1.30x faster                                                         |
| tornado_http             | 157 ms                                                       | 123 ms: 1.28x faster                                                          |
| html5lib                 | 94.6 ms                                                      | 74.6 ms: 1.27x faster                                                         |
| scimark_fft              | 361 ms                                                       | 295 ms: 1.23x faster                                                          |
| dulwich_log              | 81.1 ms                                                      | 66.3 ms: 1.22x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.20 ms: 1.21x faster                                                         |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.19x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 959 us: 1.19x faster                                                          |
| django_template          | 50.2 ms                                                      | 43.0 ms: 1.17x faster                                                         |
| nqueens                  | 115 ms                                                       | 98.7 ms: 1.16x faster                                                         |
| dask                     | 472 ms                                                       | 405 ms: 1.16x faster                                                          |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                        |
| sympy_sum                | 193 ms                                                       | 168 ms: 1.15x faster                                                          |
| 2to3                     | 350 ms                                                       | 308 ms: 1.14x faster                                                          |
| sympy_str                | 360 ms                                                       | 316 ms: 1.14x faster                                                          |
| xml_etree_generate       | 92.3 ms                                                      | 81.5 ms: 1.13x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.12x faster                                                          |
| sympy_expand             | 600 ms                                                       | 538 ms: 1.12x faster                                                          |
| sqlglot_normalize        | 144 ms                                                       | 129 ms: 1.11x faster                                                          |
| deepcopy                 | 468 us                                                       | 423 us: 1.11x faster                                                          |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                          |
| json                     | 5.86 ms                                                      | 5.31 ms: 1.10x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 64.2 ms: 1.09x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 25.8 ms: 1.09x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 28.8 ms: 1.09x faster                                                         |
| docutils                 | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                          |
| deepcopy_reduce          | 4.01 us                                                      | 3.73 us: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.78 us: 1.07x faster                                                         |
| async_generators         | 421 ms                                                       | 392 ms: 1.07x faster                                                          |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                                          |
| regex_dna                | 261 ms                                                       | 245 ms: 1.07x faster                                                          |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                         |
| unpickle_list            | 4.65 us                                                      | 4.73 us: 1.02x slower                                                         |
| genshi_xml               | 63.3 ms                                                      | 67.0 ms: 1.06x slower                                                         |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.07x slower                                                         |
| pickle_dict              | 29.5 us                                                      | 31.6 us: 1.07x slower                                                         |
| pickle_list              | 4.12 us                                                      | 4.42 us: 1.07x slower                                                         |
| create_gc_cycles         | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.43 ms: 1.11x slower                                                         |
| telco                    | 7.23 ms                                                      | 8.27 ms: 1.14x slower                                                         |
| unpickle                 | 13.5 us                                                      | 15.7 us: 1.16x slower                                                         |
| python_startup           | 11.5 ms                                                      | 13.7 ms: 1.19x slower                                                         |
| coverage                 | 63.3 ms                                                      | 80.3 ms: 1.27x slower                                                         |
| python_startup_no_site   | 7.33 ms                                                      | 9.41 ms: 1.28x slower                                                         |
| gc_traversal             | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                         |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.14.0a0-c73f8ac/bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.22x