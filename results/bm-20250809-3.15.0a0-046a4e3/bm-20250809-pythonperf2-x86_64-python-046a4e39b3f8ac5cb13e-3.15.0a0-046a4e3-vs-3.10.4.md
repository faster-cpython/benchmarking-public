# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-x86_64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.329x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.1 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 620 ms: 2.58x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 327 ms: 2.51x faster                                                        |
| async_tree_none         | 692 ms                                                       | 279 ms: 2.48x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 67.9 ms: 1.64x faster                                                       |
| nbody          | 134 ms                                                       | 91.8 ms: 1.46x faster                                                       |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| regex_dna      | 261 ms                                                       | 224 ms: 1.17x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.5 ms: 1.16x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 204 us: 1.53x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.99 sec: 1.46x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.2 ms: 1.43x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 327 us: 1.39x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 97.0 ms: 1.14x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                                       |
| unpickle             | 13.5 us                                                      | 14.6 us: 1.09x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.12 us: 1.10x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.6 us: 1.10x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.98 us: 1.21x slower                                                       |
| pickle               | 9.89 us                                                      | 12.1 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                       |
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.4 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 166 us: 3.24x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 620 ms: 2.58x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 327 ms: 2.51x faster                                                        |
| async_tree_none          | 692 ms                                                       | 279 ms: 2.48x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.15 ms: 2.38x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.36x faster                                                      |
| go                       | 262 ms                                                       | 119 ms: 2.20x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                                        |
| generators               | 57.3 ms                                                      | 27.9 ms: 2.06x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| chaos                    | 109 ms                                                       | 58.8 ms: 1.85x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 27.2 us: 1.83x faster                                                       |
| logging_silent           | 167 ns                                                       | 91.7 ns: 1.82x faster                                                       |
| pyflate                  | 733 ms                                                       | 406 ms: 1.81x faster                                                        |
| richards_super           | 90.6 ms                                                      | 50.7 ms: 1.79x faster                                                       |
| raytrace                 | 489 ms                                                       | 274 ms: 1.79x faster                                                        |
| scimark_lu               | 167 ms                                                       | 94.0 ms: 1.77x faster                                                       |
| pylint                   | 566 ms                                                       | 320 ms: 1.77x faster                                                        |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.75x faster                                                        |
| deepcopy                 | 468 us                                                       | 274 us: 1.71x faster                                                        |
| richards                 | 75.1 ms                                                      | 44.5 ms: 1.69x faster                                                       |
| comprehensions           | 26.7 us                                                      | 16.1 us: 1.66x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 64.8 ms: 1.66x faster                                                       |
| float                    | 111 ms                                                       | 67.9 ms: 1.64x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 5.79 ms: 1.63x faster                                                       |
| spectral_norm            | 139 ms                                                       | 86.5 ms: 1.61x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 75.6 ms: 1.58x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 204 us: 1.53x faster                                                        |
| logging_simple           | 8.88 us                                                      | 5.98 us: 1.48x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.54 us: 1.47x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.99 sec: 1.46x faster                                                      |
| nbody                    | 134 ms                                                       | 91.8 ms: 1.46x faster                                                       |
| regex_compile            | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| django_template          | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 66.1 ms: 1.43x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.2 ms: 1.43x faster                                                       |
| unpack_sequence          | 59.9 ns                                                      | 42.1 ns: 1.42x faster                                                       |
| thrift                   | 1.18 ms                                                      | 833 us: 1.41x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.54 sec: 1.39x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 327 us: 1.39x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 756 ms: 1.39x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 59.4 ms: 1.36x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.34x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 3.00 us: 1.34x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                                       |
| fannkuch                 | 483 ms                                                       | 367 ms: 1.31x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.6 ms: 1.29x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 21.9 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                        |
| sympy_str                | 360 ms                                                       | 285 ms: 1.26x faster                                                        |
| nqueens                  | 115 ms                                                       | 92.2 ms: 1.25x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.24x faster                                                        |
| sympy_expand             | 600 ms                                                       | 489 ms: 1.23x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 53.4 ms: 1.19x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 973 us: 1.17x faster                                                        |
| regex_dna                | 261 ms                                                       | 224 ms: 1.17x faster                                                        |
| scimark_fft              | 361 ms                                                       | 311 ms: 1.16x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 23.5 ms: 1.16x faster                                                       |
| meteor_contest           | 138 ms                                                       | 120 ms: 1.16x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.0 ms: 1.14x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| json                     | 5.86 ms                                                      | 5.57 ms: 1.05x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.87 us: 1.04x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.92 ms: 1.03x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.02x faster                                                        |
| unpickle                 | 13.5 us                                                      | 14.6 us: 1.09x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.12 us: 1.10x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.6 us: 1.10x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.98 us: 1.21x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.1 us: 1.23x slower                                                       |
| coverage                 | 63.3 ms                                                      | 83.6 ms: 1.32x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.64x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.74 ms: 1.97x slower                                                       |
| telco                    | 7.23 ms                                                      | 159 ms: 22.04x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.27 sec: 199.55x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.329x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.38x