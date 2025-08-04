# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3ec3d05
- commit date: 2025-08-03
- overall geometric mean: 1.332x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.23x faster                                        |
| docutils       | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                      |
| html5lib       | 94.6 ms                                                      | 67.7 ms: 1.40x faster                                       |
| Geometric mean | (ref)                                                        | 1.26x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 628 ms: 2.55x faster                                        |
| async_tree_memoization  | 819 ms                                                       | 326 ms: 2.51x faster                                        |
| async_tree_none         | 692 ms                                                       | 281 ms: 2.46x faster                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 503 ms: 1.86x faster                                        |
| Geometric mean          | (ref)                                                        | 2.33x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 111 ms                                                       | 64.6 ms: 1.72x faster                                       |
| nbody          | 134 ms                                                       | 99.1 ms: 1.35x faster                                       |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                        |
| Geometric mean | (ref)                                                        | 1.35x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                        |
| regex_v8       | 27.2 ms                                                      | 23.3 ms: 1.17x faster                                       |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                        |
| regex_effbot   | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                       |
| Geometric mean | (ref)                                                        | 1.13x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 194 us: 1.61x faster                                        |
| tomli_loads          | 2.92 sec                                                     | 1.92 sec: 1.52x faster                                      |
| pickle_pure_python   | 455 us                                                       | 332 us: 1.37x faster                                        |
| xml_etree_process    | 75.9 ms                                                      | 55.5 ms: 1.37x faster                                       |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                       |
| xml_etree_generate   | 92.3 ms                                                      | 80.5 ms: 1.15x faster                                       |
| json_loads           | 30.3 us                                                      | 26.5 us: 1.14x faster                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                        |
| xml_etree_iterparse  | 110 ms                                                       | 97.8 ms: 1.13x faster                                       |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.84 ms: 1.21x slower                                       |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.78 ms: 1.50x faster                                       |
| django_template | 50.2 ms                                                      | 35.5 ms: 1.41x faster                                       |
| genshi_text     | 31.4 ms                                                      | 22.9 ms: 1.37x faster                                       |
| genshi_xml      | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                       |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.15x faster                                        |
| deltablue                | 7.50 ms                                                      | 2.91 ms: 2.58x faster                                       |
| async_tree_io            | 1.60 sec                                                     | 628 ms: 2.55x faster                                        |
| async_tree_memoization   | 819 ms                                                       | 326 ms: 2.51x faster                                        |
| async_tree_none          | 692 ms                                                       | 281 ms: 2.46x faster                                        |
| mdp                      | 3.01 sec                                                     | 1.28 sec: 2.34x faster                                      |
| richards_super           | 90.6 ms                                                      | 41.4 ms: 2.19x faster                                       |
| richards                 | 75.1 ms                                                      | 35.4 ms: 2.12x faster                                       |
| go                       | 262 ms                                                       | 129 ms: 2.03x faster                                        |
| generators               | 57.3 ms                                                      | 29.5 ms: 1.94x faster                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 503 ms: 1.86x faster                                        |
| chaos                    | 109 ms                                                       | 59.0 ms: 1.84x faster                                       |
| pyflate                  | 733 ms                                                       | 408 ms: 1.80x faster                                        |
| logging_silent           | 167 ns                                                       | 93.7 ns: 1.79x faster                                       |
| scimark_sor              | 180 ms                                                       | 101 ms: 1.78x faster                                        |
| deepcopy_memo            | 49.8 us                                                      | 28.1 us: 1.77x faster                                       |
| scimark_lu               | 167 ms                                                       | 95.4 ms: 1.75x faster                                       |
| pylint                   | 566 ms                                                       | 324 ms: 1.75x faster                                        |
| spectral_norm            | 139 ms                                                       | 79.7 ms: 1.74x faster                                       |
| float                    | 111 ms                                                       | 64.6 ms: 1.72x faster                                       |
| scimark_monte_carlo      | 107 ms                                                       | 62.8 ms: 1.71x faster                                       |
| raytrace                 | 489 ms                                                       | 288 ms: 1.70x faster                                        |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                        |
| unpickle_pure_python     | 312 us                                                       | 194 us: 1.61x faster                                        |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                       |
| crypto_pyaes             | 119 ms                                                       | 77.6 ms: 1.54x faster                                       |
| tomli_loads              | 2.92 sec                                                     | 1.92 sec: 1.52x faster                                      |
| hexiom                   | 9.42 ms                                                      | 6.21 ms: 1.52x faster                                       |
| mako                     | 14.7 ms                                                      | 9.78 ms: 1.50x faster                                       |
| logging_simple           | 8.88 us                                                      | 6.10 us: 1.45x faster                                       |
| logging_format           | 9.64 us                                                      | 6.69 us: 1.44x faster                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.50 sec: 1.43x faster                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 741 ms: 1.42x faster                                        |
| django_template          | 50.2 ms                                                      | 35.5 ms: 1.41x faster                                       |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                        |
| thrift                   | 1.18 ms                                                      | 838 us: 1.40x faster                                        |
| html5lib                 | 94.6 ms                                                      | 67.7 ms: 1.40x faster                                       |
| dulwich_log              | 81.1 ms                                                      | 58.8 ms: 1.38x faster                                       |
| pickle_pure_python       | 455 us                                                       | 332 us: 1.37x faster                                        |
| genshi_text              | 31.4 ms                                                      | 22.9 ms: 1.37x faster                                       |
| xml_etree_process        | 75.9 ms                                                      | 55.5 ms: 1.37x faster                                       |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                       |
| nbody                    | 134 ms                                                       | 99.1 ms: 1.35x faster                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.98 us: 1.35x faster                                       |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                      |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                       |
| fannkuch                 | 483 ms                                                       | 376 ms: 1.28x faster                                        |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                        |
| nqueens                  | 115 ms                                                       | 90.8 ms: 1.27x faster                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.5 ms: 1.25x faster                                       |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                        |
| 2to3                     | 350 ms                                                       | 286 ms: 1.23x faster                                        |
| scimark_fft              | 361 ms                                                       | 297 ms: 1.22x faster                                        |
| sympy_expand             | 600 ms                                                       | 498 ms: 1.21x faster                                        |
| regex_v8                 | 27.2 ms                                                      | 23.3 ms: 1.17x faster                                       |
| docutils                 | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                      |
| regex_dna                | 261 ms                                                       | 227 ms: 1.15x faster                                        |
| genshi_xml               | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                       |
| xml_etree_generate       | 92.3 ms                                                      | 80.5 ms: 1.15x faster                                       |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.15x faster                                        |
| json_loads               | 30.3 us                                                      | 26.5 us: 1.14x faster                                       |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.8 ms: 1.13x faster                                       |
| json                     | 5.86 ms                                                      | 5.48 ms: 1.07x faster                                       |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.07x faster                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.96 ms: 1.02x faster                                       |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                        |
| async_generators         | 421 ms                                                       | 440 ms: 1.05x slower                                        |
| regex_effbot             | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.84 ms: 1.21x slower                                       |
| coverage                 | 63.3 ms                                                      | 80.7 ms: 1.28x slower                                       |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.64x slower                                       |
| gc_traversal             | 3.42 ms                                                      | 6.51 ms: 1.91x slower                                       |
| telco                    | 7.23 ms                                                      | 158 ms: 21.93x slower                                       |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250803-3.15.0a0-3ec3d05-JIT/bm-20250803-pythonperf2-x86_64-python-main-3.15.0a0-3ec3d05.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.332x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.40x