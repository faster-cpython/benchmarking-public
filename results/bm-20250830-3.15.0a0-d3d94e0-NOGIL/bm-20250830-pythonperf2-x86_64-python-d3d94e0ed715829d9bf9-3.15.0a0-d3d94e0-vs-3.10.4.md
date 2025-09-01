# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: linux-x86_64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.196x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.65x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 318 ms: 1.10x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.3 ms: 1.33x faster                                                       |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 562 ms: 2.84x faster                                                        |
| async_tree_none         | 692 ms                                                       | 264 ms: 2.62x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 321 ms: 2.55x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 495 ms: 1.89x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.45x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 74.1 ms: 1.50x faster                                                       |
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                        |
| nbody          | 134 ms                                                       | 125 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 153 ms: 1.24x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                       |
| regex_dna      | 261 ms                                                       | 231 ms: 1.13x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                      |
| unpickle_pure_python | 312 us                                                       | 238 us: 1.31x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 88.2 ms: 1.25x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 374 us: 1.22x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 69.9 ms: 1.09x faster                                                       |
| json_loads           | 30.3 us                                                      | 29.0 us: 1.05x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 96.6 ms: 1.05x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 33.3 us: 1.13x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.52 us: 1.19x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.01 us: 1.22x slower                                                       |
| unpickle             | 13.5 us                                                      | 16.7 us: 1.24x slower                                                       |
| pickle               | 9.89 us                                                      | 12.5 us: 1.26x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.7 ms: 1.60x slower                                                       |
| python_startup         | 11.5 ms                                                      | 19.1 ms: 1.66x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.63x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 43.6 ms: 1.15x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 30.7 ms: 1.02x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 66.6 ms: 1.05x slower                                                       |
| mako            | 14.7 ms                                                      | 17.5 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 562 ms: 2.84x faster                                                        |
| async_tree_none          | 692 ms                                                       | 264 ms: 2.62x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 321 ms: 2.55x faster                                                        |
| typing_runtime_protocols | 537 us                                                       | 212 us: 2.53x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.45 sec: 2.08x faster                                                      |
| deltablue                | 7.50 ms                                                      | 3.63 ms: 2.07x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 382 ms: 2.04x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 495 ms: 1.89x faster                                                        |
| go                       | 262 ms                                                       | 139 ms: 1.89x faster                                                        |
| generators               | 57.3 ms                                                      | 30.5 ms: 1.88x faster                                                       |
| logging_silent           | 167 ns                                                       | 97.3 ns: 1.72x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.89 sec: 1.64x faster                                                      |
| pylint                   | 566 ms                                                       | 345 ms: 1.64x faster                                                        |
| chaos                    | 109 ms                                                       | 67.2 ms: 1.62x faster                                                       |
| pyflate                  | 733 ms                                                       | 472 ms: 1.55x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.22 ms: 1.54x faster                                                       |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.53x faster                                                        |
| float                    | 111 ms                                                       | 74.1 ms: 1.50x faster                                                       |
| raytrace                 | 489 ms                                                       | 331 ms: 1.48x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.1 us: 1.47x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.49 ms: 1.45x faster                                                       |
| scimark_lu               | 167 ms                                                       | 116 ms: 1.44x faster                                                        |
| deepcopy                 | 468 us                                                       | 326 us: 1.44x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 35.1 us: 1.42x faster                                                       |
| richards_super           | 90.6 ms                                                      | 64.1 ms: 1.41x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                      |
| scimark_monte_carlo      | 107 ms                                                       | 79.4 ms: 1.35x faster                                                       |
| richards                 | 75.1 ms                                                      | 55.5 ms: 1.35x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.5 ms: 1.35x faster                                                       |
| spectral_norm            | 139 ms                                                       | 104 ms: 1.34x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.68 us: 1.33x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 71.3 ms: 1.33x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 61.3 ms: 1.32x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                      |
| unpickle_pure_python     | 312 us                                                       | 238 us: 1.31x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 92.6 ms: 1.29x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.55 us: 1.28x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 17.0 ms: 1.26x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 88.2 ms: 1.25x faster                                                       |
| regex_compile            | 190 ms                                                       | 153 ms: 1.24x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 374 us: 1.22x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 877 ms: 1.20x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.81 sec: 1.19x faster                                                      |
| thrift                   | 1.18 ms                                                      | 991 us: 1.19x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 3.47 us: 1.15x faster                                                       |
| django_template          | 50.2 ms                                                      | 43.6 ms: 1.15x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.59 us: 1.15x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                       |
| regex_dna                | 261 ms                                                       | 231 ms: 1.13x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 24.9 ms: 1.13x faster                                                       |
| sympy_sum                | 193 ms                                                       | 171 ms: 1.13x faster                                                        |
| sympy_str                | 360 ms                                                       | 326 ms: 1.10x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 54.3 ns: 1.10x faster                                                       |
| 2to3                     | 350 ms                                                       | 318 ms: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 69.9 ms: 1.09x faster                                                       |
| nqueens                  | 115 ms                                                       | 106 ms: 1.08x faster                                                        |
| sympy_expand             | 600 ms                                                       | 555 ms: 1.08x faster                                                        |
| nbody                    | 134 ms                                                       | 125 ms: 1.07x faster                                                        |
| json                     | 5.86 ms                                                      | 5.53 ms: 1.06x faster                                                       |
| fannkuch                 | 483 ms                                                       | 458 ms: 1.05x faster                                                        |
| json_loads               | 30.3 us                                                      | 29.0 us: 1.05x faster                                                       |
| scimark_fft              | 361 ms                                                       | 352 ms: 1.03x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 30.7 ms: 1.02x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 96.6 ms: 1.05x slower                                                       |
| meteor_contest           | 138 ms                                                       | 145 ms: 1.05x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 66.6 ms: 1.05x slower                                                       |
| async_generators         | 421 ms                                                       | 470 ms: 1.12x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.98 ms: 1.13x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 33.3 us: 1.13x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.52 us: 1.19x slower                                                       |
| mako                     | 14.7 ms                                                      | 17.5 ms: 1.19x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.11 ms: 1.20x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.01 us: 1.22x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.39 ms: 1.22x slower                                                       |
| unpickle                 | 13.5 us                                                      | 16.7 us: 1.24x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.5 us: 1.26x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.7 ms: 1.60x slower                                                       |
| python_startup           | 11.5 ms                                                      | 19.1 ms: 1.66x slower                                                       |
| coverage                 | 63.3 ms                                                      | 116 ms: 1.83x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 58.0 ms: 9.11x slower                                                       |
| telco                    | 7.23 ms                                                      | 174 ms: 24.00x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.15x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250830-3.15.0a0-d3d94e0-NOGIL/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.196x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.65x