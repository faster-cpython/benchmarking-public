# Results vs. 3.10.4

- fork: python
- ref: b266fbc9ecd25d08ab57
- machine: linux-x86_64
- commit hash: b266fbc
- commit date: 2025-08-04
- overall geometric mean: 1.332x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                       |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 625 ms: 2.56x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 326 ms: 2.51x faster                                                        |
| async_tree_none         | 692 ms                                                       | 280 ms: 2.47x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 64.2 ms: 1.73x faster                                                       |
| nbody          | 134 ms                                                       | 97.9 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| regex_dna      | 261 ms                                                       | 222 ms: 1.18x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.5 ms: 1.15x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.71 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 194 us: 1.61x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.93 sec: 1.51x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 334 us: 1.36x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 79.6 ms: 1.16x faster                                                       |
| json_loads           | 30.3 us                                                      | 26.7 us: 1.14x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 98.0 ms: 1.13x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                                       |
| django_template | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.2 ms: 1.36x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.7 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.13x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.87 ms: 2.61x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 625 ms: 2.56x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 326 ms: 2.51x faster                                                        |
| async_tree_none          | 692 ms                                                       | 280 ms: 2.47x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.32 sec: 2.28x faster                                                      |
| richards_super           | 90.6 ms                                                      | 40.7 ms: 2.23x faster                                                       |
| richards                 | 75.1 ms                                                      | 34.6 ms: 2.17x faster                                                       |
| go                       | 262 ms                                                       | 127 ms: 2.06x faster                                                        |
| generators               | 57.3 ms                                                      | 30.4 ms: 1.88x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| logging_silent           | 167 ns                                                       | 91.7 ns: 1.82x faster                                                       |
| chaos                    | 109 ms                                                       | 59.5 ms: 1.82x faster                                                       |
| pyflate                  | 733 ms                                                       | 407 ms: 1.80x faster                                                        |
| scimark_sor              | 180 ms                                                       | 101 ms: 1.78x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 27.9 us: 1.78x faster                                                       |
| scimark_lu               | 167 ms                                                       | 95.0 ms: 1.76x faster                                                       |
| pylint                   | 566 ms                                                       | 325 ms: 1.74x faster                                                        |
| raytrace                 | 489 ms                                                       | 283 ms: 1.73x faster                                                        |
| spectral_norm            | 139 ms                                                       | 80.4 ms: 1.73x faster                                                       |
| float                    | 111 ms                                                       | 64.2 ms: 1.73x faster                                                       |
| deepcopy                 | 468 us                                                       | 275 us: 1.70x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 64.1 ms: 1.67x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 194 us: 1.61x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 77.4 ms: 1.54x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.16 ms: 1.53x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.93 sec: 1.51x faster                                                      |
| logging_simple           | 8.88 us                                                      | 6.00 us: 1.48x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.62 us: 1.46x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.49 sec: 1.45x faster                                                      |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 738 ms: 1.42x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                       |
| thrift                   | 1.18 ms                                                      | 841 us: 1.40x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 59.1 ms: 1.37x faster                                                       |
| nbody                    | 134 ms                                                       | 97.9 ms: 1.37x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 334 us: 1.36x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.2 ms: 1.36x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.5 ms: 1.35x faster                                                       |
| fannkuch                 | 483 ms                                                       | 362 ms: 1.33x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.5 ms: 1.25x faster                                                       |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                        |
| nqueens                  | 115 ms                                                       | 93.3 ms: 1.23x faster                                                       |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                        |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                                        |
| regex_dna                | 261 ms                                                       | 222 ms: 1.18x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.17x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 79.6 ms: 1.16x faster                                                       |
| meteor_contest           | 138 ms                                                       | 119 ms: 1.16x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 54.7 ms: 1.16x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.5 ms: 1.15x faster                                                       |
| json_loads               | 30.3 us                                                      | 26.7 us: 1.14x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 98.0 ms: 1.13x faster                                                       |
| json                     | 5.86 ms                                                      | 5.47 ms: 1.07x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 380 ms: 1.03x faster                                                        |
| async_generators         | 421 ms                                                       | 458 ms: 1.09x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.71 ms: 1.20x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                       |
| coverage                 | 63.3 ms                                                      | 78.0 ms: 1.23x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.89 ms: 1.64x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.47 ms: 1.89x slower                                                       |
| telco                    | 7.23 ms                                                      | 162 ms: 22.43x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                |

Benchmark hidden because not significant (1): scimark_sparse_mat_mult
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250804-3.15.0a0-b266fbc-JIT/bm-20250804-pythonperf2-x86_64-python-b266fbc9ecd25d08ab57-3.15.0a0-b266fbc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.332x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.40x