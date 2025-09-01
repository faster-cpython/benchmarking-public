# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: linux-x86_64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.335x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                      |
| html5lib       | 94.6 ms                                                      | 67.3 ms: 1.41x faster                                                       |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 614 ms: 2.60x faster                                                        |
| async_tree_none         | 692 ms                                                       | 268 ms: 2.58x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 325 ms: 2.52x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 498 ms: 1.88x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 68.5 ms: 1.62x faster                                                       |
| nbody          | 134 ms                                                       | 93.2 ms: 1.44x faster                                                       |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.4 ms: 1.16x faster                                                       |
| regex_dna      | 261 ms                                                       | 226 ms: 1.16x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 206 us: 1.52x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.99 sec: 1.46x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 57.5 ms: 1.32x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 96.8 ms: 1.14x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.97 us: 1.07x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 33.7 us: 1.14x slower                                                       |
| pickle               | 9.89 us                                                      | 12.1 us: 1.23x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.07 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 34.7 ms: 1.45x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 22.7 ms: 1.39x faster                                                       |
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 52.9 ms: 1.20x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.15x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 614 ms: 2.60x faster                                                        |
| async_tree_none          | 692 ms                                                       | 268 ms: 2.58x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 325 ms: 2.52x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.16 ms: 2.37x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.36x faster                                                      |
| go                       | 262 ms                                                       | 117 ms: 2.24x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 368 ms: 2.12x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| generators               | 57.3 ms                                                      | 29.9 ms: 1.92x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 498 ms: 1.88x faster                                                        |
| chaos                    | 109 ms                                                       | 58.1 ms: 1.87x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 59.6 ms: 1.80x faster                                                       |
| pyflate                  | 733 ms                                                       | 406 ms: 1.80x faster                                                        |
| logging_silent           | 167 ns                                                       | 92.8 ns: 1.80x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 27.7 us: 1.80x faster                                                       |
| richards_super           | 90.6 ms                                                      | 50.6 ms: 1.79x faster                                                       |
| pylint                   | 566 ms                                                       | 318 ms: 1.78x faster                                                        |
| scimark_lu               | 167 ms                                                       | 93.7 ms: 1.78x faster                                                       |
| scimark_sor              | 180 ms                                                       | 101 ms: 1.78x faster                                                        |
| raytrace                 | 489 ms                                                       | 276 ms: 1.77x faster                                                        |
| richards                 | 75.1 ms                                                      | 44.1 ms: 1.70x faster                                                       |
| deepcopy                 | 468 us                                                       | 276 us: 1.70x faster                                                        |
| comprehensions           | 26.7 us                                                      | 16.1 us: 1.66x faster                                                       |
| float                    | 111 ms                                                       | 68.5 ms: 1.62x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 5.84 ms: 1.61x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 74.8 ms: 1.59x faster                                                       |
| spectral_norm            | 139 ms                                                       | 87.4 ms: 1.59x faster                                                       |
| logging_simple           | 8.88 us                                                      | 5.84 us: 1.52x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 206 us: 1.52x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.36 us: 1.52x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.99 sec: 1.46x faster                                                      |
| django_template          | 50.2 ms                                                      | 34.7 ms: 1.45x faster                                                       |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| nbody                    | 134 ms                                                       | 93.2 ms: 1.44x faster                                                       |
| thrift                   | 1.18 ms                                                      | 820 us: 1.43x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 67.3 ms: 1.41x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 43.1 ns: 1.39x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 22.7 ms: 1.39x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 58.5 ms: 1.39x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.38x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.38x faster                                                      |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 773 ms: 1.36x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.98 us: 1.35x faster                                                       |
| fannkuch                 | 483 ms                                                       | 361 ms: 1.34x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 57.5 ms: 1.32x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 21.8 ms: 1.29x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.6 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.29x faster                                                        |
| sympy_str                | 360 ms                                                       | 283 ms: 1.27x faster                                                        |
| nqueens                  | 115 ms                                                       | 92.1 ms: 1.25x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| sympy_expand             | 600 ms                                                       | 486 ms: 1.24x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.21x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 52.9 ms: 1.20x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 959 us: 1.19x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                      |
| scimark_fft              | 361 ms                                                       | 305 ms: 1.18x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 23.4 ms: 1.16x faster                                                       |
| regex_dna                | 261 ms                                                       | 226 ms: 1.16x faster                                                        |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.15x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 96.8 ms: 1.14x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 82.5 ms: 1.12x faster                                                       |
| json                     | 5.86 ms                                                      | 5.36 ms: 1.09x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.92 ms: 1.03x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.97 us: 1.07x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 33.7 us: 1.14x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.1 us: 1.23x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.07 us: 1.23x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.7 ms: 1.31x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.93 ms: 1.66x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.43 ms: 1.88x slower                                                       |
| telco                    | 7.23 ms                                                      | 157 ms: 21.77x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.50 sec: 234.98x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                                |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.335x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.38x