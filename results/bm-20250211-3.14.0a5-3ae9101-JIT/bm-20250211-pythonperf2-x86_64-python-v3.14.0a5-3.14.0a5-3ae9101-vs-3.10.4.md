# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a5
- machine: linux-x86_64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.331x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 290 ms: 1.21x faster                                             |
| docutils       | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                           |
| html5lib       | 94.6 ms                                                      | 67.3 ms: 1.41x faster                                            |
| Geometric mean | (ref)                                                        | 1.25x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 650 ms: 2.46x faster                                             |
| async_tree_none         | 692 ms                                                       | 296 ms: 2.34x faster                                             |
| async_tree_memoization  | 819 ms                                                       | 359 ms: 2.28x faster                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 526 ms: 1.78x faster                                             |
| Geometric mean          | (ref)                                                        | 2.20x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.2 ms: 1.58x faster                                            |
| nbody          | 134 ms                                                       | 101 ms: 1.33x faster                                             |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                             |
| Geometric mean | (ref)                                                        | 1.31x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 136 ms: 1.40x faster                                             |
| regex_v8       | 27.2 ms                                                      | 24.5 ms: 1.11x faster                                            |
| regex_dna      | 261 ms                                                       | 244 ms: 1.07x faster                                             |
| regex_effbot   | 3.09 ms                                                      | 3.14 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                        | 1.13x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 205 us: 1.52x faster                                             |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                           |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                             |
| xml_etree_process    | 75.9 ms                                                      | 56.2 ms: 1.35x faster                                            |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                            |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                             |
| xml_etree_generate   | 92.3 ms                                                      | 79.0 ms: 1.17x faster                                            |
| xml_etree_iterparse  | 110 ms                                                       | 95.5 ms: 1.16x faster                                            |
| json_loads           | 30.3 us                                                      | 26.9 us: 1.13x faster                                            |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                            |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                            |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.74 ms: 1.51x faster                                            |
| django_template | 50.2 ms                                                      | 36.5 ms: 1.38x faster                                            |
| genshi_text     | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                            |
| genshi_xml      | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                            |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.04x faster                                             |
| async_tree_io            | 1.60 sec                                                     | 650 ms: 2.46x faster                                             |
| async_tree_none          | 692 ms                                                       | 296 ms: 2.34x faster                                             |
| async_tree_memoization   | 819 ms                                                       | 359 ms: 2.28x faster                                             |
| deltablue                | 7.50 ms                                                      | 3.47 ms: 2.16x faster                                            |
| generators               | 57.3 ms                                                      | 29.8 ms: 1.92x faster                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 526 ms: 1.78x faster                                             |
| scimark_monte_carlo      | 107 ms                                                       | 60.6 ms: 1.77x faster                                            |
| scimark_lu               | 167 ms                                                       | 94.3 ms: 1.77x faster                                            |
| pylint                   | 566 ms                                                       | 320 ms: 1.77x faster                                             |
| go                       | 262 ms                                                       | 148 ms: 1.76x faster                                             |
| richards_super           | 90.6 ms                                                      | 51.4 ms: 1.76x faster                                            |
| chaos                    | 109 ms                                                       | 62.9 ms: 1.73x faster                                            |
| logging_silent           | 167 ns                                                       | 97.5 ns: 1.72x faster                                            |
| pyflate                  | 733 ms                                                       | 428 ms: 1.71x faster                                             |
| deepcopy_memo            | 49.8 us                                                      | 29.2 us: 1.70x faster                                            |
| scimark_sor              | 180 ms                                                       | 106 ms: 1.69x faster                                             |
| spectral_norm            | 139 ms                                                       | 83.1 ms: 1.67x faster                                            |
| deepcopy                 | 468 us                                                       | 283 us: 1.66x faster                                             |
| raytrace                 | 489 ms                                                       | 299 ms: 1.63x faster                                             |
| richards                 | 75.1 ms                                                      | 46.0 ms: 1.63x faster                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.38 ms: 1.62x faster                                            |
| float                    | 111 ms                                                       | 70.2 ms: 1.58x faster                                            |
| crypto_pyaes             | 119 ms                                                       | 76.6 ms: 1.55x faster                                            |
| unpickle_pure_python     | 312 us                                                       | 205 us: 1.52x faster                                             |
| sqlglot_transpile        | 2.68 ms                                                      | 1.77 ms: 1.52x faster                                            |
| mako                     | 14.7 ms                                                      | 9.74 ms: 1.51x faster                                            |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                            |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                           |
| comprehensions           | 26.7 us                                                      | 18.9 us: 1.41x faster                                            |
| html5lib                 | 94.6 ms                                                      | 67.3 ms: 1.41x faster                                            |
| regex_compile            | 190 ms                                                       | 136 ms: 1.40x faster                                             |
| logging_format           | 9.64 us                                                      | 6.90 us: 1.40x faster                                            |
| logging_simple           | 8.88 us                                                      | 6.37 us: 1.39x faster                                            |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                            |
| django_template          | 50.2 ms                                                      | 36.5 ms: 1.38x faster                                            |
| thrift                   | 1.18 ms                                                      | 856 us: 1.37x faster                                             |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                             |
| xml_etree_process        | 75.9 ms                                                      | 56.2 ms: 1.35x faster                                            |
| nbody                    | 134 ms                                                       | 101 ms: 1.33x faster                                             |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                           |
| hexiom                   | 9.42 ms                                                      | 7.14 ms: 1.32x faster                                            |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                             |
| pprint_safe_repr         | 1.05 sec                                                     | 812 ms: 1.29x faster                                             |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                           |
| pathlib                  | 21.4 ms                                                      | 16.6 ms: 1.29x faster                                            |
| fannkuch                 | 483 ms                                                       | 381 ms: 1.27x faster                                             |
| genshi_text              | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                            |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.0 ms: 1.26x faster                                            |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                            |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                             |
| scimark_fft              | 361 ms                                                       | 294 ms: 1.23x faster                                             |
| 2to3                     | 350 ms                                                       | 290 ms: 1.21x faster                                             |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.20x faster                                             |
| sympy_str                | 360 ms                                                       | 300 ms: 1.20x faster                                             |
| dulwich_log              | 81.1 ms                                                      | 68.0 ms: 1.19x faster                                            |
| sympy_integrate          | 28.2 ms                                                      | 23.7 ms: 1.19x faster                                            |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                           |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                             |
| xml_etree_generate       | 92.3 ms                                                      | 79.0 ms: 1.17x faster                                            |
| sympy_expand             | 600 ms                                                       | 514 ms: 1.17x faster                                             |
| nqueens                  | 115 ms                                                       | 98.6 ms: 1.17x faster                                            |
| bench_thread_pool        | 1.14 ms                                                      | 979 us: 1.17x faster                                             |
| docutils                 | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                           |
| sqlglot_optimize         | 70.1 ms                                                      | 60.5 ms: 1.16x faster                                            |
| xml_etree_iterparse      | 110 ms                                                       | 95.5 ms: 1.16x faster                                            |
| genshi_xml               | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                            |
| json_loads               | 30.3 us                                                      | 26.9 us: 1.13x faster                                            |
| regex_v8                 | 27.2 ms                                                      | 24.5 ms: 1.11x faster                                            |
| json                     | 5.86 ms                                                      | 5.43 ms: 1.08x faster                                            |
| sqlite_synth             | 2.99 us                                                      | 2.78 us: 1.08x faster                                            |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                             |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.75 ms: 1.07x faster                                            |
| regex_dna                | 261 ms                                                       | 244 ms: 1.07x faster                                             |
| meteor_contest           | 138 ms                                                       | 132 ms: 1.05x faster                                             |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                             |
| async_generators         | 421 ms                                                       | 428 ms: 1.02x slower                                             |
| regex_effbot             | 3.09 ms                                                      | 3.14 ms: 1.02x slower                                            |
| telco                    | 7.23 ms                                                      | 7.63 ms: 1.06x slower                                            |
| python_startup_no_site   | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                            |
| coverage                 | 63.3 ms                                                      | 82.0 ms: 1.30x slower                                            |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.68 ms: 1.52x slower                                            |
| gc_traversal             | 3.42 ms                                                      | 6.29 ms: 1.84x slower                                            |
| bench_mp_pool            | 6.37 ms                                                      | 1.74 sec: 273.37x slower                                         |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                     |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250211-3.14.0a5-3ae9101-JIT/bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.331x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.29x