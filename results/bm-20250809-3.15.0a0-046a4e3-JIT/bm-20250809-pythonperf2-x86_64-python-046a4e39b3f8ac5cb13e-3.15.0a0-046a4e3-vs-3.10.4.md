# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-x86_64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.335x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                       |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 624 ms: 2.56x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 326 ms: 2.52x faster                                                        |
| async_tree_none         | 692 ms                                                       | 280 ms: 2.47x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 499 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 65.4 ms: 1.70x faster                                                       |
| nbody          | 134 ms                                                       | 101 ms: 1.32x faster                                                        |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| regex_dna      | 261 ms                                                       | 222 ms: 1.18x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 24.4 ms: 1.11x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.84 ms: 1.24x slower                                                       |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 192 us: 1.62x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.91 sec: 1.52x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.2 ms: 1.43x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 55.1 ms: 1.38x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 332 us: 1.37x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 79.4 ms: 1.16x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 97.2 ms: 1.14x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 5.06 us: 1.09x slower                                                       |
| unpickle             | 13.5 us                                                      | 14.7 us: 1.09x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 34.6 us: 1.17x slower                                                       |
| pickle               | 9.89 us                                                      | 12.2 us: 1.23x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.18 us: 1.26x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.86 ms: 1.49x faster                                                       |
| django_template | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.2 ms: 1.35x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.1 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.17x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.84 ms: 2.64x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 624 ms: 2.56x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 326 ms: 2.52x faster                                                        |
| async_tree_none          | 692 ms                                                       | 280 ms: 2.47x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                      |
| richards_super           | 90.6 ms                                                      | 40.0 ms: 2.26x faster                                                       |
| richards                 | 75.1 ms                                                      | 33.9 ms: 2.21x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 369 ms: 2.11x faster                                                        |
| go                       | 262 ms                                                       | 126 ms: 2.08x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 499 ms: 1.87x faster                                                        |
| chaos                    | 109 ms                                                       | 59.4 ms: 1.83x faster                                                       |
| logging_silent           | 167 ns                                                       | 91.8 ns: 1.82x faster                                                       |
| generators               | 57.3 ms                                                      | 31.5 ms: 1.82x faster                                                       |
| pyflate                  | 733 ms                                                       | 405 ms: 1.81x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 27.5 us: 1.81x faster                                                       |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.77x faster                                                        |
| spectral_norm            | 139 ms                                                       | 78.6 ms: 1.77x faster                                                       |
| pylint                   | 566 ms                                                       | 322 ms: 1.76x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.1 ms: 1.75x faster                                                       |
| raytrace                 | 489 ms                                                       | 281 ms: 1.74x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 62.8 ms: 1.71x faster                                                       |
| float                    | 111 ms                                                       | 65.4 ms: 1.70x faster                                                       |
| deepcopy                 | 468 us                                                       | 279 us: 1.68x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 192 us: 1.62x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.17 ms: 1.53x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.91 sec: 1.52x faster                                                      |
| crypto_pyaes             | 119 ms                                                       | 78.4 ms: 1.52x faster                                                       |
| logging_simple           | 8.88 us                                                      | 5.93 us: 1.50x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.86 ms: 1.49x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.49 us: 1.49x faster                                                       |
| django_template          | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.50 sec: 1.43x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 733 ms: 1.43x faster                                                        |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.2 ms: 1.43x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                       |
| thrift                   | 1.18 ms                                                      | 836 us: 1.41x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 55.1 ms: 1.38x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 332 us: 1.37x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 59.5 ms: 1.36x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 23.2 ms: 1.35x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.99 us: 1.34x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.7 ms: 1.34x faster                                                       |
| fannkuch                 | 483 ms                                                       | 364 ms: 1.32x faster                                                        |
| nbody                    | 134 ms                                                       | 101 ms: 1.32x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                       |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                        |
| nqueens                  | 115 ms                                                       | 93.5 ms: 1.23x faster                                                       |
| unpack_sequence          | 59.9 ns                                                      | 49.0 ns: 1.22x faster                                                       |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| sympy_expand             | 600 ms                                                       | 503 ms: 1.19x faster                                                        |
| scimark_fft              | 361 ms                                                       | 306 ms: 1.18x faster                                                        |
| regex_dna                | 261 ms                                                       | 222 ms: 1.18x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 54.1 ms: 1.17x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 79.4 ms: 1.16x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 984 us: 1.16x faster                                                        |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.15x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.2 ms: 1.14x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 24.4 ms: 1.11x faster                                                       |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.99 ms: 1.02x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| async_generators         | 421 ms                                                       | 442 ms: 1.05x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.06 us: 1.09x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.7 us: 1.09x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 34.6 us: 1.17x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.20x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.2 us: 1.23x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.84 ms: 1.24x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.18 us: 1.26x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.7 ms: 1.31x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.92 ms: 1.66x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.55 ms: 1.92x slower                                                       |
| telco                    | 7.23 ms                                                      | 160 ms: 22.07x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.61 sec: 252.33x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.335x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.40x