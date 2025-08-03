# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-x86_64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.196x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.65x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 316 ms: 1.11x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 69.9 ms: 1.35x faster                                                       |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 558 ms: 2.86x faster                                                        |
| async_tree_none         | 692 ms                                                       | 263 ms: 2.63x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 320 ms: 2.56x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 495 ms: 1.89x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.46x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.4 ms: 1.56x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| nbody          | 134 ms                                                       | 127 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 154 ms: 1.24x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.3 ms: 1.16x faster                                                       |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.55 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 237 us: 1.32x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.30 sec: 1.27x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 87.5 ms: 1.26x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 362 us: 1.26x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 12.0 ms: 1.22x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                        |
| json_loads           | 30.3 us                                                      | 27.9 us: 1.09x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 69.9 ms: 1.09x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 99.6 ms: 1.08x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 33.8 us: 1.15x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.51 us: 1.19x slower                                                       |
| unpickle             | 13.5 us                                                      | 16.5 us: 1.22x slower                                                       |
| pickle               | 9.89 us                                                      | 12.2 us: 1.23x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.10 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.7 ms: 1.60x slower                                                       |
| python_startup         | 11.5 ms                                                      | 19.1 ms: 1.66x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.63x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 43.0 ms: 1.17x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 30.3 ms: 1.04x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 65.8 ms: 1.04x slower                                                       |
| mako            | 14.7 ms                                                      | 17.5 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 558 ms: 2.86x faster                                                        |
| async_tree_none          | 692 ms                                                       | 263 ms: 2.63x faster                                                        |
| typing_runtime_protocols | 537 us                                                       | 206 us: 2.60x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 320 ms: 2.56x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.45 sec: 2.07x faster                                                      |
| asyncio_tcp              | 779 ms                                                       | 381 ms: 2.05x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.70 ms: 2.03x faster                                                       |
| generators               | 57.3 ms                                                      | 29.9 ms: 1.91x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 495 ms: 1.89x faster                                                        |
| go                       | 262 ms                                                       | 139 ms: 1.89x faster                                                        |
| logging_silent           | 167 ns                                                       | 97.8 ns: 1.71x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.87 sec: 1.66x faster                                                      |
| pylint                   | 566 ms                                                       | 345 ms: 1.64x faster                                                        |
| chaos                    | 109 ms                                                       | 66.4 ms: 1.63x faster                                                       |
| float                    | 111 ms                                                       | 71.4 ms: 1.56x faster                                                       |
| pyflate                  | 733 ms                                                       | 476 ms: 1.54x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.22 ms: 1.54x faster                                                       |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.53x faster                                                        |
| raytrace                 | 489 ms                                                       | 323 ms: 1.51x faster                                                        |
| deepcopy                 | 468 us                                                       | 315 us: 1.49x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.2 us: 1.47x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 34.2 us: 1.46x faster                                                       |
| scimark_lu               | 167 ms                                                       | 116 ms: 1.44x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.56 ms: 1.44x faster                                                       |
| richards_super           | 90.6 ms                                                      | 64.0 ms: 1.42x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 69.9 ms: 1.35x faster                                                       |
| richards                 | 75.1 ms                                                      | 55.6 ms: 1.35x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 79.7 ms: 1.35x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                       |
| spectral_norm            | 139 ms                                                       | 105 ms: 1.32x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 237 us: 1.32x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                                      |
| logging_simple           | 8.88 us                                                      | 6.79 us: 1.31x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 62.1 ms: 1.31x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.8 ms: 1.27x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 93.8 ms: 1.27x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.30 sec: 1.27x faster                                                      |
| logging_format           | 9.64 us                                                      | 7.63 us: 1.26x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 87.5 ms: 1.26x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 362 us: 1.26x faster                                                        |
| regex_compile            | 190 ms                                                       | 154 ms: 1.24x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 12.0 ms: 1.22x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 878 ms: 1.20x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.82 sec: 1.18x faster                                                      |
| thrift                   | 1.18 ms                                                      | 993 us: 1.18x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                        |
| django_template          | 50.2 ms                                                      | 43.0 ms: 1.17x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.3 ms: 1.16x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.48 us: 1.15x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.60 us: 1.15x faster                                                       |
| sympy_sum                | 193 ms                                                       | 171 ms: 1.13x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 25.1 ms: 1.12x faster                                                       |
| regex_dna                | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| 2to3                     | 350 ms                                                       | 316 ms: 1.11x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 54.5 ns: 1.10x faster                                                       |
| sympy_str                | 360 ms                                                       | 328 ms: 1.10x faster                                                        |
| nqueens                  | 115 ms                                                       | 105 ms: 1.10x faster                                                        |
| json_loads               | 30.3 us                                                      | 27.9 us: 1.09x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 69.9 ms: 1.09x faster                                                       |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| sympy_expand             | 600 ms                                                       | 559 ms: 1.07x faster                                                        |
| nbody                    | 134 ms                                                       | 127 ms: 1.05x faster                                                        |
| json                     | 5.86 ms                                                      | 5.62 ms: 1.04x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 30.3 ms: 1.04x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 376 ms: 1.04x faster                                                        |
| scimark_fft              | 361 ms                                                       | 349 ms: 1.04x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 65.8 ms: 1.04x slower                                                       |
| meteor_contest           | 138 ms                                                       | 145 ms: 1.05x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 99.6 ms: 1.08x slower                                                       |
| async_generators         | 421 ms                                                       | 463 ms: 1.10x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 33.8 us: 1.15x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.55 ms: 1.15x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.03 ms: 1.15x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.95 ms: 1.17x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.51 us: 1.19x slower                                                       |
| mako                     | 14.7 ms                                                      | 17.5 ms: 1.19x slower                                                       |
| unpickle                 | 13.5 us                                                      | 16.5 us: 1.22x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.40 ms: 1.23x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.2 us: 1.23x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.10 us: 1.24x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.7 ms: 1.60x slower                                                       |
| python_startup           | 11.5 ms                                                      | 19.1 ms: 1.66x slower                                                       |
| coverage                 | 63.3 ms                                                      | 117 ms: 1.85x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 57.2 ms: 8.97x slower                                                       |
| telco                    | 7.23 ms                                                      | 175 ms: 24.21x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.15x faster                                                                |

Benchmark hidden because not significant (1): fannkuch
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.196x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.65x