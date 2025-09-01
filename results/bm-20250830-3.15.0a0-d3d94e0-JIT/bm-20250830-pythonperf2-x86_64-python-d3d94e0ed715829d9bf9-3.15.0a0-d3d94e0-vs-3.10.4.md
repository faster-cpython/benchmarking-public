# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: linux-x86_64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.342x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.4 ms: 1.42x faster                                                       |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 611 ms: 2.61x faster                                                        |
| async_tree_none         | 692 ms                                                       | 270 ms: 2.56x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 325 ms: 2.52x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 498 ms: 1.88x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 63.1 ms: 1.76x faster                                                       |
| nbody          | 134 ms                                                       | 104 ms: 1.29x faster                                                        |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| regex_dna      | 261 ms                                                       | 224 ms: 1.17x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.53 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 195 us: 1.60x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.90 sec: 1.54x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.1 ms: 1.45x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 326 us: 1.40x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 54.9 ms: 1.38x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 79.6 ms: 1.16x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 98.3 ms: 1.12x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 5.11 us: 1.10x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.9 us: 1.12x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.92 us: 1.20x slower                                                       |
| pickle               | 9.89 us                                                      | 12.3 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.89 ms: 1.49x faster                                                       |
| django_template | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 22.9 ms: 1.37x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.17x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.84 ms: 2.64x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 611 ms: 2.61x faster                                                        |
| async_tree_none          | 692 ms                                                       | 270 ms: 2.56x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 325 ms: 2.52x faster                                                        |
| richards_super           | 90.6 ms                                                      | 38.5 ms: 2.35x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                      |
| richards                 | 75.1 ms                                                      | 34.0 ms: 2.21x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 370 ms: 2.11x faster                                                        |
| go                       | 262 ms                                                       | 125 ms: 2.10x faster                                                        |
| generators               | 57.3 ms                                                      | 28.8 ms: 1.99x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.95x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 498 ms: 1.88x faster                                                        |
| chaos                    | 109 ms                                                       | 58.7 ms: 1.85x faster                                                       |
| pyflate                  | 733 ms                                                       | 402 ms: 1.82x faster                                                        |
| logging_silent           | 167 ns                                                       | 92.2 ns: 1.81x faster                                                       |
| spectral_norm            | 139 ms                                                       | 77.6 ms: 1.79x faster                                                       |
| scimark_lu               | 167 ms                                                       | 93.7 ms: 1.78x faster                                                       |
| float                    | 111 ms                                                       | 63.1 ms: 1.76x faster                                                       |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.76x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 28.5 us: 1.75x faster                                                       |
| pylint                   | 566 ms                                                       | 325 ms: 1.74x faster                                                        |
| raytrace                 | 489 ms                                                       | 285 ms: 1.72x faster                                                        |
| deepcopy                 | 468 us                                                       | 276 us: 1.69x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 66.6 ms: 1.61x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 195 us: 1.60x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 76.8 ms: 1.55x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.09 ms: 1.55x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.90 sec: 1.54x faster                                                      |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                       |
| logging_simple           | 8.88 us                                                      | 5.96 us: 1.49x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.89 ms: 1.49x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.52 us: 1.48x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.1 ms: 1.45x faster                                                       |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.50 sec: 1.43x faster                                                      |
| django_template          | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                       |
| thrift                   | 1.18 ms                                                      | 822 us: 1.43x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 66.4 ms: 1.42x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 741 ms: 1.42x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.20 sec: 1.40x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 326 us: 1.40x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 54.9 ms: 1.38x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 58.9 ms: 1.38x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 22.9 ms: 1.37x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.02 us: 1.33x faster                                                       |
| nbody                    | 134 ms                                                       | 104 ms: 1.29x faster                                                        |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                                       |
| fannkuch                 | 483 ms                                                       | 379 ms: 1.27x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.2 ms: 1.27x faster                                                       |
| nqueens                  | 115 ms                                                       | 91.9 ms: 1.25x faster                                                       |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                        |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                        |
| scimark_fft              | 361 ms                                                       | 298 ms: 1.21x faster                                                        |
| sympy_expand             | 600 ms                                                       | 495 ms: 1.21x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| unpack_sequence          | 59.9 ns                                                      | 50.0 ns: 1.20x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 962 us: 1.19x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                                       |
| regex_dna                | 261 ms                                                       | 224 ms: 1.17x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 79.6 ms: 1.16x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.14x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                       |
| meteor_contest           | 138 ms                                                       | 122 ms: 1.13x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 98.3 ms: 1.12x faster                                                       |
| json                     | 5.86 ms                                                      | 5.46 ms: 1.07x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.04 ms: 1.01x faster                                                       |
| async_generators         | 421 ms                                                       | 437 ms: 1.04x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.11 us: 1.10x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.9 us: 1.12x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.53 ms: 1.14x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.92 us: 1.20x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.3 us: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 81.3 ms: 1.29x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.84 ms: 1.61x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.46 ms: 1.89x slower                                                       |
| telco                    | 7.23 ms                                                      | 159 ms: 22.04x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.28 sec: 200.47x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.342x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.40x