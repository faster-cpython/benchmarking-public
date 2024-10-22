# Results vs. 3.10.4

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 311 ms: 1.13x faster                                              |
| docutils       | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                            |
| html5lib       | 94.6 ms                                                      | 69.7 ms: 1.36x faster                                             |
| tornado_http   | 157 ms                                                       | 122 ms: 1.28x faster                                              |
| Geometric mean | (ref)                                                        | 1.21x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 323 ms: 2.14x faster                                              |
| async_tree_memoization  | 819 ms                                                       | 403 ms: 2.03x faster                                              |
| async_tree_io           | 1.60 sec                                                     | 802 ms: 1.99x faster                                              |
| async_tree_cpu_io_mixed | 936 ms                                                       | 574 ms: 1.63x faster                                              |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 81.5 ms: 1.65x faster                                             |
| float          | 111 ms                                                       | 73.8 ms: 1.50x faster                                             |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                              |
| Geometric mean | (ref)                                                        | 1.39x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 149 ms: 1.27x faster                                              |
| regex_dna      | 261 ms                                                       | 233 ms: 1.12x faster                                              |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                             |
| regex_effbot   | 3.09 ms                                                      | 3.39 ms: 1.10x slower                                             |
| Geometric mean | (ref)                                                        | 1.08x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                              |
| tomli_loads          | 2.92 sec                                                     | 2.12 sec: 1.38x faster                                            |
| pickle_pure_python   | 455 us                                                       | 331 us: 1.38x faster                                              |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                             |
| xml_etree_process    | 75.9 ms                                                      | 55.9 ms: 1.36x faster                                             |
| json_loads           | 30.3 us                                                      | 24.2 us: 1.25x faster                                             |
| xml_etree_generate   | 92.3 ms                                                      | 79.1 ms: 1.17x faster                                             |
| xml_etree_iterparse  | 110 ms                                                       | 98.3 ms: 1.12x faster                                             |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                              |
| pickle               | 9.89 us                                                      | 10.7 us: 1.08x slower                                             |
| pickle_list          | 4.12 us                                                      | 4.55 us: 1.10x slower                                             |
| pickle_dict          | 29.5 us                                                      | 32.6 us: 1.11x slower                                             |
| unpickle             | 13.5 us                                                      | 15.2 us: 1.12x slower                                             |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                             |
| python_startup_no_site | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                             |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.15 ms: 1.61x faster                                             |
| django_template | 50.2 ms                                                      | 43.3 ms: 1.16x faster                                             |
| genshi_text     | 31.4 ms                                                      | 31.1 ms: 1.01x faster                                             |
| genshi_xml      | 63.3 ms                                                      | 66.8 ms: 1.05x slower                                             |
| Geometric mean  | (ref)                                                        | 1.16x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 186 us: 2.88x faster                                              |
| deltablue                | 7.50 ms                                                      | 3.21 ms: 2.34x faster                                             |
| async_tree_none          | 692 ms                                                       | 323 ms: 2.14x faster                                              |
| asyncio_tcp              | 779 ms                                                       | 372 ms: 2.09x faster                                              |
| async_tree_memoization   | 819 ms                                                       | 403 ms: 2.03x faster                                              |
| async_tree_io            | 1.60 sec                                                     | 802 ms: 1.99x faster                                              |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                            |
| deepcopy_memo            | 49.8 us                                                      | 26.6 us: 1.87x faster                                             |
| go                       | 262 ms                                                       | 149 ms: 1.76x faster                                              |
| richards_super           | 90.6 ms                                                      | 52.3 ms: 1.73x faster                                             |
| scimark_lu               | 167 ms                                                       | 97.3 ms: 1.72x faster                                             |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.71x faster                                              |
| spectral_norm            | 139 ms                                                       | 81.9 ms: 1.70x faster                                             |
| richards                 | 75.1 ms                                                      | 44.8 ms: 1.68x faster                                             |
| crypto_pyaes             | 119 ms                                                       | 71.3 ms: 1.67x faster                                             |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                              |
| nbody                    | 134 ms                                                       | 81.5 ms: 1.65x faster                                             |
| chaos                    | 109 ms                                                       | 66.1 ms: 1.64x faster                                             |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 574 ms: 1.63x faster                                              |
| mako                     | 14.7 ms                                                      | 9.15 ms: 1.61x faster                                             |
| deepcopy                 | 468 us                                                       | 297 us: 1.58x faster                                              |
| scimark_monte_carlo      | 107 ms                                                       | 68.2 ms: 1.57x faster                                             |
| pyflate                  | 733 ms                                                       | 474 ms: 1.55x faster                                              |
| raytrace                 | 489 ms                                                       | 318 ms: 1.54x faster                                              |
| sqlglot_parse            | 2.24 ms                                                      | 1.49 ms: 1.51x faster                                             |
| float                    | 111 ms                                                       | 73.8 ms: 1.50x faster                                             |
| comprehensions           | 26.7 us                                                      | 18.3 us: 1.46x faster                                             |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                              |
| pylint                   | 566 ms                                                       | 410 ms: 1.38x faster                                              |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.38x faster                                             |
| tomli_loads              | 2.92 sec                                                     | 2.12 sec: 1.38x faster                                            |
| pickle_pure_python       | 455 us                                                       | 331 us: 1.38x faster                                              |
| sqlglot_transpile        | 2.68 ms                                                      | 1.95 ms: 1.38x faster                                             |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                             |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                             |
| hexiom                   | 9.42 ms                                                      | 6.92 ms: 1.36x faster                                             |
| xml_etree_process        | 75.9 ms                                                      | 55.9 ms: 1.36x faster                                             |
| html5lib                 | 94.6 ms                                                      | 69.7 ms: 1.36x faster                                             |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                             |
| generators               | 57.3 ms                                                      | 42.5 ms: 1.35x faster                                             |
| logging_format           | 9.64 us                                                      | 7.17 us: 1.35x faster                                             |
| logging_simple           | 8.88 us                                                      | 6.61 us: 1.34x faster                                             |
| fannkuch                 | 483 ms                                                       | 360 ms: 1.34x faster                                              |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 3.81 ms: 1.33x faster                                             |
| pprint_safe_repr         | 1.05 sec                                                     | 792 ms: 1.33x faster                                              |
| thrift                   | 1.18 ms                                                      | 887 us: 1.32x faster                                              |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                            |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                            |
| tornado_http             | 157 ms                                                       | 122 ms: 1.28x faster                                              |
| regex_compile            | 190 ms                                                       | 149 ms: 1.27x faster                                              |
| dulwich_log              | 81.1 ms                                                      | 64.2 ms: 1.26x faster                                             |
| scimark_fft              | 361 ms                                                       | 288 ms: 1.26x faster                                              |
| json_loads               | 30.3 us                                                      | 24.2 us: 1.25x faster                                             |
| bench_thread_pool        | 1.14 ms                                                      | 921 us: 1.24x faster                                              |
| bench_mp_pool            | 6.37 ms                                                      | 5.21 ms: 1.22x faster                                             |
| sympy_str                | 360 ms                                                       | 308 ms: 1.17x faster                                              |
| nqueens                  | 115 ms                                                       | 98.3 ms: 1.17x faster                                             |
| xml_etree_generate       | 92.3 ms                                                      | 79.1 ms: 1.17x faster                                             |
| django_template          | 50.2 ms                                                      | 43.3 ms: 1.16x faster                                             |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.16x faster                                            |
| sympy_sum                | 193 ms                                                       | 168 ms: 1.15x faster                                              |
| sympy_expand             | 600 ms                                                       | 528 ms: 1.14x faster                                              |
| 2to3                     | 350 ms                                                       | 311 ms: 1.13x faster                                              |
| xml_etree_iterparse      | 110 ms                                                       | 98.3 ms: 1.12x faster                                             |
| regex_dna                | 261 ms                                                       | 233 ms: 1.12x faster                                              |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                              |
| json                     | 5.86 ms                                                      | 5.26 ms: 1.11x faster                                             |
| sqlite_synth             | 2.99 us                                                      | 2.71 us: 1.10x faster                                             |
| sqlglot_normalize        | 144 ms                                                       | 131 ms: 1.10x faster                                              |
| async_generators         | 421 ms                                                       | 384 ms: 1.10x faster                                              |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                              |
| docutils                 | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                            |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                              |
| sqlglot_optimize         | 70.1 ms                                                      | 65.7 ms: 1.07x faster                                             |
| sympy_integrate          | 28.2 ms                                                      | 26.4 ms: 1.07x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                             |
| genshi_text              | 31.4 ms                                                      | 31.1 ms: 1.01x faster                                             |
| asyncio_websockets       | 390 ms                                                       | 393 ms: 1.01x slower                                              |
| genshi_xml               | 63.3 ms                                                      | 66.8 ms: 1.05x slower                                             |
| pickle                   | 9.89 us                                                      | 10.7 us: 1.08x slower                                             |
| create_gc_cycles         | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                             |
| regex_effbot             | 3.09 ms                                                      | 3.39 ms: 1.10x slower                                             |
| pickle_list              | 4.12 us                                                      | 4.55 us: 1.10x slower                                             |
| pickle_dict              | 29.5 us                                                      | 32.6 us: 1.11x slower                                             |
| unpickle                 | 13.5 us                                                      | 15.2 us: 1.12x slower                                             |
| telco                    | 7.23 ms                                                      | 8.28 ms: 1.15x slower                                             |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                             |
| python_startup_no_site   | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                             |
| gc_traversal             | 3.42 ms                                                      | 4.41 ms: 1.29x slower                                             |
| coverage                 | 63.3 ms                                                      | 82.0 ms: 1.30x slower                                             |
| unpack_sequence          | 59.9 ns                                                      | 88.0 ns: 1.47x slower                                             |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                      |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.22x