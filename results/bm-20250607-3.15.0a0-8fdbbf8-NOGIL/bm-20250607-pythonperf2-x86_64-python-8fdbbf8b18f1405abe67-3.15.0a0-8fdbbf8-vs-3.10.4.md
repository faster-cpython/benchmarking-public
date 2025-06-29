# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.011x faster
- HPT reliability: 84.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 363 ms: 1.04x slower                                                        |
| docutils       | 3.41 sec                                                     | 3.24 sec: 1.05x faster                                                      |
| html5lib       | 94.6 ms                                                      | 76.6 ms: 1.24x faster                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 641 ms: 2.50x faster                                                        |
| async_tree_none         | 692 ms                                                       | 297 ms: 2.33x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 357 ms: 2.30x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 656 ms: 1.43x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 81.2 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| nbody          | 134 ms                                                       | 144 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 178 ms: 1.07x faster                                                        |
| regex_dna      | 261 ms                                                       | 249 ms: 1.05x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.44 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 296 us: 1.06x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.77 sec: 1.05x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 450 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 110 ms: 1.01x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 168 ms: 1.05x slower                                                        |
| json_dumps           | 14.5 ms                                                      | 15.6 ms: 1.07x slower                                                       |
| json_loads           | 30.3 us                                                      | 36.0 us: 1.19x slower                                                       |
| xml_etree_process    | 75.9 ms                                                      | 90.2 ms: 1.19x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 39.0 us: 1.32x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 127 ms: 1.37x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 6.39 us: 1.38x slower                                                       |
| pickle_list          | 4.12 us                                                      | 6.16 us: 1.50x slower                                                       |
| pickle               | 9.89 us                                                      | 15.7 us: 1.58x slower                                                       |
| unpickle             | 13.5 us                                                      | 21.8 us: 1.62x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 12.7 ms: 1.73x slower                                                       |
| python_startup         | 11.5 ms                                                      | 21.3 ms: 1.85x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.79x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 52.5 ms: 1.05x slower                                                       |
| genshi_text     | 31.4 ms                                                      | 36.9 ms: 1.17x slower                                                       |
| genshi_xml      | 63.3 ms                                                      | 78.1 ms: 1.23x slower                                                       |
| mako            | 14.7 ms                                                      | 20.0 ms: 1.36x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.20x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 641 ms: 2.50x faster                                                        |
| async_tree_none          | 692 ms                                                       | 297 ms: 2.33x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 357 ms: 2.30x faster                                                        |
| typing_runtime_protocols | 537 us                                                       | 258 us: 2.08x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 422 ms: 1.85x faster                                                        |
| deltablue                | 7.50 ms                                                      | 4.07 ms: 1.84x faster                                                       |
| go                       | 262 ms                                                       | 153 ms: 1.71x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.83 sec: 1.64x faster                                                      |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.90 sec: 1.63x faster                                                      |
| generators               | 57.3 ms                                                      | 36.3 ms: 1.58x faster                                                       |
| pylint                   | 566 ms                                                       | 392 ms: 1.44x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 656 ms: 1.43x faster                                                        |
| pyflate                  | 733 ms                                                       | 534 ms: 1.37x faster                                                        |
| float                    | 111 ms                                                       | 81.2 ms: 1.37x faster                                                       |
| chaos                    | 109 ms                                                       | 83.2 ms: 1.30x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 7.54 ms: 1.25x faster                                                       |
| raytrace                 | 489 ms                                                       | 392 ms: 1.25x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 76.6 ms: 1.24x faster                                                       |
| deepcopy                 | 468 us                                                       | 384 us: 1.22x faster                                                        |
| coroutines               | 30.3 ms                                                      | 24.9 ms: 1.22x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.38 sec: 1.21x faster                                                      |
| dulwich_log              | 81.1 ms                                                      | 67.7 ms: 1.20x faster                                                       |
| scimark_sor              | 180 ms                                                       | 151 ms: 1.19x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 42.1 us: 1.18x faster                                                       |
| richards_super           | 90.6 ms                                                      | 77.8 ms: 1.17x faster                                                       |
| richards                 | 75.1 ms                                                      | 65.8 ms: 1.14x faster                                                       |
| comprehensions           | 26.7 us                                                      | 23.5 us: 1.14x faster                                                       |
| gc_traversal             | 3.42 ms                                                      | 3.01 ms: 1.13x faster                                                       |
| scimark_lu               | 167 ms                                                       | 150 ms: 1.11x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| regex_compile            | 190 ms                                                       | 178 ms: 1.07x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 56.3 ns: 1.06x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 296 us: 1.06x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.24 sec: 1.05x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.77 sec: 1.05x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 20.3 ms: 1.05x faster                                                       |
| regex_dna                | 261 ms                                                       | 249 ms: 1.05x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 105 ms: 1.03x faster                                                        |
| logging_simple           | 8.88 us                                                      | 8.67 us: 1.02x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 27.7 ms: 1.02x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 450 us: 1.01x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 110 ms: 1.01x faster                                                        |
| sympy_sum                | 193 ms                                                       | 198 ms: 1.03x slower                                                        |
| 2to3                     | 350 ms                                                       | 363 ms: 1.04x slower                                                        |
| thrift                   | 1.18 ms                                                      | 1.23 ms: 1.04x slower                                                       |
| sqlite_synth             | 2.99 us                                                      | 3.12 us: 1.04x slower                                                       |
| spectral_norm            | 139 ms                                                       | 145 ms: 1.05x slower                                                        |
| django_template          | 50.2 ms                                                      | 52.5 ms: 1.05x slower                                                       |
| xml_etree_parse          | 160 ms                                                       | 168 ms: 1.05x slower                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 4.26 us: 1.06x slower                                                       |
| nbody                    | 134 ms                                                       | 144 ms: 1.07x slower                                                        |
| json_dumps               | 14.5 ms                                                      | 15.6 ms: 1.07x slower                                                       |
| sympy_str                | 360 ms                                                       | 388 ms: 1.08x slower                                                        |
| nqueens                  | 115 ms                                                       | 125 ms: 1.09x slower                                                        |
| sympy_expand             | 600 ms                                                       | 668 ms: 1.11x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.44 ms: 1.11x slower                                                       |
| meteor_contest           | 138 ms                                                       | 159 ms: 1.15x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.03 ms: 1.15x slower                                                       |
| json                     | 5.86 ms                                                      | 6.80 ms: 1.16x slower                                                       |
| genshi_text              | 31.4 ms                                                      | 36.9 ms: 1.17x slower                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 1.24 sec: 1.18x slower                                                      |
| pprint_pformat           | 2.15 sec                                                     | 2.54 sec: 1.18x slower                                                      |
| fannkuch                 | 483 ms                                                       | 571 ms: 1.18x slower                                                        |
| json_loads               | 30.3 us                                                      | 36.0 us: 1.19x slower                                                       |
| xml_etree_process        | 75.9 ms                                                      | 90.2 ms: 1.19x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 78.1 ms: 1.23x slower                                                       |
| async_generators         | 421 ms                                                       | 540 ms: 1.28x slower                                                        |
| scimark_fft              | 361 ms                                                       | 469 ms: 1.30x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.50 ms: 1.31x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 39.0 us: 1.32x slower                                                       |
| mako                     | 14.7 ms                                                      | 20.0 ms: 1.36x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 127 ms: 1.37x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 6.39 us: 1.38x slower                                                       |
| pickle_list              | 4.12 us                                                      | 6.16 us: 1.50x slower                                                       |
| pickle                   | 9.89 us                                                      | 15.7 us: 1.58x slower                                                       |
| unpickle                 | 13.5 us                                                      | 21.8 us: 1.62x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 8.21 ms: 1.62x slower                                                       |
| telco                    | 7.23 ms                                                      | 12.2 ms: 1.69x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 12.7 ms: 1.73x slower                                                       |
| python_startup           | 11.5 ms                                                      | 21.3 ms: 1.85x slower                                                       |
| coverage                 | 63.3 ms                                                      | 139 ms: 2.20x slower                                                        |
| logging_silent           | 167 ns                                                       | 793 ns: 4.74x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 61.5 ms: 9.65x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (2): crypto_pyaes, logging_format
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.011x faster

# HPT report

- Reliability score: 84.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.67x