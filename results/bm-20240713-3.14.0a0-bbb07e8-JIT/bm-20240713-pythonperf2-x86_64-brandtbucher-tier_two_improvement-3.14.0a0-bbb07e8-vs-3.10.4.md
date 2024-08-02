# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 306 ms: 1.14x faster                                                              |
| docutils       | 3.41 sec                                                     | 3.08 sec: 1.11x faster                                                            |
| html5lib       | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                             |
| tornado_http   | 157 ms                                                       | 120 ms: 1.30x faster                                                              |
| Geometric mean | (ref)                                                        | 1.22x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 338 ms: 2.05x faster                                                              |
| async_tree_memoization  | 819 ms                                                       | 407 ms: 2.01x faster                                                              |
| async_tree_io           | 1.60 sec                                                     | 813 ms: 1.97x faster                                                              |
| async_tree_cpu_io_mixed | 936 ms                                                       | 581 ms: 1.61x faster                                                              |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.7 ms: 1.60x faster                                                             |
| float          | 111 ms                                                       | 74.1 ms: 1.50x faster                                                             |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                              |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.40x faster                                                              |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                                              |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                             |
| regex_effbot   | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                             |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 211 us: 1.48x faster                                                              |
| pickle_pure_python   | 455 us                                                       | 315 us: 1.44x faster                                                              |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                            |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                             |
| xml_etree_process    | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                             |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                             |
| xml_etree_generate   | 92.3 ms                                                      | 81.8 ms: 1.13x faster                                                             |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                              |
| xml_etree_iterparse  | 110 ms                                                       | 99.4 ms: 1.11x faster                                                             |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                             |
| python_startup_no_site | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.24 ms: 1.59x faster                                                             |
| django_template | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                                             |
| genshi_text     | 31.4 ms                                                      | 29.2 ms: 1.08x faster                                                             |
| genshi_xml      | 63.3 ms                                                      | 61.9 ms: 1.02x faster                                                             |
| Geometric mean  | (ref)                                                        | 1.21x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 182 us: 2.95x faster                                                              |
| asyncio_tcp              | 779 ms                                                       | 373 ms: 2.09x faster                                                              |
| deltablue                | 7.50 ms                                                      | 3.64 ms: 2.06x faster                                                             |
| async_tree_none          | 692 ms                                                       | 338 ms: 2.05x faster                                                              |
| async_tree_memoization   | 819 ms                                                       | 407 ms: 2.01x faster                                                              |
| async_tree_io            | 1.60 sec                                                     | 813 ms: 1.97x faster                                                              |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                            |
| deepcopy_memo            | 49.8 us                                                      | 28.2 us: 1.76x faster                                                             |
| richards_super           | 90.6 ms                                                      | 52.1 ms: 1.74x faster                                                             |
| crypto_pyaes             | 119 ms                                                       | 69.7 ms: 1.71x faster                                                             |
| spectral_norm            | 139 ms                                                       | 82.3 ms: 1.69x faster                                                             |
| richards                 | 75.1 ms                                                      | 44.7 ms: 1.68x faster                                                             |
| pyflate                  | 733 ms                                                       | 437 ms: 1.68x faster                                                              |
| raytrace                 | 489 ms                                                       | 295 ms: 1.66x faster                                                              |
| chaos                    | 109 ms                                                       | 65.5 ms: 1.66x faster                                                             |
| scimark_monte_carlo      | 107 ms                                                       | 65.7 ms: 1.63x faster                                                             |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 581 ms: 1.61x faster                                                              |
| nbody                    | 134 ms                                                       | 83.7 ms: 1.60x faster                                                             |
| go                       | 262 ms                                                       | 163 ms: 1.60x faster                                                              |
| generators               | 57.3 ms                                                      | 36.0 ms: 1.59x faster                                                             |
| logging_silent           | 167 ns                                                       | 105 ns: 1.59x faster                                                              |
| mako                     | 14.7 ms                                                      | 9.24 ms: 1.59x faster                                                             |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.58x faster                                                             |
| pylint                   | 566 ms                                                       | 368 ms: 1.54x faster                                                              |
| deepcopy                 | 468 us                                                       | 307 us: 1.53x faster                                                              |
| float                    | 111 ms                                                       | 74.1 ms: 1.50x faster                                                             |
| scimark_lu               | 167 ms                                                       | 113 ms: 1.48x faster                                                              |
| unpickle_pure_python     | 312 us                                                       | 211 us: 1.48x faster                                                              |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.47x faster                                                             |
| comprehensions           | 26.7 us                                                      | 18.3 us: 1.46x faster                                                             |
| pickle_pure_python       | 455 us                                                       | 315 us: 1.44x faster                                                              |
| scimark_sor              | 180 ms                                                       | 126 ms: 1.43x faster                                                              |
| hexiom                   | 9.42 ms                                                      | 6.62 ms: 1.42x faster                                                             |
| regex_compile            | 190 ms                                                       | 135 ms: 1.40x faster                                                              |
| fannkuch                 | 483 ms                                                       | 345 ms: 1.40x faster                                                              |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                            |
| logging_simple           | 8.88 us                                                      | 6.36 us: 1.39x faster                                                             |
| logging_format           | 9.64 us                                                      | 6.96 us: 1.38x faster                                                             |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                                             |
| html5lib                 | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                             |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                             |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                            |
| bench_mp_pool            | 6.37 ms                                                      | 4.77 ms: 1.33x faster                                                             |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.04 us: 1.32x faster                                                             |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                             |
| pprint_safe_repr         | 1.05 sec                                                     | 800 ms: 1.31x faster                                                              |
| xml_etree_process        | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                             |
| tornado_http             | 157 ms                                                       | 120 ms: 1.30x faster                                                              |
| thrift                   | 1.18 ms                                                      | 906 us: 1.30x faster                                                              |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 3.92 ms: 1.29x faster                                                             |
| scimark_fft              | 361 ms                                                       | 290 ms: 1.25x faster                                                              |
| bench_thread_pool        | 1.14 ms                                                      | 918 us: 1.24x faster                                                              |
| dulwich_log              | 81.1 ms                                                      | 65.3 ms: 1.24x faster                                                             |
| django_template          | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                                             |
| nqueens                  | 115 ms                                                       | 94.0 ms: 1.22x faster                                                             |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                             |
| dask                     | 472 ms                                                       | 393 ms: 1.20x faster                                                              |
| sympy_str                | 360 ms                                                       | 308 ms: 1.17x faster                                                              |
| sympy_sum                | 193 ms                                                       | 165 ms: 1.17x faster                                                              |
| sympy_expand             | 600 ms                                                       | 519 ms: 1.16x faster                                                              |
| mdp                      | 3.01 sec                                                     | 2.61 sec: 1.15x faster                                                            |
| 2to3                     | 350 ms                                                       | 306 ms: 1.14x faster                                                              |
| xml_etree_generate       | 92.3 ms                                                      | 81.8 ms: 1.13x faster                                                             |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.13x faster                                                              |
| sqlglot_optimize         | 70.1 ms                                                      | 62.4 ms: 1.12x faster                                                             |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                              |
| xml_etree_iterparse      | 110 ms                                                       | 99.4 ms: 1.11x faster                                                             |
| regex_dna                | 261 ms                                                       | 235 ms: 1.11x faster                                                              |
| docutils                 | 3.41 sec                                                     | 3.08 sec: 1.11x faster                                                            |
| sympy_integrate          | 28.2 ms                                                      | 25.5 ms: 1.11x faster                                                             |
| async_generators         | 421 ms                                                       | 383 ms: 1.10x faster                                                              |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                              |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                                             |
| genshi_text              | 31.4 ms                                                      | 29.2 ms: 1.08x faster                                                             |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.07x faster                                                              |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                             |
| genshi_xml               | 63.3 ms                                                      | 61.9 ms: 1.02x faster                                                             |
| asyncio_websockets       | 390 ms                                                       | 395 ms: 1.01x slower                                                              |
| create_gc_cycles         | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                             |
| telco                    | 7.23 ms                                                      | 8.14 ms: 1.13x slower                                                             |
| regex_effbot             | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                             |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                             |
| python_startup_no_site   | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                             |
| coverage                 | 63.3 ms                                                      | 81.1 ms: 1.28x slower                                                             |
| gc_traversal             | 3.42 ms                                                      | 4.68 ms: 1.37x slower                                                             |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                      |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-bbb07e8-JIT/bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.19x