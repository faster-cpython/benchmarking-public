# Results vs. 3.10.4

- fork: python
- ref: v3.13.2
- machine: linux-x86_64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.284x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 294 ms: 1.19x faster                                         |
| chameleon      | 9.44 ms                                                      | 7.48 ms: 1.26x faster                                        |
| docutils       | 3.41 sec                                                     | 2.81 sec: 1.21x faster                                       |
| html5lib       | 94.6 ms                                                      | 73.7 ms: 1.28x faster                                        |
| tornado_http   | 157 ms                                                       | 122 ms: 1.29x faster                                         |
| Geometric mean | (ref)                                                        | 1.25x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 856 ms: 1.87x faster                                         |
| async_tree_none         | 692 ms                                                       | 382 ms: 1.81x faster                                         |
| async_tree_memoization  | 819 ms                                                       | 476 ms: 1.72x faster                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 614 ms: 1.52x faster                                         |
| Geometric mean          | (ref)                                                        | 1.73x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.6 ms: 1.51x faster                                        |
| float          | 111 ms                                                       | 80.3 ms: 1.38x faster                                        |
| pidigits       | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                        | 1.30x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.34x faster                                         |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                         |
| regex_v8       | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                        |
| regex_effbot   | 3.09 ms                                                      | 3.26 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 214 us: 1.46x faster                                         |
| pickle_pure_python   | 455 us                                                       | 327 us: 1.39x faster                                         |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.33x faster                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.1 ms: 1.26x faster                                        |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                        |
| tomli_loads          | 2.92 sec                                                     | 2.45 sec: 1.19x faster                                       |
| xml_etree_parse      | 160 ms                                                       | 150 ms: 1.07x faster                                         |
| xml_etree_generate   | 92.3 ms                                                      | 86.6 ms: 1.07x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                         |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.5 ms: 1.41x faster                                        |
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                        |
| genshi_text     | 31.4 ms                                                      | 26.0 ms: 1.21x faster                                        |
| genshi_xml      | 63.3 ms                                                      | 56.6 ms: 1.12x faster                                        |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.10x faster                                         |
| deltablue                | 7.50 ms                                                      | 3.36 ms: 2.23x faster                                        |
| async_tree_io            | 1.60 sec                                                     | 856 ms: 1.87x faster                                         |
| chaos                    | 109 ms                                                       | 59.3 ms: 1.83x faster                                        |
| async_tree_none          | 692 ms                                                       | 382 ms: 1.81x faster                                         |
| raytrace                 | 489 ms                                                       | 277 ms: 1.76x faster                                         |
| logging_silent           | 167 ns                                                       | 96.0 ns: 1.74x faster                                        |
| async_tree_memoization   | 819 ms                                                       | 476 ms: 1.72x faster                                         |
| generators               | 57.3 ms                                                      | 33.7 ms: 1.70x faster                                        |
| scimark_lu               | 167 ms                                                       | 98.3 ms: 1.70x faster                                        |
| scimark_monte_carlo      | 107 ms                                                       | 65.0 ms: 1.65x faster                                        |
| crypto_pyaes             | 119 ms                                                       | 72.1 ms: 1.65x faster                                        |
| go                       | 262 ms                                                       | 160 ms: 1.64x faster                                         |
| pylint                   | 566 ms                                                       | 346 ms: 1.63x faster                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                        |
| pyflate                  | 733 ms                                                       | 475 ms: 1.54x faster                                         |
| richards_super           | 90.6 ms                                                      | 59.3 ms: 1.53x faster                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 614 ms: 1.52x faster                                         |
| comprehensions           | 26.7 us                                                      | 17.6 us: 1.52x faster                                        |
| nbody                    | 134 ms                                                       | 88.6 ms: 1.51x faster                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                        |
| hexiom                   | 9.42 ms                                                      | 6.37 ms: 1.48x faster                                        |
| scimark_sor              | 180 ms                                                       | 123 ms: 1.47x faster                                         |
| unpickle_pure_python     | 312 us                                                       | 214 us: 1.46x faster                                         |
| spectral_norm            | 139 ms                                                       | 95.6 ms: 1.45x faster                                        |
| richards                 | 75.1 ms                                                      | 52.3 ms: 1.43x faster                                        |
| coroutines               | 30.3 ms                                                      | 21.4 ms: 1.42x faster                                        |
| django_template          | 50.2 ms                                                      | 35.5 ms: 1.41x faster                                        |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                        |
| pickle_pure_python       | 455 us                                                       | 327 us: 1.39x faster                                         |
| logging_format           | 9.64 us                                                      | 6.94 us: 1.39x faster                                        |
| logging_simple           | 8.88 us                                                      | 6.41 us: 1.39x faster                                        |
| float                    | 111 ms                                                       | 80.3 ms: 1.38x faster                                        |
| regex_compile            | 190 ms                                                       | 141 ms: 1.34x faster                                         |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                       |
| thrift                   | 1.18 ms                                                      | 885 us: 1.33x faster                                         |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.33x faster                                        |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                       |
| deepcopy_memo            | 49.8 us                                                      | 38.5 us: 1.29x faster                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 812 ms: 1.29x faster                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 147 ms: 1.29x faster                                         |
| bench_mp_pool            | 6.37 ms                                                      | 4.95 ms: 1.29x faster                                        |
| tornado_http             | 157 ms                                                       | 122 ms: 1.29x faster                                         |
| html5lib                 | 94.6 ms                                                      | 73.7 ms: 1.28x faster                                        |
| nqueens                  | 115 ms                                                       | 89.7 ms: 1.28x faster                                        |
| chameleon                | 9.44 ms                                                      | 7.48 ms: 1.26x faster                                        |
| xml_etree_process        | 75.9 ms                                                      | 60.1 ms: 1.26x faster                                        |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.25x faster                                         |
| bench_thread_pool        | 1.14 ms                                                      | 917 us: 1.24x faster                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.3 ms: 1.24x faster                                        |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                        |
| docutils                 | 3.41 sec                                                     | 2.81 sec: 1.21x faster                                       |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                        |
| deepcopy                 | 468 us                                                       | 387 us: 1.21x faster                                         |
| genshi_text              | 31.4 ms                                                      | 26.0 ms: 1.21x faster                                        |
| sympy_str                | 360 ms                                                       | 298 ms: 1.21x faster                                         |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.20x faster                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.5 ms: 1.20x faster                                        |
| dulwich_log              | 81.1 ms                                                      | 67.8 ms: 1.20x faster                                        |
| 2to3                     | 350 ms                                                       | 294 ms: 1.19x faster                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 59.0 ms: 1.19x faster                                        |
| tomli_loads              | 2.92 sec                                                     | 2.45 sec: 1.19x faster                                       |
| mdp                      | 3.01 sec                                                     | 2.54 sec: 1.18x faster                                       |
| sympy_expand             | 600 ms                                                       | 508 ms: 1.18x faster                                         |
| gunicorn                 | 1.16 ms                                                      | 994 us: 1.17x faster                                         |
| scimark_fft              | 361 ms                                                       | 315 ms: 1.15x faster                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.52 us: 1.14x faster                                        |
| genshi_xml               | 63.3 ms                                                      | 56.6 ms: 1.12x faster                                        |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.68 ms: 1.08x faster                                        |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                        |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                         |
| regex_v8                 | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                        |
| xml_etree_parse          | 160 ms                                                       | 150 ms: 1.07x faster                                         |
| xml_etree_generate       | 92.3 ms                                                      | 86.6 ms: 1.07x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                         |
| pidigits                 | 271 ms                                                       | 261 ms: 1.04x faster                                         |
| sqlite_synth             | 2.99 us                                                      | 2.90 us: 1.03x faster                                        |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                         |
| async_generators         | 421 ms                                                       | 427 ms: 1.02x slower                                         |
| regex_effbot             | 3.09 ms                                                      | 3.26 ms: 1.05x slower                                        |
| telco                    | 7.23 ms                                                      | 8.84 ms: 1.22x slower                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                        |
| coverage                 | 63.3 ms                                                      | 84.7 ms: 1.34x slower                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                        |
| gc_traversal             | 3.42 ms                                                      | 4.92 ms: 1.44x slower                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.72 ms: 1.54x slower                                        |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                 |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250204-3.13.2-4f8bb39/bm-20250204-pythonperf2-x86_64-python-v3.13.2-3.13.2-4f8bb39.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.284x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.24x