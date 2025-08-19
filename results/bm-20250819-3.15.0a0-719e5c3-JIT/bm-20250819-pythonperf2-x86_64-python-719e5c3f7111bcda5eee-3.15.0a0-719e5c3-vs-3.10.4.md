# Results vs. 3.10.4

- fork: python
- ref: 719e5c3f7111bcda5eee
- machine: linux-x86_64
- commit hash: 719e5c3
- commit date: 2025-08-19
- overall geometric mean: 1.330x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 288 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 67.1 ms: 1.41x faster                                                       |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 617 ms: 2.59x faster                                                        |
| async_tree_none         | 692 ms                                                       | 272 ms: 2.54x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 329 ms: 2.49x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 500 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 65.8 ms: 1.69x faster                                                       |
| nbody          | 134 ms                                                       | 103 ms: 1.30x faster                                                        |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.42x faster                                                        |
| regex_dna      | 261 ms                                                       | 224 ms: 1.17x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.62 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 194 us: 1.61x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.93 sec: 1.51x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 334 us: 1.36x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.19x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 80.9 ms: 1.14x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 149 ms: 1.08x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.85 ms: 1.49x faster                                                       |
| django_template | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 55.0 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.16x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.89 ms: 2.59x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 617 ms: 2.59x faster                                                        |
| async_tree_none          | 692 ms                                                       | 272 ms: 2.54x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 329 ms: 2.49x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.28 sec: 2.35x faster                                                      |
| richards_super           | 90.6 ms                                                      | 39.4 ms: 2.30x faster                                                       |
| richards                 | 75.1 ms                                                      | 34.2 ms: 2.20x faster                                                       |
| go                       | 262 ms                                                       | 127 ms: 2.07x faster                                                        |
| generators               | 57.3 ms                                                      | 30.1 ms: 1.91x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 500 ms: 1.87x faster                                                        |
| logging_silent           | 167 ns                                                       | 91.9 ns: 1.82x faster                                                       |
| pyflate                  | 733 ms                                                       | 404 ms: 1.82x faster                                                        |
| chaos                    | 109 ms                                                       | 59.9 ms: 1.81x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.1 us: 1.77x faster                                                       |
| scimark_lu               | 167 ms                                                       | 94.1 ms: 1.77x faster                                                       |
| raytrace                 | 489 ms                                                       | 276 ms: 1.77x faster                                                        |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.75x faster                                                        |
| pylint                   | 566 ms                                                       | 325 ms: 1.74x faster                                                        |
| spectral_norm            | 139 ms                                                       | 80.9 ms: 1.72x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 63.2 ms: 1.70x faster                                                       |
| float                    | 111 ms                                                       | 65.8 ms: 1.69x faster                                                       |
| deepcopy                 | 468 us                                                       | 282 us: 1.66x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 194 us: 1.61x faster                                                        |
| logging_simple           | 8.88 us                                                      | 5.78 us: 1.54x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 77.9 ms: 1.53x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.93 sec: 1.51x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 6.25 ms: 1.51x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.42 us: 1.50x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.85 ms: 1.49x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                       |
| regex_compile            | 190 ms                                                       | 134 ms: 1.42x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 67.1 ms: 1.41x faster                                                       |
| thrift                   | 1.18 ms                                                      | 835 us: 1.41x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.53 sec: 1.40x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 753 ms: 1.39x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 59.2 ms: 1.37x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 334 us: 1.36x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 3.04 us: 1.32x faster                                                       |
| coroutines               | 30.3 ms                                                      | 23.1 ms: 1.31x faster                                                       |
| nbody                    | 134 ms                                                       | 103 ms: 1.30x faster                                                        |
| fannkuch                 | 483 ms                                                       | 380 ms: 1.27x faster                                                        |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.8 ms: 1.27x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.5 ms: 1.25x faster                                                       |
| sympy_str                | 360 ms                                                       | 293 ms: 1.23x faster                                                        |
| nqueens                  | 115 ms                                                       | 93.7 ms: 1.23x faster                                                       |
| 2to3                     | 350 ms                                                       | 288 ms: 1.22x faster                                                        |
| scimark_fft              | 361 ms                                                       | 299 ms: 1.21x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.19x faster                                                       |
| sympy_expand             | 600 ms                                                       | 505 ms: 1.19x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| regex_dna                | 261 ms                                                       | 224 ms: 1.17x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 55.0 ms: 1.15x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 80.9 ms: 1.14x faster                                                       |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| json                     | 5.86 ms                                                      | 5.40 ms: 1.09x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 149 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                       |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.02 ms: 1.01x faster                                                       |
| async_generators         | 421 ms                                                       | 447 ms: 1.06x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.62 ms: 1.17x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.20x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                       |
| coverage                 | 63.3 ms                                                      | 84.8 ms: 1.34x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.91 ms: 1.65x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.67 ms: 1.95x slower                                                       |
| telco                    | 7.23 ms                                                      | 161 ms: 22.24x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250819-3.15.0a0-719e5c3-JIT/bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.330x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.40x